# Locked Parameters

If a team has restricted access to an Application, the parameters associated with the Application are locked unless they appear on the Parameter Unlock List (PUL). A locked parameter is displayed in Parameter Explorer or in a Window with a lock symbol superimposed, for example ![Locked measurement parameter](assets/icon_locked_measparam.gif).

- Each parameter is locked by default. When the DTV is loaded, the licence is checked for access status to the Application.
- If a user has full access to an Application, all its parameters are unlocked.
- If a user has restricted access, all its parameters are locked unless they are on the PUL.

Use **Display Unlocked Parameters Only**, **Display Locked Parameters Only** or **Display All Parameters** on the **View** menu or the Parameter Explorer context menu to choose which parameters are listed.

!!! note
    If a parameter becomes locked, it is not removed from any Windows to which it has already been added. However, its value is replaced by '-' and a lock symbol is displayed.

Users with **full** access to an Application can add parameters to, and remove parameters from, the PUL. This is done in the Select Parameters dialog box opened from the Application Properties dialog box. See [Edit the Parameter Unlock List](edit-the-parameter-unlock-list.md).

Users with **restricted** access to an Application cannot:

- display or edit the properties of a locked parameter
- add locked parameters to the Desktop
- select locked parameters for use in a virtual parameter. Existing virtual parameters that contain locked parameters are themselves locked and cannot be edited or viewed.
- access locked parameters through ActiveX controls
- use locked parameters as Transmit CAN Parameters. Existing CAN Parameters that are subsequently locked are disabled and omitted from a CAN configuration download.
- include locked parameters in a MATLAB export
- process locked parameters in Merge and Data Wizard operations

**See also:** [About the Parameter Unlock List](about-the-parameter-unlock-list.md); [Reduced Data Access](../../../getting-started/team-security-and-reduced-data-access/reduced-data-access.md)
