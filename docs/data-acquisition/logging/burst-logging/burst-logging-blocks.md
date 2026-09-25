# Burst Logging - Blocks

The Burst Logging blocks are set up on the [Parameters](burst-logging-parameters-tab.md) tab of the Configure Burst Logging dialog box.

The hardware design imposes restrictions on the way the [Logging Memory](../logging-memory-allocation.md) is used and on the speed of logging. System Monitor applies these restrictions automatically. Blocks are filled automatically and attempts to add more than the maximum number of parameters are prevented.

There are two sizes of parameter:

- **WORD** - The parameter value is coded as one WORD.
- **DWORD** - The parameter value is coded as two WORDs.

A DWORD parameter uses exactly twice as much memory as a WORD parameter, so a given amount of memory can only accept half as many DWORD parameters as WORD parameters.

Memory is arranged in **Blocks**. There are two sizes of block:

- **A Blocks** - Each A Block can contain 4 WORD parameters, 2 DWORD parameters or a mixture of both.
- **B Blocks** - Each B Block can contain 8 WORD parameters, 4 DWORD parameters or a mixture of both.

The maximum number of A Blocks and B Blocks is defined by the unit. For example, with 64 blocks of each type:

| Block type | Max. number of blocks | Max. number of WORD parameters |
|---|---|---|
| **A Blocks** | 64 | 256 |
| **B Blocks** | 64 | 512 |

Each DWORD parameter takes up two WORD parameter places.

Parameters from different units cannot share a block.

The memory in each block is ordered by data type: it is filled first with DWORD parameters and then with WORD parameters. For example, if 7 DWORD parameters and 5 WORD parameters are assigned to B Blocks, the blocks are filled as follows:

| Block | DWORDs | WORDs | Empty | Total WORD equivalent |
|---|---|---|---|---|
| 1st B Block | 4 | - | - | 8 |
| 2nd B Block | 3 | 2 | - | 8 |
| 3rd B Block | - | 3 | 5 | 8 |
| **Total** | 7 | 5 | | |

**See also:** [Burst Logging - Intervals](burst-logging-intervals.md); [Burst Logging - Parameters tab](burst-logging-parameters-tab.md)
