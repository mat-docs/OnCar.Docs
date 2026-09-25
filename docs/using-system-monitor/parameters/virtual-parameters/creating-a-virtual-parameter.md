# Creating a Virtual Parameter

!!! note
    **New Virtual Parameter** is not available until a Virtual Parameter File has been created. You must create a Virtual Parameter File before you can create Virtual Parameters. See [Creating New Files](../../../project-management/files/creating-new-files.md).

To create a Virtual Parameter:

1. If Parameter Explorer is displayed, select the **Virtual Parameters** folder (or a sub-folder below it).
2. Select **Edit** > **New Virtual Parameter** (CTRL+SHIFT+V), or select **New Virtual Parameter** from the Parameter Explorer context menu.
3. The Parameter Properties dialog box opens at the [Virtual](../parameter-properties/virtual-tab.md) tab. Enter the formula that defines the Virtual Parameter.
4. Review the other properties of the Virtual Parameter, such as its name and the way it is displayed. The default values should give acceptable results, but make sure they meet your requirements.
5. Click **OK**. The formula is checked; if it is accepted, the Virtual Parameter is created.

The new Virtual Parameter is given the [Identifier](../names-descriptions-and-groups.md) VPARAM_*n* (where *n* is the next unused number, starting at 0) and is placed in the Virtual Parameters folder. It can be moved to a sub-folder below the Virtual Parameters folder, but nowhere else.

The default Name of the new Virtual Parameter is the same as its Identifier. You can edit both the Name and the Identifier on the [General](../parameter-properties/general-tab.md) tab. A new Virtual Parameter uses a rational conversion in which the engineering value equals the raw value.

These Parameter Properties tabs are available for a Virtual Parameter:

- [General](../parameter-properties/general-tab.md)
- [Measurement](../parameter-properties/measurement-tab.md)
- [Virtual](../parameter-properties/virtual-tab.md)
- [Conversion](../parameter-properties/conversion-tab.md)
- [Display](../parameter-properties/display-tab.md)

**See also:** [Creating New Files](../../../project-management/files/creating-new-files.md); [Parameter Properties](../parameter-properties/index.md); [Parameter Properties – Virtual tab](../parameter-properties/virtual-tab.md)
