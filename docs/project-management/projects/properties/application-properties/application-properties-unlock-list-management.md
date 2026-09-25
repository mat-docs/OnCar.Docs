# Application Properties - Unlock List Management

The Unlock List Management tab allows you to manage the Parameter Unlock List (.pul file) associated with the Application's Data Version. Unlock lists are managed on a per-application basis. If you do not have sufficient permission, the controls are unavailable and the message "You do not have sufficient permission to change the Lock List Management." is shown. With consortium licences, once a Data Version is locked only its original owner can change these settings.

| Control | Description |
|---|---|
| **Lock DTV** | Locks the Data Version. The **Owner** of the lock is shown next to it. |
| Unlock list file and **...** | Browse for the Unlock List (.pul) file to associate with the Application. If the Data Version is locked with no unlock list, the message "No unlock list defined. All parameters locked." is shown. |
| **New** | Creates a new Unlock List file to associate with the Application. |
| **Edit** | Edits the unlock list: the parameters that are unlocked, and the members they are unlocked for. See [Edit the Parameter Unlock List](../../../../using-system-monitor/parameters/locked-parameters/edit-the-parameter-unlock-list.md). |
| **Edit Comment** | Opens the Unlock List Details dialog box, which shows the Filename, Saved By and Saved On details and lets you edit the Comments. |
| **Details** | Lists the **Member** and **Details** of each entry in the unlock list. |

!!! warning
    Before locking an application, make sure that a backup of the unlocked application is created, as you cannot unlock an application once it is locked. Because this backup is unlocked, store it in a secure location.

**See also:** [Application Properties](index.md); [Edit the Parameter Unlock List](../../../../using-system-monitor/parameters/locked-parameters/edit-the-parameter-unlock-list.md)
