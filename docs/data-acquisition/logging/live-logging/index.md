# Live Logging

Live Logging is the process by which System Monitor obtains data from a connected ECU. The Live Logging Configuration serves two purposes in System Monitor:

- It obtains data for display in the current Desktop, so it must include all the parameters that have been selected for display. If there is no Live Logging Configuration file in the Project, all the parameters are available for display.
- It selects the parameters to be included in a [Session](../sessions-and-telemetry.md) recorded by System Monitor.

!!! note
    The live logging functionality in System Monitor captures slow row data. To view it in ATLAS, ATLAS must be configured to display slow row parameters.

## Configure Live Logging

The Live Logging Configuration is edited in the Configure Live Logging dialog box. To open the dialog box select **Logging** > **Live Configuration** (CTRL+L).

!!! note
    If this menu item is not available, you must create a new Live Logging Configuration file or open an existing one. See [Creating New Files](../../../project-management/files/creating-new-files.md). The menu item is also unavailable while the ECU is On-Line.

The Configure Live Logging dialog box has three tabs:

- [Session](session-tab.md) - Set where the Session file is created and how it is named, and edit the Session details.
- [Trigger Timing](trigger-timing-tab.md) - Set the length of the Session and how the trigger is used.
- [Trigger Condition](trigger-condition-tab.md) - Define the condition that acts as a trigger for the recording of the Session.

The dialog box title bar displays the name of the Logging Configuration file being edited.

## Features

- Recording is controlled by commands on the Logging menu (see [Live Logging - Recording](recording.md)).
- Live Logging Configuration is not available while the ECU is On-Line.
- The Live Logging Configuration becomes active as soon as the Configure Live Logging dialog box is closed.
- Live Logging Configurations can be saved and opened (see [Logging Configuration Files](../logging-configuration-files.md)).

**See also:** [Logging](../index.md)
