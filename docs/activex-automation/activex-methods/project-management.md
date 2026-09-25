# Project Management

Methods for projects, program and data versions, desktops, CAN and remote logging configurations, virtual parameter files, Reduced Data Access (PUL) files and export/import.

See [ActiveX Methods](index.md) for the conventions used on this page, and [ActiveX Error Codes](../activex-errors/activex-error-codes.md) for the return codes.

## Functions

### AddApplication

Adds the application defined by the given DTV, and its associated PGV, to the open project.

```c
long AddApplication([in] BSTR pszDTVPath);
```

| Argument | Description |
|---|---|
| `pszDTVPath` | Full path of the DTV to add. The file must exist and must lie within one of the customer base directories of the current multi-application base (or, when unit definitions are in use, within an application folder of the project's unit definition). |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the DTV does not exist, `SMAPI_ERR_NO_CUSTOMER_BASE` (-42) if it is not within a customer base, and `SMAPI_ERR_INVALID_CMD` (-31) if the application could not be added (for example, because it is already in the project).

### AddParametersToUnlockList

Adds the given parameters to the PUL (parameter unlock list) file of an application for use with Reduced Data Access, and applies the updated PUL file to the application.

```c
long AddParametersToUnlockList(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] BSTR* pszPULFile);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | SAFEARRAY of strings containing the identifiers of the parameters to add. |
| `pszPULFile` | Receives the full path of the updated PUL file. |

!!! note
    The application's data version must already use a PUL file; otherwise `SMAPI_ERR_FILE` (-8) is returned. The updated list is written to a new file whose name includes the new checksum (`<name> - <checksum>.pul`), replacing any existing file of that name, and that file becomes the application's PUL file. Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if an identifier is not found.

### CANConfigGet

Gets the file name of the CAN configuration in the given slot.

```c
long CANConfigGet([in] short wIndex, [out] BSTR* pszFileName);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index. The value is used directly as a 0-based key (`0` = slot 1 … `15` = slot 16), unlike the other CAN slot methods, which are 1-based. |
| `pszFileName` | Receives the full path of the CAN configuration file. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if no CAN configuration is loaded in the slot.

### CanConfigLoad

Loads the specified CAN configuration file into the first CAN slot.

```c
long CanConfigLoad([in] BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the CAN configuration file (.clc). |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the file cannot be opened.

### CANConfigLoadEx

Loads the specified CAN configuration file into the given slot and optionally makes it active.

```c
long CANConfigLoadEx([in] short wIndex, [in] BSTR pszFileName, [in] boolean bActivate);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index (1–16). |
| `pszFileName` | Full path of the CAN configuration file (.clc). |
| `bActivate` | True to make the configuration active; False to load it inactive. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is out of range. If the file cannot be opened, no error is returned. If activating the configuration produces duplicate parameter identifiers, the configuration is deactivated again.

### CANConfigSave

Saves the current CAN configuration to the specified file.

```c
long CANConfigSave(boolean bSaveCopyAs, BSTR szFullPath, BSTR szComment, BSTR szNotes);
```

| Argument | Description |
|---|---|
| `bSaveCopyAs` | True to save a copy without changing the file name or modified state of the loaded configuration; False to save it under the new name. |
| `szFullPath` | Full path of the file to save. |
| `szComment` | Replaces the existing comment. An empty string leaves the comment unchanged. |
| `szNotes` | Replaces the existing notes. An empty string leaves the notes unchanged. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no CAN configuration is loaded and `SMAPI_ERR_FILE` (-8) if the save fails. With `bSaveCopyAs` True, the comment and notes are changed only in the saved copy.

### CANConfigUnload

Unloads the CAN configuration from the given slot.

```c
long CANConfigUnload([in] short wIndex);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index (2–16). Slot 1 cannot be unloaded. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is out of range.

### ClearDataVersionNotes

Clears the notes of the data version in the edit buffer for the given application.

```c
long ClearDataVersionNotes(short wAppId);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |

### CloseProject

Closes the open project. Modified documents are saved without prompting.

```c
long CloseProject();
```

This method takes no arguments.

!!! note
    Returns `SMAPI_ERR_PARTIALCOMPLETE` (-34) if the project could not be closed, including when no project is open. Use [CloseProjectEx](#closeprojectex) to choose what happens to unsaved documents.

### CloseProjectEx

Closes the open project, with a choice of what to do with unsaved documents.

```c
long CloseProjectEx([in] WORD wAction);
```

| Argument | Description |
|---|---|
| `wAction` | Action for unsaved documents:<br>`0` = Cancel: do not close the project if any document is unsaved<br>`1` = Save all modified documents, then close<br>`2` = Close without saving |

!!! note
    Returns `SMAPI_ERR_INVALID_CMD` (-31) if `wAction` is greater than 2, and `SMAPI_ERR_PARTIALCOMPLETE` (-34) if the project was not closed (for example, `wAction` = `0` with unsaved documents).

### CompareApp

Compares the data version of an application in the edit buffer with up to two DTV files. Returns the parameters that differ, with the parameter type and a reason code for each comparison.

```c
long CompareApp(
    [in] WORD wAppId,
    [in] BSTR pszDTV1,
    [in] BSTR pszDTV2,
    [out] VARIANT* str1xArrParamIds,
    [out] VARIANT* str1xParamType,
    [out] VARIANT* w1xArrReason1,
    [out] VARIANT* w1xArrReason2);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszDTV1` | Full path of the first DTV to compare against. An empty string skips this comparison. |
| `pszDTV2` | Full path of the second DTV to compare against. An empty string skips this comparison. |
| `str1xArrParamIds` | Receives a 1-D, 0-based SAFEARRAY of strings holding the identifiers of the parameters that differ. |
| `str1xParamType` | Receives a 1-D SAFEARRAY of strings holding the type of each parameter: `MEAS`, `SCALAR`, `1AXIS`, `2AXIS`, `AXIS`, `ARRAY`, `STRING` or `UNKNOWN`. |
| `w1xArrReason1` | Receives a 1-D SAFEARRAY of short integers holding the reason code for the difference between the edit buffer and the first DTV (`0` if not compared). |
| `w1xArrReason2` | Receives a 1-D SAFEARRAY of short integers holding the reason code for the difference between the edit buffer and the second DTV (`0` if not compared).<br>Reason codes (a combination of one or more of):<br>`0x0001` EQUATE_ABSENT = Not present in the program version of the candidate<br>`0x0002` EQUATE_DIFFERENT = Major difference that prevents merge<br>`0x0004` EQUATE_EQUAL = Same data type, size and value<br>`0x0008` EQUATE_DIFF_VALUE = Same data type, size and units; different value<br>`0x0010` EQUATE_DIFF_SIZE = Same data type, different size (maps only)<br>`0x0020` EQUATE_DIFF_CONV = Different display format conversion<br>`0x0040` EQUATE_DIFF_UNITS = Different units<br>`0x0080` EQUATE_DIFF_DATA_TYPE = Different data type<br>`0x0100` EQUATE_DIFF_COMMENT = Different comment<br>`0x0200` EQUATE_DIFF_DEFAULT_VALUE = Different default value<br>`0x0400` EQUATE_ABSENT_MASTER = Not present in the program version of the edit buffer |

!!! note
    When two DTVs are given, both must use the same PGV version; otherwise `SMAPI_ERR_DATAVER_MISMATCH` (-4) is returned. Returns `SMAPI_ERR_BAD_STATE` (-30) if the merge buffer contains uncommitted changes. Locked parameters are not included in the results.

### CreateNewCANConfig

Creates a new CAN configuration file and loads it into the project.

```c
long CreateNewCANConfig(
    [in] BSTR szFullPath,
    [in] boolean bSaveExisting,
    [in] boolean bOverwrite);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the new CAN configuration file (.clc). |
| `bSaveExisting` | True to save the current CAN configuration to its existing file before creating the new one. |
| `bOverwrite` | True to overwrite the file if it already exists. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the file exists and `bOverwrite` is False. Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `bSaveExisting` is True but no CAN configuration is loaded, or if the new configuration could not be created.

### CreateNewRemoteConfig

Creates a new remote logging configuration file and loads it into the project.

```c
long CreateNewRemoteConfig(
    [in] BSTR szFullPath,
    [in] boolean bSaveExisting,
    [in] boolean bOverwrite);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the new remote logging configuration file (.rlc). |
| `bSaveExisting` | True to save the current remote logging configuration to its existing file before creating the new one. |
| `bOverwrite` | True to overwrite the file if it already exists. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the file exists and `bOverwrite` is False. Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `bSaveExisting` is True but no remote logging configuration is loaded, or if the new configuration could not be created.

### CreateNewVirtualParameters

Creates a new virtual parameters file and loads it into the project.

```c
long CreateNewVirtualParameters(
    [in] BSTR szFullPath,
    [in] boolean bSaveExisting,
    [in] boolean bOverwrite);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the new virtual parameters file (.vpm). |
| `bSaveExisting` | True to save the existing document before creating the new one. See the note below. |
| `bOverwrite` | True to overwrite the file if it already exists. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the file exists and `bOverwrite` is False, and `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no virtual parameters document is loaded when `bSaveExisting` is True. In this version, `bSaveExisting` = True does not save the virtual parameters document. It calls the remote logging save routine with the path of the current virtual parameters file. Save the virtual parameters separately before calling this method, and pass False.

### CreatePGV

Creates a new PGV and its base DTV from ASAP2 definitions. No project may be open.

```c
long CreatePGV(
    [in] BSTR szLocation,
    [in] BSTR szASAP2File,
    [in] BSTR szHexFile,
    [in] BSTR szControllersFile,
    [in] BSTR szErrorsFile,
    [in] BSTR szEventsFile,
    [in] BSTR szAdjustmentParametersFile,
    [in] BSTR szSensorsFile,
    [in] BSTR szSensorInjectorFile,
    [in] BSTR szSensorEnableFile,
    [in] BSTR szLiveAutoTuneFile,
    [in] BSTR szComment,
    [in] BSTR szNotes,
    [out] BSTR pszPGV,
    [out] BSTR pszDTV);
```

| Argument | Description |
|---|---|
| `szLocation` | Existing folder for the output files. The PGV is created in a subfolder named after the program version, as `<version>\<version>.pgv`. |
| `szASAP2File` | Path of the ASAP2 project file (.a2l). Required. |
| `szHexFile` | Path of the hex definition file (.hex). Required. |
| `szControllersFile` | Path of the controllers definition file (.ini). Required. |
| `szErrorsFile` | Optional path of the errors definition file (.ini). |
| `szEventsFile` | Optional path of the events definition file (.ini). |
| `szAdjustmentParametersFile` | Optional path of the pot board (adjustment parameters) definition file (.ini). |
| `szSensorsFile` | Optional path of the sensors definition file (.ini). |
| `szSensorInjectorFile` | Optional path of the sensor injector definition file (.ini). |
| `szSensorEnableFile` | Optional path of the sensor enable/disable definition file (.ini). |
| `szLiveAutoTuneFile` | Optional path of the live auto tune definition file (.ini). |
| `szComment` | PGV comment. |
| `szNotes` | PGV notes. If empty, the notes are taken from the ASAP2 project. |
| `pszPGV` | Receives the full path of the created PGV file. |
| `pszDTV` | Receives the full path of the created base DTV file. |

!!! note
    Returns `SMAPI_ERR_BAD_STATE` (-30) if a project is open, and `SMAPI_ERR_FILE` (-8) if the folder or a required file does not exist, or if an optional file is given but does not exist. The dispinterface declares `pszPGV` and `pszDTV` as `[out] BSTR`, but the implementation takes them by reference (`BSTR*`) and writes the paths into them. Pass them by reference to receive the paths. Each path is returned only if the file was created. If creation fails after the input checks, the method still returns 0, so check the returned paths.

### CreateProject

Creates a new project in the current multi-application base and opens it. No project may be open.

```c
long CreateProject(
    [in] BSTR szProject,
    [in] VARIANT aszApps,
    [in] BSTR szDesktop,
    [in] BSTR szVirtuals,
    [in] BSTR szCAN,
    [in] BSTR szRemoteConfig);
```

| Argument | Description |
|---|---|
| `szProject` | Name of the project to create within the current multi-application base. |
| `aszApps` | SAFEARRAY of strings containing the PGV files to include. A file that is not given as a full path within the base is searched for in the base directory. |
| `szDesktop` | Name of the desktop document to create, or to include if the file already exists. Required. A name without a path is placed in the base's desktops folder. |
| `szVirtuals` | Optional name of the virtual parameters document to create, or to include if the file already exists. |
| `szCAN` | Optional name of the CAN configuration document to create, or to include if the file already exists. |
| `szRemoteConfig` | Optional name of the remote logging configuration document to create, or to include if the file already exists. |

!!! note
    If full path names are used, the path must lie within the current multi-application base; otherwise `SMAPI_ERR_FILE` (-8) is returned. `SMAPI_ERR_FILE` is also returned if a PGV cannot be found in the base. If a project is already open, nothing is done and `SMAPI_ERR_NOPROJECT` (-1) is returned.

### CreateFFCFromPGV

Creates an FFC file from the given PGV.

```c
long CreateFFCFromPGV([in] BSTR pszPGV);
```

| Argument | Description |
|---|---|
| `pszPGV` | Full path of the PGV file to convert. |

!!! note
    The FFC file is written beside the PGV, with the same name and the extension .ffc. A project does not need to be open. Returns `SMAPI_ERR_FILE` (-8) if the PGV does not exist, is empty or cannot be processed.

### DataVersionModified

Returns whether the data version in the edit buffer for the given application has been modified.

```c
long DataVersionModified([in] short wAppId, [out] boolean* pbResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pbResult` | Receives True if the data version has unsaved modifications, otherwise False. |

### DataVersionOpen

Opens the specified data version.

```c
long DataVersionOpen(short wAppId, BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `wAppId` | Ignored. The application is determined from the data version file. |
| `szFullPath` | Full path of the data version file. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the file does not exist.

### DataVersionSave

Saves the data version in the edit buffer for the given application to the specified file.

```c
long DataVersionSave(short wAppId, BSTR szFullPath, BSTR szComments, BSTR szNotes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szFullPath` | Full path of the file to save. |
| `szComments` | Replaces the existing comment. An empty string leaves the comment unchanged. |
| `szNotes` | Added before the existing notes. An empty string leaves the notes unchanged. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the save fails.

### DataVersionSaveCopyAs

Saves a copy of the data version in the edit buffer to the specified file. The file name and modified state of the edit buffer are not changed.

```c
long DataVersionSaveCopyAs(short wAppId, BSTR szFullPath, BSTR szComments, BSTR szNotes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szFullPath` | Full path of the file to save. |
| `szComments` | Replaces the comment in the saved copy. An empty string leaves the comment unchanged. |
| `szNotes` | Added before the existing notes in the saved copy. An empty string leaves the notes unchanged. |

### DataVersionSaveCopyAsEx

Saves a copy of the data version in the edit buffer to the specified file, optionally with a different consortium. The file name and modified state of the edit buffer are not changed.

```c
long DataVersionSaveCopyAsEx(
    short wAppId,
    BSTR szFullPath,
    BSTR szComments,
    BSTR szNotes,
    BSTR szConsortium);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szFullPath` | Full path of the file to save. |
| `szComments` | Replaces the comment in the saved copy. An empty string leaves the comment unchanged. |
| `szNotes` | Added before the existing notes in the saved copy. An empty string leaves the notes unchanged. |
| `szConsortium` | Name of the consortium to save the copy with, `"Disabled"` to remove team security, or an empty string to keep the current consortium. |

!!! note
    The consortium is applied only if your licence permits it (you own the data version and the consortium name is valid for your licence); otherwise `SMAPI_ERR_NOLICENCE` (-2) is returned. Set `szConsortium` to `"Disabled"` to remove team security and unlock the file. This also removes the Reduced Data Access (PUL) settings, and they are removed from the edit buffer as well as from the saved copy.

### DataVersionSaveIncrement

Saves the data version in the edit buffer under the next data version file name, generated by incrementing the current name.

```c
long DataVersionSaveIncrement([in] WORD wAppId, [in] BSTR szComments, [in] BSTR szNotes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szComments` | Replaces the existing comment. An empty string leaves the comment unchanged. |
| `szNotes` | Added before the existing notes. An empty string leaves the notes unchanged. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the next file name cannot be generated or the save fails.

### DesktopLoad

Loads the specified System Monitor desktop file.

```c
long DesktopLoad([in] BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the desktop file (.dtp). |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the desktop cannot be opened and `SMAPI_ERR_NOLICENCE` (-2) if the desktop is not licensed for use.

### DesktopSave

Saves the current desktop to the specified file.

```c
long DesktopSave(boolean bSaveCopyAs, BSTR szFullPath, BSTR szComment, BSTR szNotes);
```

| Argument | Description |
|---|---|
| `bSaveCopyAs` | True to save a copy without changing the file name or modified state of the loaded desktop; False to save it under the new name. |
| `szFullPath` | Full path of the file to save. |
| `szComment` | Replaces the existing comment. An empty string leaves the comment unchanged. |
| `szNotes` | Replaces the existing notes. An empty string leaves the notes unchanged. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no desktop is loaded and `SMAPI_ERR_FILE` (-8) if the save fails.

### DesktopSaveEx

Saves the current desktop to the specified file, optionally with a different consortium.

```c
long DesktopSaveEx(
    [in] boolean bSaveCopyAs,
    [in] BSTR szFullPath,
    [in] BSTR szComment,
    [in] BSTR szNotes,
    [in] BSTR szConsortium);
```

| Argument | Description |
|---|---|
| `bSaveCopyAs` | True to save a copy without changing the file name or modified state of the loaded desktop; False to save it under the new name. |
| `szFullPath` | Full path of the file to save. |
| `szComment` | Replaces the existing comment. An empty string leaves the comment unchanged. |
| `szNotes` | Replaces the existing notes. An empty string leaves the notes unchanged. |
| `szConsortium` | Name of the consortium to save the desktop with, `"Disabled"` to remove team security, or an empty string to keep the current consortium. |

!!! note
    The consortium is applied only if your licence permits it (the desktop has no owner or you are its owner, and the consortium name is valid for your licence); otherwise `SMAPI_ERR_NOLICENCE` (-2) is returned. Set `szConsortium` to `"Disabled"` to remove team security and unlock the file. The consortium change also stays on the loaded desktop.

### EnableDataVersionBackup

Enables or disables the data version backup that is written when parameter values change. A message is written to the log file each time the setting changes.

```c
long EnableDataVersionBackup([in] boolean bEnable);
```

| Argument | Description |
|---|---|
| `bEnable` | True to enable backups; False to suspend them. |

!!! note
    Changes made to the data version while backups are suspended are not written to the backup file when backups are re-enabled. Suspending backups is useful to speed up a large number of parameter changes.

### ExportInputSignals

Exports the input signal configuration to an XML file.

```c
long ExportInputSignals(BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the XML file to write. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if the input signal configuration cannot be read.

### ExportToHexFile

Exports the PGV and DTV of the given application to a hex file.

```c
long ExportToHexFile([in] short wAppId);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |

!!! note
    The hex file is written beside the DTV in the edit buffer, with the same name and the extension .hex. Returns `SMAPI_ERR_NOAPP` (-9) if the application is not found or the file cannot be written. If no project is open, the method does nothing and returns 0.

### ExportProject

Exports the open project to a .smx file.

```c
long ExportProject([in] boolean bSaveModified);
```

| Argument | Description |
|---|---|
| `bSaveModified` | True to save all modified documents in the project, without prompting, before exporting. |

!!! note
    The .smx file is written beside the project file, with the same name, and replaces any existing file. The method does not report an error if the export itself fails.

### GenerateParamSet

Creates a parameter set file containing the given parameters.

```c
long GenerateParamSet([in] VARIANT aszIdentifiers, [in] BSTR pszFile);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | SAFEARRAY of strings containing the identifiers of the parameters to include. Parameters are searched for in all applications. |
| `pszFile` | Full path of the parameter set file. The extension .pms is added if it is missing. |

!!! note
    If an identifier is not found, no file is written and the lookup error is returned. Returns `SMAPI_ERR_FILE` (-8) if the file cannot be written.

### GeneratePULFile

Creates a PUL (parameter unlock list) file for an application for use with Reduced Data Access.

```c
long GeneratePULFile([in] WORD wAppId, [in] VARIANT aszIdentifiers, [in] BSTR pszPULFile);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | SAFEARRAY of strings containing the identifiers of the parameters to include. |
| `pszPULFile` | Full path of the PUL file (.pul) to create. |

!!! note
    After it is created, the file is renamed to include its checksum (`<name> - <checksum>.pul`), replacing any existing file of that name. This is required to reduce file lookup times. `pszPULFile` is an input only, so the new name is not returned. Use [GeneratePULFileFromParamSet](#generatepulfilefromparamset) if you need the final name. Returns `SMAPI_ERR_FILE` (-8) if the file cannot be written.

### GeneratePULFileFromParamSet

Creates a PUL (parameter unlock list) file for an application for use with Reduced Data Access, from a saved parameter set file.

```c
long GeneratePULFileFromParamSet(
    [in] short wAppId,
    [in] BSTR pszPMSFile,
    [in,out] BSTR* pszPULFile);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszPMSFile` | Full path of the parameter set file (.pms). |
| `pszPULFile` | On input, the full path of the PUL file (.pul) to create. On success, receives the full path of the renamed file. |

!!! note
    After it is created, the file is renamed to include its checksum (`<name> - <checksum>.pul`), replacing any existing file of that name. This is required to reduce file lookup times. Returns `SMAPI_ERR_FILE` (-8) if the parameter set file does not exist or the PUL file cannot be written, `SMAPI_ERR_PROGVER_NONE` (-6) if the application has no PGV, and `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the parameter set cannot be loaded.

### GetActiveApp

Returns the bitwise OR of the application Ids of all active applications.

```c
long GetActiveApp(short* pwResult);
```

| Argument | Description |
|---|---|
| `pwResult` | Receives the bitwise OR of the Ids of the active applications. |

### GetActiveAppEx

Returns the Ids of all active applications.

```c
long GetActiveAppEx(VARIANT * pawAppIds);
```

| Argument | Description |
|---|---|
| `pawAppIds` | Receives a 1-D, 0-based SAFEARRAY of short integers holding the Ids of the active applications. |

### GetActiveCANConfig

Gets whether the CAN configuration in the given slot is active.

```c
long GetActiveCANConfig([in] short wSlotId, [out] boolean* pbActive);
```

| Argument | Description |
|---|---|
| `wSlotId` | Slot index (1–16). |
| `pbActive` | Receives True if the configuration is active. False if it is inactive or the slot is empty. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wSlotId` is out of range.

### GetActiveRemoteLogging

Gets whether the remote logging configuration in the given slot is active.

```c
long GetActiveRemoteLogging([in] short wSlotId, [out] boolean* pbActive);
```

| Argument | Description |
|---|---|
| `wSlotId` | Slot index (1–8). |
| `pbActive` | Receives True if the configuration is active. False if it is inactive or the slot is empty. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wSlotId` is out of range.

### GetAppDetails

Retrieves the Id and name of each application in the open project.

```c
long GetAppDetails(VARIANT * pawAppIds, VARIANT * pastrAppNames);
```

| Argument | Description |
|---|---|
| `pawAppIds` | Receives a 1-D, 0-based SAFEARRAY of short integers holding the application Ids. |
| `pastrAppNames` | Receives a 1-D, 0-based SAFEARRAY of strings holding the application names, in the same order as `pawAppIds`. |

### GetAppPULFileName

Gets the name of the PUL (parameter unlock list) file used by the data version of the given application.

```c
long GetAppPULFileName([in] short wAppId, [out] BSTR* pszFileName);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszFileName` | Receives the name of the PUL file. Nothing is returned if the data version has no PUL file. If it has no PUL file name but carries the all-`0xFFFF` unlock checksum, `FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF.pul` is returned. |

### GetBuildNumber

Returns the build number of System Monitor. Client code can branch on the build number, so that one client script works with System Monitor releases that have different ActiveX interfaces.

```c
long GetBuildNumber(short* pwResult);
```

| Argument | Description |
|---|---|
| `pwResult` | Receives the build number (the last field of the System Monitor version number). |

!!! note
    A project does not need to be open.

### GetDataVersion

Returns the file name of the data version in the edit buffer for the given application.

```c
long GetDataVersion(short wAppId, BSTR* pszResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszResult` | Receives the full path of the data version in the edit buffer. |

### GetDataVersionComment

Returns the comment of the data version in the edit buffer for the given application.

```c
long GetDataVersionComment(short wAppId, BSTR* pszComment);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszComment` | Receives the data version comment. |

### GetDataVersionNotes

Returns the notes of the data version in the edit buffer for the given application.

```c
long GetDataVersionNotes(short wAppId, BSTR* pszNotes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszNotes` | Receives the data version notes. |

### GetDataVersionSavedOn

Returns the date and time the data version in the edit buffer for the given application was saved.

```c
long GetDataVersionSavedOn(short wAppId, BSTR* pszSavedOn);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszSavedOn` | Receives the saved-on date and time as text, formatted using the regional settings of the PC. |

### GetDesktopFileName

Gets the file name of the desktop loaded in the project.

```c
long GetDesktopFileName([out] BSTR* pszFileName);
```

| Argument | Description |
|---|---|
| `pszFileName` | Receives the full path of the desktop file. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if no desktop is loaded.

### GetDeviceProperties

Gets the properties of the devices on the main car connection.

```c
long GetDeviceProperties(
    [out] VARIANT* strw1xArrCommsPath,
    [out] VARIANT* str1xArrDeviceName,
    [out] VARIANT* w1xArrSerialNumber,
    [out] VARIANT* str1xArrAddress);
```

| Argument | Description |
|---|---|
| `strw1xArrCommsPath` | Receives a 1-D, 0-based SAFEARRAY of strings holding the comms path of each device. |
| `str1xArrDeviceName` | Receives a 1-D SAFEARRAY of strings holding the detected name of each device. |
| `w1xArrSerialNumber` | Receives a 1-D SAFEARRAY of long integers holding the serial number of each device. |
| `str1xArrAddress` | Receives a 1-D SAFEARRAY of strings holding the address of each device. For an IP link this is the device address (empty if it is the default car address). For other links it is the connection type name. |

### GetEcuDataVersion

Returns the file name of the data version on the ECU for the given application.

```c
long GetEcuDataVersion(short wAppId, BSTR* pszResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszResult` | Receives the full path of the data version on the ECU. Empty if the matching file was not found on disk. |

!!! note
    Returns `SMAPI_ERR_NONE_SPECIFIC` (-3) if the data version on the ECU is not known.

### GetErrors

Returns the current and logged errors of all applications in the project.

```c
long GetErrors(
    [out] VARIANT* str1xError,
    [out] VARIANT* str1xDescription,
    [out] VARIANT* w1xStatus);
```

| Argument | Description |
|---|---|
| `str1xError` | Receives a 1-D, 0-based SAFEARRAY of strings holding the error names. |
| `str1xDescription` | Receives a 1-D SAFEARRAY of strings holding the error descriptions. |
| `w1xStatus` | Receives a 1-D SAFEARRAY of short integers holding the status of each error:<br>`1` = Current<br>`2` = Logged |

### GetEvents

Returns the events defined for the given application.

```c
long GetEvents(
    [in] WORD wAppId,
    [out]WORD* pwCount,
    [out] VARIANT* pwEventIds,
    [out] VARIANT* pszEvents,
    [out] VARIANT* pwLevels);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pwCount` | Receives the number of events defined in the application. |
| `pwEventIds` | Receives a 1-D, 0-based SAFEARRAY of short integers holding the event Ids. |
| `pszEvents` | Receives a 1-D SAFEARRAY of strings holding the event descriptions. |
| `pwLevels` | Receives a 1-D SAFEARRAY of short integers holding the event levels:<br>`0` = High<br>`1` = Medium<br>`2` = Low<br>`3` = Debug |

!!! note
    Returns `SMAPI_ERR_NOLICENCE` (-2) if the PGV uses enhanced Reduced Data Access and is owned by another team.

### GetEventDetails

Returns the details of an event defined in the given application.

```c
long GetEventDetails(
    [in] WORD wEventId,
    [in] WORD wAppId,
    [out]BSTR* pszDescription,
    [out] BSTR* pszConv1,
    [out] BSTR* pszConv2,
    [out] BSTR* pszConv3,
    [out] WORD* pwLevel);
```

| Argument | Description |
|---|---|
| `wEventId` | Event Id. |
| `wAppId` | Application Id. |
| `pszDescription` | Receives the event description. |
| `pszConv1` | Receives the Id of the first event conversion. |
| `pszConv2` | Receives the Id of the second event conversion. |
| `pszConv3` | Receives the Id of the third event conversion. |
| `pwLevel` | Receives the event level:<br>`0` = High<br>`1` = Medium<br>`2` = Low<br>`3` = Debug |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if the event is not defined, and `SMAPI_ERR_NOLICENCE` (-2) if the PGV uses enhanced Reduced Data Access and is owned by another team.

### GetFIACANConfig

Gets whether the CAN configuration in the given slot is set as an FIA CAN configuration.

```c
long GetFIACANConfig([in] short wSlotId, [out] boolean* pbActive);
```

| Argument | Description |
|---|---|
| `wSlotId` | Slot index (1–16). |
| `pbActive` | Receives True if the configuration is set as FIA. False if it is not, or if the slot is empty. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wSlotId` is out of range.

### GetFileDetails

Gets the file details (saved by, save date, notes, comments, build and security details) of any file type supported by System Monitor. The file is read from disk; it does not need to be open.

```c
long GetFileDetails(
    [in] BSTR szFileName,
    [out] BSTR* pszSavedBy,
    [out] DATE* pdtSaveOn,
    [out] BSTR* pszNotes,
    [out] BSTR* pszComments,
    [out] WORD* pwBuild,
    [out] BSTR* pszConsortium,
    [out] BSTR* pszOwner,
    [out] BSTR* pszRDA);
```

| Argument | Description |
|---|---|
| `szFileName` | Full path of the file to read. |
| `pszSavedBy` | Receives the name of the last user to save the file. |
| `pdtSaveOn` | Receives the date and time the file was last saved. |
| `pszNotes` | Receives the file notes. |
| `pszComments` | Receives the file comment. |
| `pwBuild` | Receives the System Monitor build number used to save the file. |
| `pszConsortium` | Receives the name of the licence consortium the file is saved to, or `Unlocked` if it has none. Set for .dtv, .rlc and .dtp files only. |
| `pszOwner` | Receives the name of the licence owner of the file. Set for .dtv, .rlc and .dtp files only. |
| `pszRDA` | Receives the RDA unlock list checksum of a locked data version. Set for .dtv files only. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the file does not exist, is not a type System Monitor supports, or cannot be read.

### GetLicenceDetails

Gets the active consortium name and licence owner.

```c
long GetLicenceDetails([out] BSTR* pszConsortium, [out] BSTR* pszOwner);
```

| Argument | Description |
|---|---|
| `pszConsortium` | Receives the name of the active consortium set in the licence. |
| `pszOwner` | Receives the name of the licence owner. |

!!! note
    Returns `SMAPI_ERR_NOLICENCE` (-2) if either the consortium or the owner is empty.

### GetLogFolder

Gets the current log folder location.

```c
long GetLogFolder([out] BSTR* pszFolder);
```

| Argument | Description |
|---|---|
| `pszFolder` | Receives the path of the log folder. |

### GetMultiApplicationBase

Gets the name and path of the active Multi-Application Base.

```c
long GetMultiApplicationBase([out] BSTR* pszName, [out] BSTR* pszPath);
```

| Argument | Description |
|---|---|
| `pszName` | Receives the name of the active Multi-Application Base. |
| `pszPath` | Receives the directory of the active Multi-Application Base. |

!!! note
    Can only be called when no project is open; otherwise returns `SMAPI_ERR_BAD_STATE` (-30). Returns `SMAPI_ERR_NO_CUSTOMER_BASE` (-42) if System Monitor is set to use unit definitions instead of Multi-Application Bases.

### GetMultiApplicationBases

Gets the names and paths of all defined Multi-Application Bases.

```c
long GetMultiApplicationBases([out] VARIANT * paNames, [out] VARIANT * paPaths);
```

| Argument | Description |
|---|---|
| `paNames` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the base names. |
| `paPaths` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the base directories, in the same order as `paNames`. |

!!! note
    Can only be called when no project is open; otherwise returns `SMAPI_ERR_BAD_STATE` (-30). Returns `SMAPI_ERR_NO_CUSTOMER_BASE` (-42) if System Monitor is set to use unit definitions instead of Multi-Application Bases.

### GetNextDataVersion

Gets the file name of the next data version that will be saved if the user selects File, Save. If the edit buffer is unmodified, this is the name of the current data version in the edit buffer.

```c
long GetNextDataVersion(short wAppId, BSTR* pszResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszResult` | Receives the full path of the next data version file. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the project has no data version for the application.

### GetPPOFileName

Gets the name of the PPO file used by the project.

```c
long GetPPOFileName([out] BSTR* pszFileName);
```

| Argument | Description |
|---|---|
| `pszFileName` | Receives the name and path of the PPO file, taken from the unit definition or, if none, from the active Multi-Application Base. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if no PPO file setting is found.

### GetProgramVersionID

Gets the program version ID of the currently loaded program version.

```c
long GetProgramVersionID(short wAppId, short* pwResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pwResult` | Receives the program version ID (the high word of the program version identifier). |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the project has no program version for the application.

### GetProgramVersionIDEx

Gets the program version ID of the currently loaded program version. Same as [GetProgramVersionID](#getprogramversionid) but with unsigned (`WORD`) arguments.

```c
long GetProgramVersionIDEx(WORD wAppId, WORD* pwResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pwResult` | Receives the program version ID (the high word of the program version identifier). |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the project has no program version for the application.

### GetProjectFileName

Gets the name of the project file.

```c
long GetProjectFileName([out] BSTR* pszFileName);
```

| Argument | Description |
|---|---|
| `pszFileName` | Receives the name and path of the project file. |

### GetRemoteLoggingDuration

Gets the estimated logging time and number of laps that can be recorded with the remote logging configuration.

```c
long GetRemoteLoggingDuration(
    [out] DATE* pdtEstimatedLoggingTime,
    [out] double* pdEstimatedLoggingLaps);
```

| Argument | Description |
|---|---|
| `pdtEstimatedLoggingTime` | Receives the estimated logging time available in recording memory, as a date/time counted from 01/01/1970 00:00:00 (for example, 2 hours is returned as 01/01/1970 02:00:00). |
| `pdEstimatedLoggingLaps` | Receives the estimated number of laps available in recording memory. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no remote logging configuration is loaded.

### GetRemoteLoggingRates

Gets the logging and telemetry rates of all channels in the remote logging configuration.

```c
long GetRemoteLoggingRates([out] VARIANT* pafLogging, [out] VARIANT* pafTelemetry);
```

| Argument | Description |
|---|---|
| `pafLogging` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_R8`), one element per channel, holding the logging rate of each channel. Channels not enabled for logging are 0. |
| `pafTelemetry` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_R8`), one element per channel, holding the telemetry rate of each channel. Channels not enabled for telemetry are 0. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no remote logging configuration is loaded.

### GetRemoteSlotCount

Gets the number of logging slots used in the remote logging configuration.

```c
long GetRemoteSlotCount([out] short* wSlotCount);
```

| Argument | Description |
|---|---|
| `wSlotCount` | Receives the total number of slots used. 0 if no remote logging configuration is loaded. |

### GetVersionNumber

Gets the version information of the System Monitor executable.

```c
long GetVersionNumber(
    [out] short* pwMajorVersion,
    [out] short* pwMinorVersion,
    [out] short* pwReleaseVersion);
```

| Argument | Description |
|---|---|
| `pwMajorVersion` | Receives the major version. |
| `pwMinorVersion` | Receives the minor version. |
| `pwReleaseVersion` | Receives the build number. |

### GetVirtualParametersFileName

Gets the name of the virtual parameters file in the project.

```c
long GetVirtualParametersFileName([out] BSTR* pszFileName);
```

| Argument | Description |
|---|---|
| `pszFileName` | Receives the name and path of the virtual parameters file. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if no virtual parameters file is loaded.

### ImportInputSignals

Imports the input signal configuration from an XML file.

```c
long ImportInputSignals(BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the XML file. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if the input signal configuration cannot be created. The result of reading the XML file is not checked, so an unreadable file does not produce an error code.

### ImportProject

Imports a project from a .smx file into the given Multi-Application Base. The files in the .smx are extracted into the base directory. The active base is restored afterwards.

```c
long ImportProject([in] BSTR szFullPath, [in] BSTR szBase);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the .smx file containing the project to import. |
| `szBase` | Name of the Multi-Application Base to import into (not case-sensitive). |

!!! note
    Returns `SMAPI_ERR_NO_CUSTOMER_BASE` (-42) if `szBase` does not match a defined Multi-Application Base, and `SMAPI_ERR_FILE` (-8) if the .smx file does not exist or cannot be extracted.

### MatlabExportSelected

Exports the listed editable parameters and axes of an application to a file in MATLAB format.

```c
long MatlabExportSelected(
    short wAppId,
    BSTR szFullPath,
    boolean bDataOnly,
    VARIANT rSelectedParams);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szFullPath` | Full path of the file to create. |
| `bDataOnly` | True to export data only; False to export data and definitions. |
| `rSelectedParams` | 1-D SAFEARRAY of strings (`VT_BSTR`) holding the identifiers of the parameters to export. Editable parameters and standard axes are accepted. |

!!! note
    Each parameter is looked up in turn and an identifier that is not found is skipped; the value returned is the result for the last identifier in the array. If there is no project, no data version for `wAppId`, or the file cannot be created, nothing is exported and the method still returns 0 (unless `rSelectedParams` is not a valid string array).

### MatlabImport

Imports the specified MATLAB .m file into System Monitor.

```c
long MatlabImport(BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the MATLAB .m file. |

!!! note
    If the import fails, returns the specific error found during the import, or `SMAPI_ERR_NONE_SPECIFIC` (-3) if there is none.

### MatLabMExport

Exports all parameters of the currently loaded data version of an application to a file in MATLAB .m format.

```c
long MatLabMExport(short wAppId, BSTR szFullPath, boolean bDataOnly);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szFullPath` | Full path of the file to create. |
| `bDataOnly` | True to export data only; False to export data and definitions. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the export fails (for example, the file cannot be created).

### MatLabMExportEx

Exports the currently loaded data version of an application to a file in MATLAB .m format, including only the parameter types selected in `dwType`.

```c
long MatLabMExportEx(short wAppId, BSTR szFullPath, boolean bDataOnly, DWORD dwType);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szFullPath` | Full path of the file to create. |
| `bDataOnly` | True to export data only; False to export data and definitions. |
| `dwType` | Bit mask of the parameter types to include. Combine with OR:<br>`0x00000001` = Scalar<br>`0x00000002` = 1-axis map<br>`0x00000004` = 2-axis map<br>`0x00000008` = 3-axis map<br>`0x00000010` = Array<br>`0x00000020` = String<br>`0x00000080` = ECU (measurement)<br>`0x00030000` = Axes<br>`0xFFFFFFFF` = All types |

!!! note
    Axes are exported only when both axis bits (`0x00030000`) are set. Returns `SMAPI_ERR_FILE` (-8) if the export fails.

### MatLabMExportForDTV

Exports the specified data version file to a file in MATLAB .m format, including only the parameter types selected in `dwType`. The data version is opened from disk and does not need to be loaded in the project.

```c
long MatLabMExportForDTV(
    [in] BSTR szDTV,
    [in] BSTR szExport,
    [in] boolean bDataOnly,
    [in] DWORD dwType);
```

| Argument | Description |
|---|---|
| `szDTV` | Full path of the DTV file. |
| `szExport` | Full path of the file to create. |
| `bDataOnly` | True to export data only; False to export data and definitions. |
| `dwType` | Bit mask of the parameter types to include. Combine with OR:<br>`0x00000001` = Scalar<br>`0x00000002` = 1-axis map<br>`0x00000004` = 2-axis map<br>`0x00000008` = 3-axis map<br>`0x00000010` = Array<br>`0x00000020` = String<br>`0x00000080` = ECU (measurement)<br>`0x00030000` = Axes<br>`0xFFFFFFFF` = All types |

!!! note
    A project must be open. If the data version is locked and the licence does not own it, only the parameters in its unlock (PUL) list are exported. Returns `SMAPI_ERR_FILE` (-8) if the export fails.

### OpenProject

Opens a project.

```c
long OpenProject(BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the project file to open. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the file does not exist, `SMAPI_ERR_NO_CUSTOMER_BASE` (-42) if no Multi-Application Base matches the project, and `SMAPI_ERR_NONE_SPECIFIC` (-3) if the project fails to open.

### RemoteGet

Gets the name of the remote logging configuration file in the given slot.

```c
long RemoteGet([in] short wIndex, [out] BSTR* pszFileName);
```

| Argument | Description |
|---|---|
| `wIndex` | 0-based slot index: `0` = slot 1 … `7` = slot 8. |
| `pszFileName` | Receives the name and path of the configuration file. |

!!! note
    Unlike the other remote logging slot methods, which take 1–8, this method takes a 0-based index. Returns `SMAPI_ERR_FILE` (-8) if no configuration is loaded in the slot.

### RemoteGetAll

Gets the file names of all active remote logging configurations.

```c
long RemoteGetAll([out] VARIANT* str1xArrFileNames);
```

| Argument | Description |
|---|---|
| `str1xArrFileNames` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`). Element `n` holds the file name of the configuration in slot `n`+1 if that configuration is active; other elements are empty. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no remote logging configuration is loaded, and `SMAPI_ERR_FILE` (-8) if no slot holds an active configuration.

### RemoteLoggingLoad

Loads the specified remote logging configuration file into slot 1.

```c
long RemoteLoggingLoad([in] BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the configuration file (.rlc) to load. |

!!! note
    Returns `SMAPI_ERR_NOLICENCE` (-2) if the licence does not give access to the file's consortium, and `SMAPI_ERR_FILE` (-8) if the file cannot be loaded.

### RemoteLoggingLoadEx

Loads the specified remote logging configuration file into the given slot and optionally makes it active.

```c
long RemoteLoggingLoadEx(
    [in] short wIndex,
    [in] BSTR pszFileName,
    [in] boolean bActivate);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index (1–8). |
| `pszFileName` | Full path of the configuration file (.rlc). |
| `bActivate` | True to make the configuration active. A configuration loaded into slot 1 is always active. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is outside 1–8, `SMAPI_ERR_NOLICENCE` (-2) if the licence does not give access to the file's consortium, and `SMAPI_ERR_FILE` (-8) if the file cannot be loaded.

### RemoteLoggingSave

Saves the current remote logging configuration to the specified file.

```c
long RemoteLoggingSave(
    boolean bSaveCopyAs,
    BSTR szFullPath,
    BSTR szComment,
    BSTR szNotes);
```

| Argument | Description |
|---|---|
| `bSaveCopyAs` | True to save a copy without changing the configuration's file name or modified status; the original comment and notes are restored after the save. False to save the configuration to the new file. |
| `szFullPath` | Full path of the file to save. |
| `szComment` | Comment to save with the file. An empty string keeps the existing comment. |
| `szNotes` | Notes to save with the file, replacing the existing notes. An empty string keeps the existing notes. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no remote logging configuration is loaded, and `SMAPI_ERR_FILE` (-8) if the save fails.

### RemoteLoggingSaveEx

Saves the current remote logging configuration to the specified file and optionally sets its consortium.

```c
long RemoteLoggingSaveEx(
    [in] boolean bSaveCopyAs,
    [in] BSTR szFullPath,
    [in] BSTR szComment,
    [in] BSTR szNotes,
    [in] BSTR szConsortium);
```

| Argument | Description |
|---|---|
| `bSaveCopyAs` | True to save a copy without changing the configuration's file name or modified status; the original comment and notes are restored after the save. False to save the configuration to the new file. |
| `szFullPath` | Full path of the file to save. |
| `szComment` | Comment to save with the file. An empty string keeps the existing comment. |
| `szNotes` | Notes to save with the file, replacing the existing notes. An empty string keeps the existing notes. |
| `szConsortium` | Consortium name to save the configuration to, or `Disabled` to remove team security and unlock the file. An empty string keeps the current consortium. |

!!! note
    The consortium is set only if the licence permits it: the configuration must have no owner or be owned by the current licence owner, and the name must be a consortium available in the licence. Otherwise the method returns `SMAPI_ERR_NOLICENCE` (-2) and does not save. Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no remote logging configuration is loaded, and `SMAPI_ERR_FILE` (-8) if the save fails.

### RemoteLoggingUnload

Unloads the remote logging configuration from the given slot.

```c
long RemoteLoggingUnload([in] short wIndex);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index (2–8). Slot 1 cannot be unloaded. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is outside 2–8 or no configuration is loaded in the slot.

### RemoveApplication

Removes the given application from the project. The application cannot be the BIOS.

```c
long RemoveApplication([in] WORD wAppId);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project or is the BIOS.

### RemoveParameterFromUnlockList

Updates the PUL (parameter unlock list) file of an application for use with Reduced Data Access by removing the given parameters, then applies the new PUL file to the application's data version.

```c
long RemoveParameterFromUnlockList(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] BSTR* pszPULFile);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of strings (`VT_BSTR`) holding the identifiers of the parameters to remove from the PUL file. |
| `pszPULFile` | Receives the file name of the updated PUL file. |

!!! note
    The PUL file name is adjusted to include the new checksum (`<name> - <checksum>.pul`), and the adjusted name is returned in `pszPULFile`. The data version must be locked and already have a PUL file; otherwise returns `SMAPI_ERR_FILE` (-8). Returns `SMAPI_ERR_NOAPP` (-9) if the project has no data version for the application, and `SMAPI_ERR_PARAM_NOT_VALID` (-28) if an identifier is not found (the PUL file is then not updated).

### SaveProject

Saves the current project.

```c
long SaveProject(boolean bSaveAll);
```

| Argument | Description |
|---|---|
| `bSaveAll` | True to save all modified files without prompting. False to save only the project file. |

!!! note
    Always returns 0, even if no project is open or the save fails.

### SaveProjectAs

Saves the current project under a new name, with new comment and notes.

```c
long SaveProjectAs(
    [in] BSTR szNewName,
    [in] boolean bSaveAll,
    [in] BSTR szComment,
    [in] BSTR szNotes);
```

| Argument | Description |
|---|---|
| `szNewName` | New project file name. `.prj` is added if missing. A relative name is placed in the base directory. |
| `bSaveAll` | True to also save all other modified files without prompting. False to save only the project file. |
| `szComment` | New project comment. Replaces the existing comment (an empty string clears it). |
| `szNotes` | New project notes. Replace the existing notes (an empty string clears them). |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if `szNewName` is a relative path and no base directory is set.

### SetActiveApp

Sets the active applications in the project.

```c
long SetActiveApp(short wResult);
```

| Argument | Description |
|---|---|
| `wResult` | Application Id. The value is used as a bit mask: every application in the project whose Id has a bit in common with it is made active, and all others are made inactive. |

!!! note
    Returns `SMAPI_ERR_LIVEUPDATESON` (-11) if live tune is on. Use [SetActiveAppEx](#setactiveappex) to pass an explicit list of Ids.

### SetActiveAppEx

Sets the active applications in the project. Applications whose Ids are in the array are made active; all others are made inactive.

```c
long SetActiveAppEx(VARIANT awAppIds);
```

| Argument | Description |
|---|---|
| `awAppIds` | 1-D SAFEARRAY of shorts (`VT_I2`) holding the Ids of the applications to make active. |

!!! note
    Returns `SMAPI_ERR_LIVEUPDATESON` (-11) if live tune is on.

### SetActiveCANConfig

Sets the active status of the CAN configuration in the given slot.

```c
long SetActiveCANConfig([in] short wIndex, [in] boolean bActivate);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index (1–16). |
| `bActivate` | True to make the configuration active; False to make it inactive. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no CAN configuration is loaded in the slot. If activating results in duplicate parameter identifiers, the configuration is deactivated again and `SMAPI_ERR_PARAM_NOT_VALID` (-28) is returned.

### SetActiveRemoteLogging

Sets the active status of the remote logging configuration in the given slot.

```c
long SetActiveRemoteLogging([in] short wIndex, [in] boolean bActivate);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index (1–8). |
| `bActivate` | True to make the configuration active; False to make it inactive. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no remote logging configuration is loaded in the slot.

### SetAppPULFile

Sets the PUL (parameter unlock list) file of the given application's data version. The file name must end with the file's own checksum (`<name> - <checksum>.pul`). The file is also copied to the configured global unlock list folders.

```c
long SetAppPULFile([in] WORD wAppId, [in] BSTR szFileName);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szFileName` | Full path of the PUL file. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project, `SMAPI_ERR_DATAVER_NONE` (-5) if it has no data version, `SMAPI_ERR_NOLICENCE` (-2) if the data version is locked and owned by another licence owner, and `SMAPI_ERR_FILE` (-8) if the file does not exist, its name does not match its checksum, or it cannot be opened.

### SetDataVersionComment

Sets the data version comment for the specified application.

```c
long SetDataVersionComment([in] WORD wAppId, [in] BSTR szComment);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szComment` | Data version comment. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project and `SMAPI_ERR_DATAVER_NONE` (-5) if it has no data version.

### SetDataVersionNotes

Sets the data version notes for the specified application, replacing the existing notes.

```c
long SetDataVersionNotes([in] short wAppId, [in] BSTR szNotes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szNotes` | Data version notes. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project and `SMAPI_ERR_DATAVER_NONE` (-5) if it has no data version.

### SetFIACANConfig

Sets the FIA status of the CAN configuration in the given slot and makes the configuration active. Equivalent to [SetFIACANConfigEx](#setfiacanconfigex) with `bActive` True.

```c
long SetFIACANConfig([in] short wIndex);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index (2–16). |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is outside 2–16 or no CAN configuration is loaded in the slot. If the change results in duplicate parameter identifiers, the configuration is deactivated and `SMAPI_ERR_PARAM_NOT_VALID` (-28) is returned.

### SetFIACANConfigEx

Sets or clears the FIA status of the CAN configuration in the given slot.

```c
long SetFIACANConfigEx([in] short wIndex, [in] boolean bActive);
```

| Argument | Description |
|---|---|
| `wIndex` | Slot index (2–16). |
| `bActive` | True to set the FIA status and make the configuration active. False to clear the FIA status; the active status is not changed. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is outside 2–16 or no CAN configuration is loaded in the slot. If the change results in duplicate parameter identifiers, the configuration is deactivated and `SMAPI_ERR_PARAM_NOT_VALID` (-28) is returned.

### SetMultiApplicationBase

Sets the active Multi-Application Base.

```c
long SetMultiApplicationBase([in] BSTR szName);
```

| Argument | Description |
|---|---|
| `szName` | Name of the Multi-Application Base (case-sensitive). |

!!! note
    Can only be called when no project is open. Returns `SMAPI_ERR_BAD_STATE` (-30) if a project is open or no base has the given name, and `SMAPI_ERR_NO_CUSTOMER_BASE` (-42) if System Monitor is set to use unit definitions instead of Multi-Application Bases.

### UploadDataVersion

Uploads the data of the given application from the ECU into the edit buffer.

```c
long UploadDataVersion(short wAppId);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |

!!! note
    Requires communication with the ECU. Returns `SMAPI_ERR_LIVEUPDATESON` (-11) if live tune is on, `SMAPI_ERR_NOAPP` (-9) if the application is not in the project, and `SMAPI_ERR_NONE_SPECIFIC` (-3) if the upload fails.

### VirtualParametersExport

Exports virtual parameters to an XML file. If a group name is given, only that group of the virtual parameter tree is exported. All virtual parameters that the exported parameters depend on are also included.

```c
long VirtualParametersExport([in] BSTR szName, [in] BSTR szGroup);
```

| Argument | Description |
|---|---|
| `szName` | Full path of the file to export to. |
| `szGroup` | Name of the group to export. An empty string exports all virtual parameters. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the export fails, for example if the group is not found.

### VirtualParametersImport

Imports the specified virtual parameter file and merges it with the current virtual parameters.

```c
long VirtualParametersImport([in] BSTR szName);
```

| Argument | Description |
|---|---|
| `szName` | Full path of the file to import. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the import fails.

### VirtualParametersLoad

Loads the specified virtual parameter file, replacing the current one.

```c
long VirtualParametersLoad([in] BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the file to load. |

!!! note
    Returns `SMAPI_ERR_FILE_NEEDS_SAVING` (-40) if the current virtual parameter file has unsaved changes; save it first or use [VirtualParametersLoadNoSave](#virtualparametersloadnosave). Returns `SMAPI_ERR_FILE` (-8) if the file cannot be loaded.

### VirtualParametersLoadNoSave

Loads the specified virtual parameter file, replacing the current one without saving it. Unsaved changes to the current file are discarded.

```c
long VirtualParametersLoadNoSave([in] BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path of the file to load. |

!!! note
    Returns `SMAPI_ERR_FILE` (-8) if the file cannot be loaded.

### VirtualParametersSave

Saves the current virtual parameters to the specified file.

```c
long VirtualParametersSave(
    boolean bSaveCopyAs,
    BSTR szFullPath,
    BSTR szComment,
    BSTR szNotes);
```

| Argument | Description |
|---|---|
| `bSaveCopyAs` | True to save a copy without changing the file name or modified status; the original comment and notes are restored after the save. False to save to the new file. |
| `szFullPath` | Full path of the file to save. |
| `szComment` | Comment to save with the file. An empty string keeps the existing comment. |
| `szNotes` | Notes to save with the file, replacing the existing notes. An empty string keeps the existing notes. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if no virtual parameters file is loaded, and `SMAPI_ERR_FILE` (-8) if the save fails.

**See also:** [ActiveX Methods](index.md); [ActiveX Error Codes](../activex-errors/activex-error-codes.md)
