# Export to MATLAB

The mathematical analysis application MATLAB is used in the design and implementation of embedded control systems.

The Data Version in the Edit Buffer can be exported to a MATLAB script file (.m).

**Export to MATLAB:**

1. Select the Active Application(s).
2. Select **Tools** > **Matlab Export**, then one of the following scopes:

    | Scope | Exports |
    |---|---|
    | **All Parameters** | All parameters of each Active Application. A separate MATLAB file is created for each Active Application. |
    | **Selected Parameters Only** | Only the parameters selected in the Parameter Explorer. |
    | **Selected Application Parameters Only** | All parameters of the selected application. |
    | **Parameter Selection** | The current parameter selection in the Parameter Explorer. |
    | **Application Differences Only** | Only the parameters of the selected application that differ. |
    | **Export without versioning** | The same scopes, but the application version is left out of the file header. |

    All scopes except **All Parameters** act on the Parameter Explorer, which must have the focus.

3. Select the format:
    - **Definition and Data** - The file includes the property settings as well as the value(s) of each Editable Parameter.
    - **Data Only** - The file only has the value(s) of each Editable Parameter.

A Save As dialog box (titled **Matlab Export**, or **Matlab Export [Data]** for Data Only) opens with the file type set to Matlab Script files (\*.m). It opens at the location of the currently loaded Data Version. The file can be stored in any location to which you have access.

The default file name is the letter V followed by the name of the Data Version file, for example V*version**nnn*.m, where:

- *version* is the version number of the Program Version used by the Application.
- *nnn* is the sequential number of the Data Version.

MATLAB export can also be used from the context menus in the Data Wizard windows (see [Data Wizard](../data-wizard/index.md)).

!!! note
    The MATLAB export commands are not available with some licences.

## Importing from MATLAB

Select **Tools** > **Matlab Import** (Ctrl+Q) to import data from one or more MATLAB script files into the Edit Buffer. If there are errors or warnings, you can view the warning log.

Alternatively, MATLAB can create Hex files, which can be imported into System Monitor with **File** > **Import Hex File** (see [Importing Hex Files](importing-hex-files.md)).

**See also:** [Edit Buffer](index.md); [Program and Data Versions](../program-and-data-versions/index.md); [Project Files](../files/types-of-files/project-files.md); [Program and Data Version Files](../files/types-of-files/program-and-data-version-files.md); [Developing Data Versions](index.md); [Exporting Files](../files/exporting-files.md)
