# Detecting System Monitor instance with Visual Basic

The following function returns `True` if an instance of System Monitor is running, by trying to open the `TES SysMon V7` mutex (see [Exit Event](exit-event.md)).

```vb
Private Declare Function OpenMutex Lib "kernel32" Alias "OpenMutexA" _
    (ByVal dwDesiredAccess As Long, ByVal bInheritHandle As Long, ByVal lpName As String) As Long
Private Declare Function CloseHandle Lib "kernel32" (ByVal hObject As Long) As Long
Private Const MUTEX_MODIFY_STATE As Long = &H1

Public Function IsSysMonRunning() As Boolean
    Dim bRet As Boolean

    '   Attempt to open the already running application through its mutual
    '   exclusion handle
    Dim hMutex As Long
    hMutex = OpenMutex(MUTEX_MODIFY_STATE, 0, "TES SysMon V7")

    If Not hMutex = 0 Then
        '   Success
        bRet = True
        CloseHandle hMutex
    End If

    '   Exit
    IsSysMonRunning = bRet
End Function
```

**See also:** [Exit Event](exit-event.md); [Visual Basic](../activex-client-languages/visual-basic.md)
