# Testbed Link

Selecting **Tools** > **Testbed** > **Enable Link** switches the link between System Monitor and the testbed on and off. A tick next to the command shows that the link is enabled.

When you enable the link, System Monitor:

1. Puts the ECU [On-Line](../ecu-control/ecu-on-line.md), if it is not already on-line. If this fails, the message "The ECU must be On-line before enabling the testbed" is shown and the link is not enabled.
2. In **Full-operation** mode (see [Testbed Properties - Link](testbed-properties/testbed-properties-link.md)), switches on [Live Tune](../tuning/live-tune.md) (**ECU** > **Live Updates**). If this fails, the message "Live Updates must be enabled for testbed Full-operation mode" is shown and the link is not enabled.
3. Checks that the program version on the ECU matches the one in the Project and, in Full-operation mode, that the data version also matches. The link is not enabled until the ECU contains the correct versions.
4. Opens the [Debug file](testbed-properties/testbed-properties-debug.md), if debug is enabled, and starts listening for PUMA commands on the configured serial port or TCP/IP port.

The Testbed Link is automatically disabled if:

- the ECU is taken **Off-line**, or
- Live Tune is switched off while the link is enabled in Full-operation mode.

If the communications link to the ECU is lost while the Testbed Link is enabled, Live Tune is switched off. When the ECU link is found again, System Monitor re-checks the program and data versions, puts the ECU back on-line and, in Full-operation mode, switches Live Tune back on.

When the link is enabled, **PUMA Enabled** is displayed on the [Status Bar](../using-system-monitor/tool-and-information-bars/status-bar.md).

System Monitor windows can be used to monitor parameter values while the link is enabled. The status of the link, and the information passing across it, are shown in the [Testbed Message](testbed-message.md) window.

The parameters that System Monitor acquires from the ECU are defined in the Live Logging Configuration. Ensure that Auto Configuration is on so that the correct data is available to send to the testbed and to display on the screen.

**See also:** [Live Logging Configuration](../data-acquisition/logging/live-logging/index.md)
