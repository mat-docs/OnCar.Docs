# Sensor Sets

Sensor Sets are files (.set) containing the sensor and actuator data. They are stored in the \SenSets\ sub-directory of the [Multi-Application Base](../../../project-management/customer-bases/multi-application-base.md).

When a Sensor Set is opened (using **File** > **Open** or **Sensors** > **Open Sensor Set**), the [Sensors & Actuators dialog box](sensors-and-actuators-dialog-box.md) for the Sensor Set is opened and the Sensor Set is associated with the Project.

## Creating new Sensor Sets

To create a new Sensor Set select **File** > **New**. The **Sensors** > **Sensor Set Upload** command automatically creates a new Sensor Set file if there is not already one associated with the Project.

!!! note
    The new file only contains sensor data for the [Active Applications](../../../project-management/active-application.md). Make the appropriate applications active before you create a new Sensor Set file.

The default name for a new Sensor Set is XXXXXnnn.set, where:

- **XXXXX** - The first five characters of the Application Name, or 'Calib' if more than one application is active.
- **nnn** - A three-digit hexadecimal number, starting at 001, which is incremented whenever a new Sensor Set file is saved.

## Uploading into a new sub set

**Sensors** > **Sensor Set Upload New** uploads the sensor set in the unit into a new sub set instead of overwriting the active sub set (see [Sensors & Actuators dialog box](sensors-and-actuators-dialog-box.md)). The Advanced Settings **Enable New Sensor Subset Upload (Y/N)** and **Prompt New Sensor Subset Upload (Y/N)** control whether a normal upload also uses a new sub set, and whether you are asked (see [Settings](../../../using-system-monitor/settings.md)).

## Saving Sensor Sets

If the sensor data changes, including by uploading from the ECU, you are prompted to save the Sensor Set when you close the Sensors & Actuators dialog box. To save a Sensor Set under a different name select **File** > **Save As**.

!!! note
    To see which Sensor Set files are in use and to upload or download files, use **Tools** > **Unit Status** (see [Unit Status](../../../ecu-control/unit-status.md)).
