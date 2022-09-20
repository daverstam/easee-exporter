# easee-exporter
## Easee Home exporter for Prometheus

Currently this exporter only fetches the Equalizer metrics, I made this mainly to monitor my total power usage however I (or someone else) will probably add more metrics in the future.

To get this running you need Prometheus and Python. I'm running my setup on an old Raspberry Pi with Debian and it works fine and dandy.

Example output:
```
# HELP easee_equalizer_state_currentL1 Current L1
# TYPE easee_equalizer_state_currentL1 gauge
easee_equalizer_state_currentL1{equalizer_id="redacted"} 0.10999999940395355
# HELP easee_equalizer_state_currentL2 Current L2
# TYPE easee_equalizer_state_currentL2 gauge
easee_equalizer_state_currentL2{equalizer_id="redacted"} 0.9110000133514404
# HELP easee_equalizer_state_currentL3 Current L3
# TYPE easee_equalizer_state_currentL3 gauge
easee_equalizer_state_currentL3{equalizer_id="redacted"} -0.6399999856948853
# HELP easee_equalizer_state_voltageNL1 Voltage NL1
# TYPE easee_equalizer_state_voltageNL1 gauge
easee_equalizer_state_voltageNL1{equalizer_id="redacted"} 230.3000030517578
# HELP easee_equalizer_state_voltageNL2 Voltage NL2
# TYPE easee_equalizer_state_voltageNL2 gauge
easee_equalizer_state_voltageNL2{equalizer_id="redacted"} 230.89999389648438
# HELP easee_equalizer_state_voltageNL3 Voltage NL3
# TYPE easee_equalizer_state_voltageNL3 gauge
easee_equalizer_state_voltageNL3{equalizer_id="redacted"} 230.5
# HELP easee_equalizer_state_activePowerImport Active Power Import
# TYPE easee_equalizer_state_activePowerImport gauge
easee_equalizer_state_activePowerImport{equalizer_id="redacted"} 0.0
# HELP easee_equalizer_state_activePowerExport Active Power Export
# TYPE easee_equalizer_state_activePowerExport gauge
easee_equalizer_state_activePowerExport{equalizer_id="redacted"} 0.039000000804662704
# HELP easee_equalizer_state_reactivePowerImport Reactive Power Import
# TYPE easee_equalizer_state_reactivePowerImport gauge
easee_equalizer_state_reactivePowerImport{equalizer_id="redacted"} 0.12600000202655792
# HELP easee_equalizer_state_reactivePowerExport Reactive Power Export
# TYPE easee_equalizer_state_reactivePowerExport gauge
easee_equalizer_state_reactivePowerExport{equalizer_id="redacted"} 0.0
# HELP easee_equalizer_state_cumulativeActivePowerImport Cumulative Active Power Import
# TYPE easee_equalizer_state_cumulativeActivePowerImport gauge
easee_equalizer_state_cumulativeActivePowerImport{equalizer_id="redacted"} 2547.530029296875
# HELP easee_equalizer_state_cumulativeActivePowerExport Cumulative Active Power Export
# TYPE easee_equalizer_state_cumulativeActivePowerExport gauge
easee_equalizer_state_cumulativeActivePowerExport{equalizer_id="redacted"} 2639.6298828125
# HELP easee_equalizer_state_rcpi Rcpi
# TYPE easee_equalizer_state_rcpi gauge
easee_equalizer_state_rcpi{equalizer_id="redacted"} -69.5
# HELP easee_equalizer_state_maxPowerImport Max Power Import
# TYPE easee_equalizer_state_maxPowerImport gauge
easee_equalizer_state_maxPowerImport{equalizer_id="redacted"} 13.800000190734863
# HELP easee_equalizer_state_softwareRelease Software Release
# TYPE easee_equalizer_state_softwareRelease gauge
easee_equalizer_state_softwareRelease{equalizer_id="redacted"} 108.0
# HELP easee_equalizer_state_latestFirmware Latest Firmware
# TYPE easee_equalizer_state_latestFirmware gauge
easee_equalizer_state_latestFirmware{equalizer_id="redacted"} 108.0
```

Example image from Grafana:
![Easee Home Equalizer in Grafana](https://github.com/daverstam/easee-exporter/blob/main/grafana-img.png?raw=true)


API Reference docs: https://developer.easee.cloud/reference/
