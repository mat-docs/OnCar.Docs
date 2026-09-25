# Accessing ActiveX Functions

To gain access to System Monitor, a client must create an instance of the System Monitor Automation Server. The exact syntax varies with the client programming language, but the function is typically called **CreateObject**. The argument supplied to this function must be the ProgID `"System Monitor API"`. Refer to the documentation for your language for further details.

Create the instance while System Monitor is running with a project open. If System Monitor is not running, Windows starts it in a windowless "OLE mode" (shown by a **System Monitor OLE Mode** tray icon). In this mode only [GetBuildNumber](activex-methods/project-management.md#getbuildnumber) and [GetVersionNumber](activex-methods/project-management.md#getversionnumber) can be used; other functions return an error, typically `SMAPI_ERR_SYSMONNOTRUNNING` (-303) or `SMAPI_ERR_NOPROJECT` (-1). System Monitor closes again when the last client releases its instance. To check whether System Monitor is already running, see [Exit Event](system-registered-handles/exit-event.md).

The instance created by CreateObject must be released once the client has finished. The syntax to release the server is language specific, but is typically achieved by setting the returned instance to **Nothing**.

!!! note
    More than one Automation client can hold an instance at the same time. Each instance keeps its own car selection (see [SelectCar](activex-methods/data-acquisition.md#selectcar)).

Most functions require a project to be loaded in System Monitor, and return `SMAPI_ERR_NOPROJECT` (-1) if none is open. While System Monitor is busy (for example, while a project is loading) functions may return `SMAPI_ERR_SM_BUSY` (-13). See [ActiveX Error Codes](activex-errors/activex-error-codes.md).

**See also:** [ActiveX Automation](index.md); [ActiveX Methods](activex-methods/index.md)
