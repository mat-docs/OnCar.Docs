# SM Script

System Monitor includes its own scripting language and script development environment, based on Sax Basic. The SM Script integrated development environment (IDE) is distributed with System Monitor and is installed in the same folder as System Monitor as the **Sax Basic** installation feature. This feature is selected by default and can be deselected in a [Custom Installation](../../getting-started/custom-installation.md). This version of SM Script is licensed only for use with System Monitor and must not be redistributed.

To open the SM Script editor, from the Windows Start menu select **McLaren Electronic Systems** > **System Monitor 8** > **Sax Basic IDE**.

SM Script is similar to Microsoft Visual Basic for Applications, and therefore does not support pointer types. An ActiveX function that receives a pointer argument may be supplied with a non-pointer variable of the correct type.

!!! note
    There are some differences between SM Script and Microsoft Visual Basic for Applications. Refer to the SM Script help for details.

The [ActiveX Examples](../activex-examples/index.md) are written in SM Script. SM Script files can also be run from System Monitor using [Custom Menus](../../developer-functions/productivity-tools/custom-menus.md).

The System Monitor type library can be accessed from SM Script. This allows the ActiveX automation methods available in System Monitor to be viewed and selected.

**To configure SM Script to recognise the System Monitor type library:**

1. In SM Script, select **Edit** > **References**. The References dialog box opens.
2. Select **System Monitor Type Library** and click **OK**.

**To view or select System Monitor methods and data types:**

1. In SM Script, select **Debug** > **Browse**.
2. In the ActiveX Automation Members dialog box, select **SystemMonitor** from the Library drop-down list.

**See also:** [ActiveX Client Languages](index.md); [ActiveX Examples](../activex-examples/index.md); [Custom Installation](../../getting-started/custom-installation.md)
