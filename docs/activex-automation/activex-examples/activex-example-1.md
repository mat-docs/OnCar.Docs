# ActiveX Example 1

**Using SendMessage() to send a Read RAM message to the ECU**

```vb
'Declare globally available SM API.
Dim SmApi As Object

Sub Main
    'Get access to System Monitor API
    Set SmApi = CreateObject("System Monitor API")

    'Application Id of the ECU application to send to. SendMessage needs a real
    'application in the open project; 0 (any application) is rejected with error -9.
    Dim wAppId As Integer
    wAppId = 1

    'Send message must be a fixed-length Integer array (signed 16-bit words, lower bound 0).
    'Its size must match the length of the message.
    Dim aSend(2) As Integer
    'Contents of message to send
    aSend(0) = &H0010    'COM_SM_READ_MEMORY and destination
    aSend(1) = 0         'Start address low
    aSend(2) = 0         'Start address high

    'The reply is returned in a Variant. System Monitor creates an Integer array
    'sized to match the response.
    Dim vReply As Variant

    'Timeout
    Dim Timeout As Integer
    Timeout = 400

    'Send the message
    Dim lErr As Long
    lErr = SmApi.SendMessage(wAppId, aSend, vReply, Timeout)

    'Print error code
    Debug.Print "Error code = ";
    Debug.Print lErr

    'Print contents of response. Use UBound() to find the size of the response.
    If IsArray(vReply) Then
        Debug.Print "Response = ";
        For i = 0 To UBound(vReply)
            Debug.Print Hex(vReply(i));
            Debug.Print ", ";
        Next i
        'Newline
        Debug.Print
    End If

    'Pause to let user see response
    Wait 10

    'You must free the SM API before running another script
    Set SmApi = Nothing
End Sub
```

**See also:** [ActiveX Examples](index.md); [SendMessage](../activex-methods/ecu-control.md#sendmessage)
