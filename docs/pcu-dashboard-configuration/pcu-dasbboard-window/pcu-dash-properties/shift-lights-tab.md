# Dash Properties - Shift Lights

Use the Shift Lights tab to configure the 15 shift lights on the top edge of the PCU-400 display unit. The lights are in three groups of five: Green (lights 1 to 5), Red (lights 6 to 10) and Blue (lights 11 to 15).

## Override Parameter

**Override Parameter** - Select this check box to control the shift lights with an override Parameter. Click **Select...** to choose the Parameter and **Properties...** to view its properties. While **Override Parameter** is selected, the **ShiftLight Parameters** options and the Shift Light Activation table are disabled.

## ShiftLight Parameters

**ShiftLight Parameters** - Select this check box to use the gear and RPM Parameters and the Shift Light Activation table. When cleared, the Parameters and the table are disabled.

- **Gear** - Click **Select...** to choose the gear position Parameter. **Properties...** shows its properties.
- **RPM** - Click **Select...** to choose the engine speed Parameter. **Properties...** shows its properties.

Only Measurement Parameters can be selected.

## Shift Light Activation

The table has a column for each gear: **N** (neutral) and **1st** to **7th**.

- **Target RPM** - For each gear, enter the RPM at which a gear change is required.
- **Offsets** - For each gear, enter an RPM offset for each shift light. The rows are labelled **Blue 5** to **1**, **Red 5** to **1** and **Green 5** to **1**. All offsets default to 0.

The offsets set the RPM at which each light comes on, and so the sweep of the lights as the Target RPM is approached. For example, if the Target RPM for a gear is 9000 RPM and the offset for Green 1 is 700, Green 1 lights at 9000 minus 700 RPM (8300 RPM).

**To configure the shift lights:**

1. Select **ShiftLight Parameters**.
2. Click **Select...** next to **Gear** and select the gear position Parameter.
3. Click **Select...** next to **RPM** and select the RPM Parameter.
4. In the **Target RPM** row, enter the gear-change RPM for each gear.
5. In the **Offsets** rows, enter an RPM offset for each light in each gear.
6. Click **OK**.
