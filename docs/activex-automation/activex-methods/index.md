# ActiveX Methods

The System Monitor Automation interface exposes methods only (no properties). The method signatures on these pages are taken from the System Monitor type library, which is described in Microsoft's Object Description Language (ODL). Arguments marked `[out]`, and pointer (`*`) arguments that receive results, return values to the caller. Array arguments are passed as `VARIANT`s holding SAFEARRAYs.

Most functions require a project to be loaded in System Monitor (see [Accessing ActiveX Functions](../accessing-activex-functions.md)).

Many functions take an argument (`wAppId`) which identifies the application in a multi-application environment (for example System, Chassis or Engine). Refer to the embedded code release notes for the Application Ids. Where noted, an Application Id of 0 means "any application".

All functions return a signed 32-bit (`long`) [error code](../activex-errors/activex-error-codes.md): 0 indicates success and negative values indicate errors.

The contents of ECU messages and responses (see [SendMessage](ecu-control.md#sendmessage)) are described in the System Monitor Message Descriptions document. Contact [Motion Applied support](https://portal.motionapplied.com/) for details of these messages.

The functions are listed under the following headings:

- [ECU Control](ecu-control.md)
- [Project Management](project-management.md)
- [Data Acquisition](data-acquisition.md)
- [Parameters](parameters.md)
- [Conversion Rules](conversion-rules.md) (also contains the [Enumeration Definitions](conversion-rules.md#enumeration-definitions))

**See also:** [ActiveX Automation](../index.md); [ActiveX Error Codes](../activex-errors/activex-error-codes.md)
