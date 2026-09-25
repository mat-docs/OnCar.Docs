# CHM → SystemMonitor.Site migration check (2026-09-25)

> **Superseded (2026-09-25):** the site has since been rebuilt to mirror the CHM structure and re-verified against source. See `review/restructure/README.md`. Page paths in this report refer to the earlier layout.

This compares the legacy help file `ATLAS9/OCSHelp/Main/SMV7HtmlHelp/SystemMonitor.chm` (last updated for SM 8.87.2, April 2026) with the MkDocs site in `docs/`.

**Result: the migration is not complete.** 229 of 436 CHM topics (53%) are fully migrated. Another 104 are partially migrated and 100 are missing. Most of the gap is in *Using System Monitor* and *PCU Dashboard Configuration*.

## Method

1. Decompiled the CHM with `hh.exe -decompile` into 436 HTML topics and 418 images, and parsed the table of contents.
2. Automated first pass (`chm_coverage.py`): for each topic, measured what share of its word 5-grams appear anywhere in `docs/`. That table is in `text-overlap-all-topics.md`. The 66 topics at ≥80% overlap were counted as migrated.
3. The other 370 topics were each read and checked by hand against the site, allowing for paraphrase, splits and merges. Each got one of these verdicts:
   - **MIGRATED**: the substance is present.
   - **PARTIAL**: some content is present; the specific gaps are listed.
   - **MISSING**: the content is absent.
   - **N/A**: no real content.

   Where a topic looked obsolete, it was spot-checked against the SM source. Per-topic verdicts are in the `topics-*.md` files.

Images were not compared file by file. The CHM has 418 GIFs and the site uses a much smaller set of PNGs. Screenshots that a PARTIAL topic depends on are listed in its notes.

## Results by CHM section

| CHM section | Topics | Migrated | Partial | Missing | N/A |
|---|---|---|---|---|---|
| Introduction | 2 | 1 | 0 | 0 | 1 |
| Getting Started | 8 | 3 | 4 | 1 | 0 |
| Project Management | 62 | 23 | 28 | 11 | 0 |
| **Using System Monitor** | 100 | 10 | 37 | **53** | 0 |
| Data Display | 40 | 27 | 13 | 0 | 0 |
| **PCU Dashboard Configuration** | 21 | 0 | 0 | **21** | 0 |
| Hardware | 10 | 3 | 1 | 6 | 0 |
| Configuration API | 2 | 0 | 1 | 1 | 0 |
| Data Acquisition | 66 | 58 | 6 | 2 | 0 |
| Tuning | 31 | 28 | 3 | 0 | 0 |
| ECU Control | 28 | 25 | 3 | 0 | 0 |
| History Report | 10 | 10 | 0 | 0 | 0 |
| Testbed Operation | 18 | 15 | 3 | 0 | 0 |
| Developer Functions | 8 | 8 | 0 | 0 | 0 |
| ActiveX Automation | 23 | 14 | 5 | 3 | 1 |
| Technical Support | 3 | 0 | 0 | 2 | 1 |
| (topics not in TOC) | 4 | 4 | 0 | 0 | 0 |
| **Total** | **436** | **229** | **104** | **100** | **3** |

Per-topic verdicts are in the `topics-*.md` files. Those were produced in batches:
- `using-system-monitor`
- `project-management-getting-started`
- `data-display-hardware-pcu-configapi`
- `data-acquisition`
- `tuning-ecu-historyreport-testbed`
- `activex`

## Gaps, by priority

### 1. Whole areas missing (features still shipped)

- **PCU Dashboard Configuration (21 topics).** None of it is on the site. The feature ships: `FUNC_PCU` is on for SM builds, the menu is **Desktop > Window > Dashboard** (Alt+Shift+D), and it is enabled for PCU-400 projects. The missing content covers the PCU-400 dashboard, `.pcu`/`.ppc` import/export, the Dash Properties tabs, the six control types and their property tabs, and assigning actions to push buttons.
- **Parameter Properties dialog (14 of 17 topics missing, 3 partial).** None of the tabs are documented. The most useful are the Conversion tab (limits, zero, value offset) and the Display tab (warning limits, trace settings).
- **Conversions** (Rational/DAMOS, Formula, Table dialogs), the **number format syntax** and the **operator table** (`&&`, `||`, `!`, `NoLog()`, `$Name`).
- **Virtual parameters.** How to create them, the `.vpx`/`.vpm` files, the XML schema, and import/export.
- **Parameter selection.** The Select Parameter(s) dialogs, Parameter Sets (`.pms`), filter wildcards, and Identifier vs Name vs Description.
- **Context menus and the window System Menu.** Edit, Windows, Data Wizard, Select Parameter, Parameter Explorer and Tool Bar menus, plus the per-window-type option matrix.
- **Tool and information bars.** The overview and docking, the Maths Bar, the Extended Comms Bar and the Notes Bar.
- **Printing.** Printing a window vs a page, Data Wizard print options, and Print Preview.
- **Configuration API Setup dialog.** Enable, listen address and port, log level, cache refresh, and the restart requirement. The Tools > Configuration API Start/Stop/Reset commands are also undocumented.
- **Customer Base Advanced Settings.** The per-base Permit… flags and the hex fill value (default 195 / 0xC3).
- **Project lifecycle.** New Project stages 3–4, Project Properties, Closing a Project, File > New types, and Multi-Application Base editing.

### 2. Reference detail dropped

- **ActiveX.**
  - 17 CHM methods are missing from `methods.md`: 12 conversion methods (`Get/SetTableConv*`, `Get/SetTextConv*`, `SetRationalConv`, `GetRationalConvFromApp`, `SetFormulaConv`, `RemoveConversion`, `RemoveAllConversions`), `GetStringValueScalar`, and 4 virtual-parameter group methods. All 17 still exist in `SystemMonitor.odl`.
  - The "Enumeration Definitions" (`ETypeFreqValue`, `ECONDITONTYPE`, `ECOMPARISON`, `EScalingUnit`) are missing, but `methods.md` still links to them.
  - Many method remarks were dropped. Examples: SAFEARRAY requirements for SendMessage, `CreateFFCFromPGV` prerequisites, and PUL filename changes.
  - The Exit Event / Mutex topic and the `IsSysMonRunning()` detection samples are missing. The site's C++ tab calls `IsSysMonRunning()` without defining it. The exit event is now named `SystemMonitor_ExitEvent_%08x`.
- **PUMA.** The table mapping PUMA command names to System Monitor names is missing, as are the Set/Increase Map inputs and the caution about online/offline data divergence.
- **Data Wizard.** The Compare/Merge tool features, Map Compare modes and colours, masking priority and symbols, and Compare vs Compare All.
- **Grid / Oscilloscope / Bar / Errors displays.** Missing items include cell contents attributes, insert/delete rules, the Extras tab (10 s timebase default), and the defaults for limits.
- **Logging.** The Set Uniform Frequency dialog (1–1000 Hz), the Burst Set Interval dialog (up to 16384 ms), the menu-disabled/greyed-while-online notes, and the memory-allocation hardware table.
- **Sensor bus.** SN-6 interface cards, drag and drop and the Spare Items Pool, the SN-6/SN-32 node detail, and the Sensor Calibration Tool buttons.
- **Keyboard.** There is no full shortcut reference. The Adjustment Board shortcuts in `hardware/index.md` disagree with the CHM (F1 and F3 are swapped); check against source.

### 3. Probably obsolete (confirm before migrating)

- **CA-card / PCMCIA era hardware.** Communication architecture, the CA-125 spec and the `CaPcmciaSlotNumber` registry procedure.
- **Other legacy material.**
  - ASAP1b/2/3 overview.
  - Dongle/Ethernet licensing background.
  - The Get Sensor Data utility (dial-up modem, TAGSVR1, DOS).
  - Pre-rebrand Technical Support contacts.
  - The "ATLAS" blurb.

### 4. Where the site correctly differs from the CHM

These were confirmed against source in the earlier review (`../DOCS-REVIEW-2026-09-25.md`). Don't revert them.

- Unit Status: there is no orange colour.
- Live logging: there is no Pre/Post trigger mode.
- ActiveX `Reprogram`, `GetStatus` and `GetEcuDataVersion` signatures.
- Event log file name and location.
- The dash shown for non-logged values in Bar Graph.
- The MATLAB export menu path.
- The PUMA command behaviours.

### 5. Site content that contradicts the CHM and needs rewriting

- **`using-sm/advanced.md`:** the Axis Properties (log scaling, custom labels), Mathematical Operators (AND/OR/NOT), Number Formats and "customisable shortcuts" sections don't match the CHM *or* the source. Replace them with the CHM content, checked against source.
- **`using-sm/windows-parameters.md`:** window types and properties are generic, including a "Strip Chart" and a "Status Indicator" that don't exist.
- **Channel count.** DATALab Channels says 4 and Remote Logging says 8. The CHM had the same conflict.

## Suggested next step

Migrate priority 1 and 2, verifying each item against the 8.87.3 source as it goes. The CHM was written for older versions, and the earlier review found drift. The largest single piece of work is rebuilding `using-sm/` from the CHM, followed by a new PCU Dashboard section.
