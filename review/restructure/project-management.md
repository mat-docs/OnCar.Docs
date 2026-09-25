# Restructure report: project-management (62 pages)

Source paths are relative to `ATLAS9/ATLASSM/Main/`. All pages: CHM artefacts removed (`i_white_sm.jpg` bullets, "See dialog box>" headings, `image\` alt text, layout tables, `<br>` soup); label/description tables rebuilt with headers; procedures renumbered; "See also" lines fixed. Strict build: no warnings from this folder.

## Per page

- **index.md** - image swapped to old-site `project-illustration.png`; "a new Data Version is created" -> "can be saved".
- **applications.md** - added File-menu application commands (Active Application Alt+A, Application Read Only, Hide Application, Hide Row Data, Add/Remove Application) (`SMv7/SMv7/SysMonApp.rc:749-755`, strings `:2151,2186-2189`).
- **active-application.md** - corrected precondition: only Live Updates off (and no wireless comms) is required, not Off-Line (`SMv7/SMv7/TSysMonFrame.cpp:2390`); Alt+A behaviour confirmed (`TSysMonFrame.cpp:2492-2553`).
- **asap-compatibility.md** - removed "third-party ASAP1b driver" claim: ASAP1b driver was merged into EcuApi in 2001 and no external driver loading exists (`Core/EcuApi/TDeviceFactory.cpp:564`, `Core/SysMonCore/inc/Asap1bDriverDefs.h`); drivers listed as built in. ASAP2: TAG2ASAP conversion utility confirmed installed (`OCSInstall/.../Product.wxs:295-298,447`). Removed "McLaren Applied is an active member of the ASAP2 working group" (unverifiable, misplaced, wrong brand).
- **customer-bases/index.md** - added note that Customer Bases are unused when Unit.Def enabled.
- **customer-bases/multi-application-base.md** - list columns corrected (Multi-Application Base / Customer Base / Base Directory; PPO is not a column) (`Core/SysMonDocs/TMultiAsapBaseSelectDlg.cpp:158-216`); Select Base shortcut Ctrl+S and "Close Project & Select Base" added (`SysMonApp.rc:663,780`); duplicate-name behaviour corrected to "asked whether to overwrite" (`TMultiAsapBaseSelectDlg.cpp:740-757`); Free User base cannot be removed (`:702`).
- **customer-bases/free-user.md** - Free User base non-removable added.
- **customer-bases/adding-and-editing-customer-bases.md** - added **Browse** (fills name/ASAP project/base dir from a .pgv) (`Core/SysMonDocs/TNewCustBaseDlg.cpp:429-472`); validation rules (no `\`, absolute path, not A:/B:) (`:210-300`); "must be sub-directory" softened to "should" (not enforced).
- **customer-bases/customer-base-advanced-settings.md** - rebuilt as table with Item/Setting grid; all 10 items and defaults confirmed (`Core/SysMonDocs/TAdvCustBaseGrid.cpp:199-265`, `inc/TCustomerBase.h:104,134`; labels `SysMonDocs.rc:269-282`); "OxC3" typo fixed.
- **customer-bases/adding-and-editing-multi-application-bases.md** - added **Prime Param Override file** field + Browse (`SysMonDocs.rc:92-108`); PPO description moved here from the multi-base page; setting name corrected to "Enforce Prime Parameter requirements (Y/N)" (`SysMonApp.rc:1542-1543`).
- **unit-def-management/introduction.md** - setting needs restart (`Core/SysMonCore/TAdvOptions.cpp:192`); menu changes (Manage Unit.Def Files Ctrl+S, Open submenu) (`SMv7/SMv7/TSysMonFrame.cpp:456-497`).
- **unit-def-management/file-management.md** - dialog/columns named (Unit Definition File Editor; Application/Folder/Is Master/Enabled; Option/Setting) (`SysMonApp.rc:356-383`, `TUnitDefAppCtrl.cpp:373-388`, `TUnitDefOptionCtrl.cpp:359-368`); added full options table with defaults (`Core/SysMonDocs/TUnitDef.cpp:21-22`); save prompt on OK/folder change and Auto Configure confirmation (`SMv7/SMv7/TUnitDefEditDlg.cpp:153-248`).
- **unit-def-management/pgv-creation.md** - "through the API" corrected to File > New with "Select project BASE location for new PGV." folder dialog (`SMv7/SMv7/TProjectFns.cpp:262-285`).
- **unit-def-management/project-import.md** - confirmed (`Core/SysMonProject/TFileExportDlg.cpp:1360-1400`); wording cleaned.
- **unit-def-management/project-management.md** - added "Creating a project" (folder prompt, auto-configure, Project Build Selection dialog) (`Core/SysMonProject/TProject.cpp:2870-2915`, `SysMonProject.rc:399-411`); 10 recent projects confirmed (`Core/SysMonRes/inc/SysMonCommonRes.h:3426-3435`).
- **program-and-data-versions/index.md** - links added; wording.
- **program-and-data-versions/creating-a-program-version.md** - newer PNG; file labels corrected (ASAP2 File ... Live AutoTune File) (`Core/SysMonProgram/TSourceDesc.cpp:188-216,681-694`, `SysMonProgram.rc:190-213`); added close-project confirmation, Unit.Def folder prompt, Notes auto-filled from ASAP, retry on failure (`TProjectFns.cpp:235-330`, `Core/SysMonProject/TProgramPropPage.cpp:1560-1590`).
- **program-and-data-versions/creating-a-program-version-command-line.md** - rewritten from `SMv7/SMv7/TSysMonCmdLineInfo.cpp` (read in full): exe `SystemMonitorU.exe` (`SMv7.vcxproj:315`, `Product.wxs:105`); **removed /prm** (returns false -> falls to Generic, `:323-329,481-486`) and **/encrypt** (commented out `:488-492`; encryption always on `:75`, applied `TSystemMonitor.cpp:2800-2805`); **added /adjust, /auto, /description, /copydir** (`:317-347`, used `TSystemMonitor.cpp:2826,2847-2854`); /customer precedence over /location (`TSystemMonitor.cpp:2745-2790`); Free User behaviour; return codes corrected: 2 is never returned, invalid/unknown flag or missing file -> 1 (`TSystemMonitor.cpp:149-154,1010-1041`).
- **projects/index.md** - wording; Unit.Def note.
- **projects/opening-a-project.md** - setting label "Open most recently used project (Y/N)" (`SysMonApp.rc:2417`); prompt is Yes/No/Cancel, Cancel = no unit, no-unit warning, gated by "Prompt for unit connection on opening project (Y/N)" (default Y) (`Core/SysMonProject/TProject.cpp:4177-4230`, `TAdvOptions.cpp:167`).
- **projects/closing-a-project.md** - added Close Project & Select Base and Cancel button (`SysMonProject.rc:307-316`).
- **projects/creating-a-project/stage-1-define-project.md** - **wizard order corrected**: Project -> Desktop -> Program Version(s) -> Virtual Parameters -> CAN Config -> Remote Logging Config; Connections shown after Finish (`Core/SysMonProject/TProjectPropSheet.cpp:129-240`, `TProject.cpp:2948,3101`); no-Customer-Base error (`TProject.cpp:2920-2935`); Unit.Def folder prompt.
- **projects/creating-a-project/stage-2-connections.md** - corrected position in flow (opens after Finish, only if prompt setting Y); **added PCAN-USB** (`Core/SysMonEcu/SysMonEcu.rc:73`), Network Adapter (ANY/adapter) and CAN Baud Rate 1M/500k/250k/125k (`TEcuConnectionsPpg.cpp:292-318,334-398`); unit/server options IP-only; screenshot kept with note.
- **projects/creating-a-project/stage-3-define-a-desktop.md** - "follows Connections" corrected to "follows Project page".
- **projects/creating-a-project/stage-4-program-version.md** - Finish is not on the last Program Version page; added Virtual Parameters / CAN Config / Remote Logging Config pages and their create/open behaviour (`TProject.cpp:3040-3075`, `TSelectOrCreateDocPropPage.cpp:145-170`); all apps made active.
- **projects/creating-a-project/car-definition.md** - file location setting "File for unit ip addresses" (`SysMonApp.rc:1611`); opened via Edit (Spare) Unit Definitions (`SysMonEcu.rc:80,83`); dialog labels (`Core/SysMonLib/SysMonLib.rc:95-113`).
- **projects/creating-a-project/spare-car.md** - availability requires IP link + spare defined (`SMv7/SMv7/TSysMonFrameSpareCar.cpp:108-117`); checkbox "Merge Program Sequence", Select All/Deselect All (`SysMonProject.rc:253-265`); component list and result messages (`TSysMonFrameSpareCar.cpp:230-320`, `SysMonApp.rc:1512-1515,1744-1749`); Sync Spare Unit to SM added.
- **projects/properties/index.md** - ECU > Connections added (`SysMonApp.rc:874`).
- **projects/properties/connections.md** - PCAN-USB; reinit behaviour on change (`SMv7/SMv7/TSystemMonitor.cpp:4726-4760`).
- **projects/properties/project-properties.md** - menu path corrected to File > Properties > Project (`SysMonApp.rc:743`); tab names corrected and **CAN Config tab added** (`TProjectPropSheet.cpp:243-312`; titles = doc type names `SysMonApp.rc:1584-1629`).
- **projects/properties/application-properties/index.md** - tab titles prefixed with app name.
- **...-data-version-tab.md / ...-program-version-tab.md** - cleanup only.
- **...-memory-layout.md** - columns Contents/Controllers/Address/Size added (`SysMonProject.rc:891-894`).
- **...-unlock-list-management.md** - **Team drop-down removed** (no longer in dialog); added Lock DTV, Owner, Edit Comment, Details list (Member/Details), messages (`SysMonProject.rc:331-365`, `Core/SysMonProject/TUnlockListPropPage.cpp:185-280`).
- **developing-data-versions/index.md** - backup naming corrected (`<dtv name><username>.dvb`, not always `000`) (`Core/SysMonDocs/TDocument.cpp:820-905`); settings "Directory for backup files" and "Disable DTV backup (Y/N)" named (`SysMonApp.rc:1610,1452`).
- **developing-data-versions/using-data-version-files.md** - nnn = highest existing + 1, hex (`Core/SysMonLib/TFileUtils.cpp:79-106`); button label DataWizard.
- **developing-data-versions/export-to-matlab.md** - **menu path corrected** to Tools > Matlab Export > (All Parameters / Selected Parameters Only / Selected Application Parameters Only / Parameter Selection / Application Differences Only / Export without versioning) > Definition and Data / Data Only (`SysMonApp.rc:970-1027`); default name `V<dtv name>.m` (`SMv7/SMv7/TSysMonFrameMatLab.cpp:148-154`); **removed "no import facility is necessary"** and added Tools > Matlab Import (Ctrl+Q) (`SysMonApp.rc:1029`, `TSysMonFrameMatLab.cpp:371-455`); licence restriction note (`:185`).
- **developing-data-versions/importing-hex-files.md** - corrected: import overwrites the Edit Buffer per active app (does not create a DV until saved), ECU taken offline, incomplete-hex warning (`SMv7/SMv7/TSystemMonitor.cpp:5130-5189`).
- **data-wizard/index.md** - added Open Any Data Version, parameter sets, Compare with ECU / Save As Data Version, Print Setup (`SysMonApp.rc:1049-1091,2318`).
- **data-wizard/compare-merge-tool.md** - Memory/Unlock List rows; value list corrected (`Core/DataWizViews/TDataMageDlgBar.cpp:565-586`, `DataWizViews.rc:149-175`).
- **data-wizard/compare-merge-tool-features.md** - "Dvt2" typo; parameter-list context menu added (`DataWizViews.rc` IDR_SM_DATAMAGE_PARAM_CONTEXT_MENU).
- **data-wizard/map-compare-window.md** - "System Menu" -> window context menu; Compare Grid added (`Core/SysMonViews/SysMonViews.rc` 1/2-axis grid context menus).
- **data-wizard/map-compare-window-features.md** - context menu items corrected to Copy Dtv1 / Copy Dtv1 to Memory / Copy Memory / Copy Dtv2 / Copy Dtv2 to Memory (`SysMonViews.rc` IDR_TMAPPARAM_CONTEXT_MENU); display options listed; MIN/MAX naming corrected to `<pgv file name>MIN.dtv/MAX.dtv` (`Core/SysMonProgram/TEmbeddedProgram.cpp:332-346,4159-4160`).
- **data-wizard/data-wizard-candidate-version.md** - Open Any Data Version added.
- **data-wizard/data-wizard-report-view.md** - cleanup; first-symbol wording.
- **data-wizard/data-wizard-parameter-masking.md** - mask list from `SysMonApp.rc:1067-1077`; **added Locked**, filled in Different Sensor Calibration; defaults corrected (all except Equal/Sensor Cal on; `Core/SysMonParams/inc/Equate.h:47-53`); Report View availability incl. Sensor Calibration (`Core/DataWizViews/TDataWizView.cpp:311-330`); Axis Different Units row fixed (was copy of Conversion).
- **data-wizard/data-wizard-selecting-parameters.md** - parameter sets added.
- **data-wizard/data-wizard-compare.md** - Compare All description aligned with status text (`SysMonApp.rc:2309-2310`).
- **data-wizard/data-wizard-merge.md** - Resolve dialog options and check labels from `DataWizViews.rc:70-112`.
- **data-wizard/data-wizard-view-parameter.md** - remaining context menu items added (`DataWizViews.rc:210-288`).
- **data-wizard/data-wizard-window-menu.md** - added Different Sensor Calibration, Locked, parameter sets, Save As Data Version; removed wrong shortcut text.
- **files/index.md** - "TAG customer support team" removed.
- **files/creating-new-files.md** - list corrected to document type names; **Pot Board Config added** (`TSystemMonitor.cpp:1600-1945` UpdateTemplates, `SysMonApp.rc:1584-1629`).
- **files/opening-files.md** - Pot Board Config added; info fields; button labels DataWizard/Merge.
- **files/saving-files.md** - "Disable Team Security" -> Team Security list "Disabled" + Disable RDA (`SysMonProject.rc:87-110`, `TFileSaveAsDlg.cpp:231-324`); shortcuts; auto-increment setting (`SysMonApp.rc:1425`).
- **files/file-type-selection.md** - Document list label.
- **files/exporting-files.md** - ".pgv" corrected to project ".prj" includes sub-documents (`TFileExportDlg.cpp:1230-1245`); Select/Deselect All; Ctrl+T.
- **files/importing-files.md** - dialog title "Import File into Customer Base"; added Intelligent Import, Skip duplicate files (both default on), Import and Open, target base drop-down, overwrite and path prompts (`SysMonProject.rc:27-38,165-194,318-329`, `TFileExportDlg.cpp:90-91,665-677`).
- **files/types-of-files/ecu-files.md** - **removed Sensor PRM file** from Program Version inputs (not in source desc; set in Advanced Settings "File for sensor calibration") (`TSourceDesc.cpp:681-694`, `TSysMonCmdLineInfo.cpp:323-329`); removed "TBC".
- **files/types-of-files/program-and-data-version-files.md** - cleanup.
- **files/types-of-files/project-files.md** - tables rebuilt; \PotBoard\ added; LogCfgs also holds XIC and CAN configs (`Core/SysMonProject/TProject3.cpp:315-345`, `SysMonProject.rc:763-777`).

## OBSOLETE topics

None.

## Needs SME

1. Command-line PGVs are always encrypted (`m_bEncryptPGV(true)`); comment says "encrypt by default ... consortium licences". Confirm intended and whether /encrypt should be restored.
2. Return code 1 for invalid command lines comes from a licence check on the bad option (`TSystemMonitor.cpp:1030-1040`); code 2 is dead. Confirm documented codes.
3. ASAP1b: confirm no third-party ASAP1b driver support remains (claim removed).
4. MATLAB "Parameter Selection" vs "Selected Parameters Only" and "Application Differences Only" - wording inferred from handlers; SME to confirm user-facing meaning.
5. Customer Base "Hex files with missing areas valid ... recommended for TAGtronic systems" - kept from CHM, ambiguous.
6. Screenshots `Project_Properties_Connections.jpg` (no PCAN-USB) and several GIFs are old; recapture desirable.
