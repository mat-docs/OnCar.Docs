# Virtual Parameter Files

The Virtual Parameters created for a Project are stored in the file *ProjectName*`.vpx`, by default in the `\Virtuals` sub-directory.

Files with the extension `.vpm` are in the original serialised binary format. They have been superseded by the `.vpx` [XML file](virtual-parameters-xml-file-schema.md) format.

By default, Virtual Parameters are saved in the `.vpx` format, but they can be saved in the original `.vpm` format from the Save As dialog box. The default format is controlled by the **Default Virtual Parameter format to XML (Y/N)** setting in [Advanced Settings](../../settings.md) (default Y; System Monitor must be restarted for a change to take effect).

You cannot [create a Virtual Parameter](creating-a-virtual-parameter.md) until this file has been created (see [Creating New Files](../../../project-management/files/creating-new-files.md)).

The location of the file is shown in the Virtual Parameters tab of the [Project Properties](../../../project-management/projects/properties/project-properties.md) dialog box.

**See also:** [Virtual Parameters Import/Export](virtual-parameters-import-export.md); [Virtual Parameter XML File Schema](virtual-parameters-xml-file-schema.md)
