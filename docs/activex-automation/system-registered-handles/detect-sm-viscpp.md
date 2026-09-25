# Detecting System Monitor instance with Visual C++

The following function returns `true` if an instance of System Monitor is running, by trying to open the `TES SysMon V7` mutex (see [Exit Event](exit-event.md)).

```cpp
#include <windows.h>

bool IsSysMonRunning(void)
{
    HANDLE hMu = ::OpenMutex(MUTEX_MODIFY_STATE, FALSE, TEXT("TES SysMon V7"));

    if (hMu)
    {
        ::CloseHandle(hMu);
        return true;
    }
    else
    {
        return false;
    }
}
```

**See also:** [Exit Event](exit-event.md); [Visual C++](../activex-client-languages/visual-cpp.md)
