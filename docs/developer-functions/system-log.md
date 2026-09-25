# System Log

System Monitor creates files of errors and events that are caused by its own operation. (These are not the same as the Errors and Events, which are due to the operation of the ECU.)

The contents of the files typically correspond to the on-screen messages but with much more detail.

## Log folder

Log files are written to the folder set by the **Directory for log files** [Advanced Setting](../using-system-monitor/settings.md). If no folder is set, System Monitor uses `Documents\McLaren Electronic Systems\System Monitor 8\Log\`. Each day's files are placed in a sub-folder named `SysMonLogs_YYYY.MM.DD`.

## Log files

| File | Contents |
|---|---|
| **Cmd_xxx.txt** | Commands issued from menus or via [ActiveX](../activex-automation/index.md). |
| **Unit_xxx.txt** | All communications with the unit. See [ECU On-Line](../ecu-control/ecu-on-line.md). |
| **Warn_xxx.txt** | Warnings from integrity checks, in particular parameters dropped from configurations. |
| **Pgv_xxx.txt** | Messages generated when [Creating Program Versions](../project-management/program-and-data-versions/creating-a-program-version.md). |
| **SM_xxx.txt** | Single Messages. Only created if the **Log Single Messages (Y/N)** Advanced Setting is on. |
| **Tune_xxx_app_ddmmyy.txt** | Data changes downloaded to the unit for application *app*. |

Where *xxx* is the username of the person logged onto the computer running System Monitor. If the **Enable log file per project (Y/N)** Advanced Setting is on, the Project name is added to the file names (for example `Cmd_xxx_project.txt`), so that each Project has its own log files.

## Message logs

A further level of detail is available in a Message Log, which records the messages between System Monitor and the unit and is used for debugging.

**To create a Message Log**:

1. Enable logging by selecting a log level in the **Message log level (for debugging)** [Advanced Setting](../using-system-monitor/settings.md). This is normally set to **Not Logging**.
2. Click ![Log IP Transactions button](assets/button_logIPTransactions.gif) (**Log IP transactions with unit**) on the Standard Tool Bar to start logging. Click it again to stop. The button is not available while the level is **Not Logging**.

The message log is written to the log folder as **SM_Msgs_yymmdd_hhmmss.txt**, named with the date and time it was started. The **Message log file size (MB)** Advanced Setting limits its size, and **Automatic IP Message Logging (Y/N)** starts message logging automatically.

All log files are in ASCII format and can be read by any text editor.

**See also:** [Developer Functions](index.md); [Event Log](../data-display/other-displays/events/event-log.md)
