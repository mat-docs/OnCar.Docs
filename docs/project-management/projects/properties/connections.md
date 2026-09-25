# Project Properties - Connections tab

The Connections tab is used to view and change the way System Monitor is connected to the ECU. To open the Connections tab, select **File** > **Properties** > **Connections** or **ECU** > **Connections**.

The connection methods are **HDLC via CA Card**, **IP via Ethernet**, **HDLC via PCMCIA card**, **CAN via VECTOR card** and **PCAN-USB**. See [New Project - Connections](../creating-a-project/stage-2-connections.md) for information on using this tab.

![Connections tab](assets/Project_Properties_Connections.jpg)

!!! note
    The screenshot does not show the **PCAN-USB** option or the **Network Adapter** / **Baud Rate** list.

If you change the connection settings and click **OK**, System Monitor turns off Live Updates, restarts communications with the new settings, and marks the project as changed so that it can be saved.

**See also:** [Properties](index.md); [New Project - Connections](../creating-a-project/stage-2-connections.md); [Unit Definition](../creating-a-project/car-definition.md); [Spare Unit](../creating-a-project/spare-car.md)
