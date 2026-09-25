# Restructure report: data-acquisition

Scope: `docs/data-acquisition/` (66 pages). Source paths are relative to `ATLAS9/ATLASSM/Main/`. Abbreviations: DAQ = `Core/SysMonDAQ/SysMonDAQ.rc`, APP = `SMv7/SMv7/SysMonApp.rc`, TSB = `Core/SysMonTSB/SysMonTSB.rc`, SAT = `Core/SysMonSat/SysMonSat.rc`.

All pages: CHM artefacts removed (`i_white_sm.jpg` icons, "See dialog box>", `image\` alt text, layout tables, `<br>` soup). Procedures made into numbered lists, definition tables given headers, notes made into admonitions. Where the old site had newer PNGs, they were copied into the page's `assets/` and used instead of the GIFs. Strict build is clean for this folder.

## Pages

### Data Acquisition / Logging
- **index.md** — Mentions the CAN tools on the Logging menu (APP:903-929).
- **logging/index.md** — Added links to Remote Configuration Compare, CAN Configuration and Input Signal Configuration (APP:919-925).
- **logging-memory-allocation.md** — Removed the TAG 3.8 and DLU hardware rows: `TTag38RemoteDaConfig.cpp` is not in `SysMonDAQ.vcxproj`. Kept TAG-300/MCU-300. Limits are unit-dependent (`TMapBurstBlockInfo.cpp:1326-1330`, `SysMonParams/TRemoteChannel.cpp:775`).
- **session-details.md** — "Edit..." label (DAQ:152). Added: the Session tab is hidden when the BIOS configures telemetry (`TTag2000RemotePropertySheet.cpp:88-108`, `TRemotePeriodicPropertySheet.cpp:97-105`).
- **sessions-and-telemetry.md** — Dropped the ATLAS 6/7 note. Sessions are .ssn (DAQ IDS_SESSIONFILTER). Added that remote channels can be sent by telemetry (DAQ:269, 530).
- **channels.md** — Removed the unverifiable "PC timer, minimum 5 ms". Added Advanced Setting "Session Row Logging Interval (ms)", default 1000 (`Core/SysMonCore/TAdvOptions.cpp:120`, `TLiveDAConfig.cpp:213`). DATALab channel count now comes from the unit, default 4 (`SysMonCore/TSystemConstants.cpp:411`). "Row Data" is the product term (`AtlasSession.rc:236`).
- **logging-configuration-files.md** — Corrected: a single shared `\LogCfgs` folder, not one per type (`SysMonProject/TProject3.cpp:319-357`, `SysMonProject.rc:765-777`). Added multi-file remote and CAN configurations.
- **loading-configurations.md** — Added a table of menu commands with shortcuts (APP:880-929, 1295-1334). Added Burst/Remote Reset, Remote New Session and Export (APP:2040-2042, 2223-2335).

### Live Logging
- **index.md** — CTRL+L (APP:1261). Greyed while On-Line (`TSysMonFrameLive.cpp:668-676`). Tab descriptions updated.
- **session-tab.md** — Corrected: "Session Location" with a folder picker, and "Incrementing Session Filename" with Name / Date/Time (DAQ:139-146, `TLiveDASessionPage.cpp:437-450`). Date/Time naming is yymmddhhmmss.ssn (`TRecodingConfig.cpp:434-452`). Maximum 999 shots (`TLiveDASessionPage.cpp:37`). Removed SESSnnn.SSN, which is now dead code (`TRecodingConfig.cpp:300-365`).
- **trigger-timing-tab.md** — Removed Pre and Post (commented out in `TLiveDATriggerPage.cpp:342, 588`; DAQ:120-123). Corrected Stop logging: started manually, stops on the trigger or when the time ends (DAQ IDS_STOP_TRIG_INFO). Removed the pre-trigger buffer note. Default 600 s (`TLiveTrigger.cpp:45`). Added low-disk warnings (DAQ IDS_SM_LOW_DISK_SPACE, IDS_SM_SESSION_CLOSED_LOW_DISK).
- **trigger-condition-tab.md** — PNG screenshot only.
- **recording.md** — When Recording is enabled (`TSysMonFrameLive.cpp:754-779`). "Trigger pending" (APP:2001).
- **automatic-recording.md** — Corrected the Start and Stop logging behaviour (as above; `TSysMonFrameLive.cpp:1038-1060`).

### Remote Logging
- **index.md** — CTRL+F5. Added the Session tab and its hiding condition (see above), .rlc files (`TConfigCompareDlg.cpp:166`) and a link to Compare.
- **channel-overview-tab.md** — Rewritten as an overview of the panels.
- **channel-properties-and-configuration.md** — Removed "eight channels" and "512 maximum": both are unit-dependent (`TTag2000RemoteDaConfig.cpp:7599-7623`). Frequencies are unit-dependent (`TTag2000RemoteChannelPage.cpp:2019-2034`). Added: Edge and Prime cell menu items (`TRemoteParamGridCtrl.cpp:1014-1024`), the header menu (DAQ:1160-1168), Filter, Logging offset/Reset (`TTag2000RemoteChannelPage.cpp:865-867, 1545-1560`), PPO file and Select Config with up to 8 configurations (DAQ:570-607, `TSelectConfigDlg.cpp`). Button labels "Parameters...", "Channel...", "Arrange..." (DAQ:394-402). The 100 Hz enable default is confirmed (`TRemoteParamGridCtrl.cpp:3356-3360`).
- **driver-push-button-panel.md** — Labels confirmed (DAQ:370-374). Removed the claims about the Channel Trigger "Driver push button" condition, which no longer exists (`TRemoteDaTriggerDlg.cpp:534-555, 777`).
- **logging-duration-and-rate.md** and **memory-end-strategy-panel.md** — Wording updated. Stop when full is the default (`TRemoteDAConfig.cpp:245`).
- **duration.md** — Labels and units (DAQ:419-455). Table format.
- **channel-trigger.md** — Conditions are On data, Ignition on, Lap trigger, External Trigger and No condition (`TRemoteDaTriggerDlg.cpp:534-555`). Six operators (DAQ:881-970). Repeat default 1, disabled for No condition (`SysMonParams/TRemoteTrigCondition.cpp:89`, `TRemoteDaTriggerDlg.cpp:249-257`). Start post-trigger ±999999 ms, Stop post-trigger 0-999999 ms (`SysMonParams/inc/TRemoteTrigger.h:38`, `TRemoteDaTriggerDlg.cpp:1408-1425`). The parameter dialog is "Set Trigger Parameter" (`:441`); the old GIF was removed. Added the Channel panel (Name, Telemetry, Logged to Unit) and Prev/Next (DAQ:262-270).
- **arrange-channels.md** — Corrected: clearing the check box hides the channel (`TArrangeChannelsDlg.cpp:152-154`).
- **synchro-pattern.md** — Added Select All / Clear All (DAQ:546-547). Only available when the unit supports it.

### Burst Logging
- **index.md** — CTRL+F1. The Session tab is conditional.
- **burst-logging-parameters-tab.md** — Size comes from the unit (`TRemotePeriodicDaConfig.cpp:287-312`). Added the Auto Assign release/assign text (DAQ:496) and the multi-unit restriction. Keypad +/- (`TBurstParamGridCtrl.cpp:291-296`), DELETE (`TParamGridCtrl.cpp:533`). Interval list is 1-16384 (DAQ:983-1018). Removed a duplicate bullet.
- **burst-logging-blocks.md** — Maximum block counts are unit-dependent (`TMapBurstBlockInfo.cpp:1326-1330`). The 64/64 table is kept as an example.
- **burst-logging-intervals.md** — Corrected the rule: Σ(blocks/interval) ≤ 1, rounded up to a power of 2 (`TMapBurstBlockInfo.cpp:337-388`, `inc/TMapBurstBlockInfo.h:29`). Changed "increased" to "reduced". Added the over-allocation warning (DAQ IDS_SM_BURST_INTERVAL_EXCEEDED).
- **burst-logging-triggers-tab.md** — Removed Throttle, which is hidden (DAQ:328-329, 335). Driver push is available only if the unit supports it; otherwise Ignition On is used (`TRPStartTriggerPage.cpp:355-364`). Defaults (`TRemotePeriodicDaConfig.cpp:163-176`). "Speed below" is a plain field (DAQ:330-331). Labels "Ignition On", "Engine Started", "Engine Speed", "Memory End strategy" (DAQ:319-339).
- **burst-logging-session-tab.md** — "Car ID" corrected to "Unit ID" (DAQ:80), range 1-4 (`TRemoteDASessionPage.cpp:45-46`). Frequency in MHz, .mbc file (`:389-400`). Added the conditional-tab note.
- **burst-logging-export.md** — Added the Advanced Setting "Directory for exported logging files" (APP:1608, `TAdvOptions.cpp:112`) and Remote Export (APP:915).

### Remote Configuration Compare
- **index.md** — CTRL+F6. Labels Memory/Compare/"..."/Filter/Invert Filter/Close (DAQ:609-633). Filter behaviour (`TConfigCompareDlg.cpp:277-302`).
- **config-tab.md** — Removed the "Row Merge via header" option, which does not exist. Corrected the merge menus to match DAQ:1210-1245 and `TCompareGridCtrl.cpp:665-800`.
- **triggers-tab.md** — Wording updated (DAQ:642-732).

### CAN Configuration
- **can-configuration-dialog-box/index.md** — Corrected 8 to 16 configurations. The FIA column of check boxes is shown only when the unit supports locked CAN (TSB:231-302, `TConfigPageCanLink.cpp:238-268`). Open/Delete labels. Added: Checksum (TSB:301, `TCanChecksum.cpp:91-137`), DBC import/export (`TCanUnit.cpp:1305-1306`, DAQ:734-746), CTRL+F8, and a CAN Configuration Compare section (APP:922, DAQ:748-770).
- **bus.md** — Added CAN FD: the "CAN-FD Supported" label and Data Speed (TSB:446-468, `TConfigPageCanBus.cpp:161-163`).
- **buffers.md** — Added the Reserved mode (TSB:432) and the Import/Export Buffers... menu items (`TCanBufferList.cpp:189-190`).
- **messages.md** — Add Message Id dialog: CAN FD and Frame Type fields (TSB:470-486). Menu items Add CAN Message, Import/Merge/Export Messages... (`TCanMessageList.cpp:941-946`). Tree naming (`TCanMessage.cpp:2459-2462`).
- **message-details.md** — Added Rate, Data Frame Type, CAN FD, Layout (TSB:123-162), FD lengths 0-64 with snapping (`TConfigPageCanMessage.cpp:147-151, 640-710`) and the Layout dialog, 8/64 rows (TSB:509-520, `TCANMessageLayoutDlg.cpp:47`).
- **parameter-details.md** — Start bit 0-63, or 0-511 for FD (`TConfigPageCanParameter.cpp:169`). Labels Signed/Unsigned/Float and "..." (TSB:164-197).
- **can-bit-definitions.md** — Added the PNG diagrams that the page lacked, and the FD bit range. Corrected the export note: v2 writes the logical bit position.
- **can-parameters.md** — Added the Add CAN Parameter menu item (`TCanMessage.cpp:288`).
- **import-export-buffers-and-messages.md** — Labels corrected ("Import Buffers..." and so on). Added Merge Messages and DBC. The fd/x/fdx ID suffixes and "-" for non-multiplexed columns come from the export code (`TCanMessage.cpp:2082-2087`, `TCanMessageList.cpp:304-307, 760-762`). The buffer header comes from `TCanBus.cpp:826`.

### Sensors
- **sensors/index.md** — External Inputs no longer handles CAN (`TUnit.cpp:903-906`: "SCR4012 - Remove Can Configuration"). Added the Input Signal tool and the Data Version sensor commands (APP:884-887).
- **sensors-and-actuators/index.md** — Added a table of Sensors menu commands and shortcuts (APP:877-902, 1302-1305).
- **sensor-sets.md** — Added Sensor Set Upload New and the Advanced Settings (APP:882, 1521-1523, 2430). Unit Status is Tools > Unit Status (APP:1036).
- **sensors-and-actuators-dialog-box.md** — Corrected: the columns are Name and Type, plus serial columns per sub set. Date and Status are now in the Sensor Properties dialog, opened by right-clicking (`TSatSensorPage.cpp:35, 393`, `TSatSensorListCtrl.cpp:672-712`, SAT IDD_SM_SENSOR_PROPS). Added sub sets, Active Page Properties (`TSensorSetFrame.cpp:82-96`), the Overall tab / Group mode (SAT IDD_SM_ACTIVE_SUBSETS) and the Comment field. The 238-character limit is confirmed (`SysMonSensor/inc/TSensorType.h:63`).
- **sensors-and-actuators-serial-numbers.md** — Fixed the broken image and the numbering. Corrected "Tools menu" to Sensors > Sensor Set Download. Added the status warnings and the injector class prompt (SAT string table).
- **sensor-and-actuator-constants.md** — Clean-up only.
- **enabling-and-disabling-sensors-and-actuators.md** — Menu label "Enable / Disable" (APP:894). The file is ENDIS.INI (`SysMonSensor/TEnDisIniParser.cpp`). Added the State values and groups (SAT string table). ENTER toggles the focused item (`TSatEnDisListCtrl.cpp:505-524`).
- **software-calibrated-sensors/index.md** — Clean-up only.
- **calibration-files.md** — Corrected Sbinary.exe to TpSbinary.exe (`SysMonSensor/TSensorPrmParser.cpp:584`). The Advanced Setting is "File for sensor calibration" (APP:1609). Force Rebuild deletes the .bcf (`TSysMonFrameSensor.cpp:444-452`). Removed the unverifiable "Install.bat from calibration disk" and the "run in DOS" wording.
- **sensor-calibration-tool.md** — Corrected: Manual Cal was "TBC"; it is now described (`TSensorCalDlg.cpp:1052-1075`). Added New Serial Number (TSB:803-810), the Finish prompt (`:1232`) and OK saving the .dat files (`:532-562`).
- **live-calibration.md** — Corrected the menu to Sensors (`TSysMonFrameTsb.cpp:248-286`). Button labels "Next >>" (TSB:361).
- **obtaining-sensor-calibration-data/index.md** — Branding changed to Motion Applied. The Get Sensor utility reference was replaced with a support portal contact.
- **external-inputs-configuration.md** — Removed CAN (see above). Added .xic (APP:1619), download/upload commands, Apply and the context menu (TSB:790-800).
- **external-inputs-input-source.md** — Removed CAN Link (`TUnit.cpp:903-906, 914-950`). Labels "TAG Sensor Buses", "Unit Sensors", "Spare Items Pool" (TSB string table).
- **external-inputs-selecting-a-bus.md** — Labels SN6/SN32 and buses A-D. Added the "editable parameters" note (TSB:112-121).
- **external-inputs-selecting-a-node.md** — Node types SN6, SN32, SN32-S, SN32-LT. Timer 0/1 resolution labels. The Unit Sensors timer (TSB:70-83, 207-216, string table). Fixed the µ mojibake.
- **external-inputs-adding-a-sensor.md** — Corrected: the Identifier is editable through its check box (TSB:95-96). Added uniqueness rules and the exact download prompt (APP:1825). The command is on the Sensors menu, not the Logging menu.
- **external-inputs-sn-6-interface-cards.md** — Corrected: the inputs are named "Input nA/nB" (`TTSBInterfaceCard.cpp:906-918`). A card has no configurable items (TSB:199-205). Added the 5-wire and BRIDGE rules (TSB string table).
- **external-inputs-drag-and-drop.md** — Added Cut/Copy/Paste.
- **external-inputs-speed-sensor-scaling.md** — Labels (TSB IDD_REVS_SCALING_DLG). The "Timer" item was wrongly nested under Edge Trigger. Radius or circumference is required.
- **input-signal-configuration-tool.md** — Import/Export descriptions un-swapped (`Core/SysMonInput/SysMonInput.rc:609-614`). Added the tab names (`TInputSignalConfigurationDlg.cpp:117-122`), Sample Entire Page (APP:925) and the scaling methods being unit-dependent (`TTabScaling.cpp:425-430`).

## OBSOLETE topics
- **sensors/obtaining-sensor-calibration-data/get-sensor-data-utility.md** and **using-get-sensor.md** (left unchanged). They describe a DOS "gs" utility used over dial-up Networking to a NetWare server (TAGSVR1\SYS:, F: drive, CD-ROM transfer, WPD.TWPD0176). The utility is not part of System Monitor: nothing in the SM source references TAGSVR, gs or TWPD0176. The dial-up and NetWare infrastructure is almost certainly retired. The parent index no longer links to these pages.

## Needs SME
1. Remote **Driver push button panel**: "Button on used as trigger condition" still exists, but the Channel Trigger has no driver-push condition. Is **External Trigger** the driver button input, or something separate?
2. **Request / Non-ECU Request channels** (channels.md): the Live Logging "Parameters" tab (DAQ IDD_LIVEDA_PARAMPAGE) is not added to the sheet (`TLiveDAPropertySheet.cpp:91-93`). Are these channel types still user-relevant?
3. **TAG 3.8 / DLU** removed from logging-memory-allocation.md. Please confirm that this hardware is no longer supported.
4. **Burst "adding parameters" precedence rules** and the "empty list → Auto Assign" wording, and the sensor set default name XXXXXnnn.set: kept from the CHM, not verified.
5. Sensor calibration .dat files: the obtaining-data page now points to the support portal. Please confirm the current process for obtaining calibration data.
