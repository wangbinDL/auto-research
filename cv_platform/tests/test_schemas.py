"""CV 平台模块单元测试"""

import json
import yaml
from pathlib import Path

INTERFACES_DIR = Path(__file__).parent.parent.parent / "interfaces"


def test_experiment_spec_schema():
    with open(INTERFACES_DIR / "experiment_spec.schema.yaml") as f:
        schema = yaml.safe_load(f)
    assert schema["type"] == "object"
    assert "experiment_id" in schema["properties"]
    assert "detection" in schema["properties"]["task_type"]["enum"]


def test_experiment_result_schema():
    with open(INTERFACES_DIR / "experiment_result.schema.json") as f:
        schema = json.load(f)
    assert "success" in schema["properties"]["status"]["enum"]
    assert "metrics" in schema["required"]


def test_mock_result_matches_schema():
    with open(Path(__file__).parent.parent.parent / "mocks" / "experiment_result_mock.json") as f:
        result = json.load(f)
    assert result["status"] == "success"
    assert "mAP" in result["metrics"]
    assert result["metrics"]["mAP"] > 0
