# Parameter Filter

The **Filter** box, in Parameter Explorer and in the Select Parameter(s) dialog boxes, helps you find the Parameters you want.

Type the text that you want to match in the Filter box and press ENTER. The list is filtered so that only the Parameters that match the text are shown.

To remove the filter, delete the text in the Filter box and press ENTER.

!!! note
    The list is filtered much faster if you close the folders before using the filter. Open the folders to view the filtered list.

## Features

- The filter supports the `?` wildcard, which matches any single character, and the `*` wildcard, which matches any number of characters.
- The filter matches text anywhere in the parameter label as it is shown (the Name, the Description, or both, depending on the Names and Descriptions options). A `*` is always assumed at the beginning and end of the filter, so do not type a `*` in front of the text; it can slow down the search.
- To match a parameter Name exactly, enclose the filter text in double quotes, for example `"NEngine"`.
- Filtering is not case sensitive. For example, entering `Aanw@` shows all parameters that contain any case combination, such as Aanw@, AAnw@ or AANW@.
- The five most recent filter strings are available in the Filter drop-down list. Previously used filter strings are also suggested as you type.
- The [Edit Context Menu](../../menus/context-menus/edit-context-menu.md) gives access to editing commands in the Filter box.

**See also:** [Parameter Explorer](../parameter-explorer.md); [Selecting a Single Parameter](selecting-a-single-parameter.md); [Selecting Multiple Parameters](selecting-multiple-parameters.md)
