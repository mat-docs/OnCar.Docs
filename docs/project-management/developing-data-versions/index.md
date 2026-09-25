# Developing Data Versions

When a project is created, a Base Data Version is allocated to each Application in the project. The Base Data Version contains a full set of Editable Parameters with values that should enable the vehicle to operate, if not at its optimum.

As the ECU is tuned to optimise the performance of the vehicle, the values of the Editable Parameters are changed. System Monitor stores the changes in the Edit Buffer. If the ECU is On-Line, the contents of the Edit Buffer can be sent to the ECU either immediately (using Live Tune) or on demand.

## Features

- The Data Version in the ECU can be uploaded to the Edit Buffer.
- Only Active Applications can be tuned. Make sure that the applications that you want to tune are set as active and are not read only.
- The contents of the Edit Buffer can be saved at any time to create a new Data Version file. If the contents of the Edit Buffer are different from the currently loaded Data Version, you are prompted to save the new Data Version when the ECU is taken Off-Line or the project is closed. Data Versions are saved in the Customer Base directory of the Active Application.
- A backup of the Edit Buffer is stored in the same folder as the Data Version, with the name of the Data Version file followed by your Windows user name and the extension .dvb. For example: \\*MultiAppName*\\*CustBaseName*\\*version*\\*version*000*username*.dvb. See [Project Files](../files/types-of-files/project-files.md) for a description of the file structure.
- The backup location can be changed with the Advanced Setting **Directory for backup files**, and backups can be turned off with **Disable DTV backup (Y/N)** (see [Settings](../../using-system-monitor/settings.md)).

**See also:** [Data Changes in the ECU](../../ecu-control/data-changes-in-the-ecu/index.md); [Data Wizard](../data-wizard/index.md); [Unit Status](../../ecu-control/unit-status.md); [Reprogramming the ECU](../../ecu-control/ecu-memory/reprogramming-the-ecu.md); [Settings](../../using-system-monitor/settings.md); [Tuning](../../tuning/index.md); [Using Data Version Files](using-data-version-files.md)
