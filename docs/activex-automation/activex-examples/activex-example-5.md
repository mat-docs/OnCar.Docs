# ActiveX Example 5

**Demonstrating functions GetValue2AxisMap and SetValue2AxisMap**

```vb
Dim SmApi As Object

Sub Main
    'Get access to System Monitor API
    Set SmApi = CreateObject("System Monitor API")

    'Param to retrieve (a 2-axis map)
    Dim szIdent As String
    'Error return code
    Dim lErr As Long
    'Variables which are to receive map values must be declared as Variants.
    'This is because System Monitor needs to allocate and dimension the array.
    Dim adValue As Variant

    'Get current values of 2-axis map
    szIdent = "EI_24704"
    lErr = SmApi.GetValue2AxisMap(0, szIdent, adValue)
    PrintIdent(szIdent, lErr)
    Print2dArray(adValue)

    'Declare the array to be passed to System Monitor to set the map values.
    'It must be declared as an array so that System Monitor can read its dimensions and values.
    Dim adValueSet() As Double

    'Copy returned values to the values we're going to set, and add 10% to all
    'breakpoints excluding the first, second and last in each dimension
    adValueSet = adValue
    For i = 2 To (UBound(adValueSet, 2) - 1)
        For n = 2 To (UBound(adValueSet, 1) - 1)
            adValueSet(n, i) = adValue(n, i) + adValue(n, i) / 10
        Next n
    Next i

    'Set map values
    lErr = SmApi.SetValue2AxisMap(0, szIdent, adValueSet)

    'Get current values of 2-axis map and print
    lErr = SmApi.GetValue2AxisMap(0, szIdent, adValue)
    PrintIdent(szIdent, lErr)
    Print2dArray(adValue)

    'Pause to let user see result
    Wait 100

    'You must free the SM API before running another script
    Set SmApi = Nothing
End Sub

Function Print2dArray(adValue)
    'Print out current values. You can use UBound to find number of axis points
    For i = 0 To UBound(adValue, 2)
        For n = 0 To UBound(adValue, 1)
            Debug.Print adValue(n, i);
            Debug.Print " ";
        Next n
        Debug.Print
    Next i
    Debug.Print                 'New line
End Function

Function PrintIdent(szIdent, lErr)
    Debug.Print "ID = ";
    Debug.Print szIdent;        'Parameter identifier
    Debug.Print ", Error = ";
    Debug.Print lErr
End Function
```

**See also:** [ActiveX Examples](index.md); [GetValue2AxisMap](../activex-methods/parameters.md#getvalue2axismap); [SetValue2AxisMap](../activex-methods/parameters.md#setvalue2axismap)
