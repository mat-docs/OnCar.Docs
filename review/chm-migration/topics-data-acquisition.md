# CHM migration check — Batch D (Data Acquisition, 52 topics)

Docs root: `C:\MclDev\SystemMonitor.Site\docs\user-guide\data-acquisition\` (paths below relative to it).

| # | CHM topic (TOC path) | file | verdict | docs page(s) | what's missing / notes |
|---|---|---|---|---|---|
| 1 | Data Acquisition > Data Acquisition | Data_Acquisition.htm | MIGRATED | index.md | Logging/Sensors categories present. |
| 2 | Logging > Logging | Logging.htm | MIGRATED | logging/index.md, index.md | Live/Remote/Burst summary present. |
| 3 | Logging > Logging Memory Allocation | Logging_Memory_Allocation.htm | PARTIAL | logging/index.md (Memory Allocation) | Burst vs DATALab memory present. Missing: hardware table (TAG-300/MCU-300 distributed units, TAG 3.8 family uses Burst memory, DLU uses DATALab memory) and the sentence that SM recognises unit type from Program Version and only enables the matching config tools / applies hardware restrictions; memory diagram (Logging_Memory_wmf.gif). POSSIBLY OBSOLETE: TAG 3.8 / DLU are legacy hardware. |
| 4 | Logging > Session Details | Session_Details.htm | MIGRATED | logging/logging-config.md (Session Details) | Near-verbatim; Session_details.gif screenshot not carried. |
| 5 | Logging > Channels | Channels.htm | MIGRATED | logging/logging-config.md (Channels) | "Row data" renamed "Raw data"; all 5 channel types present. |
| 6 | Logging > Logging Configuration Files | Logging_Configuration_Files.htm | MIGRATED | logging/logging-config.md | Verbatim. |
| 7 | Live Logging > Live Logging | Live_Logging.htm | PARTIAL | logging/live-logging.md | Purposes, slow-row note, menu path present. Missing notes: if Logging > Live Configuration is unavailable, create a new Live Logging Configuration file; menu item greyed out / config not available while ECU On-Line; configuration becomes active as soon as the dialog is closed; title bar shows config file name; short 3-tab overview (tabs themselves are documented). |
| 8 | Live Logging > Session tab | Live_Logging_Session_Sheet.htm | MIGRATED | logging/live-logging.md (Session Tab); logging-config.md (Session Details) | Docs more current (Session Location, Name/Date-Time increment). Notes and Comments > Edit button covered in Session Details section. |
| 9 | Live Logging > Trigger Timing tab | Live_Logging_Trigger_Timing_Sheet.htm | MIGRATED | logging/live-logging.md (Trigger Timing Tab) | "Pre and Post" mode omitted — correctly: source has it commented out (SysMonDAQ/TLiveDATriggerPage.cpp `//ON_BN_CLICKED(IDC_PREANDPOST...)`). |
| 10 | Live Logging > Trigger Condition tab | Live_Logging_Trigger_Condition_Sheet.htm | MIGRATED | logging/live-logging.md | — |
| 11 | Live Logging > Automatic Recording | Live_Logging_Automatic_Recording.htm | MIGRATED | logging/live-logging.md | Steps 1–5 + stop methods present. |
| 12 | Remote Logging > Remote Logging | Remote_Logging.htm | PARTIAL | logging/remote-logging.md | Missing note: if Logging > Remote Configuration is disabled a new Remote Logging Configuration file must be created; feature only available if the Customer Base has permission (Customer Base Advanced Settings); dialog resizable, title bar shows file name. (Burst and External Inputs pages have the equivalent note; Remote does not.) |
| 13 | Remote Logging > Configure dialog > Channel Overview tab | Remote_Logging_Channel_Overview_Sheet.htm | MIGRATED | logging/remote-logging.md | Screenshot present. |
| 14 | Remote Logging > Configure dialog > Driver push button panel | Driver_push_button_panel.htm | MIGRATED | logging/remote-logging.md | — |
| 15 | Remote Logging > Configure dialog > Logging duration and rate | Logging_duration_and_rate.htm | MIGRATED | logging/remote-logging.md | — |
| 16 | Remote Logging > Configure dialog > Channel Properties and Configuration | Channel_Properties_and_Configuration.htm | PARTIAL | logging/remote-logging.md | Grid columns, context menu, controls present. Missing: Set Uniform Frequency dialog details — valid frequencies (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000 Hz), keyboard selection (up/down; press 1/2/5 to cycle 1-10-100-1000 / 2-20-200 / 5-50-500 Hz), OK applies frequency including to disabled cells; Set_Uniform_Frequency.gif. Also lost cross-ref for red-cell max refresh rate (Parameter Properties > Measurement tab). Side note: CHM topic 5 (and docs Channels section) says 4 DATALab channels while this page says 8 — pre-existing inconsistency carried into docs. |
| 17 | Remote Logging > Duration | Remote_Logging_Duration.htm | MIGRATED | logging/remote-logging.md | — |
| 18 | Remote Logging > Channel Trigger | Remote_Logging_Channel_Trigger.htm | MIGRATED | logging/remote-logging.md | Docs updated vs CHM (External Trigger replaces Driver push button; extra operators; negative value only on Start). |
| 19 | Remote Logging > Arrange Channels | Arrange_Channels.htm | MIGRATED | logging/remote-logging.md | — |
| 20 | Remote Logging > Synchro Pattern | Synchro_Pattern.htm | MIGRATED | logging/remote-logging.md | — |
| 21 | Burst Logging > Burst Logging | Burst_Logging.htm | MIGRATED | logging/burst-logging.md | — |
| 22 | Burst Logging > Parameters tab | Burst_Logging_Parameters_Sheet.htm | PARTIAL | logging/burst-logging.md (Parameters) | Missing: Set Interval dialog procedure (select from Interval drop-down; intervals double from the lowest available value up to 16384 ms; click OK) — docs only list its "features"; "Other Features" (Filter text box, SHIFT/CTRL multi-select, DELETE removes selected parameters); the "Parameters" control-button entry; overview of the 4 tab areas. Screenshots Burst_Block_Select.gif, Burst_Block_Assign.gif, Burst_Log_Interval.gif not carried. |
| 23 | Remote Configuration Compare | Remote_Configuration_Compare.htm | MIGRATED | logging/config-compare.md | Only trivial "dialog resizable, size remembered" dropped. |
| 24 | CAN Configuration > CAN Configuration Dialog Box | CAN_Configuration.htm | MIGRATED | can/index.md | Docs updated (16 configs, FIA check boxes). |
| 25 | CAN Configuration > Bus | CAN_Configuration_CAN_Bus.htm | MIGRATED | can/configuration.md (CAN Bus) | — |
| 26 | CAN Configuration > Messages | CAN_Configuration_Messages.htm | MIGRATED | can/configuration.md (CAN Messages) | — |
| 27 | CAN Configuration > Message Details | CAN_Configuration_Message_Details.htm | MIGRATED | can/configuration.md | — |
| 28 | CAN Configuration > Parameter Details | CAN_Configuration_Parameter_Details.htm | MIGRATED | can/configuration.md | — |
| 29 | CAN Configuration > CAN Bit Definitions | CAN_Configuration_CAN_Bit_Definitions.htm | MIGRATED | can/configuration.md | Minor: general bit/byte numbering diagram (CAN Bit Definition.gif) and example captions ("10-bit value starting at bit 12 / bit 11") not carried; MSB first/last images present. |
| 30 | Sensors > Sensors | Sensors.htm | MIGRATED | sensors/index.md | — |
| 31 | Software Calibrated Sensors | Software_Calibrated_Sensors.htm | MIGRATED | sensors/software-calibrated-sensors.md | — |
| 32 | Software Calibrated Sensors > Calibration Files | Calibration_Files.htm | MIGRATED | sensors/software-calibrated-sensors.md | Menu updated to Sensors > Force Rebuild Sensor Database. |
| 33 | Software Calibrated Sensors > Sensor Calibration Tool | Sensor_Calibration_Tool.htm | PARTIAL | sensors/software-calibrated-sensors.md | Three panes described. Missing: button descriptions (Live Cal – opens wizard; Manual Cal – CHM "TBC", button still in source as IDC_SM_START_MANUAL_CAL; Previous/Next – edit previous/next calibration point; Finish) and dialog screenshot (sensor_calibration.gif). |
| 34 | Software Calibrated Sensors > Live Calibration | Live_Calibration.htm | MIGRATED | sensors/software-calibrated-sensors.md | — |
| 35 | Obtaining Sensor Calibration Data | Obtaining_Sensor_Calibration_Data.htm | MIGRATED | sensors/sensor-calibration-data.md | POSSIBLY OBSOLETE (see 36). |
| 36 | Get Sensor Data Utility | Get_Sensor_Data_Utility.htm | MIGRATED | sensors/sensor-calibration-data.md | POSSIBLY OBSOLETE: dial-up modem, TAGSVR1 NetWare path, F: drive. |
| 37 | Using Get Sensor | Using_Get_Sensor.htm | MIGRATED | sensors/sensor-calibration-data.md | Condensed but complete. POSSIBLY OBSOLETE (DOS 'gs' utility, CD-ROM). |
| 38 | Sensors & Actuators > Sensors & Actuators | Sensors_Actuators_Tool.htm | MIGRATED | sensors/sensors-and-actuators.md, sensors/index.md | Sensor-set prerequisite is in index.md note. |
| 39 | Sensors & Actuators > Sensor Sets | Saving_and_Loading_Sensor_Sets.htm | MIGRATED | sensors/sensors-and-actuators.md | — |
| 40 | Sensors & Actuators > dialog box | Sensors_Actuators_Dialog_Box.htm | MIGRATED | sensors/sensors-and-actuators.md | — |
| 41 | Sensors & Actuators > Serial Numbers | Sensors_Actuators_Serial_Numbers.htm | MIGRATED | sensors/sensors-and-actuators.md | Defect: warning dialog image rendered as literal text `image\S_A_Serial_Warning.gif` (broken placeholder); S_A_drop_down.gif not carried. |
| 42 | Sensors & Actuators > Constants | Sensor_and_Actuator_Constants.htm | MIGRATED | sensors/sensors-and-actuators.md | S_A_Constants.gif screenshot not carried. |
| 43 | Sensors & Actuators > Enabling and Disabling | Enabling_and_Disabling_Sensors_and_Actuators.htm | MIGRATED | sensors/sensors-and-actuators.md | — |
| 44 | External Inputs > Configuration | External_Inputs_Configuration.htm | MIGRATED | sensors/external.md | — |
| 45 | External Inputs > Input Source | External_Inputs_Input_Source.htm | MIGRATED | sensors/external.md | Cross-links to Sensor Bus / CAN Link Configuration dropped. |
| 46 | External Inputs > Selecting a Bus | External_Inputs_Selecting_a_Bus.htm | MIGRATED | sensors/external.md | — |
| 47 | External Inputs > Selecting a Node | External_Inputs_Selecting_a_Node.htm | MIGRATED | sensors/external.md | Pointer to SN-32 node types dropped; docs fix timer range unit (51.2 µs). |
| 48 | External Inputs > Adding a Sensor | External_Inputs_Adding_a_Sensor.htm | MIGRATED | sensors/external.md | Docs updated (Identifier check box; Sensors menu). Pointer to SN-6 Interface Cards dropped (see 49); download prompt image not carried. |
| 49 | External Inputs > SN-6 Interface Cards | External_Inputs_SN_6_Interface_Cards.htm | MISSING | — | Whole procedure absent: interface card must be selected before adding sensors to an SN-6; expand node > Interface Card (number = slot in SN-6); configure Input 1 / optional Input 2; each card type accepts limited sensor types and SM infers card type from the first sensor type chosen. Feature still in source (SysMonTSB TTSBInterfaceCard.h). |
| 50 | External Inputs > Drag and Drop | External_Inputs_Drag_and_Drop.htm | MISSING | (sensors/index.md only says "Supports drag-and-drop") | Absent: nodes, interface cards and sensors can be dragged to new tree locations; drop only on valid location else cancelled; expand target first; auto-scroll; Spare Items Pool as temporary holding area for any number of item copies. Feature still in source (SysMonTSB TSpareItemsPool.h). |
| 51 | External Inputs > Speed Sensor Scaling | External_Inputs_Speed_Sensor_Scaling.htm | MIGRATED | sensors/external.md (Speed Sensor Scaling) | — |
| 52 | External Inputs > Input Signal Configuration Tool | Input_Signal_Configuration_Tool.htm | MIGRATED | sensors/external.md (Input Signal Configuration Tool) | Docs fix swapped Import/Export descriptions. Minor: dialog layout sentence (tree left, output window top-right, tabs below; options enabled per signal type/ECU) and context-menu image (input2.gif) dropped. |
