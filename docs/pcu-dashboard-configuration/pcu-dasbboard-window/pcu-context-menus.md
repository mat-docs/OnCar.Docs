# PCU Context Menus

Right-click in the PCU Dash Configuration window to open a context menu. The commands available depend on where you click and whether a Control is selected.

## No Control selected

| Command | Description |
|---|---|
| **Add Static Label** | Adds a [Static Label](display-control-types/static-labels.md) (text `<Label>`) at the point you clicked and selects it. Static Labels are text-only Controls and are not associated with a Parameter. Right-click the label and select **Properties** to set its text. |
| **Add Conditional Text** | Adds a [Conditional Text](display-control-types/static-labels.md#conditional-text) Control at the point you clicked. |
| **Copy**, **Paste**, **Undo Last Move/Resize** | See [Main Menu](dash-configuration-main-menu.md). |
| **Dash Properties...** | Opens the [PCU Dash Properties](pcu-dash-properties/index.md) dialog box. |

## Control selected

| Command | Description |
|---|---|
| **Numeric**, **Bar Graph**, **Rev Bar**, **Dial**, **LED** | Changes the selected Control to this type. The current type is ticked. A Parameter dragged onto the display area is shown as a Numeric Control by default. Not shown when a Static Label or Conditional Text Control is selected. |
| **Add Static Label**, **Add Conditional Text** | See above. |
| **Copy** (Ctrl+C), **Paste** (Ctrl+V) | Copies the selected Control, or pastes a copied Control. |
| **Delete Control** (Delete) | Deletes the selected Control. |
| **Undo Last Move/Resize** (Ctrl+Z) | Undoes the last move or resize. |
| **Snap To Grid** | Aligns the selected Control to the guide grid: **Top side**, **Bottom side**, **Left side** or **Right side**. For example, **Top side** aligns the top of the Control's bounding box with the nearest horizontal grid line. Only available when **Display Guide Grid** is selected on the [Layout](pcu-dash-properties/layout-tab.md) tab. |
| **Properties...** | Opens the Properties dialog box for the selected Control. See the Display Control Types pages, for example [Numeric Control](display-control-types/numeric-control.md). |

## Page Bar context menu

Right-click the Page Bar at the bottom of the PCU Dash Configuration window to open the Page Bar context menu.

| Command | Description |
|---|---|
| **Add Page** | Opens the Page Name dialog box. Enter a name and click **OK** to add a page at the end of the configuration. Click **Cancel** to not add the page. |
| **Delete Page** | Deletes the page currently in view, after asking you to confirm. The last remaining page cannot be deleted. |
| **Rename Page** | Opens the Page Name dialog box to rename the page currently in view. |
| **Move Page Up** (Ctrl+Page Up), **Move Page Down** (Ctrl+Page Down) | Moves the page currently in view one place up or down the page order. |

!!! note
    If a Dash Configuration contains more than one page, the display unit push buttons can be assigned Actions which let the driver move between pages. See [Assign Actions to push buttons](../assign-actions-to-push-buttons.md).
