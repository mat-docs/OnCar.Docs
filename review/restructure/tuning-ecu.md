# Restructure report: tuning-ecu (docs/tuning, docs/ecu-control; 59 pages)

Source paths are relative to `ATLAS9/ATLASSM/Main/`. Every page had its CHM artefacts cleaned up: layout tables, `image\` alt text, back-to-top links, `i_white_sm` bullets, broken bold and stray `<br>` markup. Definition lists were turned into tables and procedures into numbered lists.

## Tuning

- **index.md**: added the Download Data Changes path and a link to Adjustment Board Control.
- **scalar-window.md**: formats corrected to Engineering, Raw Hexadecimal, Raw Binary and **Raw Decimal** (`Core/SysMonViews/SysMonViews.rc:620-637`). Address column appears for any raw format (`Core/SysMonViews/TScalarViewDefn.cpp:1151-1165`) and shows `-` for enhanced RDA (`:1378-1385`). Added the menu path with Alt+Shift+S (`SMv7/SMv7/SysMonApp.rc:1095`) and the font and column-heading options.
- **string-window.md**: cleaned up. Added the menu path and the font options (`SysMonViews.rc:803-815`).
- **array-window.md**: added the Engineering, Raw Hex and Raw Decimal formats (`SysMonViews.rc:742-757`) and the menu path.
- **2-axis-map-window.md**: added Raw Decimal, Live Tune Overview, Graphical/Difference/End, Toggle Grid/Graphical Alt+G, AutoZoom, Centre Active Site, Show Trace as Block and Export 3d Map (`SysMonViews.rc:697-740`).
- **1-axis-map.md**: same changes as the 2-axis page (`SysMonViews.rc:654-695`).
- **1-axis-map-multiple-parameters.md**: cleaned up and added a See also line.
- **live-tune.md**: corrected. The mismatch dialog's Ignore button is disabled for Live Updates (`SMv7/SMv7/TCarDlgs.cpp:246-250` with `bIgnoreEnabled=false`), and the button texts now come from `Core/SysMonLib/SysMonLib.rc:60-75`. The permission is named **Permit live updates** (`Core/SysMonDocs/SysMonDocs.rc:272`). Added:
  - the conditions that disable Live Updates (`SMv7/SMv7/TSysMonFrameEcu.cpp:1701-1745`)
  - the non-live-tuneable check (`SysMonApp.rc:1510`)
  - the Upload / Download / Cancel dialog shown when the data differs (`SysMonLib.rc:80-94`, `TCarDlgs.cpp:300-335`)
  - a new PNG
- **live-auto-tune.md**: verified that the feature is still present (`SysMonApp.rc:832,851`). Save Auto Tune Adjustment was corrected: it applies the adjustment to the active map value and resets it, and does not "update the data version in the ECU" (`SysMonApp.rc:2253`, `TSysMonFrameEcu.cpp:2821-2885`). Added:
  - Alt+F3 and the enabling conditions (`TSysMonFrameEcu.cpp:1787-1825`)
  - automatic On Line and Live Updates (`:655-665`)
  - Pot Board Enable being disabled during Live Auto Tune (`SMv7/SMv7/TSysMonFramePot.cpp:720`)
  - the boot and link-lost messages (`SysMonApp.rc:1489-1492`)
  - the "Live AutoTune File" name (`Core/SysMonProgram/SysMonProgram.rc:193`)
- **changing-parameter-values/index.md**: corrected **Edit > Restore Value (F2)**, which restores the value saved on disk (`SysMonApp.rc:794,1300`, `SysMonViews.rc:1397`).
- **breakpoint-monotony.md**: added the exact message text (`Core/SysMonBaseViews/SysMonBaseViews.rc:389-390`).
- **breakpoint-warning.md**: added the OK and Cancel buttons and the exact check box label (`SysMonViews.rc:206-215`).
- **value-limit-warning.md**: verified against `SysMonViews.rc:104-130` and reformatted.
- **changing-breakpoint-values-by-mouse.md**, **changing-parameter-values-by-keyboard.md**, **changing-parameter-values-by-mouse.md**, **parameter-edit-mode.md**: cleaned up only.
- **graphical-maps/index.md**: menu names are Graphical, Difference and End, plus the Slice X / Slice Y buttons and Alt+G (`SysMonViews.rc:1098-1113,1411-1419`).
- **breakpoint-spacing.md**: "Even" corrected to **Constant spacing** (`SysMonViews.rc:1413-1415`).
- **rotating-a-graphical-view.md**: the four buttons are rotate clockwise / anti-clockwise in 10° steps plus tilt forwards / backwards (`SysMonViews.rc:1100-1103`, `Core/SysMonLib/TPlotMapOpenGL.cpp:1885-1898`).
- **zooming-a-graphical-view.md**: 50% zoom verified (`Core/SysMonLib/TOpenGL.cpp:124`).
- **changing-values-in-a-graphical-view.md**: fixed the truncated sentence.
- **difference-view.md**, **end-view.md**, **slice-view.md**, **graphical-view-1-axis.md**, **graphical-view-2-axis.md**: converted from layout tables and given the AutoZoom note (`SysMonViews.rc:1259-1262`).
- **adjustment-board-configuration.md**: rewritten.
  - The command opens the **Pot Board Configuration window** (a Scalar view in pot-board mode), not a dialog (`SMv7/SMv7/TSysMonFrame.cpp:1499`, `SMv7/SMv7/TSysMonFrameViews.cpp:2156`, `SysMonViews.rc:1212`).
  - The window has 8 rows (4 pots × 2 switches) and Step/Min/Max/Pot/Switch columns (`Core/SysMonParams/inc/TStaticPtrs.h:43-45`, `SysMonViews.rc:1213-1217`, `TScalarViewDefn.cpp:833-885`).
  - Only live-tuneable scalars can be assigned (`Core/SysMonViews/TScalarView.cpp:2407`).
  - The full context menu is listed (`SysMonViews.rc:941-957`).
  - Settings live in a `.pbc` file in the `PotBoard` folder (`SysMonApp.rc:1624`, `Core/SysMonProject/SysMonProject.rc:771`).
  - Removed the `<none>` label for empty rows.
- **adjustment-board-control.md**: rewritten.
  - Removed the `Pot.ini` file, the "Adjustment Board Groups" dialog and group selection, because both dialogs are never opened (no callers of `CTAdjustmentGroupsDlg` or `CTPotConfigDlg`).
  - Enable now describes going on-line and switching on live updates automatically, and its enabling conditions (`TSysMonFramePot.cpp:694-722`).
  - Reset Adjustments restores values to disk and only works in Live Updates (`:300-350,524-545`).
  - Adjustments need On-Line (`:230`).
  - The Adjustment Parameters `.ini` file and the Adjustment tab are kept (`Core/SysMonProgram/TSourceDesc.cpp:206`, `Core/SysMonParamDlgs/TParamPropSheet.cpp:418-437`).
- **adjustment-board-keyboard-operation.md**: added Ctrl(+Shift)+5–8 for switch position 2 (`SysMonApp.rc:1215-1240`).
- **pot-board-properties.md**: the COM list shows ports COM1–COM20 that exist on the PC, not just COM1/COM2 (`Core/SysMonViews/TViewPropPagePotBoard.cpp:144-165`). The dialog is opened from the Pot Board window (`SysMonViews.rc:148-157`).

## ECU Control

- **index.md**: rewritten as a linked feature list, with menu locations.
- **cursor-control-and-trace.md**: added Show Trace as Block. Behaviour checked against `TSysMonFrameEcu.cpp:1850-1905`.
- **ecu-on-line.md**: corrected the menu item to **On Line (F3)** (`SysMonApp.rc:830`). The program-version check only runs when **Warn if Program Versions do not match** = Y, and that setting defaults to N (`Core/SysMonCore/TAdvOptions.cpp:98`, `TSysMonFrameEcu.cpp:1644-1662`). The dialog also offers Sync SM to Unit and Force Complete Reprogram (`SMv7/SMv7/TCar.cpp:620-669`). Added that you cannot go off-line during Live Auto Tune, plus a new PNG.
- **kill-engine.md**: corrected.
  - The BIOS constant is checked first.
  - If more than one application defines it, nothing is sent.
  - If none defines it, or the controller is disabled, nothing is sent. The "default to AC on TAG-300" claim was removed (`Core/EcuApi/TEcu.cpp:1492-1498,1549-1585`).
  - The command is 0x1A with a 2 s kill (`Core/SysMonCore/inc/SmCmds.h:211`).
  - The texts are Engine Disabled (red) and Engine Enabled (yellow) (`SMv7/SMv7/TPauseDlg.cpp`).
- **selecting-applications.md**: corrected.
  - ECU Properties does not use app selection (`TSysMonFrameEcu.cpp:1392`).
  - The single-app dialog only appears when more than one app qualifies (`TSysMonFrame.cpp:1249-1285`).
  - Upload Sensor Sets was removed, since only Reprogram, Force Complete and Program Spare use the dialog.
  - Added Select All / Deselect All, Merge Program Sequence, the disabled-app rules, "- Invalid PUL" and "(!)" (`Core/SysMonProject/SysMonProject.rc:253-263`, `Core/SysMonProject/TAppSelectionDlg.cpp:167-266`).
- **setting-time-and-date.md**: corrected **Set ECU from current PC** and added F12, Close and the clock-controller filter (`Core/SysMonEcu/SysMonEcu.rc:88-107`, `TSysMonFrameEcu.cpp:2786-2807`). New PNG.
- **single-message.md**: status texts corrected to Response Back OK / Response Timeout / No Comms / ECU error text (`Core/SysMonDevFunc/SysMonDevFunc.rc:275-276`, `Core/SysMonDevFunc/TSingleMsgDlg.cpp:320-362`). Added ranges and defaults (`:44,457-463`), Alt+M, and the Numeric Grid mode (`:503-518`). New PNG.
- **unit-status.md**: Orange removed; Red now covers live tunes (`SMv7/SMv7/TUnitStatusCtrl.cpp:947`). Added:
  - Hide Unused
  - the real row names (`:442-482`)
  - Project cells turning red on a BIOS mismatch (`:1320-1341`)
  - the `(L<n>)` lock marker (`:774-778`)
  - Blue meaning "config could not be read" (`:1060-1087`)
  - Ctrl+U
  - the Tools > Sync commands (`SysMonApp.rc:1036-1039`)
  - a new PNG
- **data-changes-in-the-ecu/index.md**: filled in the empty "Live Tune Off" bullet.
- **downloading-data-to-the-ecu.md**: corrected. Ignore is disabled (`TCarDlgs.cpp:246-250`). Added the data-differs dialog, the non-live-tuneable check, F7 and the offline-during-download behaviour (`TSysMonFrameEcu.cpp:2140-2150`). New PNG.
- **reset-rom.md**: rewritten, not obsolete. There is no "Reset Data to ROM" item. The function is now **Undo Data Changes in Unit & Edit Buffer** (`ID_SM_ECU_RESETDATATOECU`, `SysMonApp.rc:842`). It does **not** reprogram: it checks that ROM matches the saved file, copies ROM to RAM, then resets the Edit Buffer (`SMv7/SMv7/TCarEcu.cpp:965-1040`, message `SysMonApp.rc:1486-1487`).
- **undo-data-changes.md**: corrected the names ("in Unit", "in Unit & Edit Buffer", "in Edit Buffer"; `SysMonApp.rc:841-843`). Added the availability rules (`TSysMonFrame.cpp:1684-1697`, `TSysMonFrameEcu.cpp:1241-1285`).
- **uploading-data-from-the-ecu.md**: added Alt+F7, the note that the matching program and data versions are opened first (`TCarEcu.cpp:1392-1393`), and offline-during-upload.
- **ecu-memory/index.md**: RAM-change list now shows the current menu names.
- **copy-rom-to-ram.md**: corrected the label to **Undo Data Changes in Unit** (`SysMonApp.rc:841,2182`). Added the availability rules (`TSysMonFrameEcu.cpp:1241-1260`, `TCarEcu.cpp:896-940`).
- **force-complete-reprogram.md**: added Alt+C, ECU read-only mode, and Reprogram All (`TSysMonFrameEcu.cpp:1975-2040`).
- **min-max-statistics.md**: the permission is **Permit delete errors**, which covers DELERRORS_MINMAX (`Core/SysMonDocs/TAdvCustBaseGrid.cpp:213-215`, `TCarEcu.cpp:77-95`). Added F11.
- **run-from-ram.md**, **run-from-rom.md**: added the lock requirement for all active apps (`TSysMonFrameEcu.cpp:2297-2370`).
- **read-ram.md**: added the Locked status (`Core/SysMonDevFunc/TReadRamView.cpp:327-331`), Alt+R and floating-point format. Branding updated to Motion Applied.
- **read-ram-properties-general.md**: added the address format `hhhh:hhhh` (`Core/SysMonDevFunc/TRamPropertyPage.cpp:447-487`, `SysMonDevFunc.rc:278`), exact labels and the `.rrl` filter (`:715-718`).
- **reprogramming-the-ecu.md**: fixed the check box label to **Merge Program Sequence** and the permission to **Permit reprogramming**. Added Alt+P, Live Updates and on-line being suspended during reprogramming, the in-boot prompt, and the Reprogram All confirmation (`TSysMonFrameEcu.cpp:1975-2120`). Fixed the broken headings.
- **ecu-properties/index.md**: tabs confirmed as Controllers and Devices; the Licence page is commented out (`Core/SysMonEcu/TEcuPropertySheet.cpp:68-72`).
- **ecu-properties-controllers.md**: converted and given a new PNG.
- **ecu-properties-devices.md**: corrected: *aaaaa* is the comms path name (`Core/SysMonEcu/TEcuPpg.cpp:299`). Address is the IP or the link type (`:181-215`). Added "(not connected)". New PNG.
- **ecu-search/index.md**: dialog title is "Ecu Search" (`SysMonApp.rc:1908`). App selection only appears with more than one app (`TSysMonFrameEcu.cpp:1456-1467`).
- **ecu-search-data-version.md**: added the Consortium, Owner and RDA fields (`SysMonProject.rc:210-214`). New PNG.
- **ecu-search-program-version.md**: added the Properties list examples and the not-found text. New PNG.

## OBSOLETE topics

None. Reset ROM describes an existing function under a new menu name and has been rewritten.

## Needs SME

1. **Adjustment groups**: the "Adjustment Groups" and "Potentiometer Configuration" dialogs are unreachable (no callers), so there is no way to choose an ECU adjustment group. Pots assigned only through the Adjustment Parameters `.ini` file (`TSysMonFramePot.cpp:101-122`) therefore never act. Confirm that the `.pbc` window is the only supported workflow. `hardware/adjustment-board.md` probably needs the same fix.
2. **Adjustment Board hardware**: the CA-Card / serial VE-80/VE-81 hardware is still selectable in the UI, but confirm it is still supported.
3. **Upload Data**: "You are prompted to save the Edit Buffer as a new Data Version" has been kept from the CHM but was not traced in code.
4. **Read RAM**: the "word boundary" start address is not enforced by the property page, and the meaning of "Addressing size" is unclear. The CHM wording was kept.
