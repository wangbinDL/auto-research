#!/usr/bin/env python3
"""验证所有 interface schema 文件的合法性"""

import json
import sys
from pathlib import Path

import yaml

INTERFACES_DIR = Path(__file__).parent.parent / "interfaces"


def validate_json_schema(path: Path) -> bool:
    try:
        with open(path) as f:
            schema = json.load(f)
        assert "type" in schema or "$schema" in schema
        print(f"  [OK] {path.name}")
        return True
    except Exception as e:
        print(f"  [FAIL] {path.name}: {e}")
        return False


def validate_yaml_schema(path: Path) -> bool:
    try:
        with open(path) as f:
            schema = yaml.safe_load(f)
        assert "type" in schema or "properties" in schema
        print(f"  [OK] {path.name}")
        return True
    except Exception as e:
        print(f"  [FAIL] {path.name}: {e}")
        return False


def main():
    print("Validating interface schemas...")
    all_ok = True

    for p in sorted(INTERFACES_DIR.glob("*.json")):
        if not validate_json_schema(p):
            all_ok = False

    for p in sorted(INTERFACES_DIR.glob("*.yaml")):
        if not validate_yaml_schema(p):
            all_ok = False

    if all_ok:
        print("\nAll schemas valid.")
    else:
        print("\nSchema validation FAILED.")
        sys.exit(1)


if __name__ == "__main__":
    main()
