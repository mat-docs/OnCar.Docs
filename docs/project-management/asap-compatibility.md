# ASAP Compatibility

System Monitor has been designed around the ASAP standards.

## ASAP1b

Defines the interface to the communication hardware. The System Monitor communications layer is based on the ASAP1b interface. The drivers for the supported connection methods (HDLC, IP via Ethernet, CAN via VECTOR card and PCAN-USB) are built into System Monitor; see [New Project - Connections](projects/creating-a-project/stage-2-connections.md).

## ASAP2

Defines the format of the definition files (.a2l) that describe the ECU. System Monitor reads the ASAP2 file when a [Program Version](program-and-data-versions/index.md) is created. For older TAGtronic systems, a conversion utility (TAG2ASAP) is installed with System Monitor to port these projects into System Monitor. For current products, development tools such as MATLAB are used to provide an enhanced environment for the development of embedded programs.

## ASAP3

Defines the interface to automated test bed systems (the [AVL PUMA](../testbed-operation/index.md) system) and allows endurance and automated optimisation tests to be run unmanned.

**See also:** [Project Management](index.md); [Communication Architecture](../hardware/communication-architecture.md)
