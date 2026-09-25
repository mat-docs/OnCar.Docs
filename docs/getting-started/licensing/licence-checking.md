# Licence Checking

System Monitor checks your licence when it starts, and again when you create, open, import or export files (**File** > **New**, **Open**, **Import**, **Export** and project export).

The check looks for a licence device (a DESKey dongle or a network card) and then for a valid System Monitor licence for that device and for this version of System Monitor.

- If no licence device is found, a message says that no network adapter or dongle was detected. Check the dongle or network settings and click **Retry**, or click **Cancel**.
- If no valid licence is found, the **Licence Required** dialog box opens. Click **Add Licence** to open the [Licence Manager](adding-a-licence.md). When you close the Licence Manager, System Monitor repeats the check and, if the licence is now valid, carries on. Click **Cancel** to abandon the operation.
- If the licence is for an earlier version of System Monitor, a message says that you do not have a valid licence for this version.
- If the licence expires within the next 28 days, a warning is shown. These warnings can be turned off with the Advanced Setting **Suppress Licence Expiry Warnings (Y/N)**.

Once a valid licence is found, the features available are those enabled by the options in the licence. Features that the licence does not enable are unavailable.

**See also:** [Licensing](index.md); [Adding a Licence](adding-a-licence.md)
