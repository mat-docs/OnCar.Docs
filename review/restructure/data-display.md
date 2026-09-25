# Restructure review: data-display (+ _orphans)

Source root: `ATLAS9/ATLASSM/Main/`. Abbreviations: `APP` = `SMv7/SMv7/SysMonApp.rc`, `VRC` = `Core/SysMonViews/SysMonViews.rc`, `BRC` = `Core/SysMonBaseViews/SysMonBaseViews.rc`, `V/` = `Core/SysMonViews/`.
All pages: CHM artefacts removed (layout tables, `image\` alt text, `<br>` soup), definition lists turned into tables, headings and See also lines tidied. Newer PNGs from the old site were copied into each `assets/` folder where they match. Strict build: no warnings.

## Pages

- **data-display/index.md**: Converted the list to a table and added the Desktop > Window route (APP:1094-1118). Branding changed to Motion Applied.
- **numeric.md**: Added the menu path and shortcut (APP:1104). Added the value formats (incl. Raw Decimal) and the Limit warning 1/2 colours (`Core/SysMonBaseViews/TViewPropPageDisplay.cpp:707-721`). Added the locked-parameter symbol and dash (`V/TMeasureViewDefn.cpp:635-637,689-693`) and the System Menu items (VRC:597-617). Confirmed that a parameter that is not logged shows a dash (`Core/SysMonParams/SysMonParams.rc:91`).
- **big-number.md**: Corrected the text to say both the Name and Description columns are hidden (`V/TMeasureView.cpp:471-485`). Added a note that Desktop > Window > Big Number is always greyed, because it has no command handler (APP:1103; there is no ON_COMMAND for `ID_WINDOW_NEW_BIGNUMBER` in `SMv7/SMv7/TSysMonFrame.cpp`).
- **bar-graph.md**:
  - Corrected the "not logged" text to a dash (`V/TBarGraphView.cpp:453-460`, SysMonParams.rc:91).
  - Corrected the colour names to Bar / Limit warning 1 / Limit warning 2. The Normal default is the system inactive-border colour, not "grey" (TViewPropPageDisplay.cpp:687-690, `inc/TViewDefn.h:53,61,64`).
  - Corrected the Max/Min and warning-limit text positions and colours (TBarGraphView.cpp:660-742).
  - Added the Extras tab Orientation (BRC:145-155), Fill Window (VRC:984, TBarGraphView.cpp:398-420) and the Hex/Binary value formats (VRC:980-982).
- **bar-graph-selecting-parameters.md**: Added the other context-menu items (VRC:996-1007).
- **bar-graph-display-limits.md**: Confirmed that the defaults are the Engineering (Phys) limits (`V/TBarGraphParamHolder.cpp:88-89`) and the dialog caption (VRC:1447).
- **oscilloscope.md**: Added the menu path and shortcut (APP:1106).
- **oscilloscope-extras.md**:
  - Corrected the labels to "Display parameter information" and "Band clearing" (VRC:372-389).
  - Confirmed the defaults grid/param/band = on and all-y = off (`V/TOscViewDefn.cpp:85-93`, `V/TOscillViewPropPage.cpp:137`), and timebase 10 s (TOscViewDefn.cpp:52).
  - Added the timebase range of 5-60 s (TOscillViewPropPage.cpp:16, `Core/SysMonParams/inc/TMeasParam.h:34`).
- **oscilloscope-parameter-info.md**: Corrected "not logged" to a dash (`V/TOscilloscopeView.cpp:262-265`, SysMonParams.rc:91). Added the error symbol and the context-menu items (VRC:960-972).
- **oscilloscope-plot-area.md**: Corrected the Trace type/Trace colour labels (`Core/SysMonParamDlgs/SysMonParamDlgs.rc:177-181`).
- **oscilloscope-selecting-parameters.md**: Wording only.
- **oscilloscope-trace-limits.md**: Corrected the default limits from "Warning Limits (Window Properties Display tab)" to the Engineering limits in the Conversion tab (`V/TOscilloscopeTrace.cpp:109-111`). Confirmed the dialog (VRC:83-94).
- **oscilloscope-types-of-trace.md**: Confirmed that Linear is the default (`Core/SysMonParams/TMeasParam.cpp:4082`). Tip turned into an admonition.
- **system-menu-oscilloscope.md**: Converted to a table and confirmed the items (VRC:906-920). Reworded the All Y-Axis default (see SME).
- **grid.md**: Branding changed. Added Slider/Button/Status/Action Button cells and Import/Export plus Grid from Import (VRC:837-903, APP:1118). Corrected that editable parameters are edited with Edit Mode off (`V/TNumericGridView.cpp:3220-3230`).
- **grid-window-edit-mode.md**: Added the Toggle Edit Mode route and the behaviour when Edit Mode is off: the header is hidden and right-click opens Parameter properties (TNumericGridView.cpp:2031-2052, 253-290).
- **system-menu-grid.md**: Added Import/Export (VRC:837-850, TNumericGridView.cpp:4106-4152).
- **creating-a-grid-window.md**: Corrected the panel labels and added the default of 10x10 (VRC:278-291, `V/inc/TNumericGridViewDefn.h:47`). Added the shortcut and Grid from Import.
- **selecting-cells.md**: Added that Action Button needs a single cell (TNumericGridView.cpp:3770-3782).
- **cell-properties.md**: Added a full Grid Cell Context Menu table, including Data Format, Action Button and Auto Generate (VRC:855-903, TNumericGridView.cpp:1818-1896).
- **cell-properties-contents.md**:
  - Corrected the Format list. It adds Decimal, Slider, Button and Status (`V/TNumGridCellPropPage.cpp:869-927`, VRC:1299-1339). The default is Name, not Engineering (TNumGridCellPropPage.cpp:393-398).
  - Trend/Error/Status apply to Measurement parameters only, and Slider/Button to unlocked Scalars (Slider excludes text conversions) (`V/TConfigurableNumericGridCell.cpp:1305-1339`).
  - Mask is enabled for Engineering on non-float Measurement parameters (TNumGridCellPropPage.cpp:816-833).
  - Added the Status mode options (VRC:1122-1133, TConfigurableNumericGridCell.cpp:436-490), and Action Buttons Single Message/Run Script (VRC:424-440, `V/TActionRunScript.cpp:61-133`).
  - Removed the incorrect "colours set in the Parameter Properties Display tab" (colours come from the window Limit warning colours).
- **cell-properties-formatting.md**: Corrected the labels Left/Center/Right and the border checkboxes (VRC:337-356).
- **insert-columns-rows.md**: Added Before/After. Corrected placement to "relative to the current cell" (VRC:293-313, TNumericGridView.cpp:1638-1662).
- **delete-columns-rows.md**: Corrected that deletion uses the current cell (TNumericGridView.cpp:1766-1807). Confirmed the labels (VRC:315-335).
- **other-displays/index.md**: Converted to a table; no content change.
- **errors/index.md**: Wording only.
- **error-display.md**:
  - Corrected the colour logic: only Current, unacknowledged errors use the Unacknowledged Errors colour (`V/TErrorViewDefn.cpp:1169-1176`). The Foreground default is the system text colour.
  - Added that Acknowledge needs an active Error Window (`SMv7/SMv7/TSysMonFrameEcu.cpp:2494-2525`), the F8 shortcut (APP:846), and the title count format (`V/TErrorView.cpp:355-357`). Also confirmed restore-on-new-error (TErrorView.cpp:338-347) and pinned by default (TErrorViewDefn.cpp:98).
- **error-mask.md**: Converted to lists and replaced the screenshot with the PNG. The Mask tab was confirmed (VRC:96-102).
- **deleting-errors.md**:
  - Corrected the permission to the "Permit delete errors" Customer Base setting (`Core/SysMonDocs/TAdvCustBaseGrid.cpp:213-215`, `Core/SysMonDocs/SysMonDocs.rc:270`), which is shared with Delete Min/Max.
  - Added the conditions: comms needed, and not available in ECU read-only mode (TSysMonFrameEcu.cpp:2400-2404, `Core/SysMonCore/TAdvOptions.cpp:177`); per-controller flag (`Core/EcuApi/TEcuDataAcquisition.cpp:112`); acknowledgements cleared (TSysMonFrameEcu.cpp:2424-2460).
- **events/index.md**: Added the Count column (`V/TEventViewDefn.cpp:1415-1421`), Summary Mode (VRC:825, `V/TEventView.cpp:508-580`), and the Masked/Trimmed title counts (TEventView.cpp:425-450). Confirmed the 2000-event limit (`Core/SysMonParams/inc/TEcuEventList.h:71`).
- **event-log.md**: Corrected `\work\Ev_username.log` to `Ev_<username>.txt` in the log folder (Help > View Log Folder), with an optional `_<project>` suffix (`Core/SysMonDocs/TDocument.cpp:160-188`, VRC:1282-1285, `Core/SysMonCore/TLogFile.cpp:198-231`, APP:1451, APP:1158). Removed the "default file name Ev_.log" text.
- **event-mask.md**: Added the Mask/Unmask Debug button and the Mask Unknown checkbox (VRC:358-370, `V/TEventViewPropPage.cpp:341-531`). Corrected "Errors" to "Events".
- **event-priority.md**: Added Debug priority (`Core/SysMonParams/inc/TEcuEvent.h:139-145`, TEventViewDefn.cpp:1241-1257).
- **system-menu-events.md**: Added Mask Unknown Events, Summary and Normal/Large Font (VRC:817-834). Corrected the ECU menu name to "Clear Events" (F9) (APP:849).
- **alarms/index.md**: Wording only; added links.
- **alarm-setup.md**: Corrected the dialog name "Alarm Setup" to **Alarms**. Added the Close/Export/Import/Merge buttons (APP:63-76; `SMv7/SMv7/TAlarmsDlg.cpp:370-530`) and the locked-parameter hiding (TAlarmsDlg.cpp:313-317, 385).
- **alarm-properties.md**: Wording only.
- **alarm-properties-trigger.md**: Added the Parameter... button (screenshot/`CTFunctionPage`). The screenshot was replaced with the PNG.
- **alarm-properties-action.md**: Corrected Test (it plays, and stops only for a custom file) and the "Default" bullet formatting (`SMv7/SMv7/TAlarmActionPage.cpp:305-325`). Added the validation rules (TAlarmActionPage.cpp:150-190) and the defaults Repeat on, Duration 1, Reset 0 (`Core/SysMonDesktop/TAlarm.cpp:68-82`).
- **alarm-display.md**: Added the shortcut (APP:1112). Confirmed the columns (`V/TAlarmView.cpp:188-195`) and the pinned default (`V/TAlarmViewDefn.cpp:92`).
- **_orphans/dial-display.md**: Rewritten from source, adding creation, the single parameter limit, the Dial tab (VRC:402-422) with defaults (`V/TDialViewDefn.cpp:40-45,250-261`), and needle/limit colours (`V/TDialView.cpp:145-299`, TViewPropPageDisplay.cpp:691-694).
- **_orphans/signal-sampling-display.md**: Corrected "Selected Parameter Only" to **Sample Selected Only** (VRC:1041). Added the shortcuts (VRC:1026,1040-1041; APP:924) and the averaging/offset behaviour: 1 s window, offset = average - reference (`V/TSignalSamplingView.cpp:362-420`, `Core/SysMonParams/TInputParam.cpp:475-494`). The enable condition is On Line plus at least one parameter (TSignalSamplingView.cpp:1340-1352).
- **_orphans/pop-up-channel-properties-and-configuration.md**: Removed "eight channels" because the count comes from unit constants (see DOCS-REVIEW). Fixed the button label to "Parameters..." (`Core/SysMonDAQ/SysMonDAQ.rc:302`).
- **_orphans/popup-remote-logging-config-controls.md**: Fixed the broken anchor from `#Controls` to `#controls` and the title case.

Counts: 44 pages done; about 45 corrections, 3 removals, about 40 additions.

## OBSOLETE topics

None. Note: **Big Number** as a menu command is dead, because `ID_WINDOW_NEW_BIGNUMBER` has no handler. The topic stays valid because the display is still created through the Parameter Explorer.

## Placement of orphans (no files moved)

- **Dial Gauge** and **Signal Sampling** are live, first-class Desktop > Window displays (APP:1108, 1114). They sit in the same menu group as Numeric/Bar/Oscilloscope/Grid and are already listed in the Data Display index. They should be nav entries in the Data Display section.
- The two remote-logging pop-ups are pointer stubs to the Remote Logging page. They can stay out of nav.

## Needs SME

1. Oscilloscope System Menu **All Y-Axis**: the check mark is set from `GetSelParamAxis()`, the inverse of the Extras "Display all y-axis" (`V/TOscilloscopeView.cpp:2556` vs `TOscillViewPropPage.cpp:137`). The menu probably shows ticked when only the selected axes are shown. Is this a bug? The docs avoid stating its tick state.
2. Signal Sampling: the claim "download the logging configuration after sampling / ECU bar shows the difference" is kept from the CHM. The code writes the offset to a scalar "sample" parameter (TInputParam.cpp:488), so a data download may be what is needed.
3. Big Number menu item is permanently greyed. Should it be removed from the product menu, or should the docs just keep the note?
