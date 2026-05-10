#!/usr/bin/env python3
"""
install-extension.py

Copies extension/index.ts to Pi's auto-discovery path so /reload picks it up.

Usage:
    python install-extension.py              → global: ~/.pi/agent/extensions/
    python install-extension.py --local      → .pi/extensions/ (current dir)
    python install-extension.py -p <project> → <project>/.pi/extensions/
"""

import argparse
import shutil
import sys
from pathlib import Path

EXTENSION_SOURCE = Path(__file__).resolve().parent / "extension" / "index.ts"
EXTENSION_NAME = "ipyforge-kernel"


def install(target_extensions: Path) -> Path:
    dest = target_extensions / EXTENSION_NAME / "index.ts"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(EXTENSION_SOURCE, dest)
    return dest


def main():
    if not EXTENSION_SOURCE.exists():
        print(f"Error: extension source not found at {EXTENSION_SOURCE}", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Install the ipyforge-kernel Pi extension")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--local", action="store_true", help="Install to .pi/extensions/ in current directory")
    group.add_argument("-p", "--project-dir", type=Path, help="Install to <dir>/.pi/extensions/")
    args = parser.parse_args()

    if args.local:
        base = Path.cwd()
        target = base / ".pi" / "extensions"
    elif args.project_dir:
        base = args.project_dir.resolve()
        target = base / ".pi" / "extensions"
    else:
        base = Path.home()
        target = base / ".pi" / "agent" / "extensions"

    dest = install(target)
    print(f"✅ Installed to {dest}")
    print(f"➡️  Run /reload in Pi to activate")


if __name__ == "__main__":
    main()
