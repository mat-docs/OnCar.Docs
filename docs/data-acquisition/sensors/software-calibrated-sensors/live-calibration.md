# Live Calibration

Live Calibration allows you to calibrate a sensor using a real input.

Set up Live Calibration:

1. Set up a connection to the sensor using [External Inputs Configuration](../external-inputs/external-inputs-configuration.md). Ensure that the configuration is downloaded to the ECU.
2. Prepare to apply known engineering loads to the sensor.
3. Put the ECU On-Line.
4. Select **Sensors** > **Live Calibration...** (CTRL+SHIFT+F8) to open the [Select Live Calibration Parameter](../../../using-system-monitor/parameters/selecting-parameters/selecting-a-single-parameter.md) dialog box.
5. Select the parameter associated with the sensor that you want to calibrate.
6. Click **OK** to open the [Sensor Calibration](sensor-calibration-tool.md) dialog box.
7. Click **Live Cal** to start the calibration. The current voltage output from the sensor is shown in the **Voltage** box and under Breakpoint in the centre pane.
8. In the **Engineering** box, enter the value, in engineering units, corresponding to the load currently applied to the sensor. Click **Next >>**.
9. Change the load on the sensor so that the Voltage value increases, and repeat step 8.
10. Continue until you have entered all the calibration points. Click **Finish** to stop the calibration, and click **Yes** to accept the new calibration values.
11. Click **OK** to save the calibration. The .dat file associated with the sensor (see [Calibration Files](calibration-files.md)) is updated.

**See also:** [Calibration Files](calibration-files.md); [Sensor Calibration Tool](sensor-calibration-tool.md); [Software Calibrated Sensors](index.md)
