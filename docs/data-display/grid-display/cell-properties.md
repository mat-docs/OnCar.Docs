# Cell Properties

When a [Grid Window](grid.md) is initially opened, all the cells are empty. Use the **Cell Properties** dialog box to populate the cells.

To edit a cell:

1. Make sure the Window is in [Edit Mode](grid-window-edit-mode.md). Edit Mode is on, by default, for a new Grid Window.
2. Click the cell you want to edit.

Text can be entered into the cell directly. To access the Grid Cell Context menu, the cell must be highlighted:

1. Press ESC to highlight the cell.
2. Right-click and select **Properties** from the Context menu.

The **Cell Properties** dialog box opens. There are two tabs:

- [Contents](cell-properties-contents.md) - Enter or edit the contents of a cell.
- [Formatting](cell-properties-formatting.md) - Change the borders, justification or background colour of a single cell. (Cells can also be formatted with the Grid Cell Context menu, which operates on single or multiple cells.)

## Grid Cell Context Menu

| Item | Description |
|---|---|
| **Cut**, **Copy**, **Paste** | Cut, copy or paste the selected cells. |
| **Data Format** | Selects the attribute displayed in a Parameter cell: Name, Units, Raw Value, Engineering, Binary, Decimal, Description, Trend, Error, Status, Slider or Button. See [Cell Properties - Contents](cell-properties-contents.md). |
| **Justification** | Left Justified, Right Justified or Centre Justified. |
| **Border** | Top Border, Bottom Border, Left Border or Right Border. |
| **Action Button** | Turns the cell into a button that sends a **Single Message** or runs a script (**Run Script**). |
| **Insert** | See [Insert Columns/Rows](insert-columns-rows.md). |
| **Delete** | See [Delete Columns/Rows](delete-columns-rows.md). |
| **Auto Generate** | Available when the cell contains a Measurement Parameter with a text conversion. Fills the cells below with one **Status** cell for each entry in the text conversion, adding rows if required. |
| **Properties** | Opens the Cell Properties dialog box. |

**See also:** [Selecting Cells](selecting-cells.md); [Grid Window Edit Mode](grid-window-edit-mode.md)
