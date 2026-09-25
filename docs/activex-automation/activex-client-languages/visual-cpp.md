# Visual C++

System Monitor includes a type library, `SystemMonitor.tlb`, which is installed in the same folder as System Monitor. This type library can be imported into Visual C++ projects to generate a C++ wrapper class for the System Monitor ActiveX interface automatically.

For example (default installation folder shown):

```cpp
#import "C:\\Program Files (x86)\\McLaren Electronic Systems\\System Monitor 8\\SystemMonitor.tlb" rename("SendMessage", "SmSendMessage") named_guids
```

!!! note
    The `rename` statement prevents a conflict with the `SendMessage` API declared in `<windows.h>`.

This generates a class which can then be declared and used as follows:

```cpp
HRESULT hr = S_OK;

// ITSysMonApiDualPtr is a _com_ptr_t<ITSysMonApiDual>
SystemMonitor::ITSysMonApiDualPtr pSmApi;

// Create instance if System Monitor is running
if (SUCCEEDED(hr) && IsSysMonRunning())
{
    hr = pSmApi.CreateInstance(SystemMonitor::CLSID_TSysMonApi);
}
```

`IsSysMonRunning()` is shown in [Detect SM VisC++](../system-registered-handles/detect-sm-viscpp.md).

The generated `ITSysMonApiDual` wrapper returns each method's `long` error code as the function result (see [ActiveX Error Codes](../activex-errors/activex-error-codes.md)).

**See also:** [ActiveX Client Languages](index.md); [Accessing ActiveX Functions](../accessing-activex-functions.md)
