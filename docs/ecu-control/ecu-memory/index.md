# ECU Memory

Electronic Control Units (ECUs) used in motorsport have one or more controllers, which have access to two types of memory:

- **RAM** - Random Access Memory is volatile and needs a power supply to keep its contents. RAM can be modified quickly and individual memory locations can be changed independently, so System Monitor can change data in RAM while the ECU is On-Line and running a test. The RAM that System Monitor can modify is called Application RAM; it contains only the Data Version.

    RAM can be changed by:

    - [Copying ROM to RAM](copy-rom-to-ram.md) (**Undo Data Changes in Unit**)
    - [Reset ROM](../data-changes-in-the-ecu/reset-rom.md) (**Undo Data Changes in Unit & Edit Buffer**)
    - [Downloading Data to the ECU](../data-changes-in-the-ecu/downloading-data-to-the-ecu.md)
    - [Live Tune](../../tuning/live-tune.md)

- **ROM** - Read Only Memory is implemented by programmable, non-volatile devices such as EEPROM or Flash-RAM. These can be programmed, but only when the ECU is Off-Line. For each controller, ROM is divided into separate areas for Data, Configurations and Program. A whole memory area has to be reprogrammed at once; memory locations cannot be modified individually.

    ROM can only be changed by [Reprogramming the ECU](reprogramming-the-ecu.md).

Most types of ECU can operate from either RAM or ROM. To control which memory is used, select [Run from ROM](run-from-rom.md) or [Run from RAM](run-from-ram.md).

The [ECU Bar](../../using-system-monitor/tool-and-information-bars/ecu-bar.md) shows how the ECU is being used.

**See also:** [Developing Data Versions](../../project-management/developing-data-versions/index.md); [ECU Control](../index.md); [Read Ram](read-ram.md); [Tuning](../../tuning/index.md)
