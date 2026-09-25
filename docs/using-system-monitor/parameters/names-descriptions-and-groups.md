# Names, Descriptions and Groups

To help you find the Parameter you want, each one has the following labels:

| Label | Description |
|---|---|
| **Identifier** | A unique label for the parameter. The Identifier follows the rules for identifiers in the 'C' language, so it cannot start with a number and must not include spaces. It is shown on the [General tab](parameter-properties/general-tab.md) of the Parameter Properties dialog box. Equivalent to *IDENTIFIER* in [ASAP2](../../project-management/asap-compatibility.md). |
| **Name** | The label used by System Monitor to identify a Parameter. The Name follows the rules for identifiers in the 'C' language, so it cannot start with a number and must not include spaces. Equivalent to *DISPLAY_IDENTIFIER* in [ASAP2](../../project-management/asap-compatibility.md). |
| **Description** | A free-form text label attached to the parameter. The Description is not constrained by text rules, so it can be easier to read. It does not have to be unique. |
| **Type** | A string describing the parameter type, for example *Scalar*. Type is used to sort the parameter into a parameter type folder. These folders are shown in Parameter Explorer, and in the Select Parameter(s) dialog boxes, when the Groups option is turned off. |

Use the **Names** (CTRL+ALT+N) and **Descriptions** (CTRL+ALT+D) options on the **View** menu or the Parameter Explorer context menu to choose which labels are shown.

## Groups

The ASAP file defines the labels and also which Group each Parameter belongs to.

Groups are arbitrary and usually bring together parameters of similar function or from the same location on the vehicle. For example, one group may include temperature measurements while another includes clutch parameters. Groups may be nested. The Groups defined by the ASAP file cannot be edited in System Monitor.

Groups are used to sort parameters into group folders. When the **Groups** option (**View** > **Groups**, CTRL+ALT+G) is turned on, these folders are shown in:

- Parameter Explorer
- the Select Parameter(s) dialog boxes
- the Report View and Candidate Data Version windows in Data Wizard

Select **Group Descriptions Only** (on the **View** menu or the Parameter Explorer context menu) to label group folders with their descriptions only.

As well as the groups defined by the ASAP file, each project has the following groups:

- **External Inputs** – contains the Measurement Parameters created by the External Inputs Configuration tool.
- **Virtual Parameters** – contains the Virtual Parameters.
- **User** – this group has the same name as the Project. It is available for organising parameters as required.

## Creating Groups

With the Groups option turned on, select **Edit** > **New Group** (CTRL+SHIFT+G), or use **New Group** on the Parameter Explorer context menu, to create a new Group under the Virtual Parameters or User folder. You can rename or delete these groups with **Edit** > **Rename** and **Edit** > **Delete**, or the equivalent context menu commands. **Properties** on the group's context menu opens the Parameter Group Properties dialog box, which shows the group's **Description** and **Created By** fields.

The definitions of these New Groups are stored in the Desktop File.

## Copy and Paste

Copy and Paste commands, and their shortcuts, are available. Virtual Parameters can only be copied to a group within the Virtual Parameters group.

You can copy any parameter into a New Group below the User group (you cannot place parameters directly into the User group). The parameter is not removed from its original location.

**See also:** [Data Wizard](../../project-management/data-wizard/index.md); [Desktop File](../desktop/desktop-files.md); [External Inputs Configuration](../../data-acquisition/sensors/external-inputs/external-inputs-configuration.md); [Parameters](index.md); [Parameter Explorer](parameter-explorer.md); [Virtual Parameters](virtual-parameters/index.md)
