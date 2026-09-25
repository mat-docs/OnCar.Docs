# Loading Configurations

The [Remote](remote-logging/index.md) logging, [Burst](burst-logging/index.md) logging and [External Inputs](../sensors/external-inputs/external-inputs-configuration.md) configurations are stored in, and used by, an ECU when it is working independently of System Monitor. To change a configuration in the ECU, you must download it from System Monitor. Similarly, to modify an existing configuration in the ECU, that configuration must first be uploaded to System Monitor. This is not automatic and must be done manually using menu commands.

Separate commands are provided for Remote logging and Burst logging configurations on the [Logging Menu](../../using-system-monitor/menus/logging-menu.md), and for External Inputs configurations on the [Sensors Menu](../../using-system-monitor/menus/sensors-menu.md). Some hardware has both types of logging configuration.

| Configuration | Download | Upload |
|---|---|---|
| Burst | **Logging** > **Burst Download** (CTRL+F2) | **Logging** > **Burst Upload** (CTRL+ALT+F2) |
| Remote | **Logging** > **Remote Download** (CTRL+ALT+F5) | **Logging** > **Remote Upload** (CTRL+ALT+F6) |
| External Inputs | **Sensors** > **External Inputs Download** (CTRL+F10) | **Sensors** > **External Inputs Upload** (CTRL+ALT+F10) |

## Download

Transfers the configuration from System Monitor to the ECU.

Download only takes place if System Monitor detects an ECU that matches the [Program Version](../../project-management/program-and-data-versions/index.md) used by the current project. The old configuration is overwritten.

## Upload

Transfers the configuration from the ECU to System Monitor.

Uploading overwrites the current configuration in System Monitor. If you have modified a configuration in System Monitor, you are prompted to save it when you select Upload (see [Logging Configuration Files](logging-configuration-files.md)).

Any parameter that is not defined by the current system description is discarded from the configuration. A warning lists the parameters that have not been included in the upload.

## Other commands

The Logging menu also has the following commands for configurations in the ECU:

- **Burst Reset** (CTRL+F3) and **Remote Reset** (CTRL+F7) - Reset burst or remote logging on the unit.
- **Remote New Session** (CTRL+ALT+F7) - Create a new Remote Logging session on the ECU.
- **Burst Export** and **Remote Export** - Export the configuration to disk for use by ATLAS (see [Burst Logging - Export](burst-logging/burst-logging-export.md)).
