# Introduction

Because of the long-term limitations of [Multi-Application Bases](../customer-bases/multi-application-base.md) and [Customer Bases](../customer-bases/index.md), these are being phased out in favour of a working-directory method that uses Unit.Def files, where required, to provide configuration options.

To use Unit.Def files, set the [Advanced Setting](../../using-system-monitor/settings.md) **Enable Unit.Def configuration (Y/N)** to Y and restart System Monitor. This disables the [Customer Base](../customer-bases/index.md) interface. The default setting (N) continues to use the Customer Base interface.

When Unit.Def configuration is enabled:

- The **File** > **Select Base** command is replaced by **File** > **Manage Unit.Def Files** (Ctrl+S). See [Unit.Def Files](file-management.md).
- An additional **Open** submenu is added to the **File** menu. See [Unit.Def Project Management](project-management.md).

The folder containing the System Monitor project file is treated as the base project folder, with all project files contained in sub-folders of that folder.

If there is no Unit.Def file in a folder, System Monitor uses the default options for any projects located in that folder.

**See also:** [Unit.Def Files](file-management.md); [Unit.Def Project Management](project-management.md); [PGV Creation](pgv-creation.md); [Unit.Def Project Import](project-import.md)
