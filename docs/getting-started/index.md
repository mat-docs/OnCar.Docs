# Getting Started

The main steps needed to start using System Monitor are:

1. **Install System Monitor.** Download the System Monitor installer from the [Motion Applied portal](https://portal.motionapplied.com/) and run it. See [Installation](installation.md).
2. **Add your licence.** System Monitor is licensed to a USB dongle or to a network card in your PC. Licensing allows System Monitor activities (such as creating data sets or analysing logged data) to be carried out without an ECU connected. To add or remove licences, open the Licence Manager by selecting **Help** > **Licence Manager**, or by clicking **Add Licence** in the Licence Required dialog box. See [Licensing](licensing/index.md) and [Adding a Licence](licensing/adding-a-licence.md).
3. **Load your ECU and project management files.** See [Project Management](../project-management/index.md).
4. **Connect your ECU.**
5. **Start System Monitor.** Use the **System Monitor** desktop shortcut, or select it from the **McLaren Electronic Systems** > **System Monitor 8** folder in the Windows Start menu.
6. **Select a Multi-Application Base or configure a [Unit.Def file](../project-management/unit-def-management/file-management.md).** Customer Bases control access to files to prevent ECUs from being loaded with the wrong program. Customer Bases are associated with a project by a Multi-Application Base. Select **File** > **Select Base** (**Ctrl+S**). In the Select Active Multi-Application Base dialog box, select a Multi-Application Base from the list and click **OK**. See [Multi-Application Base](../project-management/customer-bases/multi-application-base.md).

    ![Select Active Multi-Application Base dialog box](assets/New_Multi_App_base_Normal.gif)

7. **If you use Multi-Application Bases, create a Program Version for each Customer Base.** Before a Project can be created, the Program and Data Version files for each Application in the Multi-Application Base must be defined. An ECU embedded control system is described by an ASAP file and a Hex file. System Monitor uses these files to create a Program Version (.pgv) file and a Data Version (.dtv) file.

    !!! note
        The ECU manufacturer may supply Program and Data Version files instead of, or as well as, the ASAP and Hex files. If not, you can create the Program and Data Version files in System Monitor.

    To create a Program Version, select **File** > **New** (**Ctrl+N**). In the File New dialog box select **Program Version** and click **OK**. In the New Program Version dialog box, choose the files to include: for each file, click its type in the Properties list, then enter the file name and path or browse for the file. See [Program and Data Versions](../project-management/program-and-data-versions/index.md).

8. **Create a Project.** A Project links all the files that you need to work on an ECU. The files for a Project are stored in a Multi-Application Base. A Project needs a Program Version for each Customer Base in the Multi-Application Base, so create the Program Versions first.

    To create a Project, select **File** > **New**, select **Project** and click **OK**. A series of dialog boxes takes you through creating the Project:

    1. **Project** - Enter details to define the Project. See [Define Project](../project-management/projects/creating-a-project/stage-1-define-project.md). Click **Next**.
    2. **Project Properties** - Select how to connect to the ECU. See [Connections](../project-management/projects/creating-a-project/stage-2-connections.md). Click **Next**.
    3. **Desktop** - Enter a file name for the Desktop. See [Define a Desktop](../project-management/projects/creating-a-project/stage-3-define-a-desktop.md). Click **Next**.
    4. **Program Version** - A Program Version dialog box opens for each Customer Base. Enter or browse for the Program Version to use. See [Program Version](../project-management/projects/creating-a-project/stage-4-program-version.md). Click **Finish** to create the Project.

9. **Use your Desktop to [tune](../tuning/index.md) and configure your ECU.**

Some of these tasks may already have been carried out by the manufacturer of your ECU, who can help you and supply the appropriate files.

**See also:** [Desktop](../using-system-monitor/desktop/index.md); [Introduction](../index.md); [Using System Monitor](../using-system-monitor/index.md)
