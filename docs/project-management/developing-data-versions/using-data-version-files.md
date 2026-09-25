# Using Data Version Files

When a Project is opened, it is loaded with the Data Versions that were in use when the project was last saved.

**Load a different Data Version into a project:**

1. Select the Active Application, then select **File** > **Open**. The File Type Selection dialog box opens.
2. Double-click **Data Version** in the **Document** list.

    The File Open dialog box opens with a filter set to Data Version (.dtv) files. The directory tree opens at the location of the currently loaded Data Version file. You can browse for files of this type within your Multi-Application Base directory.

    ![File Open dialog box for a Data Version](assets/Open_Data_Version.gif)

    When a file is selected, its Saved By and Saved On details and Notes are shown at the bottom of the dialog box.

3. Do one of the following:
    - To open the Data Version file in the current project, select the file and click **Open**. The new file replaces the Data Version in the [Edit Buffer](index.md). If the Edit Buffer has been changed, you are prompted to save it first.
    - To open the Data Version in the Data Wizard, click **DataWizard**. The existing Data Version is not affected and remains active in the project.

A Data Version file can only be saved when at least one Editable Parameter has been changed. You are prompted to save the Data Version file when you close the project or take the connected ECU Off-Line. You can also save the file at any time with **File** > **Save As** or **File** > **Save All**.

The default file name for a new Data Version is in the form *version**nnn*.dtv, where:

- *version* is the version number of the Program Version used by the Application.
- *nnn* is a three-digit hexadecimal number, one higher than the highest existing number in the folder.

**Notes:**

- File names and location may be changed, but the location can only be within the Multi-Application Base directory.
- The Comment and Notes in the Data Version panel can be edited before the file is saved.
- Old Data Version files are not overwritten, except to change the Comment and Notes. See [Project Properties](../projects/properties/project-properties.md).

**See also:** [Data Wizard](../data-wizard/index.md); [Program and Data Versions](../program-and-data-versions/index.md); [Program and Data Version Files](../files/types-of-files/program-and-data-version-files.md); [Developing Data Versions](index.md)
