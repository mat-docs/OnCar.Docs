# Assign Actions to push buttons

The push buttons on the side of the PCU-400 Display Unit can be assigned Actions which control the display. For example, one push button can select the next page in a multi-page Dash Configuration and the other can select the previous page.

**To assign Page Up and Page Down Actions to the push buttons:**

1. Select **Dash Properties** from the PCU Dash Configuration [Main Menu](pcu-dasbboard-window/dash-configuration-main-menu.md). The PCU Dash Properties dialog box opens.
2. Select the **Actions** tab.
3. Click **Add...** to open the PCU Action dialog box.
4. Click **Select...** to open the Select Parameter dialog box.
5. Select the Parameter **ExtSwitch1** and click **OK**. ExtSwitch1 appears in the **Parameter** field. ExtSwitch1 corresponds to the upper push button on the display unit.
6. Set both **Lo Threshold** and **Hi Threshold** to 0.
7. Clear the **Action occurs inside threshold values** check box.
8. Set **Secondary condition** to **None**.
9. From the **Action** drop-down list select **Pg Up**.
10. Click **OK** to close the PCU Action dialog box and add the new Action to the Actions list.

To assign a Page Down Action to the other push button, repeat the procedure selecting the **ExtSwitch2** Parameter and the **Pg Down** Action.

**See also:** [Dash Properties - Actions](pcu-dasbboard-window/pcu-dash-properties/actions-tab.md), [Actions](pcu-dasbboard-window/pcu-dash-properties/actions.md)
