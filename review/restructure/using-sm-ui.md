# using-sm-ui — restructure report

Scope: `docs/using-system-monitor/` (all except `parameters/`), 55 pages. Strict build clean for these pages.
Source root below: `ATLASSM/Main/`. `rc` = `SMv7/SMv7/SysMonApp.rc`; `views.rc` = `Core/SysMonViews/SysMonViews.rc`.

## Per page

- **index.md** – cleaned; captions; added section overview links.
- **main-window.md** – cleaned headings; noted MRU auto-open setting (`Core/SysMonCore/TAdvOptions.cpp:96`); listed window components.
- **keyboard-operation.md** – rebuilt from both accelerator tables (rc:1174-1206, 1208-1352) + PCU accel (`Core/SysMonPCU/SysMonPCU.rc:1021`). Corrected: PAGE UP/DOWN reversed in CHM (`Core/SysMonDesktop/TDesktop.cpp:568-600`); Remote Download is CTRL+ALT+F5 not CTRL+F6; CTRL+F6 = Remote Config Compare; Remote Upload CTRL+ALT+F6; pot board keys (Configure = CTRL+SHIFT+F1, Reset = F3; CHM had them swapped); Unit Status CTRL+U (not ALT+U); Live Calibration CTRL+SHIFT+F8; Ext Inputs Config CTRL+B; CTRL+F8/F9 = CAN Config/Compare; ALT+A is Active Application (not "next"). Removed: CTRL+R (ID_SENSOR_TOOL has no handler), ALT+SHIFT+L (no accelerator). Added: ALT+7/8/9, ALT+HOME/END, ALT+SHIFT+B/U/I/Z/D/F, CTRL+ALT+P, CTRL+Q, CTRL+I, CTRL+D, CTRL+SHIFT+D, ALT+Z/ALT+D, ALT+=, CTRL+ALT+SHIFT+P/D/S, pot switch keys CTRL(+SHIFT)+1..8 (`TSysMonFrame.cpp:1508-1517`), alternate keys (ALT+BKSP, SHIFT+DEL, CTRL/SHIFT+INS), Dashboard keys. Macro F2 / CTRL+ESC kept (`TMacroManager.cpp:1283`, WM_CANCELJOURNAL 1596).
- **settings.md** – replaced CHM table with verified 64-row Advanced Settings table from old site (matches `TAdvOptions.cpp:88-203`; old defaults e.g. Prompt on Remote Reset = N, Timeout 2000). Not carried: Axis/Operators/Number formats/shortcut sections.
- **menus/index.md** – corrected no-project menu set; Sensors menu conditional (`TSysMonFrame.cpp:3031-3098`, B_VAL_NO_SENSOR_CAL at 3188); Desktop greyed with Formula E licence (3042-3059).
- **menus/file-menu.md** – full list from IDR_PROJECT/IDR_SYSMON (rc:650-665, 732-782). Added Save Copy As, Save All As, Properties submenu (per-app entries, `TSysMonFrame.cpp:588-621`), Hide Application, Hide Row Data, Add/Remove Application (+conditions `TSysMonFrame.cpp` OnUpdate*), Export Registry (`TSystemMonitor.cpp` OnFileExportRegistry), Print Preview, Close Project & Select Base, Unit.Def variants (`TSysMonFrame.cpp:458-499`), GT Customer save restriction (`TSystemMonitor.cpp` OnUpdateFileMenu). Removed standalone "Select Base (project open)".
- **menus/edit-menu.md** – verified rc:783-800; table; no-project subset.
- **menus/view-menu.md** – added Group Descriptions Only, Display Unlocked/Locked/All, Notes/Programming/Extended Comms bars, shortcuts (rc:801-827).
- **menus/ecu-menu.md** – rc:828-876. Added Reprogram All, three Undo commands (replacing "Copy Rom to Ram"/"Reset Data to Rom" labels), Distribute PUL (`TSysMonFrameEcu.cpp` OnUpdateDistributePUL), FIA submenu Reset/Clear Logging/Set Mode; FIA enable condition corrected (`OnUpdateFIA`: secure mode + ECU public key, not licence); Remote Reset disabled in Race (`TSysMonFrameDaq.cpp:200`). Removed duplicate Reprogram Unit line.
- **menus/sensors-menu.md** – rc:877-902 + dynamic `TSysMonFrame.cpp:3067-3088`. Added Edit/Sync/Export/Import sensors DTV, Recent Files; note on mislabelled shortcuts; Ext Inputs enable condition (`TSysMonFrameTsb.cpp` OnUpdateTsbConfig).
- **menus/logging-menu.md** – rc:903-929. Added CAN Configuration Compare, shortcuts, enable conditions (`TSysMonFrameDaq.cpp` OnUpdateCanConfigConfiguration, `TSysMonFrameSensor.cpp` input-signal handlers, `OnUpdateLoggingLiveConfig`), ECU Read Only effect on Remote Reset.
- **menus/tools-menu.md** – rc:930-1046. Added History Report submenu, Configuration API Setup submenu (+conditions `TSysMonFrameTools.cpp` OnUpdateConfigurationAPI*), Matlab Export submenu structure, FIA Unlock List Management (team licence only, `TSysMonFrame.cpp:3100-3122`), shortcuts. Corrected: Macros and Customise are available with a project open (were "only with no project"); custom entries inserted above Customise (`TCustomMenuList.CPP`).
- **menus/data-wizard-menu.md** – rc:1047-1091. Added Locked mask, Recent Files, prompts for Compare/Merge; noted Different Definition not on toolbar.
- **menus/desktop-menu.md** – rc:1092-1153. Added Clear All Display Offsets (`TSysMonFrameViews.cpp` OnResetAllDisplayOffsets). Fixed broken See-also link.
- **menus/help-menu.md** – rc:1154-1165. Added Decode Message Log, View Log Folder, Configuration API Documentation (`TSystemMonitor.cpp` OnMsgLogDecode/OnViewLogFolder/OnViewApiDocumentation); "Add Licence" → "Licence Manager...".
- **menus/window-system-menu.md** – rebuilt from system-menu additions (views.rc:597-1070; `Core/SysMonBaseViews/TVIEW.CPP:1571-1587`). Added Raw Decimal, Compare commands, Show Trace as Block, Centre Active Site, Export 2d/3d Map, Zero All Values/Clear offsets, Fill Window, per-window table incl. Dial Gauge, Signal Sampling, Alarms, Dashboard (`SysMonPCU.rc:911`). Reduced always greyed (`T1AxisMapView.cpp:4845`). Close disabled when locked (TVIEW.CPP:1131).
- **context-menus/index.md** – added Bar Graph entry; clarified window-level commands.
- **context-menus/edit-context-menu.md** – edit-mode menu from `SysMonBaseViews.rc:241` (adds Delete, Copy String; enable rules `TParamEdit.cpp:233-250`); removed "Select All = F2".
- **context-menus/windows-context-menu.md** – per window type from views.rc (TPARAM/TEDITPARAM/TMAPPARAM/TPOTBOARDPARAM/TDIAL/SIGNAL_SAMPLE_PARAM) and m_nPopUpID mapping in `Core/SysMonViews/*.cpp`.
- **context-menus/bar-graph / oscilloscope** – verified (views.rc:960-1008); tables.
- **context-menus/grid-cell-context-menu.md** – views.rc:855-904: added Data Format items, Border sides, Action Button submenu; filled empty "Auto Generate".
- **context-menus/parameter-explorer-context-menu.md** – `Core/SysMonParamDlgs/SysMonParamDlgs.rc:805-1215` + `TParamBrowserContents.cpp:447-495`. Corrected shortcuts (Names = CTRL+ALT+N; New Group = CTRL+SHIFT+G; New VP = CTRL+SHIFT+V – CHM swapped). Added Display filters, Matlab Export, Export Hex/FFC, Hide Application/Row Data, Virtual Param Import/Export, CAN/input variants.
- **context-menus/select-parameter-context-menu.md** – uses "Parameter RO" popup (`TParamTreeDlg.cpp:563`); added items.
- **context-menus/tool-bar-context-menu.md** – Move/Hide confirmed (`Core/OCSToolkit/sbardock.cpp:3606-3616`).
- **context-menus/data-wizard-context-menu.md** – `Core/DataWizViews/DataWizViews.rc:210-362`; added Matlab Export Memory/Data Version, Group menu, Compare/Merge Tool menus (363-548).
- **tool-and-information-bars/index.md** – added Programming Bar (rc:2043), bar shortcuts; cleaned.
- **comms-bar.md** – new PNG; added Zone 2/3, Ctrlr Busy, Bad RESP, Invalid Device, No link, No unit, modem display and colours (`SMv7/SMv7/TCommsBar.cpp:55-105, 574-605, 710-805`).
- **extended-comms-bar.md** – "Enhanced" → "Extended"; states/colours incl. Zone 2/3, No link (grey) (`TExtendedCommsBar.cpp:520-660`).
- **ecu-bar.md** – added context menu and Hide/Show Header, Basic/Advanced mode, Unit Sync OK/NOK (`TTrackTuneStatusCtrl.cpp:838-861, 1425-1446`).
- **map-bar.md** – buttons verified (views.rc:1098-1113); table cleaned.
- **maths-bar.md** – added ALT+= (rc:1238); cleaned.
- **notes-bar.md** – minor.
- **standard-tool-bar.md** – from TOOLBAR (rc:606-642): removed Different Definition button (not on toolbar), added Locked, Enable Modem; tooltips from rc:2044, 2317-2319, 2362-2363.
- **status-bar.md** – panes from `TSysMonFrame.cpp:80-89`: added Configuration API pane + right-click menu (`TSysMonFrameTools.cpp:402-440, 500-512`, `TStatusBar.cpp`), recording texts (Trigger pending), Pot Board VE-80/VE-81 (`TSysMonFrameBars.cpp`).
- **desktop/index.md, fonts.md, merging-desktops.md** – cleaned; labels verified (rc:306-321; `Core/SysMonProject/SysMonProject.rc:220-229`).
- **desktop/desktop-files.md** – corrected app-pages desktop naming: same folder as .pgv, named by program version (4 hex digits) (`Core/SysMonProject/TProject2.cpp:1864-1882`).
- **pages/index.md** – full Page submenu (rc:1128-1146): added Resize Views On Page To Fit Contents, shortcuts, Zero All online-only and removal when zero-sample-time = 0 (`TSysMonFrameViews.cpp:965-980, 1105-1128`); page navigation corrected.
- **pages/page-properties.md** – removed "up to 34 characters" (no limit in `Core/SysMonDesktop/tpagepropdlg.cpp` / `TPage.h:244`).
- **windows/index.md, edit-windows.md, measurement-windows.md** – added Dial Gauge, Signal Sampling, Dashboard, Pot Board, Alarms; Big Number noted unavailable.
- **windows/creating-windows/*.md** – full Window submenu (rc:1094-1127) incl. Dial Gauge, Signal Sampling, Dashboard (PCU400 condition, `TSysMonFrameViews.cpp` OnUpdateWindowNewDashBoard), Grid from Import (.xml, `TNumericGridViewDefn.cpp:247`); locked-page rule (OnUpdateWindowNewGeneral). Explorer creation: removed "single parameter → Big Number" (`TSysMonFrameViews.cpp` DetermineViewDefnClass → Numeric).
- **windows/using-windows/index.md** – added Show Column Headings; table.
- **window-properties.md** – tab names from views.rc (Parameters/Parameter, Extras, Dial, Pot Board, Mask).
- **window-properties-display-tab.md** – corrected default update rates: Bar Graph 200 (was 700), Oscilloscope 100 (was 700), Numeric/Grid 100 with CVRR; added Dial 30, Signal Sampling 200 (`Core/SysMonViews/*ViewDefn.cpp`). Labels from `SysMonBaseViews.rc:93-135`.
- **columns-in-tabular-windows.md** – cleaned.
- **printing/*.md** – Report Print Options: added **Summary only** and enable rules (`DataWizViews.rc:113-133`, `tprintoptions.cpp` EnableControls); cleaned others; note→warning for Close.

## OBSOLETE topics

None whole-topic. (Big Number — someone else's page — see SME.)

## Needs SME

1. **Big Number**: Desktop > Window > Big Number and ALT+SHIFT+B have no command/update handler anywhere in source (only `Core/SysMonProject/TSysMonLicMenuMap.cpp:328`), so always greyed; no Big Number view class. Is `data-display/numeric-display/big-number.md` obsolete?
2. Menu-label/accelerator mismatches in the product: Sensors Live Calibration (label CTRL+F8 in dynamic menu, key CTRL+SHIFT+F8), Ext Inputs (label CTRL+F9, key CTRL+B), Dashboard (label ALT+SHIFT+D = page offsets), Alarms (ALT+SHIFT+L has no accelerator), Window>Pot Board (label CTRL+SHIFT+F1 = configure). Documented as-is; product fix?
3. FIA Race mode "Prime Parameters set for Channel 1" kept from CHM; not found in SM source (ECU-side?).
4. Tools menu PNG shows single "Configuration API Setup..." item (current build has a sub-menu); Logging PNG predates CAN Configuration Compare. Consider re-capturing.
