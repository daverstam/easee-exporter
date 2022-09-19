#!/usr/bin/env python3

import requests
import yaml
import time
import json
import datetime
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY

class easeeConnection(object):
    def __init__(self):
        self.easee_base_url = cfg['easee_base_url']
        self.easee_token_url = cfg['easee_token_url']
        self.easee_token = cfg['easee_token']
        self.easee_username = cfg['easee_username']
        self.easee_password = cfg['easee_password']

    def request_api_token(self):
        self.payload = f'''{{"password": "{self.easee_password}", "userName": "{self.easee_username}"}}'''
        self.headers = {'Accept': 'application/json',
                 'Content-Type': 'application/*+json',
                 'Authorization': f'Bearer {self.easee_token}'}

        self.easee_token_request = requests.post(self.easee_token_url, data=self.payload, headers=self.headers).json()

        return self.easee_token_request

class easeeMetrics(object):
    def __init__(self):
        self.easee_base_url = cfg['easee_base_url']
        self.easee_products_url = cfg['easee_products_url']
        self.easee_token = ''

    def request_equalizers(self):
        """
        Returns the ID of any found equalizer
        """
        if not self.easee_token:
            self.easee_token_response = easeeConnection().request_api_token()
            self.easee_token = self.easee_token_response['accessToken']
            self.token_expiry = self.easee_token_response['expiresIn']
            self.easee_token_creation_time = datetime.datetime.now()
        elif self.easee_token:
            if datetime.datetime.now() > (self.easee_token_creation_time + datetime.timedelta(seconds=self.token_expiry)):
                self.easee_token_response = easeeConnection().request_api_token()
                self.easee_token = self.easee_token_response['accessToken']
                self.easee_token_creation_time = datetime.datetime.now()

        self.headers = {'Accept': 'application/json',
                        'Authorization': f'Bearer {self.easee_token}'}
        self.products_response = requests.get(self.easee_products_url, headers=self.headers).json()

        try:
            self.equalizer_id = self.products_response[0]['equalizers'][0]['id']
            return self.equalizer_id
        except KeyError:
            return None

    def request_metrics(self, metric_url):
        """
        Returns metrics that is set to true in the configuration file
        """
        if not self.easee_token:
            self.easee_token_response = easeeConnection().request_api_token()
            self.easee_token = self.easee_token_response['accessToken']
            self.token_expiry = self.easee_token_response['expiresIn']
            self.easee_token_creation_time = datetime.datetime.now()
        elif self.easee_token:
            if datetime.datetime.now() > (self.easee_token_creation_time + datetime.timedelta(seconds=self.token_expiry)):
                self.easee_token_response = easeeConnection().request_api_token()
                self.easee_token = self.easee_token_response['accessToken']
                self.easee_token_creation_time = datetime.datetime.now()

        self.headers = {'Authorization': f'Bearer {self.easee_token}'}
        self.easee_metric_request = requests.get(self.easee_base_url + metric_url, headers=self.headers, timeout=30)

        return self.easee_metric_request

    def collect(self):
        for k, v in cfg['metrics'].items():
            if v['collect'] is True:
                """
                EQUALIZER
                """
                #
                # State
                #
                if k == 'state':
                    equalizer_id = self.request_equalizers()
                    equalizer_url = v['url'].format(equalizer_id)
                    metrics_data = json.loads(self.request_metrics(equalizer_url).content)
                    metrics_to_export = {
                        'currentL1': 'Current L1',
                        'currentL2': 'Current L2',
                        'currentL3': 'Current L3',
                        'voltageNL1': 'Voltage NL1',
                        'voltageNL2': 'Voltage NL2',
                        'voltageNL3': 'Voltage NL3',
                        'activePowerImport': 'Active Power Import',
                        'activePowerExport': 'Active Power Export',
                        'reactivePowerImport': 'Reactive Power Import',
                        'reactivePowerExport': 'Reactive Power Export',
                        'cumulativeActivePowerImport': 'Cumulative Active Power Import',
                        'cumulativeActivePowerExport': 'Cumulative Active Power Export',
                        'rcpi': 'Rcpi',
                        'maxPowerImport': 'Max Power Import',
                        'softwareRelease': 'Software Release',
                        'latestFirmware': 'Latest Firmware'
                    }
                    for metric_name, metric_help in metrics_to_export.items():
                        metrics = GaugeMetricFamily(
                            f'easee_equalizer_{k}_{metric_name}',
                            f'{metric_help}',
                            labels = [
                                'equalizer_id'
                            ]
                        )
                        try:
                            equalizer_id = equalizer_id
                            val = metrics_data[f'{metric_name}']
                            metrics.add_metric([
                                equalizer_id,
                                ], val)
                        except KeyError:
                            pass

                        yield metrics


if __name__ == '__main__':
    with open('./config.yml', 'r') as config:
        cfg = yaml.safe_load(config)

    REGISTRY.register(easeeMetrics())
    start_http_server(cfg['exporter_listening_port'])
    while True: time.sleep(1)
