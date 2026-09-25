# Testbed Properties

System Monitor must be configured to operate with the testbed. To open the Testbed Properties dialog box (titled **Puma Testbed**) select **Tools** > **Testbed** > **Configure**. This command is not available while the [Testbed Link](../testbed-link.md) is enabled.

The dialog box consists of the following tabs:

- [Link](testbed-properties-link.md) - Allows you to configure the link between PUMA and System Monitor.
- [Watchdog](testbed-properties-watchdog.md) - Allows you to configure the watchdogs on the link between PUMA and System Monitor.
- [Debug](testbed-properties-debug.md) - Allows you to configure the Debug File.
- [Commands](testbed-properties-commands.md) - Allows you to configure the way System Monitor responds to PUMA commands.
- [Translate](testbed-properties-translate.md) - Allows you to configure the correspondence between PUMA and System Monitor parameter identifiers.

The testbed settings are saved in the file `Testbed.cfg` in the System Monitor configuration files folder, not in the Project. If the settings cannot be read, System Monitor reports "Error reading the testbed settings - default settings will be used".
