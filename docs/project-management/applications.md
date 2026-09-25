# Applications

Applications help different engineering development teams to work together. A typical set of applications would be:

- **BIOS** - the operation of the control system itself
- **Chassis** - the operation of the vehicle chassis
- **Engine** - the operation of the vehicle engine

When a development team changes any [Editable Parameters](../using-system-monitor/parameters/editable-parameters.md), the changes can be saved as a new Data Version. The changes made in an application are filed in its own Customer Base directory and do not affect the other applications (see [Developing Data Versions](developing-data-versions/index.md)).

If Customer Bases are used, each Project is associated with a Multi-Application Base which contains one or more Applications. Each application is associated with one Customer Base.

If [Unit.Def](unit-def-management/file-management.md) support is used, the applications are defined in the Unit.Def file in the project folder.

When a Project is open, one or more of the applications are set as the [Active Applications](active-application.md).

## Application commands

The following commands on the **File** menu act on the application selected in the Parameter Explorer or the ECU Bar:

| Command | Description |
|---|---|
| **Active Application** (Alt+A) | Makes the application active or inactive. See [Active Application](active-application.md). |
| **Application Read Only** | Sets the application to read only. |
| **Hide Application** | Hides the application in the ECU Bar. |
| **Hide Row Data** | Hides Row Data for the application. |
| **Add Application** | Adds an application to the project. |
| **Remove Application** | Removes an application from the project. |

Each application in the project is also listed under **File** > **Properties**, where it opens the [Application Properties](projects/properties/application-properties/index.md) dialog box.

**See also:** [Project Management](index.md); [Active Application](active-application.md); [Customer Base](customer-bases/index.md); [Multi-Application Base](customer-bases/multi-application-base.md); [Developing Data Versions](developing-data-versions/index.md); [Application Properties](projects/properties/application-properties/index.md)
