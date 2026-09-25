# Channels

To enhance the versatility of the logging process, parameters are grouped into Channels (sometimes known as Sets). Because the channels correspond to physical storage locations in the data logging hardware, they are subject to various restrictions.

System Monitor recognises the type of unit from its [Program Version](../../project-management/program-and-data-versions/index.md) and only offers the appropriate type of channel. Individual units may have further restrictions (such as memory size limitations) which System Monitor recognises and uses to restrict the available options and to calculate sampling rates.

The following channel types are available. Other types may be added to suit special hardware.

## Row Data

Used in [Live Logging](live-logging/index.md) to acquire data from an ECU. When a live Session is recorded, row data values are written to the session at the interval set by the Advanced Setting **Session Row Logging Interval (ms)** (default 1000 ms; see [Settings](../../using-system-monitor/settings.md)). Since the ECU sends parameter values at an unknown and variable rate, some values may be recorded into the session file more often than others.

The parameters logged as row data are set by the embedded code independently of the logging configurations. Any parameter that is logged by a command from the embedded code instead of by a logging configuration is called a Fixed Parameter.

Fixed Parameters are typically those whose value does not change often, such as Battery Voltage, but any, and in some cases all, parameters may be set as Fixed Parameters.

Fixed Parameters are generally logged at a much slower rate than the parameters in a logging configuration and because of this they are sometimes called Slow Row data.

## Request Channel

Used in [Live Logging](live-logging/index.md) to acquire data from the [CA-Card](../../hardware/communication-adaptor-ca-card.md) via [CAN](../../hardware/can-link.md) or direct connection. Parameter values are acquired asynchronously. The minimum acquisition interval is calculated from the time to acquire each parameter and the number of parameters. You can set any interval at or above this minimum.

## Non-ECU Request Channel

A restricted form of the Request Channel. Used in [Live Logging](live-logging/index.md) for [Virtual Parameters](../../using-system-monitor/parameters/virtual-parameters/index.md).

## TAGtronic Channel

Used in [Burst Logging](burst-logging/index.md) to acquire data from the Burst memory in an ECU (see [Logging Memory Allocation](logging-memory-allocation.md)).

## DATALab Channel

Used in [Remote Logging](remote-logging/index.md) to acquire data from the DATALab memory in an ECU (see [Logging Memory Allocation](logging-memory-allocation.md)). Several independently triggered channels are available; the number of channels is defined by the unit (four if the unit does not specify otherwise). A different sampling rate can be assigned to each parameter in each channel.
