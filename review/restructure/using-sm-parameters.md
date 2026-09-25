# using-sm-parameters – restructure report

Scope: `docs/using-system-monitor/parameters/` (45 pages). Source root: `C:\MclDev\ATLAS9\ATLASSM\Main\` (abbreviated below: `PD` = `Core/SysMonParamDlgs`, `APP` = `SMv7/SMv7/SysMonApp.rc`). Strict build clean for these pages.

## Per page

- **index.md** – cleaned definition layout. No factual change.
- **editable-parameters.md** – cleaned. No factual change.
- **measurement-parameters.md** – added External Inputs as a source (`Core/SysMonParamDlgs/TParamPropSheet.cpp:293`).
- **names-descriptions-and-groups.md** – table layout; added View menu shortcuts Names CTRL+ALT+N / Descriptions CTRL+ALT+D / Groups CTRL+ALT+G, Group Descriptions Only (`APP:802-806`); Edit > New Group CTRL+SHIFT+G, Rename, Delete (`APP:796-799`); Parameter Group Properties dialog (`PD/SysMonParamDlgs.rc:184-196`). Removed claim that Identifier is never displayed.
- **parameter-explorer.md** – added ALT+0 (`APP:802`), Display Unlocked/Locked/All (`PD/SysMonParamDlgs.rc:814-816`), Expand/Collapse All (`:818-819`), “Default Explorer display to collapsed view” setting (`APP:1442`). Removed “process diagrams” claim (not verifiable).
- **moving-parameter-explorer.md** – layout table removed; ALT+0 added. Explorer still a dockable SECDialogBar (`PD/TParamBrowser.cpp:280`).
- **parameter-symbols.md** – proper table, alt text.
- **locked-parameters/about-the-parameter-unlock-list.md** – corrected PUL section names to `[Ecu]`, `[Scalar]`, `[1AxisMap]`… (`Core/SysMonProgram/TUnlockListDoc.cpp:582-600`); added “Use Encrypted Parameter Unlock List Files (Y/N)” default N (`Core/SysMonCore/TAdvOptions.cpp:196`, `APP:1431`); restructured.
- **locked-parameters/edit-the-parameter-unlock-list.md** – rebuilt broken procedure; tab is “*App* Unlock List Management” (`Core/SysMonProject/TUnlockListPropPage.cpp:105`); controls Lock DTV, “...”, New..., Edit, Edit Comment, Details list (Member/Details) (`Core/SysMonProject/SysMonProject.rc:331-348`, `TUnlockListPropPage.cpp:254-255`); Select PUL Members / Unlock to ALL members (`SysMonProject.rc:390-397`); Unlock List Details fields (`:350-363`). Added PUL_New.gif (Save As for New...).
- **locked-parameters/locked-parameters.md** – fixed broken list; added Display Locked/Unlocked options.
- **parameter-properties/index.md** – corrected tab table and order; added Live Auto Tune row (General + Live Auto Tune only); removed Sensor tab statement (`PD/TParamPropSheet.cpp:209-339, 359-459`); locked params cannot open (`:120`).
- **general-tab.md** – added Application field (`PD/SysMonParamDlgs.rc:93-94`), data type/byte order values (`:1298-1320`); corrected: Virtual Parameter Identifier is editable (`PD/TParamPropPageGeneral.cpp:524-537`).
- **measurement-tab.md** – added Bit shift + None/Left/Right (`PD/SysMonParamDlgs.rc:145-147, 1261-1270`); refresh-rate units incl. angle units (`PD/TParamPropPageMeasurement.cpp:734-867`); label “ASAP1b Interface Data”.
- **editable-tab.md** – filled empty Controller description; labels per `PD/SysMonParamDlgs.rc:198-216`.
- **1-axis-map-tab.md** – corrected: breakpoint threshold edits are not saved (`PD/TParamPropPage1Axis.cpp:181-182`, setter commented out `SysMonParams/inc/T1AxisMapParam.h:124`); Index parameter disabled when none (`:380-382`).
- **2-axis-map-tab.md** – same correction (`PD/TParamPropPage2Axis.cpp:281,291`).
- **array-tab.md / string-tab.md / adjustment-tab.md** – layout only; labels verified (`PD/SysMonParamDlgs.rc:310-335, 531-541`).
- **virtual-tab.md** – added expression-required/syntax check (`PD/SysMonParamDlgs.rc:1359`, `PD/TFunctionPage.cpp:381-424`).
- **conversion-tab.md** – corrected Units editability (only Virtual/CAN/External Inputs; virtual units are a per-parameter override) (`PD/TParamPropPageConversion.cpp:489-505, 660-672`); removed unverified shared-conversion warning; Select always enabled for virtuals (`:467-479`); Live Value/Zero/Value Offset visibility (Zero Offset Sampling Time default 5000, Enable Parameter Offset, online only) (`:431-433, 515-537`, `TAdvOptions.cpp:126,175`); zero-offset confirmation (`:1144`); Conversion dialog filter/columns (`PD/SysMonParamDlgs.rc:362-377`, `PD/TConversionCtrl.cpp:732-738`); added Clear All Display Offsets On Page ALT+SHIFT+D and ALT+SHIFT+Z (`APP:1135-1136`); “Format override” is not axis-only.
- **display-tab.md** – corrected: trace type options Linear (default)/Digital/Logical (`PD/TParamPropPageDisplay.cpp:237-239`); default trace colour from 12-colour palette, not black (`SysMonParams/TMeasParam.cpp:658-686`); ECU params stored in Desktop and read only without a Desktop; virtuals stored in VP file (`PD/TParamPropPageDisplay.cpp:561-584`); removed duplicated paragraph.
- **live-auto-tune-tab.md** – corrected Correction Type values to Multiply/Add/Percent/Replace (`PD/SysMonParamDlgs.rc:1382-1385`, `PD/TParamPropPageLiveAutoTune.cpp:286`); added X/Y/Z Axis tolerances (`PD/SysMonParamDlgs.rc:621-627`).
- **number-formats.md** – corrected: format must start with `%`, leading/trailing text rejected (`SysMonParams/TParam.cpp:3243-3285`); flags `- + 0 space #`, codes, `l`/`I64` modifiers (`:100-107`); added `%qIP` / `%qLId` (`:3313-3325`, `SysMonCore/TStringUtils.cpp:1053-1060`); integer codes truncate, leading spaces trimmed (`TStringUtils.cpp:1284-1340`).
- **mathematical-operators.md** – corrected: multiply is `*`, `%` is modulus not percentage (`PD/TFunctionPage.cpp:52,83-84`, `SysMonParams/bc.y:282-283`), parentheses `( )` not `[ ]`, asin/acos descriptions were swapped; Raw inserts `$$` prefix (`PD/TFunctionPage.cpp:32-33, 334-344`); Inv/Hyp mutually exclusive (`:280-307`); added min/max buttons (`:86-88`, `Core/SysMonFDL/SysMonFDL.rc:108,113`); NoLog = slow row (`SysMonParams/Tbuiltins.cpp:541`).
- **selecting-a-colour.md** – layout/procedure cleaned (standard CColorDialog, `SysMonLib/TColourBtn.cpp:187`).
- **axis-properties/index.md** – unchanged facts (`PD/TAxisPropSheet.cpp:198-200`).
- **axis-properties-general.md** – table; Read Only is display-only (`PD/TAxisPropPageGeneral.cpp:277`); Monotony values (`PD/SysMonParamDlgs.rc:1374-1381`).
- **axis-properties-conversion.md** – corrected: Lower/Upper read only and Properties disabled for a fixed axis (`PD/TAxisPropPageConversion.cpp:316-321`); filled broken “by Keyboard” link.
- **conversions/conversion-properties.md** – corrected: Type is fixed, not set from the Conversion tab; “Used by...” is a button; Format string is not axis-only (`PD/SysMonParamDlgs.rc:379-399`); four types Rational/Table/Text/Free (`PD/TConvPropSheet.cpp:166-196`).
- **conversions/rational-conversion.md** – added formula layout (`PD/SysMonParamDlgs.rc:421-438`); added Gain/Offset... dialog (Gain (Eng/Volt), Offset (Eng)) (`:439, 630-641`); Reference dialog fields (`:514-529`); default VP conversion (`SMv7/SMv7/TSysMonFrameEdit.cpp:138`).
- **conversions/formula-conversion.md** – corrected direction: Formula = raw→eng, Inverse = eng→raw (`Core/SysMonFDL/TFreeConv.cpp:533-608`); added: Formula/Inverse edits are not saved (`PD/TConvPageFree.cpp:162-166`, `TFreeConv.cpp:330-341`); X1 placeholder (`SysMonCore/inc/Asap2Consts.h:50`).
- **conversions/table-conversion.md** – added distinction Table (numeric, Interpolate between values) vs Text (default entry) (`PD/SysMonParamDlgs.rc:443-490`); duplicate-value message (`:1317`).
- **selecting-parameters/multiple-parameter-selection-window-properties.md** – added Raw decimal; per-window format lists and Bar/Oscilloscope name lists (`Core/SysMonViews/TViewPropPageGeneral.cpp:570-640`); corrected “Raw binary only Scalar/Numeric”.
- **single-parameter-selection-window-properties.md** – added Raw decimal, compare-view restriction (`Core/SysMonViews/TViewPropPageSGeneral.cpp:285-330`).
- **parameter-filter.md** – added quoted exact Name match (`PD/TParamNode.cpp:284-286`, `PD/TParamTreeCtrl.cpp:792`), auto-complete of previous filters (`PD/TParamFilterAutoComplete.cpp:292-316`); 5-entry drop-down confirmed (`PD/TComboBoxCtrl.cpp:65`); corrected “Name or Description” to the displayed label (`PD/TParamNode.cpp:277-291`).
- **selecting-a-single-parameter.md** – cleaned; also used by formula editor Parameter... (`PD/TFunctionPage.cpp:328`).
- **selecting-multiple-parameters.md** – added Recents list (loads, replaces) and second Filter on selected list (`PD/SysMonParamDlgs.rc:44-51`, `PD/inc/TMultiParamSelectionDlg.h:1874-1886`); button labels Add >> / << Remove / Param Sets; also used for PUL edit.
- **selecting-parameters-to-edit-or-display.md** – cleaned only.
- **virtual-parameters/index.md** – added type name “Virtual Measurement” (`Core/SysMonParams/SysMonParams.rc:78`).
- **virtual-parameters/creating-a-virtual-parameter.md** – corrected: Identifier is editable (see General tab); properties open automatically at Virtual tab (`SMv7/SMv7/TSysMonFrameEdit.cpp:760-765`); added CTRL+SHIFT+V (`APP:796`); VPARAM_n = next unused number (`SysMonParams/TVirtualParamsDesc.cpp:103-115`).
- **virtual-parameters/virtual-parameter-files.md** – added “Default Virtual Parameter format to XML (Y/N)” default Y, restart (`TAdvOptions.cpp:187`, `APP:1450`); `\Virtuals` default (`Core/SysMonDocs/TUnitDef.cpp:31`); `.vpx;*.vpm` (`APP:1621,1630`).
- **virtual-parameters/virtual-parameters-import-export.md** – added procedures, menu names, default file name, warning log (`PD/SysMonParamDlgs.rc:1164-1165`, `SMv7/SMv7/TSysMonFrameViews.cpp:3491-3630`).
- **virtual-parameters/virtual-parameters-xml-file-schema.md** – schema rewritten from writer code: added Header Description/Notes, `FreeFunction`, `Units`/`Default` optional on all conversions, `Properties` BitMask/ReadOnlyFlags, `Display` MaxRefresh/TraceType/BitShift/ShiftDirection/DisplayOffset/ArraySize/ChannelId/BlockOffset; Name/Identifier/DataType/Conversion/Expression made optional; fixed invalid attribute-before-sequence on `Data`; ConvRules now `xs:choice` (sorted by name) (`SysMonCore/inc/TXMLUtils.h:16-119`, `SysMonDocs/TDocument.cpp:1094-1150`, `SysMonCore/TAppSet.cpp:672-700`, `SysMonParams/TParamsDesc.cpp:982-1060`, `TParam.cpp:1251-1400`, `TMeasParam.cpp:1186-1328`, `SysMonFDL/TVirtualParam.cpp:1539-1560`, `TConv.cpp:844-880`, `TRationalConv.cpp:645-700`, `TTableConv.cpp:726-765`, `TTextConv.cpp:672-700`, `SysMonFDL/TFreeConv.cpp:39,435-460`); added element summary table with value formats.
- **parameter-properties/sensor-tab.md** – left unchanged (OBSOLETE, below).

## OBSOLETE topics

- **parameter-properties/sensor-tab.md** (Parameter Properties – Sensor tab). No Sensor tab is ever added to the Parameter Properties dialog: `DefineActivePages()` adds no page for `OB_TYPE_TSB` / `OB_TYPE_INPUT` (`Core/SysMonParamDlgs/TParamPropSheet.cpp:283-297`), `AddPages()` has no sensor page (`:359-459`), and dialog `IDD_PARAM_PROP_TSB` (“Sensor Details”, `SysMonParamDlgs.rc:337`) is not referenced by any class (only `SysMonRes/inc/SysMonCommonRes.h:726`).

## Needs SME

1. Breakpoint threshold (1-/2-axis tabs): value can no longer be changed; confirm whether the 0–50% triangle/box Live Tune behaviour still applies.
2. Formula conversion: SM shows but does not save Formula/Inverse edits — confirm this is intended rather than a defect.
3. Number formats: the dialog validator rejects text before/after `%` (CHM allowed it); confirm ASAP-supplied formats with text still display as before.
4. Storage of user New Groups: CHM says Desktop file; a `.ugl` “User Groups and Limits” document also exists (`APP:1622`).
5. Virtual XML `FreeFunction` writes formula and inverse as two `Expression` elements — confirm reader handles this.
