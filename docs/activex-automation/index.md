# ActiveX Automation

System Monitor includes an ActiveX/OLE Automation interface, which exposes programmable System Monitor objects to other applications. This allows external applications to control, or request information from, a running copy of System Monitor.

External applications may be written in any language that supports ActiveX Automation interfaces (see [ActiveX Client Languages](activex-client-languages/index.md)).

ActiveX applications, or scripts, can also be run from a menu command in System Monitor by using [Custom Menus](../developer-functions/productivity-tools/custom-menus.md).

We take all possible steps to ensure that Automation client code remains compatible with future versions of System Monitor. However, the Automation interface may change in future releases, both in the functions provided and in the arguments supplied to them.

!!! note
    ActiveX client programs compiled with Visual Studio 2003 or earlier need to be recompiled with Visual Studio 2008 or later before they can be used with System Monitor 8.0 and later. This is a Microsoft compatibility requirement.

**See also:** [Accessing ActiveX Functions](accessing-activex-functions.md); [ActiveX Methods](activex-methods/index.md); [ActiveX Errors](activex-errors/index.md); [ActiveX Examples](activex-examples/index.md); [Exit Event](system-registered-handles/exit-event.md); [Custom Menus](../developer-functions/productivity-tools/custom-menus.md)
