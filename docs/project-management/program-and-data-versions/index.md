# Program and Data Versions

Each ECU contains one or more controllers, which require programming before use. The ECU manufacturer usually programs the controllers before despatch, but System Monitor can reprogram the ECU. System Monitor also uses the program to recognise the configuration of the ECU.

A controller used in this type of application is known as an embedded control system. A description of the embedded control system is supplied in the form of an ASAP file and a Hex file. The ASAP file contains the descriptions of the embedded control system and the Hex file contains the program code and program data.

When a new Program Version is created by System Monitor, the content of the ASAP and Hex files is converted into two files:

- **Program Version file** (extension .pgv)
- **Data Version file** (extension .dtv)

The conversion serves two main purposes:

1. To check the content of the ASAP and Hex files.
2. To store the embedded control system description in a compressed format.

The compressed format allows System Monitor to handle the data quickly while taking up less space than the original files. Because these files are specific to System Monitor, together with the Customer Base settings they ensure that the correct files are used for the attached ECU.

During the creation of the Program and Data Version files, System Monitor checks the Hex file for missing memory areas. The way these are handled is controlled by the [Customer Base Advanced Settings](../customer-bases/customer-base-advanced-settings.md).

Program and Data Version files are transferred from one Customer Base to another with the [Export](../files/exporting-files.md) and [Import](../files/importing-files.md) commands.

If you use Multi-Application Bases, you need Program and Data Version files for each Application in the Multi-Application Base before you can create a Project.

The ECU manufacturer may supply Program and Data Version files instead of, or as well as, the ASAP and Hex files. If not, you can [create the Program and Data Version files](creating-a-program-version.md) using System Monitor.

**See also:** [Creating a Program Version](creating-a-program-version.md); [Creating a Project](../projects/creating-a-project/stage-1-define-project.md); [Customer Base](../customer-bases/index.md); [Developing Data Versions](../developing-data-versions/index.md); [Program and Data Version Files](../files/types-of-files/program-and-data-version-files.md); [Project Management](../index.md); [Reprogramming the ECU](../../ecu-control/ecu-memory/reprogramming-the-ecu.md)
