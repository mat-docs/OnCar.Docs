# Importing Hex Files

System Monitor creates Data Versions from the information in Hex files (see [Program and Data Versions](../program-and-data-versions/index.md) and [ECU Files](../files/types-of-files/ecu-files.md)). This is normally done as part of the process of creating a Program Version.

However, you can also import a Hex file into an existing Project. Select **File** > **Import Hex File**. For each Active Application, a dialog box opens so that you can browse for a Hex file.

The data in the Hex file overwrites the [Edit Buffer](index.md) of the application. The ECU is taken Off-Line during the import. If the Hex file does not contain all the memory areas of the Edit Buffer, a warning is shown. Save the Edit Buffer to create a new Data Version (see [Using Data Version Files](using-data-version-files.md)).

This facility can be used to bring development data from other applications, such as MATLAB, into System Monitor.

**See also:** [Creating a Program Version](../program-and-data-versions/creating-a-program-version.md); [Developing Data Versions](index.md); [Export to MATLAB](export-to-matlab.md)
