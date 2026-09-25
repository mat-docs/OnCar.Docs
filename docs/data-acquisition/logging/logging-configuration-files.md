# Logging Configuration Files

When a [Logging Configuration](index.md) is edited, the changes are stored in a Logging Configuration file.

When a [New Project is Created](../../project-management/projects/creating-a-project/stage-1-define-project.md), a \LogCfgs\ folder is created for the project (see [Project Files](../../project-management/files/types-of-files/project-files.md)). This one folder is the default location for all the logging configuration types - [Live](live-logging/index.md), [Remote](remote-logging/index.md) and [Burst](burst-logging/index.md) - and also for External Inputs and CAN configurations. The folder is initially empty.

A Logging Configuration file must be created, or an existing one opened, before a Logging Configuration can be edited.

To create a new Logging Configuration file select **File** > **New** to open the File New dialog box. See [Creating New Files](../../project-management/files/creating-new-files.md) and [Opening Files](../../project-management/files/opening-files.md).

A Logging Configuration file can be saved. See [Saving Files](../../project-management/files/saving-files.md). If you change a logging configuration, you are prompted to save the modified configuration when you close the project. To keep an old configuration, use **File** > **Save As** to save the modified configuration under a different name before closing the project.

Only one instance of each type of logging configuration can be loaded into a project. If you have modified a configuration, you are prompted to save it when you create a new file or open an existing one. A Remote Logging configuration can include up to seven further remote configuration files (see **Select Config** in [Channel Properties and Configuration](remote-logging/configure-remote-logging-dialog-box/channel-properties-and-configuration.md)), and a CAN configuration can include further CAN configuration files (see [CAN Configuration Dialog Box](can-configuration/can-configuration-dialog-box/index.md)).

Remote and Burst logging configurations can also be [Uploaded](loading-configurations.md) from an ECU.

**See also:** [Loading Configurations](loading-configurations.md)
