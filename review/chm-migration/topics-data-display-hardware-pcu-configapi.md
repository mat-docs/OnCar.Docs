# CHM migration check — Batch C (Data Display, PCU Dashboard Configuration, Configuration API, Hardware)

Docs root: `C:\MclDev\SystemMonitor.Site\docs\` (paths below relative to it). Display pages are in `user-guide/using-sm/display/`.

| # | CHM topic (TOC path) | file | verdict | docs page(s) | what's missing / notes |
|---|---|---|---|---|---|
| 1 | Data Display > Data Display | Data_Display.htm | MIGRATED | user-guide/using-sm/display/index.md | All display types listed (Dial Gauge has no page of its own in either). |
| 2 | Numeric Display > Numeric | Numeric.htm | MIGRATED | display/numeric.md | Minor: meaning of the three status icons (higher / lower / error) not spelled out, only "indicates value change or error". |
| 3 | Numeric Display > Big Number | Big_Number.htm | MIGRATED | display/numeric.md#big-number-display | |
| 4 | Bar Graph Display > Bar Graph | Bar_Graph.htm | MIGRATED | display/bar.md | Minor: CHM says an un-logged value shows "not logged"; docs say a dash (might be a source-verified correction). Doesn't say warning limits come from the Parameter Properties Display tab. |
| 5 | Bar Graph > Selecting Parameters | Bar_Graph_Selecting_Parameters.htm | MIGRATED | display/bar.md | |
| 6 | Bar Graph > Display Limits | Bar_Graph_Display_Limits.htm | PARTIAL | display/bar.md | Missing: defaults are the parameter's Upper/Lower Engineering Limits (Conversion tab). Dialog screenshot missing. |
| 7 | Oscilloscope > Oscilloscope | Oscilloscope.htm | MIGRATED | display/oscilloscope.md | |
| 8 | Oscilloscope > Plot Area | Oscilloscope_Plot_Area.htm | PARTIAL | display/oscilloscope.md | Missing: note that traces only appear once the ECU is On Line; trace colour/type set per parameter in Parameter Properties Display tab; plot width auto-sizes. |
| 9 | Oscilloscope > Parameter Info | Oscilloscope_Parameter_Info.htm | MIGRATED | display/oscilloscope.md | Minor: "not logged" value text, Y-axis follows selection. |
| 10 | Oscilloscope > System Menu - Oscilloscope | System_Menu_Oscilloscope.htm | PARTIAL | display/oscilloscope.md | Options are described as features, but not as System Menu items (Background Grid, All Y-Axis, Parameter Info, Band Clearing). Defaults (on/off/on/on) missing. |
| 11 | Oscilloscope > Selecting Parameters | Oscilloscope_Selecting_Parameters.htm | MIGRATED | display/oscilloscope.md | Docs wrap it in odd "Desktop > Window > Properties / Parameters tab" steps. The CHM describes selecting in the Parameter Info box. Worth a wording check. |
| 12 | Oscilloscope > Extras | Oscilloscope_Extras.htm | PARTIAL | display/oscilloscope.md | Missing: Extras tab option names and defaults. Missing: Timing panel default Timebase of 10 s. |
| 13 | Oscilloscope > Types of Trace | Oscilloscope_Types_of_Trace.htm | MIGRATED | display/oscilloscope.md | Minor: tip to use a Virtual Parameter to make a logical output; Logical trace shows name/value to the right. Linear is the default. |
| 14 | Oscilloscope > Trace Limits | Oscilloscope_Trace_Limits.htm | PARTIAL | display/oscilloscope.md | Missing: default limits are the Warning Limits. |
| 15 | Grid Display > Grid | Grid.htm | MIGRATED | display/grid.md | Minor: how to set the Edit Params highlight colour (Display tab), and that support teams supply Desktop files with custom grids. |
| 16 | Grid > Grid Window Edit Mode | Grid_Window_Edit_Mode.htm | MIGRATED | display/grid.md | |
| 17 | Grid > System Menu - Grid | System_Menu_Grid.htm | PARTIAL | display/grid.md | Missing: System Menu items **Toggle Gridlines** and **Toggle Edit Mode**. Docs only mention the Properties-dialog route. |
| 18 | Grid > Creating a Grid Window | Creating_a_Grid_Window.htm | PARTIAL | display/grid.md | Missing: note that deleting rows/columns with entries loses them. Missing: rows/columns can be changed later or inserted via the context menu. |
| 19 | Grid > Selecting Cells | Selecting_Cells.htm | PARTIAL | display/grid.md | Missing: click-and-drag rectangle selection (ESC if text is highlighted). Missing: context-menu commands apply to all selected cells except Cell Properties, which applies only to the top-left cell. |
| 20 | Grid > Cell Properties | Cell_Properties.htm | MIGRATED | display/grid.md | |
| 21 | Grid > Cell Properties - Contents | Cell_Properties_Contents.htm | PARTIAL | display/grid.md | Missing: the Format attribute list (Name, Units, Raw Value (hex), Engineering (default), Binary, Description, Trend, Error). Trend and Error are not available for editable params. Missing: the Select and Properties buttons. Missing: Mask detail (enabled only for Engineering; hex mask overrides the default bit mask; text-conversion highlighting). Missing: Empty = DELETE key. |
| 22 | Grid > Cell Properties - Formatting | Cell_Properties_Formatting.htm | MIGRATED | display/grid.md | Minor notes missing: Trend/Error symbols are always left-justified; borders persist when gridlines are off. |
| 23 | Grid > Insert Columns/Rows | Insert_Columns_Rows.htm | PARTIAL | display/grid.md | Only one line in the docs. Missing: Table Size panel is read-only; Insert panel (rows vs columns, count); Placement panel is relative to the top-left selected cell. Dialog screenshot missing. |
| 24 | Grid > Delete Columns/Rows | Delete_Columns_Rows.htm | PARTIAL | display/grid.md | Only one line in the docs. Missing: extra rows/columns are deleted right/below; the max keeps at least one row and one column; delete rows/cols uses only the top-left cell; Delete Cell Contents applies to all selected cells. Screenshot missing. |
| 25 | Other Displays > Other Displays | Other_Displays.htm | MIGRATED | display/*, developer-functions/index.md, ecu-control/ecu-memory.md (Read RAM) | Landing page. All four displays are covered somewhere. |
| 26 | Errors > Error | Error.htm | MIGRATED | display/error.md | Minor: explanation of the Current→Logged transition and removal when bits clear is condensed ("persist until deleted"). |
| 27 | Errors > Error Display | Error_Display.htm | PARTIAL | display/error.md | Missing: error count shown in brackets in the title bar; colours (Unacknowledged default red, Logged = Foreground default black) set in the Display tab. |
| 28 | Errors > Error Mask | Error_Mask.htm | MIGRATED | display/error.md | Minor: greyed group check box = mixed; keyboard operation (+/-/arrows/Space) missing. |
| 29 | Errors > Deleting Errors | Deleting_Errors.htm | PARTIAL | display/error.md | Missing: Delete Errors needs Customer Base permission (Customer Base Advanced Settings) and applies only to Active Applications. |
| 30 | Events > Event | Event.htm | MIGRATED | display/event.md | Minor: event count in title-bar brackets; window auto-scrolls. |
| 31 | Events > Event Log | Event_Log.htm | MIGRATED | display/event.md | Docs give `Ev_<username>.txt` in the log folder, while CHM gives `\work\Ev_username.log`. The docs look source-corrected. Missing: "Save Events As" is also on the ECU menu; files are ASCII. |
| 32 | Events > System Menu - Events | System_Menu_Events.htm | MIGRATED | display/event.md | |
| 33 | Events > Event Priority | Event_Priority.htm | MIGRATED | display/event.md | Icon images (red/blue/green) not shown. |
| 34 | Events > Event Mask | Event_Mask.htm | MIGRATED | display/event.md | Minor: Mask/Unmask Low/Med/High/All buttons toggle; keyboard operation missing. |
| 35 | Alarms > Alarms | Alarms.htm | MIGRATED | display/alarms.md | |
| 36 | Alarms > Alarm Setup | Alarm_Setup.htm | MIGRATED | display/alarms.md | |
| 37 | Alarms > Alarm Properties | Alarm_Properties.htm | MIGRATED | display/alarms.md | |
| 38 | Alarms > Alarm Properties - Trigger | Alarm_Properties_Trigger.htm | MIGRATED | display/alarms.md | |
| 39 | Alarms > Alarm Properties - Action | Alarm_Properties_Action.htm | MIGRATED | display/alarms.md | Minor: Default sound = Windows "Exclamation" system sound (Control Panel > Sounds). |
| 40 | Alarms > Alarm Display | Alarm_Display.htm | MIGRATED | display/alarms.md | |
| 41 | PCU Dashboard Configuration > PCU-400 Display Unit | PCU-400_Display_Unit.htm | MISSING | — | No PCU/Dashboard content anywhere in docs (grep "PCU", "Dashboard" = 0 hits). Covers the unit: TFT, 15 shift LEDs, 2 alarm LEDs, 2 push switches, CAN to TAG-400, config downloaded over Ethernet. |
| 42 | PCU > Requirements | Requirements.htm | MISSING | — | The Dashboard menu item is enabled only when a loaded PGV is for PCU. Tuning is not possible in the PCU app. |
| 43 | PCU > PCU Dashboard Config Window | PCU_Dashboard_Config_Window.htm | MISSING | — | Desktop > Window > Dashboard; one per page; drag parameters from Parameter Explorer; controls, pages, grid, copy/paste, shift lights, actions, import/export. |
| 44 | PCU > Import and Export the config | Import_and_Export_the_config.htm | MISSING | — | .pcu (whole config) and .ppc (single page) import/export. |
| 45 | PCU > Dash Configuration Main menu | PCU_Dashboard_menu.htm | MISSING | — | Download Config, Export/Import Config, Export Current Page/Import Page, Copy/Paste, Undo Last Move/Resize, Appears on Every Page, Dash Properties. |
| 46 | PCU > PCU Context Menus | PCU_Context_Menu.htm | MISSING | — | Context menus: nothing selected, control selected (control type, Snap to Grid, Properties) and page bar (Add/Delete/Rename/Move page). |
| 47 | PCU > PCU Dash Properties | PCU_Dashboard_Properties.htm | MISSING | — | Four tabs overview. |
| 48 | PCU > Dash Properties - Display tab | PCU_Dash_Props_-_Display.htm | MISSING | — | Title, Show Title Bar, Appears on every page, Colours, Font, Update Rate. |
| 49 | PCU > Dash Properties - Shift Lights tab | PCU_DashProps_-_Shift_Lights.htm | MISSING | — | Gear/RPM parameter, Target Gear RPM for gears 1–7, per-LED Shift Light Deltas. |
| 50 | PCU > Dash Properties - Actions tab | PCU_DashProps_-__Actions.htm | MISSING | — | Actions list and PCU Action dialog (primary Lo/Hi threshold, inside/outside, secondary condition, action, number/percentage). |
| 51 | PCU > Actions | Actions.htm | MISSING | — | Action types: Page, LED (0/1), Pg Up, Pg Down, Backlight Dim, Shiftlight Dim, Flash all LEDs. |
| 52 | PCU > Dash Properties - Layout tab | PCU_DashProps_-_Layout.htm | MISSING | — | Display Guide Grid, grid size, grid colour. |
| 53 | PCU > Control Types > Numeric Control | Numeric_Display.htm | MISSING | — | General tab (common to all controls: parameter, low-pass filter cut-off, colours, font), Display tab and Limits tab. |
| 54 | PCU > Control Types > Bar Graph Control | Bar_Graph_Control.htm | MISSING | — | Display and Limits tabs. |
| 55 | PCU > Control Types > Rev Bar Control | Rev_Bar_Control.htm | MISSING | — | Rev-bar levels, Display and Limits tabs. |
| 56 | PCU > Control Types > Dial Control | Dash_Control_-_Dial.htm | MISSING | — | Dial Display tab. |
| 57 | PCU > Control Types > LED Control | LED_Control.htm | MISSING | — | LED Display tab. |
| 58 | PCU > Control Types > Static Labels | Static_Labels.htm | MISSING | — | Text-only controls. |
| 59 | PCU > Size and Move Display Controls | PCU_Sizing_and_Moving_Display_Controls..htm | MISSING | — | Drag handles and move. |
| 60 | PCU > Create a PCU Dashboard Config | Create_a_PCU_Dashboard_Config.htm | MISSING | — | End-to-end procedure. |
| 61 | PCU > Assign Actions to push buttons | Assign_Actions_to_push_buttons.htm | MISSING | — | Mapping the unit's push switches to Pg Up/Pg Down and similar actions. |
| 62 | Configuration API > Configuration API | Configuration_API.htm | PARTIAL | developer-resources/configuration_api/index.md | Present: gRPC/protobuf, NuGet and protos, GitHub sample, caching. Missing: API is OFF by default; it starts and stops with SM when enabled; the status bar shows address/port/status. |
| 63 | Configuration API > Configuration API Setup | Configuration_API_Setup.htm | MISSING | — | "Configuration API Setup" dialog is not documented. Missing: Enable checkbox, listen address/port, log level (Information logs every call with timing), cache refresh (0 disables), Reset to defaults, SM restart needed after changes. Source (SysMonApp.rc) also has Tools-menu **Configuration API Start / Stop / Reset** items, which aren't documented either. |
| 64 | Hardware > PC System Requirements | PC_System_Requirements.htm | MIGRATED | user-guide/getting-started/index.md | Table present. |
| 65 | Hardware > Communication Architecture | Communication_Architecture.htm | MISSING | — | CA-125/126 card vs Ethernet TCP/IP; one app session per device per CA-card port; multiple apps over TCP/IP; only one CA-card per PC. Diagram missing. POSSIBLY OBSOLETE (CA-card era). |
| 66 | Hardware > Communication Architecture - Layers | Communication_Architecture_-_Layers.htm | MISSING | — | Layer model: Application / API / ASAP1b / Protocol / PC drivers / device / physical link / hardware. POSSIBLY OBSOLETE (conceptual; CCP "not supported"). |
| 67 | Hardware > Communication Adaptor (CA-Card) | Communication_Adaptor_CA_Card_.htm | MISSING | (getting-started mentions CA-card as licence device; ecu-communication.md mentions HDLC via CA-Card/PCMCIA) | CA-125 spec: PCMCIA Type III, licence dongle, 4 Mbit/s HDLC / 750 kbit/s async, CA-125T (LEMO) and CA-125M (44-way D), Adjustment Board interface. POSSIBLY OBSOLETE (PCMCIA hardware). |
| 68 | Hardware > Changing the PCMCIA card slot for the CA card | Changing_the_PCMCIA_card_slot_for_the_CA_card.htm | MISSING | — | Registry procedure: `HKLM\SYSTEM\CurrentControlSet\Services\Ca125\Ca1250\Parameters\CaPcmciaSlotNumber` = 1. POSSIBLY OBSOLETE (PCMCIA). |
| 69 | Hardware > Sensor Bus | Sensor_Bus.htm | PARTIAL | user-guide/data-acquisition/sensors/external.md | TAG Sensor Bus / DATALab are mentioned and configured. Missing: overview (DLU/ECU gathers data from SN-6/SN-32; TAG-300/MCU-300/MCU-300DA have 3 looms). DATALab system diagram missing. |
| 70 | Hardware > Sensor Node SN-6 | Sensor_Node_SN_6.htm | MISSING | (external.md only names SN-6 as a node type) | Missing: SIC table (Resistive bridge, 5V/pot, Hall, Inductive, LVDT, Pt1000, Thermocouple, Active Filter, Sample & Hold; inputs and sensor type). Missing: up to 6 SICs; Resistive Bridge only in slots 1–4; up to 4 SN-6s daisy-chained per loom. |
| 71 | Hardware > Sensor Node SN-32 | Sensor_Node_SN_32.htm | MISSING | (external.md only names SN-32) | Missing: SN-32 vs SN-32LT input-configuration table; one SN-32 per loom. |
| 72 | Hardware > CAN Link | CAN_Link.htm | MIGRATED | user-guide/hardware/index.md#can-link | |
| 73 | Hardware > Adjustment Board | Adjustment_Board.htm | MIGRATED | user-guide/hardware/index.md#adjustment-board | Full VE-80/VE-81 content present. |

## PCU feature status in shipped SM (source check, `C:\MclDev\ATLAS9\ATLASSM\Main`)

- `Core\SysMonCore\inc\OcsNetBuild.h:80` defines `FUNC_PCU` for every non-LDS, non-ATLAS build, so it is **on in System Monitor builds**.
- `SMv7\SMv7\SysMonApp.rc:1116` is the shipped SM resource. It has `Desktop > Window > &Dashboard\tAlt+Shift+D` (`ID_WINDOW_NEW_DASHBOARD`, initially GRAYED).
- `TSysMonFrame.cpp:2113-2116` wires the command under `#ifdef FUNC_PCU`.
- `TSysMonFrameViews.cpp:2384` enables the item only when the main car's ECU symbol string contains `PCU400`, no page lock is active, and no PCU view is open yet. This matches the CHM "Requirements" topic.
- `SMv7\SMv7\PCUApp.rc` is a separate resource set branded "PCU Application Tool". It is `ExcludedFromBuild` for the SM Debug/Release Unicode configs, so it's a separate product variant, not part of shipped SM.
- `Core\SysMonPCU` is in `SM.sln`, and `TCarPcu.cpp` / `TSysMonFramePcu.cpp` compile into SMv7.
- **Conclusion:** the PCU Dashboard feature is still compiled into shipped SM, but it's gated to PCU-400 projects. Its absence from the docs is a real gap, though niche (it depends on whether PCU-400 is still a supported product).
