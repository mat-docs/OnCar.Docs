# Visual Basic

Visual Basic does not support pointer types. An ActiveX function that receives a pointer argument may be supplied with a non-pointer variable of the correct type.

The System Monitor type library can be accessed from Visual Basic. This allows the ActiveX automation methods available in System Monitor to be viewed and selected.

**To configure Visual Basic to recognise the System Monitor type library:**

1. In Visual Basic, select **Project** > **References**.
2. In the **References** dialog box, check **System Monitor Type Library** and click **OK**.

Visual Basic then lists the available ActiveX function calls as you enter code (the **Auto List Members** feature).

To check whether System Monitor is running before creating the Automation object, see [Detect SM VisBasic](../system-registered-handles/detect-sm-visbasic.md).

**See also:** [ActiveX Client Languages](index.md); [Accessing ActiveX Functions](../accessing-activex-functions.md)
