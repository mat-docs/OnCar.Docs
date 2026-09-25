# ActiveX Error Codes

The following error codes are returned by the ActiveX functions. A code of 0 or greater indicates success; a negative code indicates failure. In C/C++ the macros `SMAPI_SUCCEEDED(Status)` and `SMAPI_FAILED(Status)` test for these.

## General errors

| Code | Constant | Description |
|---|---|---|
| 0 | `SMAPI_ERR_NONE` | No error, function successful. |
| -1 | `SMAPI_ERR_NOPROJECT` | No project loaded in System Monitor. |
| -2 | `SMAPI_ERR_NOLICENCE` | No licence for the requested function. |
| -3 | `SMAPI_ERR_NONE_SPECIFIC` | Non-specific error. |
| -4 | `SMAPI_ERR_DATAVER_MISMATCH` | Data version mismatch. |
| -5 | `SMAPI_ERR_DATAVER_NONE` | No data version loaded. |
| -6 | `SMAPI_ERR_PROGVER_NONE` | No program version loaded. |
| -7 | `SMAPI_ERR_NOECU` | No ECU connected. |
| -8 | `SMAPI_ERR_FILE` | Invalid file specified. |
| -9 | `SMAPI_ERR_NOAPP` | The open project does not cover the specified application. |
| -10 | `SMAPI_ERR_APP_INACTIVE` | The application must be active to support this operation. |
| -11 | `SMAPI_ERR_LIVEUPDATESON` | Operation not allowed while Live Updates are on. |
| -12 | `SMAPI_ERR_TAGONLY` | This command is only valid for TAG systems. |
| -13 | `SMAPI_ERR_SM_BUSY` | System Monitor cannot accept API calls at the moment (it might be in a critical operation, such as loading a project). |

## Message argument errors

!!! note
    Codes -20 to -25 report errors in the VARIANT arguments supplied to [SendMessage](../activex-methods/ecu-control.md#sendmessage) and the related send functions. The message must be a one-dimensional SAFEARRAY of signed 16-bit integers (`VT_I2`) with a lower bound of 0.

| Code | Constant | Description |
|---|---|---|
| -20 | `SMAPI_ERR_MSGARGMISMATCH` | Type mismatch in the SendMessage argument; pass an array of 16-bit integers (WORDs). |
| -21 | `SMAPI_ERR_MSGARGDIM` | Array dimension mismatch in the SendMessage argument; pass a one-dimensional array. |
| -22 | `SMAPI_ERR_MSGLOWERBOUND` | Lower bound of the SendMessage argument was not 0. (Defined, but not currently returned: a non-zero lower bound gives -25.) |
| -23 | `SMAPI_ERR_BOUNDERROR` | Unexpected error getting the array bounds of the SendMessage argument. |
| -24 | `SMAPI_ERR_MSGREPLYARG` | Error in the ReplyMessage argument. |
| -25 | `SMAPI_ERR_MSGSENDARG` | Error in the SendMessage argument. |

## Parameter and state errors

| Code | Constant | Description |
|---|---|---|
| -26 | `SMAPI_ERR_FDL_NOT_PARSED` | Virtual parameter contains invalid FDL. |
| -27 | `SMAPI_ERR_CONV_NOT_VALID` | Conversion for the parameter does not exist or is invalid. |
| -28 | `SMAPI_ERR_PARAM_NOT_VALID` | Parameter name does not exist or is invalid. |
| -29 | `SMAPI_ERR_PARAM_EXISTS` | Parameter exists and overwriting is not allowed. |
| -30 | `SMAPI_ERR_BAD_STATE` | Request cannot be actioned because System Monitor is in the wrong state (for example, a document is missing). |
| -31 | `SMAPI_ERR_INVALID_CMD` | Command passed to System Monitor is not valid. |
| -32 | `SMAPI_ERR_NO_DATA_PRESENT` | Missing document or similar. |
| -33 | `SMAPI_ERR_BAD_MEM_ALLOC` | Memory allocation failed. |
| -34 | `SMAPI_ERR_PARTIALCOMPLETE` | The operation could not be fully completed. |
| -35 | `SMAPI_ERR_DOCUMENTFULL` | The current document (configuration) is full. |
| -36 | `SMAPI_ERR_IDENT_EXISTS` | The parameter identifier already exists in another application. |
| -37 | `SMAPI_ERR_READ_ONLY` | Parameter is read-only; write access denied. |
| -38 | `SMAPI_ERR_NON_LIVE_TUNEABLE` | Parameter is not live-tuneable; write access denied. |
| -39 | `SMAPI_ERR_GROUP_NOTFOUND` | Requested group not found. |
| -40 | `SMAPI_ERR_FILE_NEEDS_SAVING` | The previous file needs saving before a new one is opened. |
| -41 | `SMAPI_ERR_FREQ_OVERRIDDEN` | The frequency set was overridden to the minimum frequency of the prime parameter. |
| -42 | `SMAPI_ERR_NO_CUSTOMER_BASE` | No customer base found for the project being opened. |

## Editable parameter errors

!!! note
    The range -100 to -199 is reserved for errors returned by the parameter get and set value functions. Apart from -100, each code is -100 minus the internal parameter error number.

| Code | Constant | Description |
|---|---|---|
| -100 | `SMAPI_ERR_PARAMNOTFOUND` | The specified parameter does not exist in the current program version. |
| -101 | | Tried to set a read-only parameter. |
| -102 | | Tried to set a parameter outside its limits. |
| -103 | | Axis monotony restrictions not adhered to. |
| -104 | | Tried to get or set a parameter or axis value at an invalid breakpoint. |
| -105 | | The parameter has an invalid address. |
| -106 | | String containing non-numeric characters supplied to a set function. |
| -107 | | Exceeded the specified size of an array or string parameter. |
| -108 | | Live tune enabled, but failed to update the value in the ECU. |
| -109 | | Tried to get an interpolated value, but there is no input quantity or axis points. |
| -110 | | No active live auto tune "layer" (group). |
| -111 | | Operating point is outside the breakpoint tolerances (for example, for live auto tune). |
| -112 | | The number of axis breakpoints has changed between program versions. |
| -113 | | Parameter is not modifiable in the live tune area (warning only, not an error). |
| -114 | | The attempt to validate the value in the unit failed (not the same as the value being invalid). |
| -115 | | The value was updated in the unit, but was invalid when read back. |
| -116 | | Serial number not found for the sensor channel. |
| -117 | | An unknown error. |
| -118 | | Attempt to set the value was cancelled (by the user or because of invalid input). |
| -119 | | Access denied: parameter locked by Reduced Data Access. |
| -120 | | The value set does not match the value in the unit. |

## Data acquisition errors

| Code | Constant | Description |
|---|---|---|
| -200 | `SMAPI_ERR_DETAIL_UNKNOWN` | Session detail does not exist. |
| -201 | `SMAPI_ERR_DUMPROW` | Failed to dump row data. |

## ECU control errors

| Code | Constant | Description |
|---|---|---|
| -300 | `SMAPI_ERR_LIVEUPDATE` | Failed to enter live tune (Live Updates). |
| -301 | `SMAPI_ERR_ONLINE` | Failed to go online. |
| -302 | `SMAPI_ERR_DOWNLOAD_DATA` | Failed to download data. |

## OLE mode and locking errors

| Code | Constant | Description |
|---|---|---|
| -303 | `SMAPI_ERR_SYSMONNOTRUNNING` | System Monitor is only running in OLE mode, so the requested action cannot be performed (see [Accessing ActiveX Functions](../accessing-activex-functions.md)). |
| -304 | `SMAPI_ERR_PARAMETER_LOCKED` | Parameter locked by Reduced Data Access. |

## Communications errors

!!! note
    The range -1000 to -10000 is reserved for System Monitor communications, CA-Card, Ethernet or ECU errors, which may be returned by a SendMessage call or other ECU operations. Each code is -1000 minus the communications status code; codes from -1001 to about -1116 are status codes returned by the ECU itself.

| Code | Description |
|---|---|
| -5096 | There is a communications problem that is unknown. |
| -5097 | General timeout during communications. |
| -5098 | Link to ECU not OK. |
| -5099 | CA-Card code failed to load. |
| -5100 | Failed to open the CA-Card device driver. |
| -5101 | Failed to close the CA-Card device driver. |
| -5102 | DPC area is blank: CA-Card code is not running. |
| -5103 | DPR CaPc buffer is full: incoming messages have been lost. |
| -5104 | Driver kernel buffer is full: incoming messages have been lost. |
| -5105 | The driver has timed out waiting for some data. |
| -5106 | There is no card in the machine. |
| -5107 | Receive buffer passed to DeviceIoControl is too small. |
| -5108 | The CA-Card code has been loaded but has crashed. |
| -5109 | `IOCTL_CA125_CASEND`: not enough data returned. |
| -5110 | `IOCTL_CA125_CAREAD`: not enough data returned. |
| -5111 | Attempt to send more data than the CA-Card said it can accept. |
| -5112 | The CA-Card has given more data than it said it would. |
| -5113 | Error response to the `MESSAGE_ID_SETUP_SESSION` message. |
| -5114 | Error response to the `MESSAGE_ID_OPEN_SESSION` message. |
| -5115 | Error response to the `MESSAGE_ID_CLOSE_SESSION` message. |
| -5116 | Error response to the `MESSAGE_ID_SEND_SESSION` message. |
| -5117 | Error response to the `MESSAGE_ID_RECEIVE_SESSION` message. |
| -5121 | CA-Session in use. |
| -5123 | Failed to resolve the address for the session. |
| -5124 | User cancelled the operation. |
| -5125 | Data on the unit is not as expected. |
| -5126 | Failed to establish encrypted communications. |
| -5127 | Invalid session: re-query the unit. |

**See also:** [ActiveX Errors](index.md); [ActiveX Methods](../activex-methods/index.md)
