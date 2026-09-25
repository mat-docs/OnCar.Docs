# Team Security

The Team Security feature of the FIA Standard ECU prevents unauthorised retrieval of data from an ECU by other teams.

## Team IDs

Team security is achieved by allocating a unique Team ID to each team. The Team ID is set in the licence file, and the same Team ID is used for all instances of System Monitor used by a team. More than one team may be available for selection as the Active Team (for example, where one team is affiliated to another). Some licences use Consortiums instead of Teams, in which case a Consortium ID is used in the same way.

Select the Active Team (or Active Consortium) in the [Licence Manager](../licensing/adding-a-licence.md).

## Verification

When System Monitor connects to an FIA Standard ECU, it checks the ID of the Active Team against the ID in the ECU. If they match, System Monitor operates normally and ECU tuning can be carried out.

If they do not match, a message tells you that the Team ID does not match the ID in the ECU, that the ECU must be cleared and reprogrammed for full access, and asks whether you wish to clear it.

- Click **Yes** to clear and reprogram the ECU. After reprogramming, a clear logging command is sent to the ECU. When the link to the ECU is re-established, the Team ID is checked again and ECU tuning can be carried out.
- Click **No** for restricted access only: **Live Updates** and **Live Auto Tune** are turned off.

## Data Version file security

Team security also prevents Data Version (`.dtv`) files being loaded by other teams. Data Version files contain a list of Team IDs, which are verified when the file is loaded. The file does not load unless a valid Team ID is found.

When you save a Data Version with **File** > **Save As**, the **Team Security** drop-down list in the File Save As dialog box sets the team the file is secured to. Select **Disabled** to save it without Team Security. The drop-down list is only shown if your licence allows you to change the security of that file. The same option is available when saving logging configurations and Desktops.

Data Version security can be turned on or off with the Advanced Setting **Enable Data Version Security (Y/N)** (**Tools** > **Advanced Settings**). The default is Y. If it is set to N, Data Versions are saved without Team Security, whatever is selected in the **Team Security** drop-down list. This setting is ignored for Data Versions that use enhanced Reduced Data Access.

**See also:** [Reduced Data Access](reduced-data-access.md); [Adding a Licence](../licensing/adding-a-licence.md)
