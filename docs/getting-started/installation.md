# Installation

System Monitor is installed with a single installer program, available from the [Motion Applied portal](https://portal.motionapplied.com/). Run the installer and follow the instructions.

The installer first installs the Microsoft .NET 8 Desktop Runtime and ASP.NET Core Runtime (64-bit) if they are not already present, and then installs System Monitor.

Three types of installation are available:

- **Typical** - Installs the standard set of components. In the current installer every component is included in a Typical installation.
- **Custom** - Lets you choose which components to install and where to install them. See [Custom Installation](custom-installation.md).
- **Complete** - Installs all components.

## System requirements

See [PC System Requirements](../hardware/pc-system-requirements.md). The installer checks the Windows version only; it does not check memory, disk space or processor.

## Installation folders

System Monitor is installed in the following folder by default:

`C:\Program Files (x86)\McLaren Electronic Systems\System Monitor 8`

A different folder can be selected in a Custom installation.

The installer also creates:

- the Licence Manager, in `C:\Program Files (x86)\Motion Applied\LicenceManager`
- a **System Monitor** shortcut on the desktop
- a **McLaren Electronic Systems** folder in the Windows Start menu, containing **Licence Manager** and a **System Monitor 8** folder with the **System Monitor** and **Sax Basic IDE** shortcuts
- `Log` and `Unlock Lists` folders under `Documents\McLaren Electronic Systems\System Monitor 8`.

If System Monitor is running when you install, the installer asks you to close it. You may be asked to restart your computer if components that need a restart were installed.

## Removing System Monitor from your computer

To remove System Monitor, uninstall it from **Apps** (or **Programs and Features**) in Windows Settings.

**See also:** [Custom Installation](custom-installation.md); [Introduction](../index.md); [PC System Requirements](../hardware/pc-system-requirements.md)
