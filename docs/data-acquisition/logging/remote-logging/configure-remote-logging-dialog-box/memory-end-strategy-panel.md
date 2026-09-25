# Memory end strategy panel

The Memory end strategy applies to all the channels. Two strategies are available:

- **Stop when full** - Data is logged from the start trigger until either the stop trigger occurs or the ECU memory is full. This is the default.
- **Wrap** - Data is logged from the start trigger until the stop trigger occurs. If the available memory is exceeded, new data overwrites the oldest data in the memory, so the memory always contains the most recent logged data. Use this strategy if you want to analyse data leading up to a specific event.

**See also:** [Remote Logging - Channel Overview tab](channel-overview-tab.md)
