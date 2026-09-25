# ECU Search

The [ECU Bar](../../using-system-monitor/tool-and-information-bars/ecu-bar.md) displays Data Version information for all Applications. ECU Search gives more detail about the Program and Data Version files loaded into the ECU.

To start an ECU search, select **ECU** > **Search for Versions...**. If the project has more than one Application, select one in the Select an Application dialog box. The **Ecu Search** dialog box opens, with the following tabs:

- [Program Version on ECU](ecu-search-program-version.md) - Information about the Program Version used by the ECU.
- [Data Version in Flash-RAM](ecu-search-data-version.md) - Information about the Data Version used by the ECU.

## How files are found

When an ECU is connected, System Monitor locates the files that were used to program it. The ECU does not hold the file name, but stores an ID that System Monitor uses to identify the file.

System Monitor searches for files when a new project is loaded, when the ECU memory is changed and when the ECU is reconnected after the link has been lost. A search can also be forced with **ECU** > **Query Versions**.

The Program Version ID is taken from the Reference Controller. If that controller is faulty or not connected, System Monitor cannot locate the Program Version and `???` is shown in the ECU Bar. Make sure the Reference Controller is enabled in [ECU Properties - Controllers](../ecu-properties/ecu-properties-controllers.md).

Data Version file locations are searched in the following order:

1. The folder that contains the Data Version currently loaded into the project.
2. The folder and sub-folders created for the Program Version detected in the ECU.
3. The entire Customer Base folder and sub-folders.

Once the Data Version file is located, its contents are compared with the data in each controller in turn. If the data in any controller differs from the file, `(*)` is shown in the ECU Bar.

The status of the search is shown by the background colour of the ECU Bar.

The search can take some time. To speed up the ECU Bar, you can stop System Monitor searching the entire Customer Base folder: set **Search base for versions (Y/N)** to **N** in [Advanced Settings](../../using-system-monitor/settings.md).

**See also:** [Advanced Settings](../../using-system-monitor/settings.md); [ECU Bar](../../using-system-monitor/tool-and-information-bars/ecu-bar.md); [ECU Control](../index.md)
