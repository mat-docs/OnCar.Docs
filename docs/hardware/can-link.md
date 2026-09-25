# CAN Link

CAN (Controller Area Network) is a serial data communication protocol that was originally developed for automotive applications and is now also used in other industrial applications. The CAN protocol is described in ISO 11898.

- Access to the bus is controlled by non-destructive, bit-wise arbitration.
- Messages are small (up to eight data bytes in classic CAN) and are protected by a checksum.
- Messages have no explicit address. Each message carries a numeric value that controls its priority on the bus and can also identify the contents of the message.
- Error handling ensures that messages are retransmitted if they are not received correctly.
- Faults are isolated, and faulty nodes are removed from the bus.

System Monitor can be used to configure an ECU or data logger to interpret sensor data on a CAN link, and to configure the CAN messages it transmits. Where the unit supports CAN FD, the CAN bus page of the configuration shows **CAN-FD Supported** and a **Data Speed** can be selected. See [CAN Configuration Dialog Box](../data-acquisition/logging/can-configuration/can-configuration-dialog-box/index.md).

An ECU can also be connected to System Monitor over CAN, using a Vector CAN card or a PCAN-USB adapter. See [Communication Architecture](communication-architecture.md).

**See also:** [CAN Configuration Dialog Box](../data-acquisition/logging/can-configuration/can-configuration-dialog-box/index.md); [External Inputs - Input Source](../data-acquisition/sensors/external-inputs/external-inputs-input-source.md)
