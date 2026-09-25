# Conversion Rules

Methods for reading and creating conversion rules. The [Enumeration Definitions](#enumeration-definitions) used by the ActiveX methods are listed at the end of this page.

See [ActiveX Methods](index.md) for the conventions used on this page, and [ActiveX Error Codes](../activex-errors/activex-error-codes.md) for the return codes.

## Functions

### GetConversions

Returns the identifiers and types of all conversion rules in an application, or in the non-application parameter sets (for example virtual and CAN).

```c
long GetConversions(
    [in] short wAppId,
    [out] VARIANT* str1xIdentifiers,
    [out] VARIANT* str1xType);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. `0` returns the conversions of the non-application parameter sets (for example virtual and CAN) instead. |
| `str1xIdentifiers` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the conversion identifiers. |
| `str1xType` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the type of each conversion: `RATIONAL`, `TABLE`, `TEXT` or `FREE`. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project.

### GetConversionType

Returns the type of a conversion rule. All applications and the virtual and CAN parameters are searched.

```c
long GetConversionType([in] BSTR pszConversionId, [out] BSTR* pszConversionType);
```

| Argument | Description |
|---|---|
| `pszConversionId` | Conversion identifier. |
| `pszConversionType` | Receives the conversion type: `RATIONAL`, `TABLE`, `TEXT` or `FREE`. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the conversion is not found.

### GetConversionUse

Returns the parameters that use a conversion rule.

```c
long GetConversionUse(
    [in] short wAppId,
    [in] BSTR pszConversion,
    [out] VARIANT* str1xParameters);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. Only parameters in this application are returned. `0` returns parameters from all applications, including virtual and CAN parameters. |
| `pszConversion` | Conversion identifier. |
| `str1xParameters` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the parameter identifiers. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the conversion is not found.

### GetFormulaConv

Retrieves a formula (free) conversion rule. All applications and the virtual and CAN parameters are searched.

```c
long GetFormulaConv(
    [in] BSTR pszConvId,
    [out] BSTR* pszComment,
    [out] BSTR* pszFormat,
    [out] BSTR* pszUnits,
    [out] BSTR* pszFormula,
    [out] BSTR* pszInverse);
```

| Argument | Description |
|---|---|
| `pszConvId` | Unique identifier of the conversion. |
| `pszComment` | Receives the description. |
| `pszFormat` | Receives the format string (e.g. `%1.3f`). |
| `pszUnits` | Receives the units of the converted value. |
| `pszFormula` | Receives the formula. |
| `pszInverse` | Receives the inverse formula. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the conversion is not found or is not a formula conversion.

### GetRationalConv

Retrieves a rational conversion rule. All applications and the virtual and CAN parameters are searched.

```c
long GetRationalConv(
    BSTR pszConvId,
    double * pdPar1,
    double * pdPar2,
    double * pdPar3,
    double * pdPar4,
    double * pdPar5,
    double * pdPar6,
    BSTR * pszComment,
    BSTR * pszFormat,
    BSTR * pszUnits,
    BSTR * pszDefault);
```

| Argument | Description |
|---|---|
| `pszConvId` | Unique identifier of the conversion. |
| `pdPar1` | Receives coefficient 1. |
| `pdPar2` | Receives coefficient 2. |
| `pdPar3` | Receives coefficient 3. |
| `pdPar4` | Receives coefficient 4. |
| `pdPar5` | Receives coefficient 5. |
| `pdPar6` | Receives coefficient 6. |
| `pszComment` | Receives the description. |
| `pszFormat` | Receives the format string (e.g. `%1.3f`). |
| `pszUnits` | Receives the units of the converted value. |
| `pszDefault` | Receives the default value. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the conversion is not found or is not a rational conversion.

### GetRationalConvFromApp

Retrieves a rational conversion rule from a given application.

```c
long GetRationalConvFromApp(
    short wAppId,
    BSTR pszConvId,
    double * pdPar1,
    double * pdPar2,
    double * pdPar3,
    double * pdPar4,
    double * pdPar5,
    double * pdPar6,
    BSTR * pszComment,
    BSTR * pszFormat,
    BSTR * pszUnits,
    BSTR * pszDefault);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszConvId` | Unique identifier of the conversion. |
| `pdPar1` | Receives coefficient 1. |
| `pdPar2` | Receives coefficient 2. |
| `pdPar3` | Receives coefficient 3. |
| `pdPar4` | Receives coefficient 4. |
| `pdPar5` | Receives coefficient 5. |
| `pdPar6` | Receives coefficient 6. |
| `pszComment` | Receives the description. |
| `pszFormat` | Receives the format string (e.g. `%1.3f`). |
| `pszUnits` | Receives the units of the converted value. |
| `pszDefault` | Receives the default value. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project, or `SMAPI_ERR_NONE_SPECIFIC` (-3) if the conversion is not found in the application.

### GetTableConv

Retrieves a table conversion rule. All applications and the virtual and CAN parameters are searched.

```c
long GetTableConv(
    BSTR pszConvId,
    BSTR * pszComment,
    BSTR * pszFormat,
    BSTR * pszUnits,
    BSTR * pszDefault,
    boolean * pbInterpolate,
    VARIANT * pafVariantRaw,
    VARIANT * pafVariantMapped);
```

| Argument | Description |
|---|---|
| `pszConvId` | Unique identifier of the conversion rule. |
| `pszComment` | Receives the description. |
| `pszFormat` | Receives the format string (e.g. `%1.3f`). |
| `pszUnits` | Receives the units of the converted value. |
| `pszDefault` | Receives the default value. |
| `pbInterpolate` | Receives True if interpolation is on, otherwise False. |
| `pafVariantRaw` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_R8`) holding the raw values. |
| `pafVariantMapped` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_R8`) holding the mapped values. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the conversion is not found or is not a table conversion.

### GetTableConvFromApp

Retrieves a table conversion rule from a given application.

```c
long GetTableConvFromApp(
    short wAppId,
    BSTR pszConvId,
    BSTR * pszComment,
    BSTR * pszFormat,
    BSTR * pszUnits,
    BSTR * pszDefault,
    boolean * pbInterpolate,
    VARIANT * pafVariantRaw,
    VARIANT * pafVariantMapped);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pszConvId` | Unique identifier of the conversion rule. |
| `pszComment` | Receives the description. |
| `pszFormat` | Receives the format string (e.g. `%1.3f`). |
| `pszUnits` | Receives the units of the converted value. |
| `pszDefault` | Receives the default value. |
| `pbInterpolate` | Receives True if interpolation is on, otherwise False. |
| `pafVariantRaw` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_R8`) holding the raw values. |
| `pafVariantMapped` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_R8`) holding the mapped values. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project, or `SMAPI_ERR_NONE_SPECIFIC` (-3) if the conversion is not found in the application.

### GetTextConv

Retrieves the raw values and text mappings of a text conversion rule.

```c
long GetTextConv(
    [in] short wAppId,
    [in] BSTR pszConversionId,
    [out] BSTR* pszFormat,
    [out] BSTR* pszUnits,
    [out] BSTR* pszDefault,
    [out] VARIANT* pafRawInput,
    [out] VARIANT* pastrTextMapping);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. `0` searches all applications. The application does not need to be active. |
| `pszConversionId` | Unique identifier of the conversion rule. |
| `pszFormat` | Receives the format string. |
| `pszUnits` | Receives the units. |
| `pszDefault` | Receives the default value. |
| `pafRawInput` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_R8`) holding the raw values. |
| `pastrTextMapping` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the text for each raw value. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project, or `SMAPI_ERR_PARAMNOTFOUND` (-100) if the conversion is not found.

### GetTextConvEx

Retrieves the raw values and text mappings of a text conversion rule, without an Application Id. All applications and the virtual and CAN parameters are searched.

```c
long GetTextConvEx(
    [in] BSTR pszConversionId,
    [out] BSTR* pszFormat,
    [out] BSTR* pszUnits,
    [out] BSTR* pszDefault,
    [out] VARIANT* pafRawInput,
    [out] VARIANT* pastrTextMapping);
```

| Argument | Description |
|---|---|
| `pszConversionId` | Unique identifier of the conversion rule. |
| `pszFormat` | Receives the format string. |
| `pszUnits` | Receives the units. |
| `pszDefault` | Receives the default value. |
| `pafRawInput` | Receives a 1-D, 0-based SAFEARRAY of doubles (`VT_R8`) holding the raw values. |
| `pastrTextMapping` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the text for each raw value. |

!!! note
    Returns `SMAPI_ERR_PARAMNOTFOUND` (-100) if the conversion is not found or is not a text conversion.

### RemoveAllConversions

Removes all user-created (virtual parameter) conversion rules.

```c
long RemoveAllConversions();
```

This method takes no arguments.

!!! note
    Nothing is removed and `SMAPI_ERR_NONE_SPECIFIC` (-3) is returned if any virtual parameter uses one of these conversions. Returns `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no virtual parameters document.

### RemoveConversion

Removes a user-created (virtual parameter) conversion rule.

```c
long RemoveConversion(BSTR pszConvId);
```

| Argument | Description |
|---|---|
| `pszConvId` | Unique identifier of the conversion rule to remove. |

!!! note
    Returns `SMAPI_ERR_NONE_SPECIFIC` (-3) if the conversion is not found or is used by a virtual parameter, or `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no virtual parameters document.

### SetFormulaConv

Creates or modifies a formula (free) conversion rule in the virtual parameters.

```c
long SetFormulaConv(
    [in] BSTR pszConvId,
    [in] BSTR szComment,
    [in] BSTR szFormat,
    [in] BSTR szUnits,
    [in] BSTR szFormula,
    [in] BSTR szInverse,
    [in] boolean bOverwriteFlag);
```

| Argument | Description |
|---|---|
| `pszConvId` | Unique identifier of the conversion. Must not be empty. |
| `szComment` | Description. |
| `szFormat` | Format string (e.g. `%1.3f`). |
| `szUnits` | Units of the converted value. |
| `szFormula` | Formula. |
| `szInverse` | Inverse formula. |
| `bOverwriteFlag` | True to overwrite an existing virtual conversion with the same identifier. |

!!! note
    Returns `SMAPI_ERR_CONV_NOT_VALID` (-27) if `pszConvId` is empty, `SMAPI_ERR_PARAM_EXISTS` (-29) if the conversion exists and `bOverwriteFlag` is False, `SMAPI_ERR_IDENT_EXISTS` (-36) if an application already has a conversion with this identifier, or `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no virtual parameters document.

### SetRationalConv

Creates or modifies a rational conversion rule in the virtual parameters.

```c
long SetRationalConv(
    BSTR pszConvId,
    double dP1,
    double dP2,
    double dP3,
    double dP4,
    double dP5,
    double dP6,
    BSTR pszComment,
    BSTR pszFormat,
    BSTR pszUnits,
    BSTR pszDefault,
    boolean bOverwriteFlag);
```

| Argument | Description |
|---|---|
| `pszConvId` | Unique identifier of the conversion. Must not be empty. |
| `dP1` | Coefficient 1. |
| `dP2` | Coefficient 2. |
| `dP3` | Coefficient 3. |
| `dP4` | Coefficient 4. |
| `dP5` | Coefficient 5. |
| `dP6` | Coefficient 6. |
| `pszComment` | Description. |
| `pszFormat` | Format string (e.g. `%1.3f`). |
| `pszUnits` | Units of the converted value. |
| `pszDefault` | Default value. |
| `bOverwriteFlag` | True to overwrite an existing virtual conversion with the same identifier. |

!!! note
    Returns `SMAPI_ERR_CONV_NOT_VALID` (-27) if `pszConvId` is empty, `SMAPI_ERR_PARAM_EXISTS` (-29) if the conversion exists and `bOverwriteFlag` is False, `SMAPI_ERR_IDENT_EXISTS` (-36) if an application already has a conversion with this identifier, or `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no virtual parameters document.

### SetTableConv

Creates or modifies a table conversion rule in the virtual parameters.

```c
long SetTableConv(
    BSTR pszConvId,
    BSTR pszComment,
    BSTR pszFormat,
    BSTR pszUnits,
    BSTR pszDefault,
    boolean bInterpolate,
    VARIANT afRawValues,
    VARIANT afMappedValues,
    boolean bOverwriteFlag);
```

| Argument | Description |
|---|---|
| `pszConvId` | Unique identifier of the conversion rule. Must not be empty. |
| `pszComment` | Description. |
| `pszFormat` | Format string (e.g. `%1.3f`). |
| `pszUnits` | Units of the converted value. |
| `pszDefault` | Default value. |
| `bInterpolate` | True to turn interpolation on, False to turn it off. |
| `afRawValues` | 1-D SAFEARRAY of doubles (`VT_R8`) holding the raw values. Any lower bound is accepted. A 2-D array with a single row or column is also accepted. |
| `afMappedValues` | 1-D SAFEARRAY of doubles (`VT_R8`) holding the mapped values, one for each raw value. |
| `bOverwriteFlag` | True to overwrite an existing virtual conversion with the same identifier. |

!!! note
    Returns `SMAPI_ERR_CONV_NOT_VALID` (-27) if `pszConvId` is empty or the table is not valid, `SMAPI_ERR_PARAM_EXISTS` (-29) if the conversion exists and `bOverwriteFlag` is False, `SMAPI_ERR_IDENT_EXISTS` (-36) if an application already has a conversion with this identifier, or `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no virtual parameters document.

### SetTextConv

Creates a text conversion rule in the virtual parameters. An existing conversion is not modified; use [SetTextConvEx](#settextconvex) to overwrite one.

```c
long SetTextConv(
    [in] short wAppId,
    [in] BSTR pszConversionId,
    [in] BSTR pszFormat,
    [in] BSTR pszUnits,
    [in] BSTR pszDefault,
    [in] VARIANT afRawInput,
    [in] VARIANT astrTextMapping);
```

| Argument | Description |
|---|---|
| `wAppId` | Ignored. |
| `pszConversionId` | Unique identifier of the conversion rule. |
| `pszFormat` | Format string. |
| `pszUnits` | Units. |
| `pszDefault` | Default value. |
| `afRawInput` | 1-D SAFEARRAY of doubles (`VT_R8`) holding the raw values. |
| `astrTextMapping` | 1-D SAFEARRAY of strings (`VT_BSTR`) holding the text for each raw value. |

!!! note
    Returns `SMAPI_ERR_PARAM_EXISTS` (-29) if the conversion already exists, `SMAPI_ERR_IDENT_EXISTS` (-36) if an application already has a conversion with this identifier, or `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no virtual parameters document.

### SetTextConvEx

Creates or modifies a text conversion rule in the virtual parameters.

```c
long SetTextConvEx(
    [in] BSTR pszConversionId,
    [in] BSTR pszFormat,
    [in] BSTR pszUnits,
    [in] BSTR pszDefault,
    [in] VARIANT afRawInput,
    [in] VARIANT astrTextMapping,
    [in] boolean bOverwriteExisting);
```

| Argument | Description |
|---|---|
| `pszConversionId` | Unique identifier of the conversion rule. |
| `pszFormat` | Format string. |
| `pszUnits` | Units. |
| `pszDefault` | Default value. |
| `afRawInput` | 1-D SAFEARRAY of doubles (`VT_R8`) holding the raw values. |
| `astrTextMapping` | 1-D SAFEARRAY of strings (`VT_BSTR`) holding the text for each raw value. |
| `bOverwriteExisting` | True to overwrite an existing virtual conversion with the same identifier. |

!!! note
    Returns `SMAPI_ERR_PARAM_EXISTS` (-29) if the conversion exists and `bOverwriteExisting` is False, `SMAPI_ERR_IDENT_EXISTS` (-36) if an application already has a conversion with this identifier, or `SMAPI_ERR_NO_DATA_PRESENT` (-32) if there is no virtual parameters document.

## Enumeration Definitions

The following enumerations are used by functions on the ActiveX method pages. Each is shown as it would be declared in Visual Basic; the raw values can be used in their place. Apart from `enumDataType`, these enumerations are not part of the System Monitor type library, so clients must declare them (or use the raw values) themselves.

### ETypeFreqValue

Type of logging rate value for a remote logging parameter (the `wValueType` argument of the AddRemoteParam functions).

```vb
Public Enum ETypeFreqValue
    eFrequency = 0        ' Value is a frequency
    eCylinder = 1         ' Value is an engine segment (cylinder)
    eCycle = 2            ' Once per engine cycle (value not used)
    eUnknownLogType = 3
    eEdge = 4             ' Log on every edge
End Enum
```

### ECONDITONTYPE

Remote logging trigger condition type.

```vb
Public Enum ECONDITONTYPE
    DAQ_ONDATA = 0            ' On data (with parameter)
    DAQ_DRIVERPUSH = 1        ' Driver push (not supported)
    DAQ_IGNITIONON = 2        ' Ignition on
    DAQ_LAPTRIGGER = 3        ' Lap trigger
    DAQ_NOCONDITION = 4       ' No condition
    DAQ_EXTERNALTRIGGER = 5   ' External trigger
End Enum
```

### ECOMPARISON

Comparison operator of an "On data" trigger condition.

```vb
Public Enum ECOMPARISON
    DAQ_EQUALS = 0        ' =
    DAQ_LESS = 1          ' <
    DAQ_GREAT = 2         ' >
    DAQ_NOTEQUALS = 3     ' !=
    DAQ_GREATEQUALS = 4   ' >=
    DAQ_LESSEQUALS = 5    ' <=
End Enum
```

### EScalingUnit

Scaling unit (logging rate unit) of a parameter, as used by the virtual and CAN parameter functions.

```vb
Public Enum EScalingUnit
    TSU_1_MCSEC = 0       ' 1 microsecond
    TSU_10_MCSEC = 1      ' 10 microseconds
    TSU_100_MCSEC = 2     ' 100 microseconds
    TSU_1_MSEC = 3        ' 1 millisecond
    TSU_10_MSEC = 4       ' 10 milliseconds
    TSU_100_MSEC = 5      ' 100 milliseconds
    TSU_1_SEC = 6         ' 1 second
    TSU_10_SEC = 7        ' 10 seconds
    TSU_1_MIN = 8         ' 1 minute
    TSU_1_HOUR = 9        ' 1 hour
    TSU_1_DAY = 10        ' 1 day
    TSU_1_DEG = 11        ' 1 angular degree
    TSU_1_REV = 12        ' 1 revolution (360 degrees)
    TSU_1_CYC = 13        ' 1 cycle (720 degrees)
    TSU_1_SEG = 14        ' 1 cylinder segment
    TSU_ON_NEW = 15       ' Always on new value
    TSU_NON_DET = 1000    ' Non-deterministic (no fixed scaling)
    TSU_UNDEFINED = 10000 ' Not defined in the ASAP file
End Enum
```

### enumDataType

Data type of a virtual parameter. This enumeration is defined in the System Monitor type library.

```vb
Public Enum enumDataType
    ADT_UBYTE = 0          ' Unsigned byte
    ADT_SBYTE = 1          ' Signed byte
    ADT_UWORD = 2          ' Unsigned word
    ADT_SWORD = 3          ' Signed word
    ADT_ULONG = 4          ' Unsigned long
    ADT_SLONG = 5          ' Signed long
    ADT_FLOAT32_IEEE = 6   ' Float
    ADT_FLOAT64_IEEE = 7   ' Double
End Enum
```

**See also:** [ActiveX Methods](index.md); [ActiveX Error Codes](../activex-errors/activex-error-codes.md)
