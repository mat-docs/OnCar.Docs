# Puma Errors

Although PUMA is designed for unattended tuning, commands will not always be successful. System Monitor may send the following error messages to PUMA:

| Error | Meaning |
|---|---|
| *command not executed* | System Monitor did not execute the command because of an incorrect command sequence: a command other than **Identify** was sent after **Init** but before a successful **Identify**. |
| *error during execution* | System Monitor started execution of the command but did not complete it, because the command arguments were incorrect (for example, an unknown parameter) or because of an external error. The [Testbed Message](../testbed-message.md) window shows the reason, for example "Invalid parameter", "Not online", "Invalid checksum", "Could not translate identifier" or "Incorrect LUN value (not = 1)". |
| *command not available* | The testbed has issued a command which System Monitor does not support, or a Scalar or Map command while the link is in **Measurement** mode. |

!!! note
    System Monitor only allows PUMA to work with one project at a time, so the LUN parameter must be given a value of 1 wherever it occurs. If it has any other value, System Monitor replies with an *error during execution* error message.

Errors can be viewed in the [Testbed Message](../testbed-message.md) window. The most recent error is also shown in its **Last Error** field.
