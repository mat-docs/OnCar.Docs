# Desktop Files

Desktops are stored as `.dtp` files in the `Desktops` sub-folder. An empty Desktop is created when a Project is created. The contents of an existing Desktop file can be copied into the new Desktop file.

## Features

- When a Project is loaded into System Monitor, the Desktop that was open when the Project was last saved is opened.
- You cannot close a Desktop without closing the Project, but you can open a new empty Desktop (see [Creating New Files](../../project-management/files/creating-new-files.md)) or an existing Desktop from a file (see [Opening Files](../../project-management/files/opening-files.md)). The Desktop currently open is closed and replaced.
- Pages from other Desktops can be added to the current Desktop by [Merging](merging-desktops.md).
- The contents of the current Desktop can be cleared by selecting **Close All** on the [Desktop Menu](../menus/desktop-menu.md).

The Desktop file also contains:

- The definitions of New Groups (see [Names, Descriptions & Groups](../parameters/names-descriptions-and-groups.md)).
- Changes to the Warning Limits for a Parameter, as set in the Parameter Properties dialog box.

## Associating a Desktop with a Program Version

A Desktop can be associated with a [Program Version](../../project-management/program-and-data-versions/index.md). To do this, save the Desktop in the same folder as the `.pgv` file, named after the program version number (four hex digits). For example, `1065.dtp` is the Desktop for program version 1065.

To open the Desktops associated with the Program Versions:

1. Select **Desktop** > **Show Application Pages** (a tick shows that the option is selected).

The Desktop associated with the Program Version of each Application is opened and its Pages are placed at the head of the list of Pages in the Page Bar. The state of this option is saved in the Project.

**See also:** [Desktop](index.md); [Desktop Menu](../menus/desktop-menu.md)
