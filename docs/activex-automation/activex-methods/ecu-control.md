# ECU Control

Methods for going online, Live Updates, reprogramming, downloading data changes, selecting the car connection and sending messages to the ECU.

See [ActiveX Methods](index.md) for the conventions used on this page, and [ActiveX Error Codes](../activex-errors/activex-error-codes.md) for the return codes.

## Functions

### ClearEvents

Clears the event window in System Monitor.

```c
long ClearEvents();
```

This method takes no arguments.

### DeleteErrors

Runs the System Monitor ECU menu command **Delete Errors**, which deletes the errors held by the ECU.

```c
long DeleteErrors();
```

This method takes no arguments.

!!! note
    The command is sent to the System Monitor main window. The return value only reports whether the command could be issued, not whether the errors were deleted.

### DeleteMinMax

Runs the System Monitor ECU menu command **Delete Min/Max**, which deletes the minimum and maximum values held by the ECU.

```c
long DeleteMinMax();
```

This method takes no arguments.

!!! note
    The command is sent to the System Monitor main window. The return value only reports whether the command could be issued, not whether the values were deleted.

### DownloadDataChanges

Downloads the changes made in the System Monitor edit buffer for an application to the ECU.

```c
long DownloadDataChanges(short wAppId);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project, or `SMAPI_ERR_DOWNLOAD_DATA` (-302) if the download fails.

### DownloadRemoteInProgress

Returns whether a remote logging download is currently in progress.

```c
long DownloadRemoteInProgress([out] boolean* bInProgress);
```

| Argument | Description |
|---|---|
| `bInProgress` | Receives True if a remote logging download is in progress, otherwise False. |

!!! note
    This method does not need a project to be open.

### EditBufferSynced

Returns whether the edit buffer of an application is in sync with the ECU. The program version, data version and controller data IDs in the ECU are compared with those in the edit buffer.

```c
long EditBufferSynced(short wAppId, boolean* pbResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pbResult` | Receives True if the edit buffer is in sync with the ECU, otherwise False. False is also returned if the ECU cannot be queried. |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) if the application is not in the project, or `SMAPI_ERR_NONE_SPECIFIC` (-3) if the ECU or the data version for the application is not available.

### ForceReprogram

Performs a forced complete reprogram of the ECU for the given applications. Otherwise it behaves as [ReprogramEx](#reprogramex).

```c
long ForceReprogram(VARIANT awAppIds);
```

| Argument | Description |
|---|---|
| `awAppIds` | 1-D SAFEARRAY of 16-bit integers (`VT_I2` or `VT_UI2`) holding the Application Ids to reprogram, one Id per element. Any lower bound is accepted. |

!!! note
    Live updates are switched off during the reprogram. Returns `SMAPI_ERR_LIVEUPDATESON` (-11) if live updates cannot be switched off, `SMAPI_ERR_NOAPP` (-9) if none of the given applications can be reprogrammed, or `SMAPI_ERR_DOWNLOAD_DATA` (-302) if the reprogram fails. An application is skipped if its data version uses an unlock list whose file cannot be found.

### GetCarByIndex

Returns the name, unit type and IP address of an entry in the car/unit list (as returned by [GetCarList](#getcarlist)).

```c
long GetCarByIndex(
    [in] short wIndex,
    [out] BSTR* pszName,
    [out] BSTR* pszType,
    [out] BSTR* pszIPAddress);
```

| Argument | Description |
|---|---|
| `wIndex` | 0-based index of the entry in the list returned by [GetCarList](#getcarlist). |
| `pszName` | Receives the car/connection name. |
| `pszType` | Receives the unit type(s) of the car. For a car with more than one unit the types are separated by `/`. |
| `pszIPAddress` | Receives the IP address of the car. For a car with more than one unit, the address of the first unit is repeated once per unit, separated by spaces. |

!!! note
    Returns `SMAPI_ERR_INVALID_CMD` (-31) if `wIndex` is outside the list.

### GetCarList

Returns the cars/units defined in the `carfile.ini` file (the connections that appear in the connections dialog). Only cars whose system type matches the communications path of the applications in the project are returned.

```c
long GetCarList(
    [out] VARIANT* aszName,
    [out] VARIANT* aszType,
    [out] VARIANT* aszIPAddress);
```

| Argument | Description |
|---|---|
| `aszName` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the car/connection names. |
| `aszType` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the unit type(s) of each car. For a car with more than one unit the types are separated by `/`. |
| `aszIPAddress` | Receives a 1-D, 0-based SAFEARRAY of strings (`VT_BSTR`) holding the IP address of each car. For a car with more than one unit, the address of the first unit is repeated once per unit, separated by spaces. |

### GetCarName

Returns the name of the current car/connection.

```c
long GetCarName(BSTR* pszResult);
```

| Argument | Description |
|---|---|
| `pszResult` | Receives the car name. |

### GetLinkStatus

Gets the status of the link to the ECU that holds an application.

```c
long GetLinkStatus(short wAppId, short* pwResult);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. |
| `pwResult` | Receives the link status:<br>`0` = Link OK<br>`1` = Link not OK<br>`2` = Controller is busy<br>`3` = Device is in boot<br>`4` = Device is in Zone 1<br>`5` = Device is in Zone 2<br>`6` = Device is in Zone 3<br>`7` = Bad response<br>`8` = Wrong device connected<br>`-1` = Unknown status |

!!! note
    Returns `SMAPI_ERR_NOAPP` (-9) and a status of `-1` if there is no ECU for the application.

### GetLiveUpdates

Gets whether live updates are enabled.

```c
long GetLiveUpdates(boolean* bResult);
```

| Argument | Description |
|---|---|
| `bResult` | Receives True if live updates are enabled, otherwise False. |

### GetOnline

Gets whether System Monitor is online to the ECU.

```c
long GetOnline(boolean* bResult);
```

| Argument | Description |
|---|---|
| `bResult` | Receives True if online, False if offline. |

### GetStatus

Gets the online state, live updates state, link status and active applications in one call. It combines [GetOnline](#getonline), [GetLiveUpdates](#getliveupdates), [GetLinkStatus](#getlinkstatus) and `GetActiveApp`, and stops at the first error.

```c
long GetStatus(
    boolean* pbOnlineResult,
    boolean* pbLiveUpdatesResult,
    short wLinkStatusAppId,
    short* pwLinkStatusResult,
    short* pwActiveAppResult);
```

| Argument | Description |
|---|---|
| `pbOnlineResult` | Receives True if online, False if offline. |
| `pbLiveUpdatesResult` | Receives True if live updates are enabled, otherwise False. |
| `wLinkStatusAppId` | Application Id whose link status is returned. |
| `pwLinkStatusResult` | Receives the link status:<br>`0` = Link OK<br>`1` = Link not OK<br>`2` = Controller is busy<br>`3` = Device is in boot<br>`4` = Device is in Zone 1<br>`5` = Device is in Zone 2<br>`6` = Device is in Zone 3<br>`7` = Bad response<br>`8` = Wrong device connected<br>`-1` = Unknown status |
| `pwActiveAppResult` | Receives the Application Ids of the active applications, combined with bitwise OR. |

### Reprogram

Reprograms the ECU with the given applications. Application Ids can be combined with bitwise OR to reprogram more than one application at the same time.

```c
long Reprogram(short wAppId);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id, or several Application Ids combined with bitwise OR. |

!!! note
    Live updates are switched off during the reprogram. Returns `SMAPI_ERR_LIVEUPDATESON` (-11) if live updates cannot be switched off, `SMAPI_ERR_NOAPP` (-9) if none of the given applications can be reprogrammed, or `SMAPI_ERR_DOWNLOAD_DATA` (-302) if the reprogram fails. An application is skipped if its data version uses an unlock list whose file cannot be found.

### ReprogramEx

Reprograms the ECU with the applications given in an array.

```c
long ReprogramEx(VARIANT awAppIds);
```

| Argument | Description |
|---|---|
| `awAppIds` | 1-D SAFEARRAY of 16-bit integers (`VT_I2` or `VT_UI2`) holding the Application Ids to reprogram, one Id per element. Any lower bound is accepted. |

!!! note
    Live updates are switched off during the reprogram. Returns `SMAPI_ERR_LIVEUPDATESON` (-11) if live updates cannot be switched off, `SMAPI_ERR_NOAPP` (-9) if none of the given applications can be reprogrammed, or `SMAPI_ERR_DOWNLOAD_DATA` (-302) if the reprogram fails. An application is skipped if its data version uses an unlock list whose file cannot be found.

### SendMessage

Sends a message to the ECU that holds an application and returns the reply. The message is sent once.

```c
long SendMessage(
    short wAppId,
    VARIANT rSendMessage,
    VARIANT* pReplyMessage,
    short wTimeout);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. It must be an application in the project. |
| `rSendMessage` | Message to send, as a 1-D SAFEARRAY of signed 16-bit words (`VT_I2`) with a lower bound of 0. |
| `pReplyMessage` | Receives the reply as a new 1-D, 0-based SAFEARRAY of signed 16-bit words (`VT_I2`). |
| `wTimeout` | Message timeout. |

!!! note
    `rSendMessage` must be a SAFEARRAY of type `VT_ARRAY|VT_I2`, passed by value or by reference, with one dimension and a lower bound of 0. Otherwise the method returns `SMAPI_ERR_MSGARGMISMATCH` (-20) for the wrong type, `SMAPI_ERR_MSGARGDIM` (-21) for the wrong number of dimensions, `SMAPI_ERR_BOUNDERROR` (-23) if the bounds cannot be read, or `SMAPI_ERR_MSGSENDARG` (-25) if an element cannot be read (for example, when the lower bound is not 0).

    Returns `SMAPI_ERR_NOAPP` (-9) if `wAppId` is not an application in the project. The link to the ECU is checked before sending. Communication errors are returned as -1000 minus the ECU status code; a reply may still be returned with such an error.

### SendMessageEx

Sends a message to the ECU that holds an application and returns the reply, with a set number of tries.

```c
long SendMessageEx(
    short wAppId,
    VARIANT rSendMessage,
    VARIANT* pReplyMessage,
    short wTimeout,
    short wTries);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. It must be an application in the project. |
| `rSendMessage` | Message to send, as a 1-D SAFEARRAY of signed 16-bit words (`VT_I2`) with a lower bound of 0. |
| `pReplyMessage` | Receives the reply as a new 1-D, 0-based SAFEARRAY of signed 16-bit words (`VT_I2`). |
| `wTimeout` | Message timeout. |
| `wTries` | Number of tries before an error is returned. |

!!! note
    The array requirements and error codes are the same as for [SendMessage](#sendmessage).

### SendModemMessage

Sends a message to the ECU that holds an application via the modem and returns the reply. The message is sent once.

```c
long SendModemMessage(
    short wAppId,
    VARIANT rSendMessage,
    VARIANT* pReplyMessage,
    short wTimeout);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. It must be an application in the project. |
| `rSendMessage` | Message to send, as a 1-D SAFEARRAY of signed 16-bit words (`VT_I2`) with a lower bound of 0. |
| `pReplyMessage` | Receives the reply as a new 1-D, 0-based SAFEARRAY of signed 16-bit words (`VT_I2`). |
| `wTimeout` | Message timeout. |

!!! note
    The array requirements and error codes are the same as for [SendMessage](#sendmessage), except that the link is not checked before sending.

### SendModemMessageEx

Sends a message to the ECU that holds an application via the modem and returns the reply, with a set number of tries.

```c
long SendModemMessageEx(
    short wAppId,
    VARIANT rSendMessage,
    VARIANT* pReplyMessage,
    short wTimeout,
    short wTries);
```

| Argument | Description |
|---|---|
| `wAppId` | Application Id. It must be an application in the project. |
| `rSendMessage` | Message to send, as a 1-D SAFEARRAY of signed 16-bit words (`VT_I2`) with a lower bound of 0. |
| `pReplyMessage` | Receives the reply as a new 1-D, 0-based SAFEARRAY of signed 16-bit words (`VT_I2`). |
| `wTimeout` | Message timeout. |
| `wTries` | Number of tries before an error is returned. |

!!! note
    The array requirements and error codes are the same as for [SendMessage](#sendmessage), except that the link is not checked before sending.

### SetCarByIndex

Sets the car/unit connection to an entry in the car/unit list (as returned by [GetCarList](#getcarlist)). If the car changes, System Monitor goes offline, restarts communications with the new car and then restores the online state.

```c
long SetCarByIndex([in] short wIndex, boolean bPrimaryCar);
```

| Argument | Description |
|---|---|
| `wIndex` | 0-based index of the entry in the list returned by [GetCarList](#getcarlist). |
| `bPrimaryCar` | True if the connection is for the main car, False if it is for the spare car. |

!!! note
    Returns `SMAPI_ERR_LIVEUPDATESON` (-11) if live updates are enabled, or `SMAPI_ERR_INVALID_CMD` (-31) if `wIndex` is outside the list.

### SetLiveupdates

Enables or disables the sending of live updates to the ECU.

```c
long SetLiveupdates(boolean bState);
```

| Argument | Description |
|---|---|
| `bState` | True to enable, False to disable. |

!!! note
    When enabling, the program version, data version and controller data IDs of each active application are compared with the ECU. If they do not match, live updates are not enabled and `SMAPI_ERR_DATAVER_MISMATCH` (-4) is returned. Returns `SMAPI_ERR_LIVEUPDATE` (-300) if the live update state cannot be changed.

### SetLiveUpdatesEx

Enables or disables the sending of live updates to the ECU, with an action to take when the data version matches but the data is different.

```c
long SetLiveUpdatesEx([in] boolean bState, [in] WORD wAction);
```

| Argument | Description |
|---|---|
| `bState` | True to enable, False to disable. |
| `wAction` | Action on a data mismatch:<br>`0` = No action<br>`1` = Upload data from the unit into the edit buffer<br>`2` = Download the edit buffer into the unit (live tunes in the unit may be lost) |

!!! note
    Returns `SMAPI_ERR_BAD_STATE` (-30) if `wAction` is greater than 2, or `SMAPI_ERR_LIVEUPDATE` (-300) if the live update state cannot be changed.

### SetOnline

Turns System Monitor online or offline to the ECU. Does nothing if it is already in the requested state.

```c
long SetOnline(boolean bState);
```

| Argument | Description |
|---|---|
| `bState` | True to go online, False to go offline. |

!!! note
    Returns `SMAPI_ERR_ONLINE` (-301) if the online state cannot be changed.

### UndoDataChanges

Undoes data changes in the unit, in the edit buffer, or both, for all applications on the main car. This is the same as the **Undo Data Changes** commands in the ECU menu.

```c
long UndoDataChanges([in] short wType);
```

| Argument | Description |
|---|---|
| `wType` | Undo type:<br>`1` = Undo data changes in unit<br>`2` = Undo data changes in edit buffer<br>`3` = Undo data changes in unit and edit buffer |

!!! note
    Returns `SMAPI_ERR_NOECU` (-7) if wireless communications are in use. Returns `SMAPI_ERR_INVALID_CMD` (-31) if `wType` is not 1, 2 or 3, or if the undo cannot be done: types 1 and 3 need communications with the unit and the ECU read-only option to be off; types 1 and 2 need live updates to be off.

**See also:** [ActiveX Methods](index.md); [ActiveX Error Codes](../activex-errors/activex-error-codes.md)
