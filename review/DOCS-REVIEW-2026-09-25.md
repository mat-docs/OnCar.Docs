# System Monitor docs review (2026-09-25)

> **Superseded (2026-09-25):** the site has since been rebuilt to mirror the CHM structure and re-verified against source. See `review/restructure/README.md`. Page paths in this report refer to the earlier layout.

Audit of every page in `docs/` against System Monitor source in `ATLAS9/ATLASSM/Main`, at the shipped release branch `release/2026-SM-R03` (v8.87.3.x). For all SM paths, the local checkout matches that branch. Source paths below are relative to `ATLASSM/Main/`.

- **Pages reviewed:** 73
- **Claims checked:** ~2,700 (including ~1,600 API items, diffed by script against the `.proto` and `.odl` files)
- **Fixed in place:** ~150 wrong claims across 49 files
- **Strict build (`mkdocs build --strict`):** passes

The Configuration API protocol reference (`developer-resources/configuration_api/docs.md`) is fully in sync with the six `.proto` files. All messages, enums, fields and RPCs match. The Advanced Settings tables in `using-sm/advanced.md` match `TAdvOptions.cpp` for all 67 settings.

---

## Needs SME confirmation

### Priority: docs describe behaviour the shipped product doesn't have

| Page | Claim | Finding |
|---|---|---|
| user-guide/projects/program-data-versions.md | `/encrypt 0\|1` command-line flag; "if not specified, no encryption" | Parsing of `encrypt` is commented out (`SMv7/SMv7/TSysMonCmdLineInfo.cpp:488-491`), and encryption defaults to **on** (`:75`). An unrecognised flag switches the command to "Generic" (`:480-485`), so passing `/encrypt` probably breaks `/newpgv`. |
| user-guide/projects/program-data-versions.md | `/prm"path"` flag | Rejected by the code (`TSysMonCmdLineInfo.cpp:352-358`, "set in Advanced Settings"). The supported flags `/description`, `/adjust`, `/auto` and `/copydir` are undocumented. |
| user-guide/testbed/puma-commands.md | `APS_Errors` / `APS_LinkOK` special parameters | Not found anywhere in testbed code. Get Scalar only looks up ECU scalar parameters. |
| user-guide/testbed/puma-commands.md | Put Map "returns error if breakpoints out of sequence" | There is no sequence check. The only errors are lookup-length mismatch and "Axis not editable". |
| user-guide/testbed/puma-commands.md | Switch Offline/Online "generates new data stamp" | Only toggles Live Updates (`SMv7/SMv7/TSysMonFrameTestbed.cpp:304`). |
| user-guide/testbed/testbed-properties.md | Debug can be toggled while the link is enabled | The whole Configure menu is disabled while the link is enabled. |
| user-guide/getting-started/rda.md | After answering **No**, Online and Single Message are restricted | The code only disables Live Tune and Live Auto Tune (`TSysMonFrameEcu.cpp:3270-3274`). The prompt actually asks "Do you wish to Clear?" |
| user-guide/ecu-control/programming-data.md | "Reset Data to ROM" command | No such menu item. The behaviour matches "Undo Data Changes in Unit & Edit Buffer", which the page already covers. |
| user-guide/ecu-control/ecu-operations.md | With no constant defined, messages go to controller AC on TAG-300 | The code sends nothing unless a BIOS or application constant defines the controller. |
| user-guide/hardware/index.md | "Adjustment Board Configuration" dialog; groups in `Pot.ini` | The matching dialog is "Potentiometer Configuration" (`Core/SysMonParamDlgs/SysMonParamDlgs.rc:560`), and its class is never opened. No `Pot.ini` exists; the program version reads an "Adjustment Parameters" `.ini`. The VE-80/VE-81 steps also depend on this. |
| user-guide/data-acquisition/can/configuration.md | "DBC Export includes the CAN FD flag" | The DBC export code has no CAN FD handling (`TCANConfigDoc.cpp`). |
| user-guide/data-acquisition/logging/burst-logging.md | Engine-speed start uses a Throttle position threshold | The Throttle field is hidden (`SysMonDAQ.rc:328-329`, `NOT WS_VISIBLE`). |
| user-guide/data-acquisition/logging/remote-logging.md | Driver push button works "as a trigger input for Channel Trigger conditions" | That condition was removed in 2004. The replacement "External Trigger" wording that was added is minimal and needs checking. |
| user-guide/using-sm/windows-parameters.md | Window types "Strip Chart", "Status Indicator"; "Gauge" | No Strip Chart or Status Indicator in source; the gauge is "Dial Gauge". Window properties list and Explorer filters don't match the source (Explorer: Groups/Names/Descriptions and Unlocked/Locked/All). |
| user-guide/using-sm/advanced.md | "Shortcuts can be customised"; axis scaling "logarithmic" | Tools > Customise only customises menus; "logarithmic" isn't in any view resource. |
| developer-resources/active-x/index.md | "Only one Automation client"; "SM cannot be started by an ActiveX call" | Source counts multiple API instances and has an OLE-only launch mode (`SMv7/SMv7/TSysMonApi.cpp:98-114`). |

### Contradictions and numbers

| Page | Claim | Finding |
|---|---|---|
| developer-resources/configuration_api/index.md | "Available from System Monitor 8.85 onwards" | The protos are already on `release/2023-SM-R02` (8.84.2). 8.85 may be the official GA; confirm. |
| logging/remote-logging.md vs logging/logging-config.md | "eight channels" vs "four independently triggered channels" | The pages contradict each other; the channel count comes from unit system constants. |
| logging/remote-logging.md | "Maximum parameters allowed: 512" | The limit comes from unit system constants (`TTag2000RemoteDaConfig.cpp:7601-7623`). |
| logging/remote-logging.md | Enable / Freq +/- default of 100 Hz | 100 is only a fallback minimum. |
| logging/burst-logging.md | "Each block takes 1 ms"; minimum-interval formula; "can be **increased**" | Not in source; "increased" probably should be "reduced". |
| logging/logging-config.md | Channel type names; 5 ms PC-timer minimum; a folder per config type | Not found. Source shows one shared default folder, `\LogCfgs` (`TUnitDef.cpp:31`). |
| logging/live-logging.md | Stop Logging "ends when trigger TRUE"; pre-trigger buffer note | Product info text: started manually, stopped on trigger or at logging-time end. |
| history-report/history-details.md | `\HistReps\` folder, `XXXXXnnn.hrs` naming; breakpoints default 16 | Only the `.hrs` extension and the 1–16 range are confirmed. |
| ecu-control/diagnostics-status.md | Devices tab "aaaaa = ECU type" | Formatted as the comms path name (`Core/SysMonEcu/TEcuPpg.cpp:299`). |
| ecu-control/ecu-operations.md | Single Message status OK / Link NOK / Timeout | The code shows "Response Timeout", "No Server", "No Comms" or error text. |
| developer-functions/index.md | Macro repeat 0, speed x1, `CTRL+ESC` stops playback; log folder behaviour | No `CTRL+ESC` handler found (F2 to stop recording is confirmed). |
| display/bar.md | Normal bar colour defaults to grey | Low=blue and high=red are confirmed; no default found for normal. |
| display/oscilloscope.md | Trace Limits via right-click on Plot Area; Band Clearing behaviour | Not confirmed. |
| active-x/methods.md | `GetSlotPercentage` `szIdentifier` described as "Filename and full path" | It's a parameter ID. |
| active-x/methods.md | `CreatePGV` `BSTR*` outputs | The dispinterface declares `[out] BSTR` (`SystemMonitor.odl:2139`), which looks like an ODL bug. |
| active-x/examples/example-1.md | Titled SendMessage but calls `SendMessageEx`; `App` undefined; prints `aReply` | Bugs in the sample code. |
| active-x/examples/example-5.md | Uses `EC_1147` (a 1-axis map in examples 3–4) as a 2-axis map | Likely copy-paste. |

### Omissions (the docs are accurate but incomplete; nothing was added)

- **Connection methods:** getting-started, ecu-communication. The Connections page also offers **PCAN-USB** (`Core/SysMonEcu/SysMonEcu.rc:73`).
- **projects/unit-def.md:** the feature only appears when the Advanced Setting "Enable Unit.Def configuration (Y/N)" is on.
- **projects/data-wizard.md:** Parameter Masking is missing "Different Sensor Calibration", "Absent from Edit Buffer" and "Locked".
- **display/alarms.md:** the Alarms dialog also has Export, Import and Merge.
- **history-report/history-details.md:** the Auxiliary tab also has NMisfire and Misfire ppm.
- **can/configuration.md:** Buffer Mode "Reserved" option (may be hidden at runtime).
- **active-x/methods.md:** 22 ODL methods are undocumented. These include DeleteErrors, DeleteMinMax, GetDownloadedRemoteConfig, GetStringValueScalar, Table/Text/Rational/Formula conversion getters and setters, the virtual-parameter group methods, and SetFIACANConfigEx. About 150 argument names differ cosmetically from the ODL; COM is positional, so they weren't changed.
- **getting-started/index.md:** the Licence Manager **Copy Devices** button.
- **menus.md:** the Desktop menu is also present (greyed) with no project open; the Sensors menu is inserted conditionally.

### Content and structure gaps

- **getting-started/index.md:** numbered steps jump from 2 to 5, and step 5 has no body.
- **testbed/system-monitor-puma.md:** no H1 heading.
- **tuning/graphical-maps.md:** truncated sentence ("To change multiple values.").
- **history-report/index.md:** "Open filename" row ends mid-sentence.
- **ecu-control/programming-data.md:** "Live Tune Off" bullet has no description.
- **developer-functions/index.md** (`image\Custom_Menu_*_icon.gif`) and **sensors/sensors-and-actuators.md** (`image\S_A_Serial_Warning.gif`): leftover plain-text image paths; the files don't exist.

### Not verifiable from SM source

- **Installer and system requirements:** system requirements table, install types, default install paths (`...\System Monitor 8`, `...\System Monitor V7\`), Start-menu paths.
- **Licensing and RDA:** licence access states `FullAccess`/`RestrictedAccess`/`NoAccess` and the `Locked:` prefix in rda.md.
- **Sensors:** sensor-calibration-data.md (Get Sensor Data utility, TAGSVR1) is outside SM source.
- **Blog posts:** the 8.87.1 and 8.87.3 minor versions and every listed fix/feature match commits on `release/2026-SM-R01` and `R03`. The build numbers, the BIOS requirement and the download URLs can't be checked.

### Editorial / policy

- **configuration_api/index.md:** embeds an internal SharePoint iframe ("Proposed gRPC API", futureapplied.sharepoint.com) on a public page.
- **Branding and URLs:** "McLaren Applied" vs "Motion Applied", and portal.mclarenapplied.com vs portal.motionapplied.com, are mixed across pages.
- **using-sm/advanced.md:** the version note says 8.87.2; the defaults were verified against 8.87.3.x, so the note could be bumped.
- **tuning/graphical-maps.md:** says "Even" breakpoint spacing where the UI says "Constant spacing".
