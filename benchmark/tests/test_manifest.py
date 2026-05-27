"""Benchmark 模块单元测试"""

import yaml
from pathlib import Path

INTERFACES_DIR = Path(__file__).parent.parent.parent / "interfaces"


def test_model_manifest_schema():
    with open(INTERFACES_DIR / "model_manifest.schema.yaml") as f:
        schema = yaml.safe_load(f)
    assert "model_id" in schema["properties"]
    assert "sft" in schema["properties"]["training_method"]["enum"]


def test_eval_tasks_defined():
    with open(INTERFACES_DIR / "model_manifest.schema.yaml") as f:
        schema = yaml.safe_load(f)
    tasks = schema["properties"]["eval_request"]["properties"]["tasks"]["items"]["enum"]
    assert "full_loop" in tasks
    assert "experiment_design" in tasks
