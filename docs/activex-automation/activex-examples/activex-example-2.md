# ActiveX Example 2

**Getting and setting the value of a scalar editable parameter**

```vb
'Declare globally available SM API.
Dim SmApi As Object

Sub Main
    'Get access to System Monitor API
    Set SmApi = CreateObject("System Monitor API")

    'Param to retrieve
    Dim szIdent As String
    szIdent = "BiosAC_Hiside1ScaledUpper"

    'Current value
    Dim dValue As Double

    'Error return code
    Dim lErr As Long

    'Get current value of param (Application Id 0 = any application)
    lErr = SmApi.GetValueScalar(0, szIdent, dValue)
    Debug.Print szIdent;
    Debug.Print " = ";
    Debug.Print dValue

    'Add on 10% and set value
    dValue = dValue + (dValue / 10)
    Debug.Print "Adding 10% to ";
    Debug.Print szIdent
    lErr = SmApi.SetValueScalar(0, szIdent, dValue)

    'Get current value
    lErr = SmApi.GetValueScalar(0, szIdent, dValue)
    Debug.Print szIdent;
    Debug.Print " = ";
    Debug.Print dValue

    'Pause to let user see result
    Wait 10

    'You must free the SM API before running another script
    Set SmApi = Nothing
End Sub
```

**Sample output:**

```text
BiosAC_Hiside1ScaledUpper = 2.64
Adding 10% to BiosAC_Hiside1ScaledUpper
BiosAC_Hiside1ScaledUpper = 2.904
```

**See also:** [ActiveX Examples](index.md); [GetValueScalar](../activex-methods/parameters.md#getvaluescalar); [SetValueScalar](../activex-methods/parameters.md#setvaluescalar)
