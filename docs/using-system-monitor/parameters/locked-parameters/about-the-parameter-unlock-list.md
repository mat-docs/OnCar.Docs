# About the Parameter Unlock List (PUL)

- System Monitor BIOS files are distributed in an unlocked state (base data version).
- Users with [Full Access](../../../getting-started/team-security-and-reduced-data-access/reduced-data-access.md#RDA_Full) can lock any application that is contained in their System Monitor licence file.
- Parameter Unlock Lists (PULs) can then be created to allow users who have [Restricted Access](../../../getting-started/team-security-and-reduced-data-access/reduced-data-access.md#RDA_Res) to view certain parameters within the locked application.
- Users with Full Access can edit a PUL at any time to add or remove parameters.
- PULs can be stored in a user-definable location, or in the same location (common to all users) as the program and data version files (PGVs and DTVs).
- PUL files are included with the relevant Applications in exported System Monitor Projects.
- When a PUL is created, System Monitor generates a checksum and stores it in both the Data Version and the PUL file. Any later attempt by ATLAS or System Monitor to access data from this Data Version validates the checksums in the PUL file and the Data Version, and restricts access to parameters that fail validation.

## PUL files

- Each Application in a Project has an associated PUL (`.pul`) file.
- The `.pul` file is a plain text file in `.ini` file format, with a header section and a section for each parameter type (for example `[Ecu]` for measurement parameters, `[Scalar]`, `[1AxisMap]`, `[2AxisMap]`, `[Array]` and `[String]`).
- If **Use Encrypted Parameter Unlock List Files (Y/N)** is set in [Advanced Settings](../../settings.md) (default N), PUL files are saved in encrypted form.

## PULs in ATLAS

- The PUL file is loaded into ATLAS based on the checksum stored in the Data Version (DTV) and the PUL.
- When ATLAS processes DTVs (during recording and data access), any associated PULs are also processed. This determines the parameters that are available to the user in ATLAS.
- Only parameters that appear in the PUL for locked applications are visible in ATLAS to users with Restricted Access. They can edit the properties and display values of those parameters in the normal way, but cannot edit the PUL.
- Only teams with Full Access can [edit the PUL](edit-the-parameter-unlock-list.md) file on the Unlock List Management tab of the Application Properties dialog box.

!!! note
    By default the file is saved in the PGV directory for the Application. If required, a secondary global directory can be set up for PUL files, for access by other users. Set the path to the secondary directory in the **Directory for Parameter Unlock List files** setting in the [Advanced Settings](../../settings.md) dialog box. If the PUL file exists in both the default and secondary directories, the file in the default directory is read on loading.

**See also:** [Edit the Parameter Unlock List](edit-the-parameter-unlock-list.md); [Locked Parameters](locked-parameters.md); [Reduced Data Access](../../../getting-started/team-security-and-reduced-data-access/reduced-data-access.md)
