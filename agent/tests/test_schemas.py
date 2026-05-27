"""Agent 模块单元测试"""

import json
from pathlib import Path


def test_trajectory_schema_loadable():
    schema_path = Path(__file__).parent.parent.parent / "interfaces" / "trajectory.schema.json"
    with open(schema_path) as f:
        schema = json.load(f)
    assert schema["type"] == "object"
    assert "trajectory_id" in schema["properties"]


def test_experiment_spec_phases():
    schema_path = Path(__file__).parent.parent.parent / "interfaces" / "trajectory.schema.json"
    with open(schema_path) as f:
        schema = json.load(f)
    phases = schema["properties"]["phase"]["enum"]
    assert "observe" in phases
    assert "reflect" in phases
