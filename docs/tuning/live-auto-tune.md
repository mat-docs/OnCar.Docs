# Live Auto Tune

Live Auto Tune assists with manual testbed tuning. It is used in conjunction with Live Tune and the Adjustment Board.

The Live Auto Tune definition file (the **Live AutoTune File** selected when the Program Version is created) defines a set of Live Auto Tune parameters. A Live Auto Tune parameter defines a group of maps and an adjustment parameter. The maps in a Live Auto Tune parameter share the same axes, for example throttle position against engine speed.

Typically, Live Auto Tune parameters are provided for ignition, injection quantity, injection end angle and nominal lambda. Turbocharged engines may have additional parameters for boost pressure and waste gate control.

The Live Auto Tune tab of the Parameter Properties dialog box gives information about the selected Live Auto Tune parameter.

The Live Auto Tune parameters all have the same number of maps in a set order (for example 1, 2, 3). The group of maps at the same level in all the Live Auto Tune parameters is called a Tune Group. Typically, the Tune Groups are set up for different operating conditions such as "Optimum Power", "Minimum Consumption" or "Wet Racing".

The active Tune Group can be selected by the result of a calculation in the ECU, by the value of a measurement parameter or by the driver using a cockpit-mounted switch. The index that selects the Tune Group is called the Z axis.

As a test is run, the various indexes and controls select a value on one of the maps in each Live Auto Tune parameter. The adjustment parameter is then applied to this value. If the adjustment parameter is associated with a control on the Adjustment Board, turning the control applies the adjustment. The way in which the adjustment is applied is defined by the Correction type in the Parameter Properties.

To ensure that a value is selected properly, the Live Auto Tune parameter defines breakpoint tolerances which override the breakpoint tolerances set for each map (see Parameter Properties - 1-Axis Map tab).

## Using Live Auto Tune

1. Select **ECU** > **Live Auto Tune** (Alt+F3). The command is only available when an Active Application has Live Auto Tune parameters, a Live Logging Configuration is open and there is communication with the unit.
2. System Monitor goes On-Line and switches on Live Updates if they are not already on. While Live Auto Tune is on, Live Updates cannot be switched off and the ECU cannot be taken Off-line. When Live Auto Tune is switched off, the previous On-Line and Live Updates states are restored.
3. When you are satisfied with an adjustment, select **ECU** > **Save Auto Tune Adjustment** (F10). The adjustment is applied to the value at the active breakpoints of the active map and the adjustment value is reset. Because Live Updates is on, the new map value is sent to the unit.

!!! note
    **Tools** > **Pot Board** > **Enable** is not available while Live Auto Tune is on. Enable the Adjustment Board before starting Live Auto Tune.

If the unit enters boot or the link is lost, Live Auto Tune is disabled until the unit leaves boot or the link returns.

**See also:** [Adjustment Board](../hardware/adjustment-board.md); [ECU Control](../ecu-control/index.md); [Live Tune](live-tune.md); [Parameter Properties - Live Auto Tune tab](../using-system-monitor/parameters/parameter-properties/live-auto-tune-tab.md)
