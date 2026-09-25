# Burst Logging - Intervals

The logging interval for each Burst Logging block is set up on the [Parameters](burst-logging-parameters-tab.md) tab of the Configure Burst Logging dialog box.

The hardware design imposes restrictions on the way the [Logging Memory](../logging-memory-allocation.md) is used and on the speed of logging. System Monitor applies these restrictions automatically and calculates the minimum interval.

Intervals are powers of two from 1 ms to 16384 ms. Parameters can only be logged in complete blocks, even if a block is not full. Logging is ECU time synchronous.

The unit can log one block every millisecond. The total of (number of blocks ÷ interval in ms) must therefore not exceed 1. When all the blocks with parameters assigned use the same interval:

Minimum interval (ms) = number of blocks with parameters assigned, rounded up to the next power of two

A Blocks and B Blocks are independent and have different minimum intervals.

If higher rate sampling (a shorter interval) is required for selected parameters, the minimum interval can be reduced by doing one or more of the following:

- Increase the interval of some other parameters.
- Move parameters from A Blocks to B Blocks, or from B Blocks to A Blocks.
- Set the interval of some other parameters to ---.
- Set the block assignment of some other parameters to ---.
- Remove some other parameters.

If the interval allocation exceeds what the unit can support, System Monitor warns you that the logged data is likely to have errors and asks you to correct the block intervals.

**See also:** [Burst Logging - Blocks](burst-logging-blocks.md)
