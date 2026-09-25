# System Monitor site rebuild (2026-09-25)

The site was rebuilt so that it:

1. **Has the same structure as the legacy `SystemMonitor.chm`.**
   - One page per CHM topic, with the same hierarchy, names and order.
   - A single collapsible sidebar tree, with no navbar tabs.
2. **Is accurate to what System Monitor does today.**
   - Every page was checked against the 8.87.3 source (`ATLAS9/ATLASSM/Main`, shipped branch `release/2026-SM-R03`). That covers the source code, resources, ODL, protos and installer.
   - The CHM content was used as the starting point, not as the source of truth. It had not been maintained.

The per-section reports in this folder list, page by page, what was corrected, removed and added, each with `path:line` source citations. The ActiveX findings are in `activex/`.

## Structure versus the CHM

The 16 top-level sections are identical to the CHM, in the same order. Books and topics keep their CHM names and nesting.

Deliberate differences:

| Change | Why |
|---|---|
| **Release Notes** added at the end | Site blog; the CHM had no equivalent. |
| **Configuration API** has three extra items: Protocol Documentation, Protobuf Definitions, Client Example | Reference material that was on the previous site. |
| **Data Display** has two extra pages: *Dial Gauge Display* and *Signal Sampling Display* | Both are shipped displays on **Desktop > Window** (Alt+Shift+U / Alt+Shift+I). In the CHM they were popups missing from the TOC. |
| Books with a single topic appear as a single page | For example *Keyboard Operation* and *Scalar Window*. Same name and position. |
| *McLaren Applied* page renamed **Motion Applied** | Rebrand. |
| **Removed**, as obsolete (see below) | They describe functionality that no longer exists. |

### Topics removed as obsolete

| CHM topic | Evidence |
|---|---|
| Hardware › Changing the PCMCIA card slot for the CA card | The shipped `cacard.sys` is a 32-bit driver. It cannot load on the 64-bit Windows that the installer requires. The installer only copies the file and never registers it, so the registry key the page tells you to edit never exists. |
| Using SM › Parameter Properties › Sensor tab | The property sheet never adds a Sensor tab (`TParamPropSheet.cpp:283-297, 359-459`). The dialog resource is unused. |
| Testbed › Puma Commands › Special Puma Parameters | `APS_Errors` / `APS_LinkOK` do not exist anywhere in the source. |
| Developer Functions › FIA Upload | FIAUpload is not in `SM.sln` or `SM-Build.proj`, and the SM installer doesn't ship it. **Confirm that it isn't distributed separately.** |
| Data Acquisition › Obtaining Sensor Calibration Data › Get Sensor Data Utility, Using Get Sensor | DOS `gs` utility over dial-up to a NetWare server (TAGSVR1). Nothing in the source refers to it. The parent page now points to the support portal. |

## What changed, in numbers (approximate)

| Section | Pages | Corrected | Removed | Added |
|---|---|---|---|---|
| Introduction, Getting Started, Hardware, Technical Support, Configuration API | 25 | 30 | 15 | 25 |
| Project Management | 62 | 75 | 12 | 45 |
| Using System Monitor (UI) | 55 | 35 | 10 | 60 |
| Using System Monitor › Parameters | 45 | 33 | 6 | 45 |
| Tuning + ECU Control | 59 | 45 | 12 | 55 |
| History Report, Testbed, Developer Functions | 36 | 70 | 25 | 40 |
| Data Display (+2 displays) | 44 | 45 | 3 | 40 |
| Data Acquisition | 66 | 45 | 12 | 40 |
| PCU Dashboard Configuration | 21 | 22 | 1 | 45 |
| ActiveX Automation | 23 | 60 | 12 | 120 |
| **Total** | **~436** | **~460** | **~110** | **~515** |

Highlights:
- **ActiveX:** all 326 methods in `SystemMonitor.odl` now appear exactly once, and a script confirmed every signature matches the ODL. The Enumeration Definitions are restored.
- **Command line:** `/encrypt` and `/prm` are not accepted and have been removed. The real flags are now documented: `/adjust`, `/auto`, `/description`, `/copydir`.
- **CAN FD** is documented for the first time.
- **PCU Dashboard** is documented for the first time since the CHM. The Shift Lights tab was completely rewritten for the current dialog.
- **Other new content:** the Configuration API Setup dialog and the Tools-menu commands, full menu listings and the accelerator table.
- **Formula conversion direction** was backwards in the CHM and is now corrected.
- **Mathematical operators** were wrong in the CHM (`x`, `%`, `[ ]`) and are now corrected.

## Needs SME confirmation (material items)

Full lists are in each section report. The ones most worth deciding:

1. **Suspected product bugs**, which the docs describe as the code behaves today:
   - `GetVirtualParameterEx/Ex2` returns the last four strings in a different order from the ODL.
   - `CreatePGV` outputs are declared `[out] BSTR` but written through `BSTR*`.
   - `CreateNewVirtualParameters(bSaveExisting=True)` saves to the remote logging path.
   - `CANConfigGet` is 0-based while the other slot methods are 1-based.
   - Formula conversion edits are not saved.
   - The breakpoint threshold is not saved.
   - Oscilloscope "All Y-Axis" tick is inverted.
   - Menus show shortcuts that don't work: Big Number Alt+Shift+B, Dashboard Alt+Shift+D, Alarms Alt+Shift+L, Live Calibration Ctrl+F8, External Inputs Ctrl+F9.
2. **Hardware support status:**
   - CA-125 card / HDLC via CA Card and the VE-80 adjustment board, given the 32-bit driver.
   - PCU-400 as a current product.
   - TAG 3.8 and DLU.
3. **Adjustment Board:** the Adjustment Groups and Potentiometer Configuration dialogs are never opened. Confirm that the `.pbc` Pot Board Configuration window is the only workflow.
4. **Command line:** PGVs are always encrypted, but a code comment says this was meant for consortium licences only. Should `/encrypt` come back?
5. **Macros** use journal hooks that Windows 11 may block.
6. **FIA Upload** distribution; see the table above.
7. **PC System Requirements:** CPU, RAM and disk values are kept from the CHM (the installer checks only the OS).
8. **Screenshots:**
   - CHM GIFs were kept where no newer image existed.
   - Some are known to be outdated: Connections (no PCAN-USB), and the Tools/Logging menus (no Configuration API or CAN Configuration Compare).
   - A recapture pass against 8.87.3 is recommended.

## Checks run

- `mkdocs build --strict`: no warnings.
- Every page is in the nav and every nav entry has a page.
- Every internal link and image resolves; 134 unused CHM images were removed.
- No CHM artefacts remain (show/hide/print buttons, `image\` alt text, `javascript:` links).
- The remaining "McLaren Electronic Systems" references are real install and Start-menu paths (`Program Files (x86)\McLaren Electronic Systems\System Monitor 8`), confirmed in the installer source.
- The rendered site was checked: one sidebar tree in CHM order, no header tabs, images load.
