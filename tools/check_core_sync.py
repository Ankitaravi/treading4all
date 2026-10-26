#!/usr/bin/env python3
"""Verify (or enforce) that the CORE section is identical in the indicator and the strategy.

The core signal rules live between the markers
    // ============================ CORE START ============================
    // ============================ CORE END ==============================
in both CRT_Smart_Entry_Pro.pine and CRT_Smart_Entry_Strategy.pine.

Usage:
    python3 tools/check_core_sync.py          # exit 1 if the sections differ
    python3 tools/check_core_sync.py --write  # copy the indicator's core into the strategy
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDICATOR = ROOT / "CRT_Smart_Entry_Pro.pine"
STRATEGY = ROOT / "CRT_Smart_Entry_Strategy.pine"
START = "// ============================ CORE START ============================"
END = "// ============================ CORE END =============================="


def split(text: str, name: str):
    if text.count(START) != 1 or text.count(END) != 1:
        sys.exit(f"{name}: expected exactly one CORE START and one CORE END marker")
    a = text.index(START)
    b = text.index(END) + len(END)
    return text[:a], text[a:b], text[b:]


def main() -> int:
    ind_core = split(INDICATOR.read_text(encoding="utf-8"), INDICATOR.name)[1]
    head, strat_core, tail = split(STRATEGY.read_text(encoding="utf-8"), STRATEGY.name)
    if "--write" in sys.argv[1:]:
        STRATEGY.write_text(head + ind_core + tail, encoding="utf-8")
        print(f"Core copied from {INDICATOR.name} into {STRATEGY.name}")
        return 0
    if ind_core == strat_core:
        print(f"OK: CORE sections are identical ({len(ind_core.splitlines())} lines)")
        return 0
    import difflib
    diff = difflib.unified_diff(ind_core.splitlines(), strat_core.splitlines(),
                                INDICATOR.name, STRATEGY.name, lineterm="")
    print("\n".join(list(diff)[:80]))
    print("MISMATCH: CORE sections differ. Run with --write to sync from the indicator.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
