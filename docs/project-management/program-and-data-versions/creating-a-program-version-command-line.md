# Creating a Program Version - Command Line

You can create a Program Version from the command line without opening the System Monitor user interface. The syntax is:

```
SystemMonitorU.exe /newpgv /asap2 "pathasap2" /hex "pathhex" /controller "pathcontroller"
    [/error "patherror"] [/event "pathevent"] [/adjust "pathadjust"]
    [/sensor "pathsensor"] [/injector "pathinjector"] [/endis "pathendis"] [/auto "pathauto"]
    [/customer basename | /location folder] [/description "comment"] [/copydir "folder"]
```

Flags are not case sensitive. Each flag is followed by its value, separated by a space. Enclose values that contain spaces in quotation marks.

## Files

*pathxxxx* is the path of the following files. Relative paths are converted to full paths. Each file must exist.

| Flag | File | Rule |
|---|---|---|
| **/asap2** | ASAP2 File | Required. Must come from the ASAP project specified in the Customer Base. |
| **/hex** | Hex File | Required. Must match the ASAP2 file and be suitable for the ECU. |
| **/controller** | Controllers File | Required. Must be suitable for the ECU. |
| **/error** | Errors File | Required if you want to view [Errors](../../data-display/other-displays/errors/index.md). |
| **/event** | Events File | Required if you want to view [Events](../../data-display/other-displays/events/index.md). |
| **/adjust** | Adjustment Parameters | Required if you want to use an [Adjustment Board](../../hardware/adjustment-board.md). |
| **/sensor** | Sensors File | Required if a Sensor Injector file is loaded (see [Sensors](../../data-acquisition/sensors/index.md)). |
| **/injector** | Sensor Injector File | Required if the Sensors file includes injectors. |
| **/endis** | Sensor Enable/Disable File | Required if you want to enable and disable sensors. |
| **/auto** | Live AutoTune File | Required if you want to use [Live Auto Tune](../../tuning/live-auto-tune.md). |

## Other options

| Flag | Description |
|---|---|
| **/customer** *basename* | Optional. The name of the Customer Base in which the Program Version is to be stored. The ASAP project of that Customer Base must match the ASAP project in the ASAP2 file. |
| **/location** *folder* | Optional. The base folder in which the Program Version is to be stored (used in place of a Customer Base directory, for example with [Unit.Def](../unit-def-management/pgv-creation.md) configuration). Ignored if **/customer** is also given. |
| **/description** *comment* | Optional. The Comment of the new Program Version. The Notes are taken from the ASAP2 file. |
| **/copydir** *folder* | Optional. After the Program Version has been created, the contents of this folder are copied into the new Program Version folder. The folder must exist. |

If you specify a Customer Base with **/customer**, the Program Version is stored in the directory of that Customer Base, provided that the ASAP project specified by that Customer Base is the same as the ASAP project in the ASAP2 file.

If you specify neither a Customer Base nor a location, System Monitor searches the Customer Bases in the active [Multi-Application Base](../customer-bases/multi-application-base.md) for one that specifies the same ASAP project as the ASAP2 file, and stores the Program Version in the directory of that Customer Base. If the active Multi-Application Base is the Free User base, the Program Version is stored under the Multi-Application Base Directory.

In all cases, the Program Version is created in a sub-folder named after the version string in the ASAP2 file, in the same way as [Creating a Program Version](creating-a-program-version.md).

Program Versions created from the command line are always encrypted.

!!! warning
    The **/prm** and **/encrypt** flags are no longer supported. Any unrecognised flag, including these two, stops the Program Version from being created. The sensor calibration (.prm) file is set for System Monitor as a whole in the Advanced Setting **File for sensor calibration**.

## Return codes

| Code | Meaning |
|---|---|
| **0** | The command succeeded. |
| **1** | The command line could not be processed: no valid licence, an unrecognised flag, or a file that does not exist. |
| **3** | The command line was valid but the command failed (for example, no Customer Base matches the ASAP project). |

**See also:** [Creating a Program Version](creating-a-program-version.md); [Customer Base](../customer-bases/index.md); [Unit.Def PGV Creation](../unit-def-management/pgv-creation.md); [ECU Files](../files/types-of-files/ecu-files.md); [Errors](../../data-display/other-displays/errors/index.md); [Events](../../data-display/other-displays/events/index.md); [Sensors](../../data-acquisition/sensors/index.md)
