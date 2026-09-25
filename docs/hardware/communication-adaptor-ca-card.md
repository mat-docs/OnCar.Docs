# Communication Adaptor (CA-Card)

The **CA-125** is a high-speed communications adaptor that plugs into a PCMCIA Type III slot in the PC running System Monitor. It is integrated with the System Monitor software: select **HDLC via CA Card** on the [Connections](../project-management/projects/properties/connections.md) tab of the Project Properties to use it.

The **CA-125** has a 4 Mbit/s HDLC link for a wired connection to a TAG ECU. It can run at 4 Mbit/s synchronous or 750 kbit/s asynchronous, full duplex. The link can receive data at up to 4 Mbit/s from a TAG PAA-100 Parallel Adaptor.

The **CA-125T** has a flying lead with a LEMO connector. The **CA-125M** has a flying lead with a 44-way D connector.

The **CA-125** also provides an interface to the [Adjustment Board](adjustment-board.md).

!!! note
    The CA-Card is not a licence device. System Monitor is licensed to a DESKey dongle or a network card. See [Licensing](../getting-started/licensing/index.md).

The driver and embedded code for the CA-Card are installed with System Monitor, as part of the **Device Drivers** component. In a [Custom Installation](../getting-started/custom-installation.md) you can choose not to install them.

**See also:** [Communication Architecture](communication-architecture.md); [Adjustment Board](adjustment-board.md)
