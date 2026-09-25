# Exit Event

When System Monitor starts with its user interface, it creates a named Windows event called `SystemMonitor_ExitEvent_xxxxxxxx`, where `xxxxxxxx` is the window handle of the System Monitor main window, written as 8 lower-case hexadecimal digits. The event is a manual-reset event. It is not signalled while System Monitor is running normally, and is signalled when System Monitor exits.

This event can be used to detect when System Monitor exits.

!!! note
    The event is not created when System Monitor is running only in OLE mode (see [Accessing ActiveX Functions](../accessing-activex-functions.md)).

## Mutex Handle

When System Monitor starts with its user interface, it creates a named mutex (see `CreateMutex`) called `TES SysMon V7`. A client can try to open this mutex to find out whether an instance of System Monitor is running.

!!! note
    By default, several instances of System Monitor can run at the same time (Advanced Setting **Enable Multiple Instances (Y/N)**, default Y; see [Settings](../../using-system-monitor/settings.md)). All instances share the same mutex, so it shows only that at least one instance is running.

See the following examples:

- [Detect SM VisC++](detect-sm-viscpp.md)
- [Detect SM VisBasic](detect-sm-visbasic.md)

**See also:** [ActiveX Automation](../index.md)
