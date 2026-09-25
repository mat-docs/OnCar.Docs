# Custom Installation

Custom Installation lets you choose which components to install, and the installation folder. To use it, start the [Installation](installation.md) in the usual way and select **Custom** when the setup type options appear.

By default all components are selected. When you upgrade an existing installation, the components you previously selected are kept.

The following components are available:

- **System Monitor**
    - **Program Files**
        - **Program Files Unicode** - System Monitor itself, the Licence Manager, the Configuration API service, the ActiveX type library, file associations, and the registry settings for the default Free User [Customer Base](../project-management/customer-bases/index.md) and [Multi-Application Base](../project-management/customer-bases/multi-application-base.md).
        - **Conversion Utility** - The TAG2ASAP conversion utility.
        - **Sax Basic** - The [Sax Basic](../activex-automation/activex-client-languages/sm-script.md) development environment, used to create ActiveX scripts for System Monitor.
    - **PCU** - Files needed to communicate with a PCU.
    - **Device Drivers** - Drivers and embedded code for hardware used by System Monitor, including the [CA-Card](../hardware/communication-adaptor-ca-card.md) driver and embedded code, and the Vector CAN driver library.
- **DESKey Dongle Drivers** - Copies the DESKey driver installer for the DK2 USB, Parallel and Network dongles to `C:\Program Files (x86)\Deskey`. Run it to install the dongle drivers.
- **VE-82 Drivers** - Copies the Microchip drivers for the VE-82 Pot Board to the System Monitor folder. Run `USBDriverInstaller.exe` from that folder to install them.

**See also:** [Installation](installation.md)
