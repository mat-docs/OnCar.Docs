# History Report

During its operation the ECU generates various statistics about the operation of the vehicle that it is controlling. History Report extracts these statistics and displays them. System Monitor can also control aspects of the way the statistics are collected and stored.

History Report is only available when:

- one of the applications in the Project supports History Report. Otherwise System Monitor reports that a history report cannot be created or opened because it "is not supported by any of the applications in your project".
- the relevant Customer Base has permission, set by **Permit engine history report** in [Customer Base Advanced Settings](../project-management/customer-bases/customer-base-advanced-settings.md).

Each Project has one History Report file associated with it (see [History Report - Files](history-report-files.md)). If the Project has none, one is created the first time you upload history data.

## History Report menu

Select **Tools** > **History Report** to access the submenu options:

| Option | Description |
|---|---|
| **Open *filename*** | Opens the [History Report dialog box](history-report-dialog-box.md) for the History Report file associated with the Project. The menu item shows the file name (for example **Open FIA001**). Not available if the Project has no History Report file, or if the History Report is already open. To open a different History Report file, see [Opening Files](../project-management/files/opening-files.md). |
| **Upload** | Extracts history data from the ECU and shows it in the History Report dialog box. The contents of the History Report file associated with the Project are overwritten. If there is no History Report file, a new one is created. Available when an application in the Project supports History Report and the ECU is connected. |
| **Download** | Sends the history data in the History Report to the ECU. The previous set of history data in the ECU is deleted. Use this if you want to continue gathering data for a vehicle in which you have changed the ECU. This command also sends the [Setup](history-report-setup.md) data to the ECU. Available when the Project has a History Report file and the ECU is connected. |
| **Reset Engine Stats** | Resets the history data in the ECU for the engine currently selected in the [Summary](history-report-summary.md) tab. You are asked to confirm first. The previous history data for that engine is deleted. Available when the Project has a History Report file. |
| **Reset Chassis Stats** | Resets the history data in the ECU for the chassis currently selected in the Summary tab. You are asked to confirm first. The previous history data for that chassis is deleted. Available when the Project has a History Report file. |

If uploaded history data fails validation, System Monitor reports that the history report information is invalid. Use **Show Defaults** in the upload progress dialog box to display default values instead.

An existing History Report file can also be selected from the File Type Selection dialog box. When selected, the History Report dialog box opens, showing data from the file.

**See also:** [Customer Base Advanced Settings](../project-management/customer-bases/customer-base-advanced-settings.md); [Using System Monitor](../using-system-monitor/index.md)
