# Data Acquisition

Methods for live, burst and remote logging, including remote logging parameters, channels and trigger conditions.

The methods are grouped as: [General](#functions---general), [Burst Parameters](#functions---burst-parameters), [Remote Parameters](#functions---remote-parameters).

See [ActiveX Methods](index.md) for the conventions used on this page, and [ActiveX Error Codes](../activex-errors/activex-error-codes.md) for the return codes.

## Functions - General

### DownloadExternalInputs

Downloads the external inputs (sensor bus) configuration to the main car.

```c
long DownloadExternalInputs();
```

This method takes no arguments.

!!! note
    The download always goes to the main car, whatever car is selected with [SelectCar](#selectcar). The return code does not report whether the transfer succeeded.

### DumpErrors

Writes the errors of all applications that are currently active or logged to a tab-separated text file (name, description and status of each error).

```c
long DumpErrors(BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path and file name of the file to write. An existing file is overwritten. |

Returns `SMAPI_ERR_FILE` (-8) if the file cannot be written.

!!! note
    Only those errors included in the live logging configuration will be dumped.

### DumpEvents

Writes all events received since the Event window was last cleared to a file.

```c
long DumpEvents(BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path and file name of the file to write. |

Returns `SMAPI_ERR_FILE` (-8) if the file cannot be written.

### DumpRowData

Writes the current values of the parameters in the live logging configuration to a file, one parameter identifier and scaled value per line, preceded by the date and time.

```c
long DumpRowData(BSTR szFullPath);
```

| Argument | Description |
|---|---|
| `szFullPath` | Full path and file name of the file to write. An existing file is overwritten. |

Returns `SMAPI_ERR_DUMPROW` (-201) if the file cannot be written, and `SMAPI_ERR_NONE_SPECIFIC` (-3) if there is no live logging configuration.

!!! note
    Only parameters included in the live logging configuration are dumped.

### GetErrorDefinitions

Gets the error definitions of an application.

```c
long GetErrorDefinitions(
    [in] short wAppId,
    [out] WORD* pwCount,
    [out] VARIANT* paszNames,
    [out] VARIANT* paszIdentifiers,
    [out] VARIANT* paszDescriptions,
    [out] VARIANT* paszGroup,
    [out] VARIANT* pawBitNumber,
    [out] VARIANT* paszCurrent,
    [out] VARIANT* paszLogged);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pwCount` | Receives the number of error definitions returned. |
| `paszNames` | Receives a 1-D, 0-based SAFEARRAY of `BSTR`: the name of each error. |
| `paszIdentifiers` | Receives a 1-D, 0-based SAFEARRAY of `BSTR`: the identifier of each error. |
| `paszDescriptions` | Receives a 1-D, 0-based SAFEARRAY of `BSTR`: the description of each error. |
| `paszGroup` | Receives a 1-D, 0-based SAFEARRAY of `BSTR`: the error group each error belongs to. |
| `pawBitNumber` | Receives a 1-D, 0-based SAFEARRAY of `short`: the bit number of each error in its current and logged parameters. |
| `paszCurrent` | Receives a 1-D, 0-based SAFEARRAY of `BSTR`: the identifier of the current error parameter of each error. |
| `paszLogged` | Receives a 1-D, 0-based SAFEARRAY of `BSTR`: the identifier of the logged error parameter of each error. |

All arrays have one element per error, in the same order. Errors with an enhanced lock level are not returned. Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project.

### GetLiveLogging

Gets whether Live Logging is currently recording.

```c
long GetLiveLogging([out] boolean* bResult);
```

| Argument | Description |
|---|---|
| `bResult` | Receives True if Live Logging is recording, otherwise False. |

### GetProgramVersionPath

Gets the full path of the program version (PGV) file of an application.

```c
long GetProgramVersionPath(short wAppId, BSTR* pszResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszResult` | Receives the full path of the PGV file. |

Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project.

### SelectCar

Selects the car that later burst and remote logging download and upload calls apply to.

```c
long SelectCar(short wCar);
```

| Argument | Description |
|---|---|
| `wCar` | `1` = Main car<br>`2` = Spare car<br>Selecting the spare car starts it; selecting the main car stops the spare car. Other values are ignored. |

### SetLiveLogging

Starts or stops Live Logging recording.

```c
long SetLiveLogging([in] boolean bState);
```

| Argument | Description |
|---|---|
| `bState` | True to start Live Logging, False to stop it. |

Returns `SMAPI_ERR_BAD_STATE` (-30) if asked to start while already recording or to stop while not recording, and `SMAPI_ERR_FILE` (-8) if there is no live logging configuration.

## Functions - Burst Parameters

### BurstLoggingSave

Saves the current burst logging configuration to a file.

```c
long BurstLoggingSave(boolean bSaveCopyAs, BSTR szFullPath, BSTR szComment, BSTR szNotes);
```

| Argument | Description |
|---|---|
| `bSaveCopyAs` | True to save a copy: the loaded configuration keeps its file name and modified state, and the comment and notes are applied to the copy only. False to save the configuration under the new file name. |
| `szFullPath` | Full path and file name to save to. |
| `szComment` | Comment to store in the file. An empty string keeps the existing comment. |
| `szNotes` | Notes to store in the file, replacing the existing notes. An empty string keeps the existing notes. |

Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no burst logging configuration, and `SMAPI_ERR_FILE` (-8) if the save fails.

### DownloadBurst

Downloads the burst logging configuration to the ECU of the selected car.

```c
long DownloadBurst();
```

This method takes no arguments.

!!! note
    The return code does not report whether the download succeeded.

### GetBurstSessionDetail

Gets the value of a session detail from the burst logging configuration.

```c
long GetBurstSessionDetail(BSTR szName, BSTR* pszValue);
```

| Argument | Description |
|---|---|
| `szName` | Name of the session detail. It must match a session detail defined in the configuration. |
| `pszValue` | Receives the value of the session detail. |

Returns `SMAPI_ERR_DETAIL_UNKNOWN` (-200) if the session detail does not exist, and `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no burst logging configuration.

!!! note
    This and the other session detail functions operate on the logging configuration loaded in System Monitor, which does not necessarily match the configuration in the ECU.

### SetBurstSessionDetail

Sets the value of a session detail in the burst logging configuration.

```c
long SetBurstSessionDetail(BSTR szName, BSTR szValue);
```

| Argument | Description |
|---|---|
| `szName` | Name of the session detail. It must match a session detail defined in the configuration. |
| `szValue` | New value of the session detail. |

Returns `SMAPI_ERR_DETAIL_UNKNOWN` (-200) if the session detail does not exist, and `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no burst logging configuration.

### UploadBurst

Uploads the burst logging configuration from the ECU of the selected car.

```c
long UploadBurst();
```

This method takes no arguments.

!!! note
    The return code does not report whether the upload succeeded.

## Functions - Remote Parameters

### AddRemoteParam

Adds a measurement parameter to a channel of the current remote logging configuration.

```c
long AddRemoteParam(
    short wAppId,
    BSTR pszParamId,
    short wChannel,
    short wValue,
    short wValueType);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszParamId` | Unique parameter identifier. |
| `wChannel` | 0-based channel index (channel 1 = 0). |
| `wValue` | Logging value. For type Frequency, one of the logging frequencies supported by the configuration; for other types, the engine segment or cycle value. |
| `wValueType` | Type of `wValue` ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)):<br>`0` = Frequency<br>`1` = Cylinder/engine segment<br>`2` = Cycle<br>`3` = Unknown<br>`4` = Edge |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the value is not valid for the value type, `SMAPI_ERR_DOCUMENTFULL` (-35) if the configuration is full, `SMAPI_ERR_FREQ_OVERRIDDEN` (-41) if the frequency was overridden to the minimum frequency of the prime parameter, and `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

### AddRemoteParamEx

Adds a measurement parameter to a channel of the current remote logging configuration. Same as [AddRemoteParam](#addremoteparam), but the logging value is a `long`, which allows higher frequencies.

```c
long AddRemoteParamEx(
    [in] short wAppId,
    [in] BSTR pszParamId,
    [in] short wChannel,
    [in] long lValue,
    [in] short wValueType);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszParamId` | Unique parameter identifier. |
| `wChannel` | 0-based channel index (channel 1 = 0). |
| `lValue` | Logging value. For type Frequency, one of the logging frequencies supported by the configuration; for other types, the engine segment or cycle value. |
| `wValueType` | Type of `lValue` ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)):<br>`0` = Frequency<br>`1` = Cylinder/engine segment<br>`2` = Cycle<br>`3` = Unknown<br>`4` = Edge |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the value is not valid for the value type, `SMAPI_ERR_DOCUMENTFULL` (-35) if the configuration is full, `SMAPI_ERR_FREQ_OVERRIDDEN` (-41) if the frequency was overridden to the minimum frequency of the prime parameter, and `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

### AddRemoteVirtualParam

Adds a virtual parameter to a channel of the current remote logging configuration.

```c
long AddRemoteVirtualParam(
    BSTR pszParamId,
    short wChannel,
    short wValue,
    short wValueType);
```

| Argument | Description |
|---|---|
| `pszParamId` | Unique identifier of the virtual parameter. |
| `wChannel` | 0-based channel index (channel 1 = 0). |
| `wValue` | Logging value. For type Frequency, one of the logging frequencies supported by the configuration; for other types, the engine segment or cycle value. |
| `wValueType` | Type of `wValue` ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)):<br>`0` = Frequency<br>`1` = Cylinder/engine segment<br>`2` = Cycle<br>`3` = Unknown<br>`4` = Edge |

Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the project has no virtual parameters, `SMAPI_ERR_PARAMNOTFOUND` (-100) if the virtual parameter does not exist, `SMAPI_ERR_INVALID_CMD` (-31) if the value is not valid for the value type, and `SMAPI_ERR_DOCUMENTFULL` (-35) if the configuration is full.

### AddRemoteVirtualParamEx

Adds a virtual parameter to a channel of the current remote logging configuration. Same as [AddRemoteVirtualParam](#addremotevirtualparam), but the logging value is a `long`, which allows higher frequencies.

```c
long AddRemoteVirtualParamEx(
    BSTR pszParamId,
    short wChannel,
    long dwValue,
    short wValueType);
```

| Argument | Description |
|---|---|
| `pszParamId` | Unique identifier of the virtual parameter. |
| `wChannel` | 0-based channel index (channel 1 = 0). |
| `dwValue` | Logging value. For type Frequency, one of the logging frequencies supported by the configuration; for other types, the engine segment or cycle value. |
| `wValueType` | Type of `dwValue` ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)):<br>`0` = Frequency<br>`1` = Cylinder/engine segment<br>`2` = Cycle<br>`3` = Unknown<br>`4` = Edge |

Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the project has no virtual parameters, `SMAPI_ERR_INVALID_CMD` (-31) if the value is not valid for the value type, and `SMAPI_ERR_DOCUMENTFULL` (-35) if the configuration is full.

### ClearRemoteParams

Removes all parameters from the current remote logging configuration, except those used by trigger conditions. If removal is forced, all parameters are removed and any On Data trigger conditions that use them are reset.

```c
long ClearRemoteParams([in, defaultvalue(FALSE)] boolean bForceRemovalFromTriggers);
```

| Argument | Description |
|---|---|
| `bForceRemovalFromTriggers` | True to remove all parameters, including those used by triggers. False (default) to keep parameters used by triggers. |

Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration. Returns 0 even when parameters used by triggers were kept.

### DownloadRemote

Downloads the remote logging configuration to the ECU of the selected car.

```c
long DownloadRemote();
```

This method takes no arguments.

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the download fails.

!!! note
    If a logging download script is configured, System Monitor runs the script instead of downloading.

### DownloadRemoteEx

Downloads the remote logging configuration to the ECU, waits for a given delay, then reads the value of a measurement parameter so the caller can check that the configuration write is complete.

```c
long DownloadRemoteEx(
    [in] WORD wAppId,
    [in] BSTR pszIdentifier,
    [in] WORD wReadDelay,
    [out] BSTR* pszValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id of the parameter to read. |
| `pszIdentifier` | Unique identifier of the measurement parameter to read. |
| `wReadDelay` | Delay in ms between the download and the read, to give the ECU time to process the configuration. |
| `pszValue` | Receives the current value of the parameter as a string. |

If the download fails, its error is returned and the parameter is not read.

### GetRemoteChannelCount

Gets the number of channels in the current remote logging configuration.

```c
long GetRemoteChannelCount([out] long* pnChannelCount);
```

| Argument | Description |
|---|---|
| `pnChannelCount` | Receives the number of channels. |

Returns `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteChannelNames

Gets the names of the channels in the current remote logging configuration.

```c
long GetRemoteChannelNames([out] VARIANT* str1xArrChannelNames);
```

| Argument | Description |
|---|---|
| `str1xArrChannelNames` | Receives a 1-D, 0-based SAFEARRAY of `BSTR`: the name of each channel (channel 1 at index 0). |

Returns `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteChannelNamesAll

Gets the names of the channels in the current remote logging configuration, and the configuration slot that defines each channel.

```c
long GetRemoteChannelNamesAll(
    [out] VARIANT* str1xArrChannelNames,
    [out] VARIANT* w1xSlots);
```

| Argument | Description |
|---|---|
| `str1xArrChannelNames` | Receives a 1-D, 0-based SAFEARRAY of `BSTR`: the name of each channel (channel 1 at index 0). |
| `w1xSlots` | Receives a 1-D, 0-based SAFEARRAY of `short`: the 0-based slot of the configuration that defines each channel. |

Returns `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteChannelProperties

Gets the properties of a channel in the current remote logging configuration.

```c
long GetRemoteChannelProperties(
    [in] short wChannel,
    [out] BSTR* pstrChannelName,
    [out] boolean* pbLogToUnit,
    [out] boolean* pbTelemetry,
    [out] boolean* pbTriggerRearmsAfterStopped);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `pstrChannelName` | Receives the name of the channel. |
| `pbLogToUnit` | Receives True if the channel logs to the unit. |
| `pbTelemetry` | Receives True if the channel is sent over telemetry. |
| `pbTriggerRearmsAfterStopped` | Receives True if the trigger re-arms after the stop condition. |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel index is out of range, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetDownloadedRemoteConfig

Gets the identifier of the logging configuration last downloaded to the ECU.

```c
long GetDownloadedRemoteConfig([out] BSTR* pszConfig);
```

| Argument | Description |
|---|---|
| `pszConfig` | Receives the configuration identifier (the date/time stamp of the downloaded configuration) as an 8-digit hexadecimal string. |

Returns `SMAPI_ERR_FILE` (-8), with an empty string, if no logging configuration has been downloaded.

### GetRemoteChannelPropertiesAll

Gets the properties of a channel in the current remote logging configuration, and the configuration slot that defines the channel.

```c
long GetRemoteChannelPropertiesAll(
    [in] short wChannel,
    [out] BSTR* pstrChannelName,
    [out] boolean* pbLogToUnit,
    [out] boolean* pbTelemetry,
    [out] boolean* pbTriggerRearmsAfterStopped,
    [out] short* wSlot);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `pstrChannelName` | Receives the name of the channel. |
| `pbLogToUnit` | Receives True if the channel logs to the unit. |
| `pbTelemetry` | Receives True if the channel is sent over telemetry. |
| `pbTriggerRearmsAfterStopped` | Receives True if the trigger re-arms after the stop condition. |
| `wSlot` | Receives the 0-based slot of the configuration that defines the channel. |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel index is out of range, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteOffset

Gets the logging offset of the current remote logging configuration.

```c
long GetRemoteOffset([out] WORD* pwOffset);
```

| Argument | Description |
|---|---|
| `pwOffset` | Receives the logging offset. |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the configuration does not support a logging offset, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteParams

Gets the parameters of the current remote logging configuration, with their logging values on each channel.

```c
long GetRemoteParams(
    [out] VARIANT* w1xArrAppIds,
    [out] VARIANT* str1xArrParamNames,
    [out] VARIANT* str1xArrParamDescriptions,
    [out] VARIANT* str1xArrChannelNames,
    [out] VARIANT* w1xArrParamSizes,
    [out] VARIANT* w2xArrParamValues,
    [out] VARIANT* w2xArrParamLogTypes,
    [out] long *nParamCount,
    [out] long *nChannelCount);
```

| Argument | Description |
|---|---|
| `w1xArrAppIds` | Receives a 1-D SAFEARRAY of `short`: the application Id of each parameter. |
| `str1xArrParamNames` | Receives a 1-D SAFEARRAY of `BSTR`: the identifier of each parameter (not the name). |
| `str1xArrParamDescriptions` | Receives a 1-D SAFEARRAY of `BSTR`: the description of each parameter. |
| `str1xArrChannelNames` | Receives a 1-D SAFEARRAY of `BSTR`: the name of each channel. |
| `w1xArrParamSizes` | Receives a 1-D SAFEARRAY of `short`: the data size of each parameter. |
| `w2xArrParamValues` | Receives a 2-D SAFEARRAY of `short`, indexed (parameter, channel): the logging value of each parameter on each channel. For type Frequency this is the frequency; for other types, the lower 12 bits of the value; 0 if the parameter is not logged on that channel. |
| `w2xArrParamLogTypes` | Receives a 2-D SAFEARRAY of `short`, indexed (parameter, channel): the logging value type of each parameter on each channel ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)). |
| `nParamCount` | Receives the number of parameters. |
| `nChannelCount` | Receives the number of channels. |

Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

!!! note
    All arrays are 0-based. For example, the name of channel 1 is at `str1xArrChannelNames(0)`. Values are 16-bit; use [GetRemoteParamsEx](#getremoteparamsex) for frequencies that need a `long`.

### GetRemoteParamsAll

Gets the parameters of all active remote logging configuration slots, with their logging values on each channel and the slot that defines each parameter.

```c
long GetRemoteParamsAll(
    [out] VARIANT* w1xArrAppIds,
    [out] VARIANT* str1xArrParamNames,
    [out] VARIANT* str1xArrParamDescriptions,
    [out] VARIANT* str1xArrChannelNames,
    [out] VARIANT* w1xArrParamSizes,
    [out] VARIANT* w2xArrParamValues,
    [out] VARIANT* w2xArrParamLogTypes,
    [out] long *nParamCount,
    [out] long *nChannelCount,
    [out] VARIANT* w1xSlots);
```

| Argument | Description |
|---|---|
| `w1xArrAppIds` | Receives a 1-D SAFEARRAY of `short`: the application Id of each parameter. |
| `str1xArrParamNames` | Receives a 1-D SAFEARRAY of `BSTR`: the identifier of each parameter (not the name). |
| `str1xArrParamDescriptions` | Receives a 1-D SAFEARRAY of `BSTR`: the description of each parameter. |
| `str1xArrChannelNames` | Receives a 1-D SAFEARRAY of `BSTR`: the name of each channel. |
| `w1xArrParamSizes` | Receives a 1-D SAFEARRAY of `short`: the data size of each parameter. |
| `w2xArrParamValues` | Receives a 2-D SAFEARRAY of `short`, indexed (parameter, channel): the logging value of each parameter on each channel. For type Frequency this is the frequency; for other types, the lower 12 bits of the value; 0 if the parameter is not logged on that channel. |
| `w2xArrParamLogTypes` | Receives a 2-D SAFEARRAY of `short`, indexed (parameter, channel): the logging value type of each parameter on each channel ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)). |
| `nParamCount` | Receives the number of parameters. |
| `nChannelCount` | Receives the number of channels. |
| `w1xSlots` | Receives a 1-D SAFEARRAY of `short`: the 0-based slot of the configuration that defines each parameter. |

Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

!!! note
    All arrays are 0-based. For example, the name of channel 1 is at `str1xArrChannelNames(0)`.

### GetRemoteParamsEx

Gets the parameters of the current remote logging configuration, with their logging values on each channel. Same as [GetRemoteParams](#getremoteparams), but the logging values are returned as `long`, which allows higher frequencies.

```c
long GetRemoteParamsEx(
    [out] VARIANT* w1xArrAppIds,
    [out] VARIANT* str1xArrParamNames,
    [out] VARIANT* str1xArrParamDescriptions,
    [out] VARIANT* str1xArrChannelNames,
    [out] VARIANT* w1xArrParamSizes,
    [out] VARIANT* w2xArrParamValues,
    [out] VARIANT* w2xArrParamLogTypes,
    [out] long *nParamCount,
    [out] long *nChannelCount);
```

| Argument | Description |
|---|---|
| `w1xArrAppIds` | Receives a 1-D SAFEARRAY of `short`: the application Id of each parameter. |
| `str1xArrParamNames` | Receives a 1-D SAFEARRAY of `BSTR`: the identifier of each parameter (not the name). |
| `str1xArrParamDescriptions` | Receives a 1-D SAFEARRAY of `BSTR`: the description of each parameter. |
| `str1xArrChannelNames` | Receives a 1-D SAFEARRAY of `BSTR`: the name of each channel. |
| `w1xArrParamSizes` | Receives a 1-D SAFEARRAY of `short`: the data size of each parameter. |
| `w2xArrParamValues` | Receives a 2-D SAFEARRAY of `long`, indexed (parameter, channel): the logging value of each parameter on each channel. For type Frequency this is the frequency; for other types, the lower 12 bits of the value; 0 if the parameter is not logged on that channel. |
| `w2xArrParamLogTypes` | Receives a 2-D SAFEARRAY of `short`, indexed (parameter, channel): the logging value type of each parameter on each channel ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)). |
| `nParamCount` | Receives the number of parameters. |
| `nChannelCount` | Receives the number of channels. |

Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

!!! note
    All arrays are 0-based. For example, the name of channel 1 is at `str1xArrChannelNames(0)`.

### GetRemoteParamsExAll

Gets the parameters of all active remote logging configuration slots, with their logging values on each channel and the slot that defines each parameter. Same as [GetRemoteParamsAll](#getremoteparamsall), but the logging values are returned as `long`.

```c
long GetRemoteParamsExAll(
    [out] VARIANT* w1xArrAppIds,
    [out] VARIANT* str1xArrParamNames,
    [out] VARIANT* str1xArrParamDescriptions,
    [out] VARIANT* str1xArrChannelNames,
    [out] VARIANT* w1xArrParamSizes,
    [out] VARIANT* w2xArrParamValues,
    [out] VARIANT* w2xArrParamLogTypes,
    [out] long *nParamCount,
    [out] long *nChannelCount,
    [out] VARIANT* w1xSlots);
```

| Argument | Description |
|---|---|
| `w1xArrAppIds` | Receives a 1-D SAFEARRAY of `short`: the application Id of each parameter. |
| `str1xArrParamNames` | Receives a 1-D SAFEARRAY of `BSTR`: the identifier of each parameter (not the name). |
| `str1xArrParamDescriptions` | Receives a 1-D SAFEARRAY of `BSTR`: the description of each parameter. |
| `str1xArrChannelNames` | Receives a 1-D SAFEARRAY of `BSTR`: the name of each channel. |
| `w1xArrParamSizes` | Receives a 1-D SAFEARRAY of `short`: the data size of each parameter. |
| `w2xArrParamValues` | Receives a 2-D SAFEARRAY of `long`, indexed (parameter, channel): the logging value of each parameter on each channel. For type Frequency this is the frequency; for other types, the lower 12 bits of the value; 0 if the parameter is not logged on that channel. |
| `w2xArrParamLogTypes` | Receives a 2-D SAFEARRAY of `short`, indexed (parameter, channel): the logging value type of each parameter on each channel ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)). |
| `nParamCount` | Receives the number of parameters. |
| `nChannelCount` | Receives the number of channels. |
| `w1xSlots` | Receives a 1-D SAFEARRAY of `short`: the 0-based slot of the configuration that defines each parameter. |

Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

!!! note
    All arrays are 0-based. For example, the name of channel 1 is at `str1xArrChannelNames(0)`.

### GetRemoteParamDetails

Gets the parameters of all active remote logging configuration slots, with both the identifier and the name of each parameter, their logging values on each channel and the slot that defines each parameter.

```c
long GetRemoteParamDetails(
    [out] VARIANT* awAppIds,
    [out] VARIANT* aszParamIds,
    [out] VARIANT* aszParamNames,
    [out] VARIANT* aszParamDescriptions,
    [out] VARIANT* aszChannelNames,
    [out] VARIANT* awParamSizes,
    [out] VARIANT* a2dwParamValues,
    [out] VARIANT* a2wParamLogTypes,
    [out] long* pnParamCount,
    [out] long* pnChannelCount,
    [out] VARIANT* awSlots);
```

| Argument | Description |
|---|---|
| `awAppIds` | Receives a 1-D SAFEARRAY of `short`: the application Id of each parameter. |
| `aszParamIds` | Receives a 1-D SAFEARRAY of `BSTR`: the identifier of each parameter. |
| `aszParamNames` | Receives a 1-D SAFEARRAY of `BSTR`: the name of each parameter. |
| `aszParamDescriptions` | Receives a 1-D SAFEARRAY of `BSTR`: the description of each parameter. |
| `aszChannelNames` | Receives a 1-D SAFEARRAY of `BSTR`: the name of each channel. |
| `awParamSizes` | Receives a 1-D SAFEARRAY of `short`: the data size of each parameter. |
| `a2dwParamValues` | Receives a 2-D SAFEARRAY of `long`, indexed (parameter, channel): the logging value of each parameter on each channel. For type Frequency this is the frequency; for other types, the lower 12 bits of the value; 0 if the parameter is not logged on that channel. |
| `a2wParamLogTypes` | Receives a 2-D SAFEARRAY of `short`, indexed (parameter, channel): the logging value type of each parameter on each channel ([ETypeFreqValue](conversion-rules.md#etypefreqvalue)). |
| `pnParamCount` | Receives the number of parameters. Initialise it to 0 before the call: its input value is used as the starting count. |
| `pnChannelCount` | Receives the number of channels. |
| `awSlots` | Receives a 1-D SAFEARRAY of `short`: the 0-based slot of the configuration that defines each parameter. |

Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

!!! note
    All arrays are 0-based. For example, the name of channel 1 is at `aszChannelNames(0)`.

### GetRemoteSessionDetail

Gets the value of a session detail from the remote logging configuration.

```c
long GetRemoteSessionDetail(BSTR szName, BSTR* pszValue);
```

| Argument | Description |
|---|---|
| `szName` | Name of the session detail. It must match a session detail defined in the configuration. |
| `pszValue` | Receives the value of the session detail. |

Returns `SMAPI_ERR_DETAIL_UNKNOWN` (-200) if the session detail does not exist.

!!! note
    If there is no remote logging configuration, the method returns 0 and `pszValue` is not set.

### GetRemoteTrigger

Gets the start and stop trigger times of a channel in the current remote logging configuration.

```c
long GetRemoteTrigger(
    [in] short wChannel,
    [out] long* pnStartPostTriggerMs,
    [out] long* pnStopPostTriggerMs);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `pnStartPostTriggerMs` | Receives the start trigger time in ms (the channel's pre-trigger time). |
| `pnStopPostTriggerMs` | Receives the stop trigger time in ms (the channel's post-trigger time). |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel does not exist, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteTriggerAll

Gets the start and stop trigger times of a channel in the current remote logging configuration, and the configuration slot that defines the channel.

```c
long GetRemoteTriggerAll(
    [in] short wChannel,
    [out] long* pnStartPostTriggerMs,
    [out] long* pnStopPostTriggerMs,
    [out] short* wSlot);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `pnStartPostTriggerMs` | Receives the start trigger time in ms (the channel's pre-trigger time). |
| `pnStopPostTriggerMs` | Receives the stop trigger time in ms (the channel's post-trigger time). |
| `wSlot` | Receives the 0-based slot of the configuration that defines the channel. |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel does not exist, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteTriggerCondition

Gets one of the start or stop trigger conditions of a channel in the current remote logging configuration.

```c
long GetRemoteTriggerCondition(
    [in] short wChannel,
    [in] long nTriggerIndex,
    [out] short* pnTriggerType,
    [out] BSTR* pszParamName,
    [out] short* pwParamAppId,
    [out] short* pnTriggerCondition,
    [out] double* pfTriggerThreshold,
    [out] long* pnTriggerCount);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `nTriggerIndex` | Condition index, 0 to 5: `0`–`2` are the start conditions and `3`–`5` the stop conditions. |
| `pnTriggerType` | Receives the condition type ([ECONDITONTYPE](conversion-rules.md#econditontype)):<br>`0` = On Data<br>`1` = Driver push<br>`2` = Ignition On<br>`3` = Lap trigger<br>`4` = No condition<br>`5` = External Trigger |
| `pszParamName` | Receives the name of the parameter used by an On Data condition. Not set if the condition has no parameter. |
| `pwParamAppId` | Receives the application Id of the parameter used by an On Data condition. Not set if the condition has no parameter. |
| `pnTriggerCondition` | Receives the comparison operator of an On Data condition ([ECOMPARISON](conversion-rules.md#ecomparison)):<br>`0` = `=`<br>`1` = `<`<br>`2` = `>`<br>`3` = `!=`<br>`4` = `>=`<br>`5` = `<=` |
| `pfTriggerThreshold` | Receives the value the parameter is compared with in an On Data condition. |
| `pnTriggerCount` | Receives the number of times the condition must occur before it is considered true. |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel or condition index does not exist, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteTriggerConditionAll

Gets one of the start or stop trigger conditions of a channel in the current remote logging configuration, and the configuration slot that defines the channel.

```c
long GetRemoteTriggerConditionAll(
    [in] short wChannel,
    [in] long nTriggerIndex,
    [out] short* pnTriggerType,
    [out] BSTR* pszParamName,
    [out] short* pwParamAppId,
    [out] short* pnTriggerCondition,
    [out] double* pfTriggerThreshold,
    [out] long* pnTriggerCount,
    [out] short* wSlot);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `nTriggerIndex` | Condition index, 0 to 5: `0`–`2` are the start conditions and `3`–`5` the stop conditions. |
| `pnTriggerType` | Receives the condition type ([ECONDITONTYPE](conversion-rules.md#econditontype)):<br>`0` = On Data<br>`1` = Driver push<br>`2` = Ignition On<br>`3` = Lap trigger<br>`4` = No condition<br>`5` = External Trigger |
| `pszParamName` | Receives the name of the parameter used by an On Data condition. Not set if the condition has no parameter. |
| `pwParamAppId` | Receives the application Id of the parameter used by an On Data condition. Not set if the condition has no parameter. |
| `pnTriggerCondition` | Receives the comparison operator of an On Data condition ([ECOMPARISON](conversion-rules.md#ecomparison)):<br>`0` = `=`<br>`1` = `<`<br>`2` = `>`<br>`3` = `!=`<br>`4` = `>=`<br>`5` = `<=` |
| `pfTriggerThreshold` | Receives the value the parameter is compared with in an On Data condition. |
| `pnTriggerCount` | Receives the number of times the condition must occur before it is considered true. |
| `wSlot` | Receives the 0-based slot of the configuration that defines the channel. |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel or condition index does not exist, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetRemoteWrap

Gets whether the current remote logging configuration wraps round when the logging memory is full.

```c
long GetRemoteWrap([out] boolean* pbWrap);
```

| Argument | Description |
|---|---|
| `pbWrap` | Receives True if logging wraps round when memory is full, False if logging stops when memory is full. |

Returns `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### GetSlotPercentage

Gets the percentage (0 to 100) of a logging slot used by a parameter in the current remote logging configuration.

```c
long GetSlotPercentage(short wAppId, BSTR szIdentifier, double* pdPercentage);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szIdentifier` | Unique parameter identifier. |
| `pdPercentage` | Receives the percentage of the slot used by the parameter. |

Returns `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### RemoveRemoteParam

Removes a parameter from the current remote logging configuration.

```c
long RemoveRemoteParam([in] short wAppId, [in] BSTR pszParamId);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Not needed for virtual, CAN and input signal parameters, which are also found by identifier alone. |
| `pszParamId` | Unique parameter identifier. |

Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the parameter is not in the configuration or is used by a trigger condition, and `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

### SetRemoteChannelProperties

Sets the properties of a channel in the current remote logging configuration.

```c
long SetRemoteChannelProperties(
    short wChannel,
    BSTR strChannelName,
    boolean bLogToUnit,
    boolean bTelemetry,
    boolean bTriggerRearmsAfterStopped);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `strChannelName` | New name of the channel. Must not be empty. |
| `bLogToUnit` | True to log the channel to the unit. |
| `bTelemetry` | True to send the channel over telemetry. |
| `bTriggerRearmsAfterStopped` | True if the trigger re-arms after the stop condition. |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel does not exist or the name is empty, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### SetRemoteOffset

Sets the logging offset of the current remote logging configuration.

```c
long SetRemoteOffset([in] WORD wOffset);
```

| Argument | Description |
|---|---|
| `wOffset` | New logging offset. |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the configuration does not support a logging offset, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### SetRemoteSessionDetail

Sets the value of a session detail in the remote logging configuration.

```c
long SetRemoteSessionDetail(BSTR szName, BSTR szValue);
```

| Argument | Description |
|---|---|
| `szName` | Name of the session detail. It must match a session detail defined in the configuration. |
| `szValue` | New value of the session detail. |

Returns `SMAPI_ERR_DETAIL_UNKNOWN` (-200) if the session detail does not exist, and `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no remote logging configuration.

### SetRemoteTrigger

Sets the start and stop trigger times of a channel in the current remote logging configuration.

```c
long SetRemoteTrigger(
    [in] short wChannel,
    [in] long nStartPostTriggerMs,
    [in] long nStopPostTriggerMs);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `nStartPostTriggerMs` | Start trigger time in ms (stored as the channel's pre-trigger time). |
| `nStopPostTriggerMs` | Stop trigger time in ms (stored as the channel's post-trigger time). |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel does not exist, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### SetRemoteTriggerCondition

Sets one of the start or stop trigger conditions of a channel in the current remote logging configuration.

```c
long SetRemoteTriggerCondition(
    [in] short wChannel,
    [in] long nTriggerIndex,
    [in] short nTriggerType,
    [in] BSTR pszParamName,
    [in] short wParamAppId,
    [in] short nTriggerCondition,
    [in] double fTriggerThreshold,
    [in] long nTriggerCount);
```

| Argument | Description |
|---|---|
| `wChannel` | 0-based channel index. |
| `nTriggerIndex` | Condition index, 0 to 5: `0`–`2` are the start conditions and `3`–`5` the stop conditions. |
| `nTriggerType` | Condition type ([ECONDITONTYPE](conversion-rules.md#econditontype)):<br>`0` = On Data<br>`2` = Ignition On<br>`3` = Lap trigger<br>`4` = No condition<br>`5` = External Trigger<br>`1` (Driver push) is rejected. |
| `pszParamName` | Unique identifier of the parameter used by an On Data condition. Required for On Data; ignored for other types. |
| `wParamAppId` | Application Id of the parameter used by an On Data condition. |
| `nTriggerCondition` | Comparison operator of an On Data condition ([ECOMPARISON](conversion-rules.md#ecomparison)):<br>`0` = `=`<br>`1` = `<`<br>`2` = `>`<br>`3` = `!=`<br>`4` = `>=`<br>`5` = `<=`<br>Must be in this range for every condition type. |
| `fTriggerThreshold` | Value the parameter is compared with in an On Data condition. |
| `nTriggerCount` | Number of times the condition must occur before it is considered true (maximum 65535). |

Returns `SMAPI_ERR_INVALID_CMD` (-31) if the channel or condition index does not exist or an argument is out of range, and `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration. For an On Data condition, returns the parameter lookup error (e.g. `SMAPI_ERR_PARAMNOTFOUND` (-100)) if the parameter is not found.

!!! note
    This method takes the parameter identifier, whereas [GetRemoteTriggerCondition](#getremotetriggercondition) returns the parameter name.

### SetRemoteWrap

Sets whether the current remote logging configuration wraps round when the logging memory is full.

```c
long SetRemoteWrap([in] boolean bWrap);
```

| Argument | Description |
|---|---|
| `bWrap` | True to wrap round when memory is full, False to stop logging when memory is full. |

Returns `SMAPI_ERR_BAD_STATE` (-30) if there is no remote logging configuration.

### UploadRemote

Uploads the remote logging configuration from the ECU of the selected car.

```c
long UploadRemote();
```

This method takes no arguments.

!!! note
    The return code does not report whether the upload succeeded.

**See also:** [ActiveX Methods](index.md); [ActiveX Error Codes](../activex-errors/activex-error-codes.md)
