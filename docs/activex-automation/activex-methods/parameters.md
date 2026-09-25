# Parameters

Methods for reading and writing parameter values and properties, including CAN, input signal and virtual parameters.

The methods are grouped as: [CAN Parameters](#functions---can-parameters), [Input Signal Parameters](#functions---input-signal-parameters), [Parameters](#functions---parameters), [Virtual Parameters](#functions---virtual-parameters), [Enhanced Rate Row Parameters](#enhanced-rate-row-parameters).

See [ActiveX Methods](index.md) for the conventions used on this page, and [ActiveX Error Codes](../activex-errors/activex-error-codes.md) for the return codes.

## Functions - CAN Parameters

### CANBuffersExport

Exports the CAN buffer configuration of the given CAN bus to a CSV file.

```c
long CANBuffersExport([in] short wIndex, [in] BSTR pszFileName);
```

| Argument | Description |
|---|---|
| `wIndex` | CAN bus index, 1-based. |
| `pszFileName` | Full path and name of the CSV file to create. An existing file is overwritten. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is 0 or no CAN bus exists at that index, and `SMAPI_ERR_FILE` (-8) if the file cannot be created or written.

### CANBuffersImport

Imports a CAN buffer configuration CSV file into the given CAN bus, then rebuilds the CAN configuration.

```c
long CANBuffersImport([in] short wIndex, [in] BSTR pszFileName);
```

| Argument | Description |
|---|---|
| `wIndex` | CAN bus index, 1-based. |
| `pszFileName` | Full path and name of the CSV file to import. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is 0, no CAN bus exists at that index or the import fails. The CAN configuration is marked as modified.

### CANMessagesExport

Exports the CAN message configuration of the given CAN bus to a CSV file.

```c
long CANMessagesExport([in] short wIndex, [in] BSTR pszFileName);
```

| Argument | Description |
|---|---|
| `wIndex` | CAN bus index, 1-based. |
| `pszFileName` | Full path and name of the CSV file to create. An existing file is overwritten. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is 0 or no CAN bus exists at that index, and `SMAPI_ERR_FILE` (-8) if the file cannot be created or written.

### CANMessagesImport

Imports a CAN message configuration CSV file into the given CAN bus, then rebuilds the CAN configuration.

```c
long CANMessagesImport([in] short wIndex, [in] BSTR pszFileName, [in] boolean bMerge);
```

| Argument | Description |
|---|---|
| `wIndex` | CAN bus index, 1-based. |
| `pszFileName` | Full path and name of the CSV file to import. |
| `bMerge` | True to merge the imported messages with the existing messages on the bus. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if `wIndex` is 0, no CAN bus exists at that index or the import fails. The CAN configuration is marked as modified.

### GetCANParameter

Retrieves the details of a CAN parameter from the active CAN configurations.

```c
long GetCANParameter(
    BSTR rszParamId,
    BSTR* rszName,
    BSTR* rszDescription,
    double* pdwMaxDisplay,
    double* pdwMinDisplay,
    int* pnMinLoggingRate,
    int* pnScalingFactor,
    boolean* pbIsMinNotDef,
    BSTR* rszConvId,
    boolean* pbIsRx);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the CAN parameter. |
| `rszName` | Receives the display name of the parameter. |
| `rszDescription` | Receives the description of the parameter. |
| `pdwMaxDisplay` | Receives the upper display (range) limit. |
| `pdwMinDisplay` | Receives the lower display (range) limit. |
| `pnMinLoggingRate` | Receives the default logging rate, in the units given by `pnScalingFactor`. |
| `pnScalingFactor` | Receives the unit of the logging rate. See [EScalingUnit](conversion-rules.md#escalingunit). |
| `pbIsMinNotDef` | Receives True if the logging rate is a minimum rate, False if it is a default rate. |
| `rszConvId` | Receives the identifier of the conversion rule used by the parameter. |
| `pbIsRx` | Receives True if the parameter is in a receive message, False if it is in a transmit message. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no CAN configuration and `SMAPI_ERR_PARAMNOTFOUND` (-100) if the parameter is not found. Use [GetCANParameterEx](#getcanparameterex) to also get the data type and signal layout.

### GetCANParameterBatch

Retrieves the details of a list of CAN parameters. Each output array has one element per identifier, in the same order.

```c
long GetCANParameterBatch(
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* aszNames,
    [out] VARIANT* aszDescriptions,
    [out] VARIANT* adMaxDisplays,
    [out] VARIANT* adMinDisplays,
    [out] VARIANT* adwMinLoggingRates,
    [out] VARIANT* awScalingFactors,
    [out] VARIANT* abIsMinNotDefs,
    [out] VARIANT* aszConvIds,
    [out] VARIANT* abIsRxs,
    [out] VARIANT* aszDataTypes,
    [out] VARIANT* aszCANBus,
    [out] VARIANT* aszCANMsg,
    [out] VARIANT* awStartBit,
    [out] VARIANT* awBitLength,
    [out] VARIANT* adGain,
    [out] VARIANT* adOffset,
    [out] VARIANT* awByteOrder,
    [out] VARIANT* aszMuxId,
    [out] VARIANT* alErrorCodes);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of strings holding the CAN parameter identifiers. |
| `aszNames` | Receives a 1-D SAFEARRAY of strings holding the display names. |
| `aszDescriptions` | Receives a 1-D SAFEARRAY of strings holding the descriptions. |
| `adMaxDisplays` | Receives a 1-D SAFEARRAY of doubles holding the upper display (range) limits. |
| `adMinDisplays` | Receives a 1-D SAFEARRAY of doubles holding the lower display (range) limits. |
| `adwMinLoggingRates` | Receives a 1-D SAFEARRAY of longs holding the default logging rates. |
| `awScalingFactors` | Receives a 1-D SAFEARRAY of shorts holding the logging rate units. See [EScalingUnit](conversion-rules.md#escalingunit). |
| `abIsMinNotDefs` | Receives a 1-D SAFEARRAY of booleans: True if the logging rate is a minimum rate, False if it is a default rate. |
| `aszConvIds` | Receives a 1-D SAFEARRAY of strings holding the conversion rule identifiers. |
| `abIsRxs` | Receives a 1-D SAFEARRAY of booleans: True for a receive message, False for a transmit message. |
| `aszDataTypes` | Receives a 1-D SAFEARRAY of strings holding the data type descriptions, e.g. `Unsigned Byte`. |
| `aszCANBus` | Receives a 1-D SAFEARRAY of strings holding the names of the CAN buses. |
| `aszCANMsg` | Receives a 1-D SAFEARRAY of strings holding the CAN message identifiers in hexadecimal, e.g. `0x1A0`. |
| `awStartBit` | Receives a 1-D SAFEARRAY of shorts holding the start bits within the message. |
| `awBitLength` | Receives a 1-D SAFEARRAY of shorts holding the bit lengths. |
| `adGain` | Receives a 1-D SAFEARRAY of doubles holding the gains. |
| `adOffset` | Receives a 1-D SAFEARRAY of doubles holding the offsets. |
| `awByteOrder` | Receives a 1-D SAFEARRAY of shorts holding the byte orders:<br>`0` = MSB first<br>`1` = MSB last |
| `aszMuxId` | Receives a 1-D SAFEARRAY of strings holding the multiplexer ids. Blank if the parameter is not in a multiplexed message. |
| `alErrorCodes` | Receives a 1-D SAFEARRAY of longs holding the error code for each parameter: `0` if found, `SMAPI_ERR_PARAMNOTFOUND` (-100) if not. |

!!! note
    All arrays are 0-based. Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no CAN configuration or `aszIdentifiers` is not a valid string array.

### GetCANParameterEx

Retrieves the details of a CAN parameter, including its data type, message and signal layout.

```c
long GetCANParameterEx(
    [in] BSTR szParamId,
    [out] BSTR* pszName,
    [out] BSTR* pszDescription,
    [out] double* pdMaxDisplay,
    [out] double* pdMinDisplay,
    [out] DWORD* pdwMinLoggingRate,
    [out] WORD* pwScalingFactor,
    [out] boolean* pbIsMinNotDef,
    [out] BSTR* pszConvId,
    [out] boolean* pbIsRx,
    [out] BSTR* pszDataType,
    [out] BSTR* pszCANBus,
    [out] BSTR* pszCANMsg,
    [out] WORD* pwStartBit,
    [out] WORD* pwBitLength,
    [out] double* pdGain,
    [out] double* pdOffset,
    [out] WORD* pwByteOrder,
    [out] BSTR* pszMuxId);
```

| Argument | Description |
|---|---|
| `szParamId` | Identifier of the CAN parameter. |
| `pszName` | Receives the display name of the parameter. |
| `pszDescription` | Receives the description of the parameter. |
| `pdMaxDisplay` | Receives the upper display (range) limit. |
| `pdMinDisplay` | Receives the lower display (range) limit. |
| `pdwMinLoggingRate` | Receives the default logging rate, in the units given by `pwScalingFactor`. |
| `pwScalingFactor` | Receives the unit of the logging rate. See [EScalingUnit](conversion-rules.md#escalingunit). |
| `pbIsMinNotDef` | Receives True if the logging rate is a minimum rate, False if it is a default rate. |
| `pszConvId` | Receives the identifier of the conversion rule used by the parameter. |
| `pbIsRx` | Receives True if the parameter is in a receive message, False if it is in a transmit message. |
| `pszDataType` | Receives the data type description, e.g. `Unsigned Byte`. |
| `pszCANBus` | Receives the name of the CAN bus containing the parameter. |
| `pszCANMsg` | Receives the identifier of the CAN message containing the parameter, in hexadecimal, e.g. `0x1A0`. |
| `pwStartBit` | Receives the start bit of the parameter within the message. |
| `pwBitLength` | Receives the bit length of the parameter. |
| `pdGain` | Receives the gain of the parameter. |
| `pdOffset` | Receives the offset of the parameter. |
| `pwByteOrder` | Receives the byte order:<br>`0` = MSB first<br>`1` = MSB last |
| `pszMuxId` | Receives the multiplexer id of the parameter. Blank if the parameter is not in a multiplexed message. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no CAN configuration and `SMAPI_ERR_PARAMNOTFOUND` (-100) if the parameter is not found.

### GetCANParameterList

Returns the identifiers of all CAN parameters in the active CAN configurations.

```c
long GetCANParameterList(VARIANT * paParams);
```

| Argument | Description |
|---|---|
| `paParams` | Receives a 1-D, 0-based SAFEARRAY of strings holding the CAN parameter identifiers. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if the project has no CAN configuration.

### GetCANParameterListEx

Returns the identifiers and names of all CAN parameters in the active CAN configurations, and their count.

```c
long GetCANParameterListEx(
    VARIANT* paParameterIds,
    VARIANT* paParameterNames,
    long* pnParameterCount);
```

| Argument | Description |
|---|---|
| `paParameterIds` | Receives a 1-D, 0-based SAFEARRAY of strings holding the CAN parameter identifiers. |
| `paParameterNames` | Receives a 1-D, 0-based SAFEARRAY of strings holding the matching parameter names. |
| `pnParameterCount` | Receives the number of parameters returned. |

!!! note
    Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if the project has no CAN configuration.

### GetValueCAN

Retrieves the current value of a CAN parameter.

```c
long GetValueCAN(BSTR pszIdentifier, double* pdResult);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Identifier of the CAN parameter. |
| `pdResult` | Receives the current scaled (engineering) value of the parameter. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the parameter is not found in any active CAN configuration.

## Functions - Input Signal Parameters

### RegenerateInputSignalParameters

Recreates the Input Signal parameters from their raw values and redraws all views.

```c
long RegenerateInputSignalParameters();
```

This method takes no arguments.

!!! note
    Returns `SMAPI_ERR_INVALID_CMD` (-31) if the project has no Input Signal parameters.

## Functions - Parameters

### ChangeSensorSerialNumber

Changes the serial number of the specified sensor, applying the calibration for the new serial number to the edit buffer.

```c
long ChangeSensorSerialNumber(short wAppId, BSTR pszIdentifier, long dwSerialNumber);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Sensor identifier. |
| `dwSerialNumber` | New serial number. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the sensor is not found and `SMAPI_ERR_NONE_SPECIFIC` (-3) if the serial number change fails.

### GetAppsHoldingControlParameter

Returns the applications that contain the specified non-measurement (editable or axis) parameter.

```c
long GetAppsHoldingControlParameter([in] BSTR szParamIdent, [out] VARIANT* pawAppIds);
```

| Argument | Description |
|---|---|
| `szParamIdent` | Parameter identifier. |
| `pawAppIds` | Receives a 1-D, 0-based SAFEARRAY of shorts holding the Ids of the applications that contain the parameter. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if no application contains the parameter.

### GetAppsHoldingMeasurementParameter

Returns the applications that contain the specified measurement parameter.

```c
long GetAppsHoldingMeasurementParameter([in] BSTR szParamIdent, [out] VARIANT* pawAppIds);
```

| Argument | Description |
|---|---|
| `szParamIdent` | Parameter identifier. |
| `pawAppIds` | Receives a 1-D, 0-based SAFEARRAY of shorts holding the Ids of the applications that contain the parameter. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if no application contains the parameter.

### GetAppsHoldingParam

Returns the applications that contain the specified parameter, as a combined value.

```c
long GetAppsHoldingParam(BSTR szParamIdent, short* pwAppsMask);
```

| Argument | Description |
|---|---|
| `szParamIdent` | Parameter identifier. |
| `pwAppsMask` | Receives the bitwise OR of the Ids of all applications that contain the parameter. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if no application contains the parameter. When more than one application contains the parameter, the combined value cannot always be separated into Ids; use [GetAppsHoldingParamEx](#getappsholdingparamex) instead.

### GetAppsHoldingParamEx

Returns the applications that contain the specified parameter.

```c
long GetAppsHoldingParamEx([in] BSTR szParamIdent, [out] VARIANT* pawAppIds);
```

| Argument | Description |
|---|---|
| `szParamIdent` | Parameter identifier. |
| `pawAppIds` | Receives a 1-D, 0-based SAFEARRAY of shorts holding the Ids of the applications that contain the parameter. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if no application contains the parameter.

### GetAxisAddress

Retrieves the address of an axis parameter.

```c
long GetAxisAddress([in] short wAppId, [in] BSTR pszIdentifier, [out] long* plAddress);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Axis parameter identifier. |
| `plAddress` | Receives the address of the axis parameter. |

### GetAxisParameterFromMap

Retrieves the axis parameters used by a map parameter in the application.

```c
long GetAxisParameterFromMap(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] VARIANT* str1xAxisParameters);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Identifier of a 1-axis, 2-axis or 3-axis map parameter. |
| `str1xAxisParameters` | Receives a 1-D, 0-based SAFEARRAY of strings holding the axis parameter identifiers, in the order X, Y, Z. |

### GetDTVValue1AxisMap

Returns the values of a 1-axis map (CURVE) editable parameter at all axis points, read from the supplied DTV file.

```c
long GetDTVValue1AxisMap(
    [in] BSTR pszIdentifier,
    [in] BSTR pszDTV,
    [out] VARIANT* pResult);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Parameter identifier. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pResult` | Receives a 1-D, 0-based SAFEARRAY of doubles holding the scaled values. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the parameter is not a 1-axis map in the DTV.

### GetDTVValue1AxisMapBatch

Returns the values of a list of 1-axis map (CURVE) editable parameters at all axis points, read from the supplied DTV file.

```c
long GetDTVValue1AxisMapBatch(
    [in] VARIANT aszIdentifiers,
    [in] BSTR pszDTV,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles with one row per parameter. The first element of each row holds the number of values; the values follow it. Rows shorter than the longest are padded with 0. |

!!! note
    Stops at the first parameter that cannot be read and returns an error, for example `SMAPI_ERR_PARAM_NOT_VALID` (-28) if a parameter is not a 1-axis map in the DTV. No values are returned in that case.

### GetDTVValue2AxisMap

Returns the values of a 2-axis map (MAP) editable parameter at all axis points, read from the supplied DTV file.

```c
long GetDTVValue2AxisMap(
    [in] BSTR pszIdentifier,
    [in] BSTR pszDTV,
    [out] VARIANT* pResult);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Parameter identifier. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pResult` | Receives a 2-D, 0-based SAFEARRAY of doubles holding the scaled values, indexed [x][y]. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the parameter is not a 2-axis map in the DTV.

### GetDTVValue2AxisMapBatch

Returns the values of a list of 2-axis map (MAP) editable parameters at all axis points, read from the supplied DTV file.

```c
long GetDTVValue2AxisMapBatch(
    [in] VARIANT aszIdentifiers,
    [in] BSTR pszDTV,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pafValues` | Receives a 3-D, 0-based SAFEARRAY of doubles indexed [parameter][x][y]. For each parameter, the values are at [x][y] with x, y ≥ 1; [0][y] (y ≥ 1) holds the number of x points and [x][0] holds the number of y points. Maps smaller than the largest are padded with 0. |

!!! note
    Stops at the first parameter that cannot be read and returns an error, for example `SMAPI_ERR_PARAM_NOT_VALID` (-28) if a parameter is not a 2-axis map in the DTV. No values are returned in that case.

### GetDTVValueArray

Returns the values of an array (VAL_BLK) editable parameter at all index positions, read from the supplied DTV file.

```c
long GetDTVValueArray([in] BSTR pszIdentifier, [in] BSTR pszDTV, [out] VARIANT* pResult);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Parameter identifier. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pResult` | Receives a 1-D, 0-based SAFEARRAY of doubles holding the scaled values. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the parameter is not an array parameter in the DTV.

### GetDTVValueArrayBatch

Returns the values of a list of array (VAL_BLK) editable parameters at all index positions, read from the supplied DTV file.

```c
long GetDTVValueArrayBatch(
    [in] VARIANT aszIdentifiers,
    [in] BSTR pszDTV,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles with one row per parameter. The first element of each row holds the number of values; the values follow it. Rows shorter than the longest are padded with 0. |

!!! note
    Stops at the first parameter that cannot be read and returns an error, for example `SMAPI_ERR_PARAM_NOT_VALID` (-28) if a parameter is not an array parameter in the DTV. No values are returned in that case.

### GetDTVValueAxis

Returns the values of an axis (AXIS_PTS) editable parameter at all axis points, read from the supplied DTV file.

```c
long GetDTVValueAxis([in] BSTR pszIdentifier, [in] BSTR pszDTV, [out] VARIANT* pResult);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Parameter identifier. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pResult` | Receives a 1-D, 0-based SAFEARRAY of doubles holding the scaled axis values. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the parameter is not an axis parameter in the DTV.

### GetDTVValueAxisBatch

Returns the values of a list of axis (AXIS_PTS) editable parameters at all axis points, read from the supplied DTV file.

```c
long GetDTVValueAxisBatch(
    [in] VARIANT aszIdentifiers,
    [in] BSTR pszDTV,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles with one row per parameter. The first element of each row holds the number of values; the values follow it. Rows shorter than the longest are padded with 0. |

!!! note
    Stops at the first parameter that cannot be read and returns an error, for example `SMAPI_ERR_PARAM_NOT_VALID` (-28) if a parameter is not an axis parameter in the DTV. No values are returned in that case.

### GetDTVValueScalar

Returns the value of a scalar (VALUE) editable parameter, read from the supplied DTV file.

```c
long GetDTVValueScalar([in] BSTR pszIdentifier, [in] BSTR pszDTV, [out] double* pdResult);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Parameter identifier. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pdResult` | Receives the scaled value of the parameter. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the DTV cannot be opened. If the parameter is not a scalar in the DTV, the method returns 0 and `pdResult` is not set.

### GetDTVValueScalarBatch

Returns the values of a list of scalar (VALUE) editable parameters, read from the supplied DTV file.

```c
long GetDTVValueScalarBatch(
    [in] VARIANT aszIdentifiers,
    [in] BSTR pszDTV,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pafValues` | Receives a 1-D, 0-based SAFEARRAY of doubles holding the scaled values, in the same order as `aszIdentifiers`. |

!!! note
    Stops at the first parameter that cannot be read and returns an error, for example `SMAPI_ERR_PARAM_NOT_VALID` (-28) if a parameter is not a scalar in the DTV. No values are returned in that case.

### GetDTVValueString

Returns the value of a string editable parameter, read from the supplied DTV file.

```c
long GetDTVValueString([in] BSTR pszIdentifier, [in] BSTR pszDTV, [out] BSTR* pszValue);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Parameter identifier. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `pszValue` | Receives the string value. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the parameter is not a string parameter in the DTV.

### GetDTVValueStringBatch

Returns the values of a list of string editable parameters, read from the supplied DTV file.

```c
long GetDTVValueStringBatch(
    [in] VARIANT aszIdentifiers,
    [in] BSTR pszDTV,
    [out] VARIANT* paszValues);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `pszDTV` | Full path and file name of the DTV to read. |
| `paszValues` | Receives a 1-D, 0-based SAFEARRAY of strings holding the values, in the same order as `aszIdentifiers`. |

!!! note
    Stops at the first parameter that cannot be read and returns an error, for example `SMAPI_ERR_PARAM_NOT_VALID` (-28) if a parameter is not a string parameter in the DTV. No values are returned in that case.

### GetECUMeasurementAddress

Retrieves the address (or ident) and controller of an ECU measurement parameter.

```c
long GetECUMeasurementAddress(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] long* plAddress,
    [out] BYTE* pbIdent);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Measurement parameter identifier. |
| `plAddress` | Receives the address or ident of the parameter. `0` if the parameter has none. |
| `pbIdent` | Receives the controller Id of the parameter. |

### GetExternalInputGainOffset

Gets the gain and offset of an External Input parameter.

```c
long GetExternalInputGainOffset(
    [in] BSTR pszIdentifier,
    [out] double* pdGain,
    [out] double* pdOffset);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Identifier of the External Input parameter. |
| `pdGain` | Receives the gain. |
| `pdOffset` | Receives the offset. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the External Input parameter is not found. If the parameter does not use a rational conversion, the method returns 0 and `pdGain` and `pdOffset` are not set.

### GetMapProperties

Returns the axis parameters and axis sizes of a 1-axis or 2-axis map parameter.

```c
long GetMapProperties(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] BSTR* pszXAxisId,
    [out] BSTR* pszYAxisId,
    [out] short* psXAxisPts,
    [out] short* psYAxisPts);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Map parameter identifier. |
| `pszXAxisId` | Receives the identifier of the X axis parameter. |
| `pszYAxisId` | Receives the identifier of the Y axis parameter, or `NONE` for a 1-axis map. |
| `psXAxisPts` | Receives the number of breakpoints in the X axis. |
| `psYAxisPts` | Receives the number of breakpoints in the Y axis, or `0` for a 1-axis map. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the parameter is not a 1-axis or 2-axis map in the application.

### GetModifiedParametersList

Returns the identifiers and names of the editable parameters in an application whose values differ from the saved data version.

```c
long GetModifiedParametersList(
    [in] short wAppId,
    [out] VARIANT* str1xArrParameterIds,
    [out] VARIANT* str1xArrParameterNames,
    [out] long* pnParameterCount);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Must not be `0`. |
| `str1xArrParameterIds` | Receives a 1-D, 0-based SAFEARRAY of strings holding the parameter identifiers. |
| `str1xArrParameterNames` | Receives a 1-D, 0-based SAFEARRAY of strings holding the matching parameter names. |
| `pnParameterCount` | Receives the number of parameters returned. |

!!! note
    This method always returns 0. If the call is not valid (for example `wAppId` is `0` or there is no project), the output arguments are not set.

### GetParameterBitMask

Retrieves the bit mask of a parameter.

```c
long GetParameterBitMask(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] long* plBitMask);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `plBitMask` | Receives the bit mask of the parameter. |

### GetParameterBitShift

Retrieves the bit shift of a measurement parameter.

```c
long GetParameterBitShift(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] int* pnBitShift);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Measurement parameter identifier. |
| `pnBitShift` | Receives the number of bits shifted: positive for a left shift, negative for a right shift, `0` for none. |

### GetParameterByteOrder

Retrieves the byte order of a parameter.

```c
long GetParameterByteOrder(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] long* plByteOrder);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `plByteOrder` | Receives the byte order of the parameter:<br>`0` = MSB first<br>`1` = MSB last<br>`2` = Undefined |

### GetParameterList

Returns the identifiers and names of all parameters, including axis parameters, in an application.

```c
long GetParameterList(
    [in] short wAppId,
    [out] BSTR* pszApplicationName,
    [out] VARIANT* str1xArrParameterIds,
    [out] VARIANT* str1xArrParameterNames,
    [out] long* pnParameterCount);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Must not be `0`. |
| `pszApplicationName` | Receives the name of the application. |
| `str1xArrParameterIds` | Receives a 1-D, 0-based SAFEARRAY of strings holding the parameter identifiers. |
| `str1xArrParameterNames` | Receives a 1-D, 0-based SAFEARRAY of strings holding the matching parameter names. |
| `pnParameterCount` | Receives the number of parameters returned. |

!!! note
    This method always returns 0. If the call is not valid (for example `wAppId` is `0` or not in the project), the output arguments are not set.

### GetParameterListByType

Returns the identifiers and names of the parameters of one type in an application.

```c
long GetParameterListByType(
    [in] short wAppId,
    [in] BSTR pszParamType,
    [out] BSTR* pszApplicationName,
    [out] VARIANT* str1xArrParameterIds,
    [out] VARIANT* str1xArrParameterNames,
    [out] long* pnParameterCount);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Must not be `0`. |
| `pszParamType` | Type of parameters to return (case-sensitive): `MEAS`, `SCALAR`, `AXIS`, `1AXIS`, `2AXIS`, `ARRAY` or `STRING`. `AXIS` excludes fixed axes. |
| `pszApplicationName` | Receives the name of the application. |
| `str1xArrParameterIds` | Receives a 1-D, 0-based SAFEARRAY of strings holding the parameter identifiers. |
| `str1xArrParameterNames` | Receives a 1-D, 0-based SAFEARRAY of strings holding the matching parameter names. |
| `pnParameterCount` | Receives the number of parameters returned. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if `pszParamType` is not a valid type. Otherwise the method always returns 0; if the call is not valid (for example `wAppId` is `0` or not in the project), the output arguments are not set.

### GetParameterProperties

Returns the common properties of a parameter.

```c
long GetParameterProperties(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] BSTR* pszUnits,
    [out] double* pdLowerEngLimit,
    [out] double* pdUpperEngLimit,
    [out] BSTR* pszFormat,
    [out] BSTR* pszConversionId,
    [out] BSTR* pszDescription);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pszUnits` | Receives the units of the parameter. |
| `pdLowerEngLimit` | Receives the lower engineering limit of the parameter. |
| `pdUpperEngLimit` | Receives the upper engineering limit of the parameter. |
| `pszFormat` | Receives the display format of the parameter. |
| `pszConversionId` | Receives the identifier of the conversion rule. Not set if the parameter has no conversion rule. |
| `pszDescription` | Receives the description (comment) of the parameter. |

### GetParameterPropertiesByApp

Returns the properties of all parameters, including axis parameters, in an application. Each output array has one element per parameter, in the same order.

```c
long GetParameterPropertiesByApp(
    [in] short wAppId,
    [out] VARIANT* aszIdentifier,
    [out] VARIANT* aszName,
    [out] VARIANT* aszDescription,
    [out] VARIANT* aszParamType,
    [out] VARIANT* aszUnits,
    [out] VARIANT* aszFormat,
    [out] VARIANT* aszConversionId,
    [out] VARIANT* aszGroups,
    [out] VARIANT* aszDataType,
    [out] VARIANT* avwDataSize,
    [out] VARIANT* avdLowerEngLimit,
    [out] VARIANT* avdUpperEngLimit,
    [out] VARIANT* avdwMaxLoggingRate,
    [out] VARIANT* avbPrime,
    [out] VARIANT* avbReadOnly,
    [out] VARIANT* avbLiveTuneable);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Must not be `0`. |
| `aszIdentifier` | Receives a 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `aszName` | Receives a 1-D SAFEARRAY of strings holding the parameter names. |
| `aszDescription` | Receives a 1-D SAFEARRAY of strings holding the parameter descriptions. |
| `aszParamType` | Receives a 1-D SAFEARRAY of strings holding the parameter types: `MEAS`, `SCALAR`, `AXIS`, `1AXIS`, `2AXIS`, `ARRAY`, `STRING` or `UNKNOWN`. |
| `aszUnits` | Receives a 1-D SAFEARRAY of strings holding the units. |
| `aszFormat` | Receives a 1-D SAFEARRAY of strings holding the display formats. |
| `aszConversionId` | Receives a 1-D SAFEARRAY of strings holding the conversion rule identifiers. |
| `aszGroups` | Receives a 2-D SAFEARRAY of strings indexed [parameter][group] holding the identifiers of the groups that contain each parameter. Unused entries are empty. |
| `aszDataType` | Receives a 1-D SAFEARRAY of strings holding the data type descriptions, e.g. `Unsigned Byte`. |
| `avwDataSize` | Receives a 1-D SAFEARRAY of shorts holding the data sizes. |
| `avdLowerEngLimit` | Receives a 1-D SAFEARRAY of doubles holding the lower engineering limits. |
| `avdUpperEngLimit` | Receives a 1-D SAFEARRAY of doubles holding the upper engineering limits. |
| `avdwMaxLoggingRate` | Receives a 1-D SAFEARRAY of longs holding the maximum logging rates in Hz. `0` for non-measurement parameters. |
| `avbPrime` | Receives a 1-D SAFEARRAY of booleans: True if the measurement parameter is prime. False for non-measurement parameters. |
| `avbReadOnly` | Receives a 1-D SAFEARRAY of booleans: True if the parameter is read-only. Always True for measurement parameters and fixed axes. |
| `avbLiveTuneable` | Receives a 1-D SAFEARRAY of booleans: True if the parameter is live tuneable. |

!!! note
    All arrays are 0-based. Returns `SMAPI_ERR_INVALID_CMD` (-31) if `wAppId` is `0`. A parameter with no conversion rule adds no entry to `aszConversionId`, so that array can be shorter than the others.

### GetParameterPropertiesByAppAndType

Returns the properties of all parameters of one type in an application. Each output array has one element per parameter, in the same order.

```c
long GetParameterPropertiesByAppAndType(
    [in] short wAppId,
    [in] BSTR pszParamType,
    [out] VARIANT* aszIdentifier,
    [out] VARIANT* aszName,
    [out] VARIANT* aszDescription,
    [out] VARIANT* aszUnits,
    [out] VARIANT* aszFormat,
    [out] VARIANT* aszConversionId,
    [out] VARIANT* aszGroups,
    [out] VARIANT* aszDataType,
    [out] VARIANT* avwDataSize,
    [out] VARIANT* avdLowerEngLimit,
    [out] VARIANT* avdUpperEngLimit,
    [out] VARIANT* avdwMaxLoggingRate,
    [out] VARIANT* avbPrime,
    [out] VARIANT* avbReadOnly,
    [out] VARIANT* avbLiveTuneable);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Must not be `0`. |
| `pszParamType` | Type of parameters to return (case-sensitive): `MEAS`, `SCALAR`, `AXIS`, `1AXIS`, `2AXIS`, `ARRAY` or `STRING`. |
| `aszIdentifier` | Receives a 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `aszName` | Receives a 1-D SAFEARRAY of strings holding the parameter names. |
| `aszDescription` | Receives a 1-D SAFEARRAY of strings holding the parameter descriptions. |
| `aszUnits` | Receives a 1-D SAFEARRAY of strings holding the units. |
| `aszFormat` | Receives a 1-D SAFEARRAY of strings holding the display formats. |
| `aszConversionId` | Receives a 1-D SAFEARRAY of strings holding the conversion rule identifiers. |
| `aszGroups` | Receives a 2-D SAFEARRAY of strings indexed [parameter][group] holding the identifiers of the groups that contain each parameter. Unused entries are empty. |
| `aszDataType` | Receives a 1-D SAFEARRAY of strings holding the data type descriptions, e.g. `Unsigned Byte`. |
| `avwDataSize` | Receives a 1-D SAFEARRAY of shorts holding the data sizes. |
| `avdLowerEngLimit` | Receives a 1-D SAFEARRAY of doubles holding the lower engineering limits. |
| `avdUpperEngLimit` | Receives a 1-D SAFEARRAY of doubles holding the upper engineering limits. |
| `avdwMaxLoggingRate` | Receives a 1-D SAFEARRAY of longs holding the maximum logging rates in Hz. `0` for non-measurement parameters. |
| `avbPrime` | Receives a 1-D SAFEARRAY of booleans: True if the measurement parameter is prime. False for non-measurement parameters. |
| `avbReadOnly` | Receives a 1-D SAFEARRAY of booleans: True if the parameter is read-only. Always True for measurement parameters and fixed axes. |
| `avbLiveTuneable` | Receives a 1-D SAFEARRAY of booleans: True if the parameter is live tuneable. |

!!! note
    All arrays are 0-based. Returns `SMAPI_ERR_INVALID_CMD` (-31) if `wAppId` is `0` and `SMAPI_ERR_PARAMNOTFOUND` (-100) if `pszParamType` is not a valid type. A parameter with no conversion rule adds no entry to `aszConversionId`, so that array can be shorter than the others.

### GetParameterPropertiesByAppAndTypeEx

Returns the properties of all parameters of one type in an application, as [GetParameterPropertiesByAppAndType](#getparameterpropertiesbyappandtype), plus the identifiers of other parameters that share each parameter's address.

```c
long GetParameterPropertiesByAppAndTypeEx(
    [in] short wAppId,
    [in] BSTR pszParamType,
    [out] VARIANT* aszIdentifier,
    [out] VARIANT* aszName,
    [out] VARIANT* aszDescription,
    [out] VARIANT* aszUnits,
    [out] VARIANT* aszFormat,
    [out] VARIANT* aszConversionId,
    [out] VARIANT* aszGroups,
    [out] VARIANT* aszDataType,
    [out] VARIANT* avwDataSize,
    [out] VARIANT* avdLowerEngLimit,
    [out] VARIANT* avdUpperEngLimit,
    [out] VARIANT* avdwMaxLoggingRate,
    [out] VARIANT* avbPrime,
    [out] VARIANT* avbReadOnly,
    [out] VARIANT* avbLiveTuneable,
    [out] VARIANT* aszMultiplexedIds);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Must not be `0`. |
| `pszParamType` | Type of parameters to return (case-sensitive): `MEAS`, `SCALAR`, `AXIS`, `1AXIS`, `2AXIS`, `ARRAY` or `STRING`. |
| `aszIdentifier` | Receives a 1-D SAFEARRAY of strings holding the parameter identifiers. |
| `aszName` | Receives a 1-D SAFEARRAY of strings holding the parameter names. |
| `aszDescription` | Receives a 1-D SAFEARRAY of strings holding the parameter descriptions. |
| `aszUnits` | Receives a 1-D SAFEARRAY of strings holding the units. |
| `aszFormat` | Receives a 1-D SAFEARRAY of strings holding the display formats. |
| `aszConversionId` | Receives a 1-D SAFEARRAY of strings holding the conversion rule identifiers. |
| `aszGroups` | Receives a 2-D SAFEARRAY of strings indexed [parameter][group] holding the identifiers of the groups that contain each parameter. Unused entries are empty. |
| `aszDataType` | Receives a 1-D SAFEARRAY of strings holding the data type descriptions, e.g. `Unsigned Byte`. |
| `avwDataSize` | Receives a 1-D SAFEARRAY of shorts holding the data sizes. |
| `avdLowerEngLimit` | Receives a 1-D SAFEARRAY of doubles holding the lower engineering limits. |
| `avdUpperEngLimit` | Receives a 1-D SAFEARRAY of doubles holding the upper engineering limits. |
| `avdwMaxLoggingRate` | Receives a 1-D SAFEARRAY of longs holding the maximum logging rates in Hz. `0` for non-measurement parameters. |
| `avbPrime` | Receives a 1-D SAFEARRAY of booleans: True if the measurement parameter is prime. False for non-measurement parameters. |
| `avbReadOnly` | Receives a 1-D SAFEARRAY of booleans: True if the parameter is read-only. Always True for measurement parameters and fixed axes. |
| `avbLiveTuneable` | Receives a 1-D SAFEARRAY of booleans: True if the parameter is live tuneable. |
| `aszMultiplexedIds` | Receives a 2-D SAFEARRAY of strings indexed [parameter][n] holding the identifiers of the other parameters of the same type that share the parameter's controller and address. Only `MEAS` and `SCALAR` parameters are checked. A parameter with no such parameters has a single empty entry. |

!!! note
    All arrays are 0-based. Returns `SMAPI_ERR_INVALID_CMD` (-31) if `wAppId` is `0` and `SMAPI_ERR_PARAMNOTFOUND` (-100) if `pszParamType` is not a valid type. A parameter with no conversion rule adds no entry to `aszConversionId`, so that array can be shorter than the others.

### GetParameterPropertiesByType

Returns the common properties of a parameter of a specified type.

```c
long GetParameterPropertiesByType(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [in] BSTR pszParamType,
    [out] BSTR* pszUnits,
    [out] double* pdLowerEngLimit,
    [out] double* pdUpperEngLimit,
    [out] BSTR* pszFormat,
    [out] BSTR* pszConversionId,
    [out] BSTR* pszDescription);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pszParamType` | Type of the parameter (case-sensitive): `MEAS`, `SCALAR`, `AXIS`, `1AXIS`, `2AXIS`, `ARRAY` or `STRING`. Any other value matches a parameter of any type. |
| `pszUnits` | Receives the units of the parameter. |
| `pdLowerEngLimit` | Receives the lower engineering limit of the parameter. |
| `pdUpperEngLimit` | Receives the upper engineering limit of the parameter. |
| `pszFormat` | Receives the display format of the parameter. |
| `pszConversionId` | Receives the identifier of the conversion rule. Not set if the parameter has no conversion rule. |
| `pszDescription` | Receives the description (comment) of the parameter. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if no parameter of the given type has this identifier.

### GetParameterPropertiesEx

Returns extended properties of a parameter.

```c
long GetParameterPropertiesEx(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] BSTR* pszName,
    [out] BSTR* pszParamType,
    [out] VARIANT* pszGroups,
    [out] BSTR* pszDataType,
    [out] short* psDataSize,
    [out] long* plMaxLoggingRate,
    [out] boolean* pbPrime,
    [out] boolean* pbReadOnly,
    [out] boolean* pbLiveTuneable);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pszName` | Receives the name of the parameter. |
| `pszParamType` | Receives the parameter type: `MEAS`, `SCALAR`, `AXIS`, `1AXIS`, `2AXIS`, `ARRAY`, `STRING` or `UNKNOWN`. |
| `pszGroups` | Receives a 1-D, 0-based SAFEARRAY of strings holding the identifiers of the groups that contain the parameter. |
| `pszDataType` | Receives the data type description, e.g. `Unsigned Byte`. |
| `psDataSize` | Receives the data size of the parameter. |
| `plMaxLoggingRate` | Receives the maximum logging rate in Hz. Set only for measurement parameters. |
| `pbPrime` | Receives True if the measurement parameter is prime. False for non-measurement parameters. |
| `pbReadOnly` | Receives True if the parameter is read-only. Always True for measurement parameters and fixed axes. |
| `pbLiveTuneable` | Receives True if the parameter is live tuneable. |

### GetParameterPropertiesExByType

Gets the name, type, groups, data type and access properties of a parameter, looking the parameter up by the given parameter type.

```c
long GetParameterPropertiesExByType(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [in] BSTR szParamType,
    [out] BSTR* pszName,
    [out] BSTR* pszParamType,
    [out] VARIANT* pszGroups,
    [out] BSTR* pszDataType,
    [out] short* psDataSize,
    [out] long* plMaxLoggingRate,
    [out] boolean* pbPrime,
    [out] boolean* pbReadOnly,
    [out] boolean* pbLiveTuneable);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `szParamType` | Type of parameter to look for: `MEAS`, `SCALAR`, `1AXIS`, `2AXIS`, `AXIS`, `ARRAY` or `STRING`. Any other value searches all parameter types. |
| `pszName` | Receives the parameter name. |
| `pszParamType` | Receives the parameter type: `MEAS`, `SCALAR`, `1AXIS`, `2AXIS`, `AXIS`, `ARRAY`, `STRING` or `UNKNOWN`. |
| `pszGroups` | Receives a 1-D, 0-based SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the identifiers of the groups that contain the parameter. |
| `pszDataType` | Receives the data type as text, for example `Unsigned Byte` or `Signed Word`. |
| `psDataSize` | Receives the size of the data type in 16-bit words (for example `1` for byte and word types, `2` for 32-bit types). |
| `plMaxLoggingRate` | Receives the maximum logging rate in Hz. Set for measurement parameters only; left unchanged for other types. |
| `pbPrime` | Receives True if the parameter is a prime measurement parameter. Always False for other types. |
| `pbReadOnly` | Receives True if the editable parameter is read-only. Always True for measurement parameters and fixed axes. |
| `pbLiveTuneable` | Receives True if the editable parameter is live-tuneable. Always False for measurement parameters and fixed axes. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if no parameter of the requested type is found, or `SMAPI_ERR_PARAMETER_LOCKED` (-304) if the parameter is locked.

### GetParametersAndGroups

Returns all parameters held in the groups of an application, with the group path of each.

```c
long GetParametersAndGroups(
    [in] short wAppId,
    [out] VARIANT* str1xIdentifiers,
    [out] VARIANT* str1xGroups);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `str1xIdentifiers` | Receives a 1-D, 0-based SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `str1xGroups` | Receives a 1-D, 0-based SAFEARRAY of BSTR, the same length as `str1xIdentifiers`. Each element is the group path of the parameter at the same index, built from the group descriptions separated by `\`. |

!!! note
    Only parameters that belong to a group are returned. A parameter in more than one group appears once for each group. Returns `SMAPI_ERR_NOAPP` (-9) if no program is loaded for the application.

### GetParameterWarningLimits

Gets the display warning limits of a measurement parameter.

```c
long GetParameterWarningLimits(
    [in] WORD wAppId,
    [in] BSTR pszIdentifier,
    [out] double* pdLow,
    [out] double* pdHigh);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Measurement parameter identifier. |
| `pdLow` | Receives the lower display warning limit. |
| `pdHigh` | Receives the upper display warning limit. |

### GetRowDetails

Gets the row details (row Id and ident offset) of a measurement parameter.

```c
long GetRowDetails(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [out] short* pnId,
    [out] long* plIdentOffset);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Measurement parameter identifier. |
| `pnId` | Receives the row (controller) Id from the parameter's KP_BLOB data. `0` if not found. |
| `plIdentOffset` | Receives the ident offset from the parameter's KP_BLOB data. `0` if not found. |

!!! note
    Returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) if the parameter has no KP_BLOB row details.

### GetScalarAddress

Gets the memory address of an editable parameter.

```c
long GetScalarAddress([in] short wAppId, [in] BSTR pszIdentifier, [out] long* plAddress);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Editable parameter identifier (scalar, map, array, axis or string). |
| `plAddress` | Receives the parameter address. `0` on failure. |

### GetStringValue1AxisMap

Returns the current values of a 1-axis map (CURVE) editable parameter at all axis points as formatted text.

```c
long GetStringValue1AxisMap(short wAppId, BSTR pszIdentifier, VARIANT* pValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pValue` | Receives a 1-D, 0-based SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`), one formatted value per axis point. |

!!! note
    If the values cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetStringValue2AxisMap

Returns the current values of a 2-axis map (MAP) editable parameter at all axis points as formatted text.

```c
long GetStringValue2AxisMap(short wAppId, BSTR pszIdentifier, VARIANT* pValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pValue` | Receives a 2-D, 0-based SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) dimensioned [X axis points, Y axis points], holding the formatted values. |

!!! note
    If the values cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetStringValueArray

Returns the current values of an array (VAL_BLK) editable parameter at all index positions as formatted text.

```c
long GetStringValueArray(short wAppId, BSTR pszIdentifier, VARIANT* pValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pValue` | Receives a 1-D, 0-based SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`), one formatted value per index position. |

!!! note
    If the values cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetStringValueAxis

Returns the current values of an axis (AXIS_PTS) parameter at all axis points as formatted text. Works for standard and fixed axes.

```c
long GetStringValueAxis(short wAppId, BSTR pszIdentifier, VARIANT* pValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pValue` | Receives a 1-D, 0-based SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`), one formatted value per axis point. |

!!! note
    If the values cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetStringValueMeasurement

Returns the current value of a measurement parameter as formatted text.

```c
long GetStringValueMeasurement(short wAppId, BSTR pszIdentifier, BSTR* pszValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pszValue` | Receives the current value, formatted using the parameter's display format. |

### GetStringValueScalar

Returns the current value of a scalar (VALUE) editable parameter as formatted text.

```c
long GetStringValueScalar(short wAppId, BSTR pszIdentifier, BSTR* pszValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pszValue` | Receives the current value, formatted using the parameter's display format. |

!!! note
    If the value cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetValue1AxisMap

Returns the current values of a 1-axis map (CURVE) editable parameter at all axis points.

```c
long GetValue1AxisMap(short wAppId, BSTR pszIdentifier, VARIANT* pResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pResult` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one value per axis point. The array is allocated by System Monitor. |

!!! note
    If the values cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetValue1AxisMapBatch

Returns the current values of a list of 1-axis map (CURVE) editable parameters at all axis points.

```c
long GetValue1AxisMapBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) dimensioned [number of parameters, largest axis size + 1]. For parameter `i`, element `[i][0]` holds the number of values and `[i][1]` onwards the values. Unused elements are `0`. |

!!! note
    The call stops at the first parameter that fails and returns no values. An identifier that is not found, or is not a 1-axis map, returns `SMAPI_ERR_PARAM_NOT_VALID` (-28); a value that cannot be read returns -100 minus the parameter error code (-101 to -120).

### GetValue1AxisMapBatchEx

Returns the current values of a list of 1-axis map (CURVE) editable parameters at all axis points, with an error code for each parameter.

```c
long GetValue1AxisMapBatchEx(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) dimensioned [number of parameters, largest axis size + 1]. For parameter `i`, element `[i][0]` holds the number of values and `[i][1]` onwards the values. A parameter that failed has a count of `0`. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found, or -100 minus the parameter error code (-101 to -120) if the value could not be read. |

### GetValue2AxisMap

Returns the current values of a 2-axis map (MAP) editable parameter at all axis points.

```c
long GetValue2AxisMap(short wAppId, BSTR pszIdentifier, VARIANT* pResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pResult` | Receives a 2-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) dimensioned [X axis points, Y axis points]. The array is allocated by System Monitor. |

!!! note
    If the values cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetValue2AxisMapBatch

Returns the current values of a list of 2-axis map (MAP) editable parameters at all axis points.

```c
long GetValue2AxisMapBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 3-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) dimensioned [number of parameters, largest X size + 1, largest Y size + 1]. For parameter `i`: `[i][x][0]` holds the number of Y points, `[i][0][y]` (y ≥ 1) holds the number of X points, and `[i][x][y]` (x, y ≥ 1) holds the value at X point x−1, Y point y−1. Unused elements are `0`. |

!!! note
    The call stops at the first parameter that fails and returns no values. An identifier that is not found, or is not a 2-axis map, returns `SMAPI_ERR_PARAM_NOT_VALID` (-28); a value that cannot be read returns -100 minus the parameter error code (-101 to -120).

### GetValue2AxisMapBatchEx

Returns the current values of a list of 2-axis map (MAP) editable parameters at all axis points, with an error code for each parameter.

```c
long GetValue2AxisMapBatchEx(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 3-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) laid out as for [GetValue2AxisMapBatch](#getvalue2axismapbatch). A parameter that failed is all `0`. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found, or -100 minus the parameter error code (-101 to -120) if the value could not be read. |

### GetValueArray

Returns the current values of an array (VAL_BLK) editable parameter at all index positions.

```c
long GetValueArray(short wAppId, BSTR pszIdentifier, VARIANT* pResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pResult` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one value per index position. The array is allocated by System Monitor. |

!!! note
    If the values cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetValueArrayBatch

Returns the current values of a list of array (VAL_BLK) editable parameters at all index positions.

```c
long GetValueArrayBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) dimensioned [number of parameters, largest array size + 1]. For parameter `i`, element `[i][0]` holds the number of values and `[i][1]` onwards the values. Unused elements are `0`. |

!!! note
    The call stops at the first parameter that fails and returns no values. An identifier that is not found, or is not an array, returns `SMAPI_ERR_PARAM_NOT_VALID` (-28); a value that cannot be read returns -100 minus the parameter error code (-101 to -120).

### GetValueArrayBatchEx

Returns the current values of a list of array (VAL_BLK) editable parameters at all index positions, with an error code for each parameter.

```c
long GetValueArrayBatchEx(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) dimensioned [number of parameters, largest array size + 1]. For parameter `i`, element `[i][0]` holds the number of values and `[i][1]` onwards the values. A parameter that failed has a count of `0`. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found, or -100 minus the parameter error code (-101 to -120) if the value could not be read. |

### GetValueAxis

Returns the current values of an axis (AXIS_PTS) parameter at all axis points. Works for standard and fixed axes.

```c
long GetValueAxis(short wAppId, BSTR pszIdentifier, VARIANT* pResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pResult` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one value per axis point. The array is allocated by System Monitor. |

!!! note
    If the values cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetValueAxisBatch

Returns the current values of a list of axis (AXIS_PTS) parameters at all axis points.

```c
long GetValueAxisBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) dimensioned [number of parameters, largest axis size + 1]. For parameter `i`, element `[i][0]` holds the number of values and `[i][1]` onwards the values. Unused elements are `0`. |

!!! note
    The call stops at the first parameter that fails and returns no values. An identifier that is not found, or is not an axis, returns `SMAPI_ERR_PARAM_NOT_VALID` (-28); a value that cannot be read returns -100 minus the parameter error code (-101 to -120).

### GetValueAxisBatchEx

Returns the current values of a list of axis (AXIS_PTS) parameters at all axis points, with an error code for each parameter.

```c
long GetValueAxisBatchEx(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 2-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`) dimensioned [number of parameters, largest axis size + 1]. For parameter `i`, element `[i][0]` holds the number of values and `[i][1]` onwards the values. A parameter that failed has a count of `0`. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found, or -100 minus the parameter error code (-101 to -120) if the value could not be read. |

### GetValueCANBatch

Returns the current values of a list of CAN parameters, with an error code for each parameter. CAN parameters are found in any application.

```c
long GetValueCANBatch(
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the CAN parameter identifiers. |
| `pafValues` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one current value per identifier. `0` for a parameter that failed. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found. |

### GetValueMeasurement

Returns the current value of a measurement parameter.

```c
long GetValueMeasurement(
    short wAppId,
    BSTR pszIdentifier,
    boolean bAddToDaq,
    double* pdResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `bAddToDaq` | Not used; the value is ignored. |
| `pdResult` | Receives the current value in engineering units. |

### GetValueMeasurementBatch

Returns the current values of a list of measurement parameters.

```c
long GetValueMeasurementBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one current value per identifier. |

!!! note
    If an identifier is not found, or is not a measurement parameter, the call stops, returns `SMAPI_ERR_PARAM_NOT_VALID` (-28) and returns no values.

### GetValueMeasurementBatchEx

Returns the current values of a list of measurement parameters, with an error code for each parameter.

```c
long GetValueMeasurementBatchEx(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one current value per identifier. `0` for a parameter that failed. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found. |

### GetValueOffset

Gets the live value offset of a measurement or virtual parameter.

```c
long GetValueOffset(short wAppId, BSTR szIdentifier, double* pdOffset);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Ignored when the parameter is a virtual parameter. |
| `szIdentifier` | Parameter identifier. If no measurement parameter is found in the application, the virtual parameters are searched. |
| `pdOffset` | Receives the live (display) value offset. |

### GetValueScalar

Returns the current value of a scalar (VALUE) editable parameter.

```c
long GetValueScalar(short wAppId, BSTR pszIdentifier, double* pdResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pdResult` | Receives the current value in engineering units. |

!!! note
    If the value cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetValueScalarBatch

Returns the current values of a list of scalar (VALUE) editable parameters.

```c
long GetValueScalarBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one current value per identifier. |

!!! note
    The call stops at the first parameter that fails and returns no values. An identifier that is not found, or is not a scalar, returns `SMAPI_ERR_PARAM_NOT_VALID` (-28); a value that cannot be read returns -100 minus the parameter error code (-101 to -120).

### GetValueScalarBatchEx

Returns the current values of a list of scalar (VALUE) editable parameters, with an error code for each parameter.

```c
long GetValueScalarBatchEx(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `pafValues` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one current value per identifier. `0` for a parameter that failed. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found, or -100 minus the parameter error code (-101 to -120) if the value could not be read. |

### GetValueString

Returns the current value of a string editable parameter.

```c
long GetValueString(short wAppId, BSTR pszIdentifier, BSTR* pszValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pszValue` | Receives the current string value. |

!!! note
    If the value cannot be read, returns -100 minus the parameter error code (-101 to -120).

### GetValueStringBatch

Returns the current values of a list of string editable parameters.

```c
long GetValueStringBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* paszValues);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `paszValues` | Receives a 1-D, 0-based SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`), one string value per identifier. |

!!! note
    The call stops at the first parameter that fails and returns no values. An identifier that is not found, or is not a string parameter, returns `SMAPI_ERR_PARAM_NOT_VALID` (-28); a value that cannot be read returns -100 minus the parameter error code (-101 to -120).

### GetValueStringBatchEx

Returns the current values of a list of string editable parameters, with an error code for each parameter.

```c
long GetValueStringBatchEx(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* paszValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the parameter identifiers. |
| `paszValues` | Receives a 1-D, 0-based SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`), one string value per identifier. Empty for a parameter that failed. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found, or -100 minus the parameter error code (-101 to -120) if the value could not be read. |

### GetValueVirtualBatch

Returns the current values of a list of virtual parameters, with an error code for each parameter. Virtual parameters are found in any application.

```c
long GetValueVirtualBatch(
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* pafValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the virtual parameter identifiers. |
| `pafValues` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_ARRAY \| VT_R8`), one current value per identifier. `0` for a parameter that failed. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of `long` (`VT_ARRAY \| VT_I4`), one error code per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = not found. |

### IsParameterLoggable

Checks whether a measurement parameter is loggable.

```c
long IsParameterLoggable(short wAppId, BSTR szIdentifier, boolean* pbResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szIdentifier` | Measurement parameter identifier. |
| `pbResult` | Receives True if the parameter is loggable, otherwise False. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) whenever the parameter cannot be looked up, including when there is no project or the application does not exist.

### ParameterExists

Checks whether a parameter exists, searching the application's parameters and then the virtual and CAN parameters.

```c
long ParameterExists(short wAppId, BSTR szIdentifier, boolean* pbResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Not used for the virtual and CAN parameter search. |
| `szIdentifier` | Parameter identifier. |
| `pbResult` | Receives True if the parameter exists, otherwise False. |

!!! note
    Returns `0` (success) with `pbResult` False when the parameter is not found.

### ParameterExistsEx

Checks whether a parameter of the given type exists.

```c
long ParameterExistsEx(
    [in] short wAppId,
    [in] BSTR pszIdentifier,
    [in] BSTR pszParamType,
    [out] boolean* pbResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Ignored for `VIRTUAL` and `CAN`. |
| `pszIdentifier` | Parameter identifier. |
| `pszParamType` | One of `MEAS`, `SCALAR`, `1AXIS`, `2AXIS`, `AXIS`, `ARRAY`, `STRING`, `VIRTUAL` or `CAN`. Any other value searches all parameter types in the application. |
| `pbResult` | Receives True if a parameter of the given type exists, otherwise False. |

!!! note
    Returns `0` (success) with `pbResult` False when the parameter is not found. Other lookup errors (for example `SMAPI_ERR_NOAPP` (-9) or `SMAPI_ERR_PARAMETER_LOCKED` (-304)) are returned.

### RestoreValue

Restores an editable parameter to its last saved value at all points and refreshes the views.

```c
long RestoreValue([in] short wAppId, [in] BSTR szIdentifier);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szIdentifier` | Identifier of a scalar, 1-axis map, 2-axis map, standard axis, array or string parameter. |

!!! note
    If restoring fails, the method stops and returns the parameter error code as a positive value (for example `1` = read-only, `2` = outside limits), not the -100-based code used by the Get/Set methods.

### SetBatchMode

Enters or leaves batch mode for creating virtual parameters. Enter batch mode before creating or updating several virtual parameters and leave it afterwards; the parameters are only available in System Monitor after leaving batch mode.

```c
long SetBatchMode(boolean bEnter);
```

| Argument | Description |
|---|---|
| `bEnter` | True to enter batch mode, False to leave it. |

!!! note
    Leaving batch mode turns off live tuning and monitoring, then checks the project and updates all views. The method does nothing (and returns `0`) if the project has no virtual parameters document.

### SetExternalInputGainOffset

Sets the gain and offset of an External Input parameter's conversion.

```c
long SetExternalInputGainOffset(
    [in] BSTR pszIdentifier,
    [in] double dGain,
    [in] double dOffset);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | External Input parameter identifier. |
| `dGain` | Gain to set. |
| `dOffset` | Offset to set. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the parameter is not found. If the parameter does not use a rational conversion, nothing is changed and the method still returns `0`.

### SetParameterWarningLimits

Sets the display warning limits of a measurement parameter.

```c
long SetParameterWarningLimits(
    [in] WORD wAppId,
    [in] BSTR pszIdentifier,
    [in] double dLow,
    [in] double dHigh);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Measurement parameter identifier. |
| `dLow` | Lower display warning limit. |
| `dHigh` | Upper display warning limit. |

### SetStringValue1AxisMap

Sets the values of a 1-axis map (CURVE) editable parameter at one or more axis points from formatted text.

```c
long SetStringValue1AxisMap(short wAppId, BSTR pszIdentifier, VARIANT rValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `rValue` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the new values. The lower bound of the array is the first axis point (0-based) to set, so part of the map can be updated. |

!!! note
    If the values cannot be set, returns -100 minus the parameter error code, for example -101 read-only, -102 outside limits or -106 non-numeric text.

### SetStringValue2AxisMap

Sets the values of a 2-axis map (MAP) editable parameter at one or more axis points from formatted text.

```c
long SetStringValue2AxisMap(short wAppId, BSTR pszIdentifier, VARIANT rValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `rValue` | 2-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) dimensioned [X axis points, Y axis points], holding the new values. Use a 0-based array. |

!!! note
    If the values cannot be set, returns -100 minus the parameter error code, for example -101 read-only, -102 outside limits or -106 non-numeric text.

### SetStringValueArray

Sets the values of an array (VAL_BLK) editable parameter at one or more index positions from formatted text.

```c
long SetStringValueArray(short wAppId, BSTR pszIdentifier, VARIANT rValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `rValue` | 1-D SAFEARRAY of BSTR (`VT_ARRAY \| VT_BSTR`) holding the new values. The lower bound of the array is the first index position (0-based) to set, so part of the array can be updated. |

!!! note
    If the values cannot be set, returns -100 minus the parameter error code, for example -101 read-only, -102 outside limits or -106 non-numeric text.

### SetStringValueAxis

Sets the values of a standard axis (AXIS_PTS) Editable Parameter at one or more axis points from an array of formatted strings.

```c
long SetStringValueAxis(short wAppId, BSTR pszIdentifier, VARIANT rValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `rValue` | 1-D SAFEARRAY of BSTRs holding the new values as formatted text. The lower bound of the array is the index of the first axis point to set. |

!!! note
    Fixed axes cannot be set: the method returns -101 (read-only) for them. Other parameter errors are returned as -100 minus the `EErrorCode` value (for example -102 outside limits).

### SetStringValueScalar

Sets the current value of a specified scalar (VALUE) Editable Parameter from a formatted string.

```c
long SetStringValueScalar(short wAppId, BSTR pszIdentifier, BSTR pszValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pszValue` | New value as formatted text. |

### SetValueScalarBatch

Sets the values of a list of scalar (VALUE) Editable Parameters and returns an error code for each parameter.

```c
long SetValueScalarBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [in] VARIANT adValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the parameter identifiers. |
| `adValues` | 1-D SAFEARRAY of doubles holding the new values, in the same order as `aszIdentifiers`. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of longs holding one error code per identifier, in the same order (`0` = success). |

!!! note
    For a FLOAT32 parameter, the per-parameter code is -120 if the stored value differs from the requested value after rounding (the value is still set).

### SetValue1AxisMapBatch

Sets all values of a list of 1-axis map (CURVE) Editable Parameters and returns an error code for each parameter.

```c
long SetValue1AxisMapBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [in] VARIANT adValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the parameter identifiers. |
| `adValues` | 2-D SAFEARRAY of doubles with one row per parameter, in the same order as `aszIdentifiers`. In each row, element 0 holds the number of values and elements 1 to n hold the values. Values are written from the first axis point. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of longs holding one error code per identifier, in the same order (`0` = success). |

!!! note
    The per-parameter code is -102 (outside limits) if the value count is greater than the number of axis points.

### SetValue2AxisMapBatch

Sets all values of a list of 2-axis map (MAP) Editable Parameters and returns an error code for each parameter.

```c
long SetValue2AxisMapBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [in] VARIANT adValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the parameter identifiers. |
| `adValues` | 3-D SAFEARRAY of doubles indexed [parameter][x][y], with parameters in the same order as `aszIdentifiers`. For each parameter, element [0][1] holds the number of X points, element [1][0] holds the number of Y points, and elements [1..nx][1..ny] hold the values. Values are written from the first X and Y axis points. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of longs holding one error code per identifier, in the same order (`0` = success). |

!!! note
    The per-parameter code is -102 (outside limits) if either count is zero or greater than the number of points on that axis.

### SetValueArrayBatch

Sets the values of a list of array (VAL_BLK) Editable Parameters and returns an error code for each parameter.

```c
long SetValueArrayBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [in] VARIANT adValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the parameter identifiers. |
| `adValues` | 2-D SAFEARRAY of doubles with one row per parameter, in the same order as `aszIdentifiers`. In each row, element 0 holds the number of values and elements 1 to n hold the values. Values are written from the index given by the lower bound of the second dimension (normally 0). |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of longs holding one error code per identifier, in the same order (`0` = success). |

!!! note
    The per-parameter code is -102 (outside limits) if the value count is greater than the array size.

### SetValueAxisBatch

Sets the values of a list of axis (AXIS_PTS) Editable Parameters and returns an error code for each parameter.

```c
long SetValueAxisBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [in] VARIANT adValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the parameter identifiers. |
| `adValues` | 2-D SAFEARRAY of doubles with one row per parameter, in the same order as `aszIdentifiers`. In each row, element 0 holds the number of values and elements 1 to n hold the values. Values are written from the axis point given by the lower bound of the second dimension (normally 0). |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of longs holding one error code per identifier, in the same order (`0` = success). |

!!! note
    The per-parameter code is -102 (outside limits) if the value count is greater than the number of axis points.

### SetValueStringBatch

Sets the values of a list of string Editable Parameters and returns an error code for each parameter.

```c
long SetValueStringBatch(
    [in] short wAppId,
    [in] VARIANT aszIdentifiers,
    [in] VARIANT aszValues,
    [out] VARIANT* palErrorCodes);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the parameter identifiers. |
| `aszValues` | 1-D SAFEARRAY of BSTRs holding the new values, in the same order as `aszIdentifiers`. |
| `palErrorCodes` | Receives a 1-D, 0-based SAFEARRAY of longs holding one error code per identifier, in the same order (`0` = success). |

### SetValue1AxisMap

Sets the values of a specified 1-axis map (CURVE) Editable Parameter at one or more axis points.

```c
long SetValue1AxisMap(short wAppId, BSTR pszIdentifier, VARIANT rValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `rValue` | 1-D SAFEARRAY of doubles holding the new values. The lower bound of the array is the index of the first axis point to set. A 2-D array with a single row or column is also accepted. |

!!! note
    For a FLOAT32 parameter, the method returns -120 if a stored value differs from the requested value after rounding (the values are still set).

### SetValue2AxisMap

Sets the values of a specified 2-axis map (MAP) Editable Parameter at one or more axis points.

```c
long SetValue2AxisMap(short wAppId, BSTR pszIdentifier, VARIANT rValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `rValue` | 2-D SAFEARRAY of doubles holding the new values, indexed [x][y]. The lower bounds of the two dimensions are the indexes of the first X and Y axis points to set. |

### SetValueArray

Sets the values of a specified array (VAL_BLK) Editable Parameter at one or more index positions.

```c
long SetValueArray(short wAppId, BSTR pszIdentifier, VARIANT rValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `rValue` | 1-D SAFEARRAY of doubles holding the new values. The lower bound of the array is the index of the first element to set. |

### SetValueAxis

Sets the values of a specified standard axis (AXIS_PTS) Editable Parameter at one or more axis points.

```c
long SetValueAxis(short wAppId, BSTR pszIdentifier, VARIANT rValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `rValue` | 1-D SAFEARRAY of doubles holding the new values. The lower bound of the array is the index of the first axis point to set. |

!!! note
    Fixed axes cannot be set: the method returns -101 (read-only) for them.

### SetValueOffset

Sets the display value offset applied to the live value of a measurement parameter or virtual parameter.

```c
long SetValueOffset(short wAppId, BSTR szIdentifier, double dOffset);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szIdentifier` | Parameter identifier. If no measurement parameter with this identifier is found in the application, a virtual parameter with this identifier is used. |
| `dOffset` | Display value offset. |

### SetValueScalar

Sets the current value of a specified scalar (VALUE) Editable Parameter.

```c
long SetValueScalar(short wAppId, BSTR pszIdentifier, double pdValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pdValue` | New value. |

!!! note
    For a FLOAT32 parameter, the method returns -120 if the stored value differs from the requested value after rounding (the value is still set).

### SetValueString

Sets the current value of a specified string Editable Parameter.

```c
long SetValueString(short wAppId, BSTR pszIdentifier, BSTR pszValue);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszIdentifier` | Parameter identifier. |
| `pszValue` | New value. |

### ZeroLiveValue

Zeroes the live value of a measurement parameter by setting its display value offset from the current value.

```c
long ZeroLiveValue(short wAppId, BSTR szIdentifier);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `szIdentifier` | Parameter identifier. Only measurement parameters are supported (unlike [SetValueOffset](#setvalueoffset), virtual parameters are not). |

## Functions - Virtual Parameters

### AddVirtualParameterGroup

Adds a virtual parameter group, either at the top level or inside an existing group.

```c
long AddVirtualParameterGroup(
    BSTR szPath,
    BSTR szName,
    BSTR szDescription,
    boolean bParamsReadOnly);
```

| Argument | Description |
|---|---|
| `szPath` | Path of the parent group, e.g. `\TopLevelGroup\SubGroup`. Every group in the path must already exist. An empty string adds a top-level group. |
| `szName` | Identifier of the new group. |
| `szDescription` | Description of the new group. |
| `bParamsReadOnly` | True to mark the parameters in the group as read-only. |

!!! note
    Returns `SMAPI_ERR_NONE_SPECIFIC` (-3) if a group in `szPath` does not exist. If a group called `szName` already exists, nothing is changed and the method returns 0.

### GetValueVirtual

Gets the current value of a specified virtual parameter.

```c
long GetValueVirtual(BSTR pszIdentifier, double* pdResult);
```

| Argument | Description |
|---|---|
| `pszIdentifier` | Virtual parameter identifier. |
| `pdResult` | Receives the current value of the virtual parameter. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the virtual parameter does not exist. If the project has no virtual parameters, the method returns 0 without setting `pdResult`.

### GetVirtualParamCount

Gets the number of virtual parameters in the active project.

```c
long GetVirtualParamCount(long* pnParamCount);
```

| Argument | Description |
|---|---|
| `pnParamCount` | Receives the number of virtual parameters in the active project. |

### GetVirtualParameterCountGroup

Gets the number of virtual parameters in a group.

```c
long GetVirtualParameterCountGroup(BSTR Path, long* pnParameterCount);
```

| Argument | Description |
|---|---|
| `Path` | Path of the group, e.g. `\TopLevelGroup\SubGroup`. Only the last group in the path is used to find the group. An empty string or `\` counts the virtual parameters that are not in any group. |
| `pnParameterCount` | Receives the number of virtual parameters directly in the group (parameters in subgroups are not counted). |

!!! note
    Returns `SMAPI_ERR_GROUP_NOTFOUND` (-39) if the group does not exist.

### GetVirtualParameter

Gets the details of a specified virtual parameter.

```c
long GetVirtualParameter(
    BSTR rszParamId,
    BSTR *rszName,
    BSTR *rszDescription,
    double * pdwMaxDisplay,
    double * pdwMinDisplay,
    int * pnMinLoggingRate,
    int * pnScalingFactor,
    boolean * pbIsMinNotDef,
    BSTR * rszExpression,
    BSTR * rszConvId);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the virtual parameter. |
| `rszName` | Receives the display name of the parameter. |
| `rszDescription` | Receives the description of the parameter. |
| `pdwMaxDisplay` | Receives the upper display limit. |
| `pdwMinDisplay` | Receives the lower display limit. |
| `pnMinLoggingRate` | Receives the logging rate, as a number of `pnScalingFactor` units. `0` if no logging rate is defined. |
| `pnScalingFactor` | Receives the unit of the logging rate, see [EScalingUnit](conversion-rules.md#escalingunit). `10000` (undefined) if no logging rate is defined. |
| `pbIsMinNotDef` | Receives True if the logging rate is a minimum rate (the parameter is a Prime Parameter), False if it is a default rate. |
| `rszExpression` | Receives the FDL expression used to evaluate the virtual parameter. |
| `rszConvId` | Receives the identifier of the conversion rule used by the parameter. |

!!! note
    Returns `SMAPI_ERR_NONE_SPECIFIC` (-3) if the virtual parameter does not exist.

### GetVirtualParameterBatch

Gets the details of a list of virtual parameters.

```c
long GetVirtualParameterBatch(
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* astrNames,
    [out] VARIANT* astrDescriptions,
    [out] VARIANT* afMaxDisplays,
    [out] VARIANT* afMinDisplays,
    [out] VARIANT* anMinLoggingRates,
    [out] VARIANT* anScalingFactors,
    [out] VARIANT* abIsMinNotDefs,
    [out] VARIANT* astrExpressions,
    [out] VARIANT* astrUnits,
    [out] VARIANT* astrFormats,
    [out] VARIANT* astrGroups,
    [out] VARIANT* astrConvIds);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the virtual parameter identifiers. |
| `astrNames` | Receives an array (BSTR) of display names. |
| `astrDescriptions` | Receives an array (BSTR) of descriptions. |
| `afMaxDisplays` | Receives an array (double) of upper display limits. |
| `afMinDisplays` | Receives an array (double) of lower display limits. |
| `anMinLoggingRates` | Receives an array (long) of logging rates, as a number of scaling units. |
| `anScalingFactors` | Receives an array (long) of logging rate units, see [EScalingUnit](conversion-rules.md#escalingunit). |
| `abIsMinNotDefs` | Receives an array (boolean) of flags: True if the logging rate is a minimum rate (Prime Parameter), False if it is a default rate. |
| `astrExpressions` | Receives an array (BSTR) of FDL expressions. |
| `astrUnits` | Receives an array (BSTR) of units. |
| `astrFormats` | Receives an array (BSTR) of display formats. |
| `astrGroups` | Receives an array (BSTR) of the descriptions of the groups holding the parameters (empty if a parameter is not in a group). |
| `astrConvIds` | Receives an array (BSTR) of conversion rule identifiers. |

!!! note
    All output arrays are 1-D, 0-based and in the order of `aszIdentifiers`. The method stops at the first identifier that is not found and returns `SMAPI_ERR_PARAMNOTFOUND` (-100) without filling the output arrays; use [GetVirtualParameterBatchEx](#getvirtualparameterbatchex) for per-parameter error codes.

### GetVirtualParameterBatchEx

Gets the details, including the data type, of a list of virtual parameters, with an error code for each parameter.

```c
long GetVirtualParameterBatchEx(
    [in] VARIANT aszIdentifiers,
    [out] VARIANT* aszNames,
    [out] VARIANT* aszDescriptions,
    [out] VARIANT* adMaxDisplays,
    [out] VARIANT* adMinDisplays,
    [out] VARIANT* adwMinLoggingRates,
    [out] VARIANT* awScalingFactors,
    [out] VARIANT* abIsMinNotDefs,
    [out] VARIANT* aszExpressions,
    [out] VARIANT* aszUnits,
    [out] VARIANT* aszFormats,
    [out] VARIANT* aszGroups,
    [out] VARIANT* aszConvIds,
    [out] VARIANT* aszDataTypes,
    [out] VARIANT* alErrorCodes);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the virtual parameter identifiers. |
| `aszNames` | Receives an array (BSTR) of display names. |
| `aszDescriptions` | Receives an array (BSTR) of descriptions. |
| `adMaxDisplays` | Receives an array (double) of upper display limits. |
| `adMinDisplays` | Receives an array (double) of lower display limits. |
| `adwMinLoggingRates` | Receives an array (long) of logging rates, as a number of scaling units. |
| `awScalingFactors` | Receives an array (short) of logging rate units, see [EScalingUnit](conversion-rules.md#escalingunit). |
| `abIsMinNotDefs` | Receives an array (boolean) of flags: True if the logging rate is a minimum rate (Prime Parameter), False if it is a default rate. |
| `aszExpressions` | Receives an array (BSTR) of FDL expressions. |
| `aszUnits` | Receives an array (BSTR) of units. |
| `aszFormats` | Receives an array (BSTR) of display formats. |
| `aszGroups` | Receives an array (BSTR) of the descriptions of the groups holding the parameters (empty if a parameter is not in a group). |
| `aszConvIds` | Receives an array (BSTR) of conversion rule identifiers. |
| `aszDataTypes` | Receives an array (BSTR) of data type names, e.g. `Unsigned Byte`. |
| `alErrorCodes` | Receives an array (long) of error codes, one per identifier: `0` = success, `SMAPI_ERR_PARAMNOTFOUND` (-100) = virtual parameter not found. |

!!! note
    All output arrays are 1-D, 0-based and in the order of `aszIdentifiers`.

### GetVirtualParameterEx

Gets the extended details (including units, format and group) of a specified virtual parameter.

```c
long GetVirtualParameterEx(
    BSTR rszParamId,
    BSTR *rszName,
    BSTR *rszDescription,
    double * pdwMaxDisplay,
    double * pdwMinDisplay,
    int * pnMinLoggingRate,
    int * pnScalingFactor,
    boolean * pbIsMinNotDef,
    BSTR * rszExpression,
    BSTR * pszUnits,
    BSTR * pszFormat,
    BSTR * pszGroup,
    BSTR * rszConvId);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the virtual parameter. |
| `rszName` | Receives the display name of the parameter. |
| `rszDescription` | Receives the description of the parameter. |
| `pdwMaxDisplay` | Receives the upper display limit. |
| `pdwMinDisplay` | Receives the lower display limit. |
| `pnMinLoggingRate` | Receives the logging rate, as a number of `pnScalingFactor` units. `0` if no logging rate is defined. |
| `pnScalingFactor` | Receives the unit of the logging rate, see [EScalingUnit](conversion-rules.md#escalingunit). `10000` (undefined) if no logging rate is defined. |
| `pbIsMinNotDef` | Receives True if the logging rate is a minimum rate (the parameter is a Prime Parameter), False if it is a default rate. |
| `rszExpression` | Receives the FDL expression used to evaluate the virtual parameter. |
| `pszUnits` | Receives the identifier of the conversion rule (see note). |
| `pszFormat` | Receives the units (see note). |
| `pszGroup` | Receives the display format (see note). |
| `rszConvId` | Receives the description of the group holding the parameter, or an empty string if it is not in a group (see note). |

!!! note
    The last four [out] arguments are filled by position, not by their ODL names: the 10th receives the conversion rule identifier, the 11th the units, the 12th the display format and the 13th the group description.

!!! note
    Returns `SMAPI_ERR_NONE_SPECIFIC` (-3) if the virtual parameter does not exist.

### GetVirtualParameterEx2

Gets the extended details, including the data type, of a specified virtual parameter.

```c
long GetVirtualParameterEx2(
    [in] BSTR szParamId,
    [out] BSTR* pszName,
    [out] BSTR* pszDescription,
    [out] double* pdMaxDisplay,
    [out] double* pdMinDisplay,
    [out] DWORD* pdwMinLoggingRate,
    [out] WORD* pwScalingFactor,
    [out] boolean* pbIsMinNotDef,
    [out] BSTR* pszExpression,
    [out] BSTR* pszUnits,
    [out] BSTR* pszFormat,
    [out] BSTR* pszGroup,
    [out] BSTR* pszConvId,
    [out] BSTR* pszDataType);
```

| Argument | Description |
|---|---|
| `szParamId` | Identifier of the virtual parameter. |
| `pszName` | Receives the display name of the parameter. |
| `pszDescription` | Receives the description of the parameter. |
| `pdMaxDisplay` | Receives the upper display limit. |
| `pdMinDisplay` | Receives the lower display limit. |
| `pdwMinLoggingRate` | Receives the logging rate, as a number of `pwScalingFactor` units. `0` if no logging rate is defined. |
| `pwScalingFactor` | Receives the unit of the logging rate, see [EScalingUnit](conversion-rules.md#escalingunit). `10000` (undefined) if no logging rate is defined. |
| `pbIsMinNotDef` | Receives True if the logging rate is a minimum rate (the parameter is a Prime Parameter), False if it is a default rate. |
| `pszExpression` | Receives the FDL expression used to evaluate the virtual parameter. |
| `pszUnits` | Receives the identifier of the conversion rule (see note). |
| `pszFormat` | Receives the units (see note). |
| `pszGroup` | Receives the display format (see note). |
| `pszConvId` | Receives the description of the group holding the parameter, or an empty string if it is not in a group (see note). |
| `pszDataType` | Receives the name of the data type, e.g. `Unsigned Byte`. |

!!! note
    The 10th to 13th arguments are filled by position, not by their ODL names: the 10th receives the conversion rule identifier, the 11th the units, the 12th the display format and the 13th the group description.

!!! note
    Returns `SMAPI_ERR_NONE_SPECIFIC` (-3) if the virtual parameter does not exist.

### GetVirtualParameterGroup

Gets the details of a virtual parameter group.

```c
long GetVirtualParameterGroup(
    [in] BSTR szGroup,
    [out] BSTR* szName,
    [out] BSTR* szDescription,
    [out] boolean* pbParamsReadOnly);
```

| Argument | Description |
|---|---|
| `szGroup` | Identifier of the group (not a path). If no group has this identifier, the group whose name or description matches is used. |
| `szName` | Receives the name of the group. |
| `szDescription` | Receives the description of the group. |
| `pbParamsReadOnly` | Receives True if the group's parameters are read-only. |

!!! note
    Returns `SMAPI_ERR_GROUP_NOTFOUND` (-39) if the group does not exist.

### GetVirtualParameterGroupList

Gets the paths of all virtual parameter groups in the active project.

```c
long GetVirtualParameterGroupList([out] VARIANT* paGroupPaths, [out] long* pnGroupCount);
```

| Argument | Description |
|---|---|
| `paGroupPaths` | Receives a 1-D, 0-based SAFEARRAY of BSTRs holding the path of every group and subgroup, e.g. `TopLevelGroup\SubGroup` (no leading backslash). |
| `pnGroupCount` | Receives the total number of groups. |

### GetVirtualParameterList

Gets the identifiers of all virtual parameters in the active project.

```c
long GetVirtualParameterList(VARIANT * paParams);
```

| Argument | Description |
|---|---|
| `paParams` | Receives a 1-D, 0-based SAFEARRAY of BSTRs holding the virtual parameter identifiers. |

### GetVirtualParameterListEx

Gets the identifiers, names and number of all virtual parameters in the active project.

```c
long GetVirtualParameterListEx(
    VARIANT* paParameterIds,
    VARIANT* paParameterNames,
    long* pnParameterCount);
```

| Argument | Description |
|---|---|
| `paParameterIds` | Receives a 1-D, 0-based SAFEARRAY of BSTRs holding the virtual parameter identifiers. |
| `paParameterNames` | Receives a 1-D, 0-based SAFEARRAY of BSTRs holding the display names, in the same order as `paParameterIds`. |
| `pnParameterCount` | Receives the number of virtual parameters. |

### GetVirtualParameterListGroup

Gets the identifiers of the virtual parameters in a group.

```c
long GetVirtualParameterListGroup(BSTR Path, VARIANT * paParams);
```

| Argument | Description |
|---|---|
| `Path` | Path of the group, e.g. `\TopLevelGroup\SubGroup`. Only the text after the last backslash is used to find the group. `\` returns the virtual parameters that are not in any group. |
| `paParams` | Receives a 1-D, 0-based SAFEARRAY of BSTRs holding the identifiers of the parameters directly in the group (parameters in subgroups are not included). |

!!! note
    Returns `SMAPI_ERR_GROUP_NOTFOUND` (-39) if the group does not exist or `Path` is empty. A path with no backslash is treated as `\`, so start the path with a backslash.

### RemoveAllVirtualParameters

Removes all virtual parameters from the active project.

```c
long RemoveAllVirtualParameters();
```

This method takes no arguments.

### RemoveAllVirtualParametersFromGroup

Removes all virtual parameters from a group. The group itself and its subgroups are kept.

```c
long RemoveAllVirtualParametersFromGroup(BSTR Path);
```

| Argument | Description |
|---|---|
| `Path` | Path of the group whose parameters are to be removed, e.g. `\TopLevelGroup\SubGroup`. Only the last group in the path is used. An empty string or `\` removes the virtual parameters that are not in any group. |

!!! note
    Other virtual parameters that depend on a removed parameter are also removed. If the group does not exist, nothing is removed and the method returns 0.

### RemoveVirtualParameter

Removes a specified virtual parameter.

```c
long RemoveVirtualParameter(BSTR rszParamId);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the virtual parameter to remove. |

!!! note
    Returns `SMAPI_ERR_NONE_SPECIFIC` (-3) if the virtual parameter could not be removed (for example, it does not exist).

### RemoveVirtualParameterGroup

Removes a virtual parameter group, including its subgroups and all the virtual parameters they contain.

```c
long RemoveVirtualParameterGroup(BSTR szPath);
```

| Argument | Description |
|---|---|
| `szPath` | Path of the group to remove, e.g. `\TopLevelGroup\SubGroup`. The last group in the path is found by identifier, or else by name or description. |

!!! note
    Other virtual parameters that depend on a removed parameter are also removed. Returns `SMAPI_ERR_GROUP_NOTFOUND` (-39) if a parent group in the path does not exist, or if the path gives no parent for a group that is not top-level. If the group itself is not found, nothing is removed and the method returns 0.

### SetVirtualParameter

Creates a virtual parameter, or modifies an existing one.

```c
long SetVirtualParameter(
    BSTR rszParamId,
    BSTR rszName,
    BSTR rszDescription,
    double dwMaxDisplay,
    double dwMinDisplay,
    int nMinLoggingRate,
    int nScalingFactor,
    boolean bIsMinNotDef,
    BSTR rszExpression,
    BSTR rszConvId,
    boolean bOverwrite);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the virtual parameter. Must not be empty or contain any of `$ % ^ / \ ! &` or a pipe character. |
| `rszName` | Display name of the virtual parameter. Must not be empty or contain the same characters. |
| `rszDescription` | Description of the virtual parameter. |
| `dwMaxDisplay` | Upper limit (sets the upper display and physical limits). |
| `dwMinDisplay` | Lower limit (sets the lower display and physical limits). |
| `nMinLoggingRate` | Logging rate, as a number of `nScalingFactor` units. |
| `nScalingFactor` | Unit of the logging rate, see [EScalingUnit](conversion-rules.md#escalingunit). `10000` (undefined) means no logging rate is set. |
| `bIsMinNotDef` | True to make the logging rate a minimum rate, which marks the virtual parameter as a Prime Parameter. False to make it a default rate. |
| `rszExpression` | FDL expression to evaluate. |
| `rszConvId` | Identifier of the conversion rule that converts the output value to engineering units. Use `App::ConvName` for a conversion from an application. If no conversion with this identifier exists, a placeholder conversion is created. |
| `bOverwrite` | True to overwrite an existing virtual parameter with the same identifier. |

!!! note
    Specific return codes: `SMAPI_ERR_PARAM_NOT_VALID` (-28) empty or invalid identifier or name; `SMAPI_ERR_CONV_NOT_VALID` (-27) empty `rszConvId` or `App::ConvName` not found; `SMAPI_ERR_IDENT_EXISTS` (-36) the identifier is already used by another parameter; `SMAPI_ERR_PARAM_EXISTS` (-29) the parameter or name already exists and `bOverwrite` is False; `SMAPI_ERR_FDL_NOT_PARSED` (-26) invalid expression.

### SetVirtualParameterDataType

Sets the data type of a virtual parameter.

```c
long SetVirtualParameterDataType(BSTR pszParamId, enumDataType eDataType);
```

| Argument | Description |
|---|---|
| `pszParamId` | Identifier of the virtual parameter. |
| `eDataType` | Data type, see [enumDataType](conversion-rules.md#enumdatatype). |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the virtual parameter does not exist.

### SetVirtualParameterEx

Creates or modifies a virtual parameter, with units and display format overrides.

```c
long SetVirtualParameterEx(
    BSTR rszParamId,
    BSTR rszName,
    BSTR rszDescription,
    double dwMaxDisplay,
    double dwMinDisplay,
    int nMinLoggingRate,
    int nScalingFactor,
    boolean bIsMinNotDef,
    BSTR rszExpression,
    BSTR rszConvId,
    boolean bOverwrite,
    BSTR szUnits,
    BSTR szFormatOverride);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the virtual parameter. Must not be empty or contain any of `$ % ^ / \ ! &` or a pipe character. |
| `rszName` | Display name of the virtual parameter. Must not be empty or contain the same characters. |
| `rszDescription` | Description of the virtual parameter. |
| `dwMaxDisplay` | Upper limit (sets the upper display and physical limits). |
| `dwMinDisplay` | Lower limit (sets the lower display and physical limits). |
| `nMinLoggingRate` | Logging rate, as a number of `nScalingFactor` units. |
| `nScalingFactor` | Unit of the logging rate, see [EScalingUnit](conversion-rules.md#escalingunit). `10000` (undefined) means no logging rate is set. |
| `bIsMinNotDef` | True to make the logging rate a minimum rate, which marks the virtual parameter as a Prime Parameter. False to make it a default rate. |
| `rszExpression` | FDL expression to evaluate. |
| `rszConvId` | Identifier of the conversion rule that converts the output value to engineering units. Use `App::ConvName` for a conversion from an application. If no conversion with this identifier exists, a placeholder conversion is created. |
| `bOverwrite` | True to overwrite an existing virtual parameter with the same identifier. |
| `szUnits` | Units in which to display the value. Ignored if empty. |
| `szFormatOverride` | Display format override. Ignored if not a valid format. |

!!! note
    Returns the same specific codes as [SetVirtualParameter](#setvirtualparameter) (-26, -27, -28, -29, -36).

### SetVirtualParameterExtended

Creates or modifies a virtual parameter with all options: units, format, group, data type and warning limits.

```c
long SetVirtualParameterExtended(
    [in] BSTR rszParamId,
    [in] BSTR rszName,
    [in] BSTR rszDescription,
    [in] double dwMaxDisplay,
    [in] double dwMinDisplay,
    [in] int nMinLoggingRate,
    [in] int nScalingFactor,
    [in] boolean bIsMinNotDef,
    [in] BSTR rszExpression,
    [in] BSTR rszConvId,
    [in] boolean bOverwrite,
    [in] BSTR szUnits,
    [in] BSTR szFormatOverride,
    [in] BSTR szGroupPath,
    [in] enumDataType eDataType,
    [in] double dwUpperWarningLimit,
    [in] double dwLowerWarningLimit);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the virtual parameter. Must not be empty or contain any of `$ % ^ / \ ! &` or a pipe character. |
| `rszName` | Display name of the virtual parameter. Must not be empty or contain the same characters. |
| `rszDescription` | Description of the virtual parameter. |
| `dwMaxDisplay` | Upper physical limit. |
| `dwMinDisplay` | Lower physical limit. |
| `nMinLoggingRate` | Logging rate, as a number of `nScalingFactor` units. |
| `nScalingFactor` | Unit of the logging rate, see [EScalingUnit](conversion-rules.md#escalingunit). `10000` (undefined) means no logging rate is set. |
| `bIsMinNotDef` | True to make the logging rate a minimum rate, which marks the virtual parameter as a Prime Parameter. False to make it a default rate. |
| `rszExpression` | FDL expression to evaluate. |
| `rszConvId` | Identifier of the conversion rule that converts the output value to engineering units. Use `App::ConvName` for a conversion from an application. If no conversion with this identifier exists, a placeholder conversion is created. |
| `bOverwrite` | True to overwrite an existing virtual parameter with the same identifier. |
| `szUnits` | Units in which to display the value. Ignored if empty. |
| `szFormatOverride` | Display format override. Ignored if not a valid format. |
| `szGroupPath` | Path of the group to add the parameter to, e.g. `\TopLevelGroup\SubGroup`. Only the last group in the path is used. If the group does not exist, the parameter is not put in a group. |
| `eDataType` | Data type, see [enumDataType](conversion-rules.md#enumdatatype). |
| `dwUpperWarningLimit` | Upper warning (display range) limit. This is the value later returned as the maximum display value. |
| `dwLowerWarningLimit` | Lower warning (display range) limit. This is the value later returned as the minimum display value. |

!!! note
    Returns the same specific codes as [SetVirtualParameter](#setvirtualparameter) (-26, -27, -28, -29, -36).

### SetVirtualParameterToGroup

Creates or modifies a virtual parameter and puts it in an existing group.

```c
long SetVirtualParameterToGroup(
    BSTR rszParamId,
    BSTR rszName,
    BSTR rszDescription,
    double dwMaxDisplay,
    double dwMinDisplay,
    int nMinLoggingRate,
    int nScalingFactor,
    boolean bIsMinNotDef,
    BSTR rszExpression,
    BSTR rszConvId,
    boolean bOverwrite,
    BSTR szUnits,
    BSTR szFormatOverride,
    BSTR szGroupPath);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the virtual parameter. Must not be empty or contain any of `$ % ^ / \ ! &` or a pipe character. |
| `rszName` | Display name of the virtual parameter. Must not be empty or contain the same characters. |
| `rszDescription` | Description of the virtual parameter. |
| `dwMaxDisplay` | Upper limit (sets the upper display and physical limits). |
| `dwMinDisplay` | Lower limit (sets the lower display and physical limits). |
| `nMinLoggingRate` | Logging rate, as a number of `nScalingFactor` units. |
| `nScalingFactor` | Unit of the logging rate, see [EScalingUnit](conversion-rules.md#escalingunit). `10000` (undefined) means no logging rate is set. |
| `bIsMinNotDef` | True to make the logging rate a minimum rate, which marks the virtual parameter as a Prime Parameter. False to make it a default rate. |
| `rszExpression` | FDL expression to evaluate. |
| `rszConvId` | Identifier of the conversion rule that converts the output value to engineering units. Use `App::ConvName` for a conversion from an application. If no conversion with this identifier exists, a placeholder conversion is created. |
| `bOverwrite` | True to overwrite an existing virtual parameter with the same identifier. |
| `szUnits` | Units in which to display the value. Ignored if empty. |
| `szFormatOverride` | Display format override. Ignored if not a valid format. |
| `szGroupPath` | Path of the group to add the parameter to, e.g. `\TopLevelGroup\SubGroup`. Only the last group in the path is used. If the group does not exist, the parameter is not put in a group. |

!!! note
    Returns the same specific codes as [SetVirtualParameter](#setvirtualparameter) (-26, -27, -28, -29, -36).

### SetVirtualParameterToGroupWithDataType

Creates or modifies a virtual parameter with a data type and puts it in an existing group.

```c
long SetVirtualParameterToGroupWithDataType(
    [in] BSTR rszParamId,
    [in] BSTR rszName,
    [in] BSTR rszDescription,
    [in] double dwMaxDisplay,
    [in] double dwMinDisplay,
    [in] int nMinLoggingRate,
    [in] int nScalingFactor,
    [in] boolean bIsMinNotDef,
    [in] BSTR rszExpression,
    [in] BSTR rszConvId,
    [in] boolean bOverwrite,
    [in] BSTR szUnits,
    [in] BSTR szFormatOverride,
    [in] BSTR szGroupPath,
    [in] enumDataType eDataType);
```

| Argument | Description |
|---|---|
| `rszParamId` | Identifier of the virtual parameter. Must not be empty or contain any of `$ % ^ / \ ! &` or a pipe character. |
| `rszName` | Display name of the virtual parameter. Must not be empty or contain the same characters. |
| `rszDescription` | Description of the virtual parameter. |
| `dwMaxDisplay` | Upper limit (sets the upper display and physical limits). |
| `dwMinDisplay` | Lower limit (sets the lower display and physical limits). |
| `nMinLoggingRate` | Logging rate, as a number of `nScalingFactor` units. |
| `nScalingFactor` | Unit of the logging rate, see [EScalingUnit](conversion-rules.md#escalingunit). `10000` (undefined) means no logging rate is set. |
| `bIsMinNotDef` | True to make the logging rate a minimum rate, which marks the virtual parameter as a Prime Parameter. False to make it a default rate. |
| `rszExpression` | FDL expression to evaluate. |
| `rszConvId` | Identifier of the conversion rule that converts the output value to engineering units. Use `App::ConvName` for a conversion from an application. If no conversion with this identifier exists, a placeholder conversion is created. |
| `bOverwrite` | True to overwrite an existing virtual parameter with the same identifier. |
| `szUnits` | Units in which to display the value. Ignored if empty. |
| `szFormatOverride` | Display format override. Ignored if not a valid format. |
| `szGroupPath` | Path of the group to add the parameter to, e.g. `\TopLevelGroup\SubGroup`. Only the last group in the path is used. If the group does not exist, the parameter is not put in a group. |
| `eDataType` | Data type, see [enumDataType](conversion-rules.md#enumdatatype). |

!!! note
    Returns the same specific codes as [SetVirtualParameter](#setvirtualparameter) (-26, -27, -28, -29, -36).

## Enhanced Rate Row Parameters

### RegisterEnhancedRowParameters

Adds measurement parameters from an application to the enhanced speed row parameter list. The list takes effect when [ActivateEnhancedRowParameters](#activateenhancedrowparameters) is called.

```c
long RegisterEnhancedRowParameters([in] short wAppId, [in] VARIANT aszIdentifiers);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the identifiers of the parameters to add. Parameters already in the list are ignored. |

### RegisterCANEnhancedRowParameters

Adds CAN parameters to the enhanced speed row parameter list. The list takes effect when [ActivateEnhancedRowParameters](#activateenhancedrowparameters) is called.

```c
long RegisterCANEnhancedRowParameters([in] VARIANT aszIdentifiers);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the identifiers of the CAN parameters to add. Parameters already in the list are ignored. |

### RegisterVirtualEnhancedRowParameters

Adds virtual parameters to the enhanced speed row parameter list. The list takes effect when [ActivateEnhancedRowParameters](#activateenhancedrowparameters) is called.

```c
long RegisterVirtualEnhancedRowParameters([in] VARIANT aszIdentifiers);
```

| Argument | Description |
|---|---|
| `aszIdentifiers` | 1-D SAFEARRAY of BSTRs holding the identifiers of the virtual parameters to add. |

!!! note
    On activation, each virtual parameter is replaced by all the measurement parameters its expression uses.

### ClearEnhancedRowParameters

Removes the parameters registered for an application from the enhanced speed row parameter list.

```c
long ClearEnhancedRowParameters([in] short wAppId);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. `0` clears the whole list, including CAN and virtual parameters (which can only be cleared this way). |

### ActivateEnhancedRowParameters

Activates the current enhanced speed row parameter list and regenerates the enhanced row configuration.

```c
long ActivateEnhancedRowParameters();
```

This method takes no arguments.

!!! note
    Registered identifiers that are not found in the project are skipped.

**See also:** [ActiveX Methods](index.md); [ActiveX Error Codes](../activex-errors/activex-error-codes.md)
