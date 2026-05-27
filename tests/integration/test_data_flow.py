"""集成测试 — 验证接口间数据流通"""

import json
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
INTERFACES = ROOT / "interfaces"
MOCKS = ROOT / "mocks"


def test_spec_to_result_id_consistency():
    """experiment_spec 的 ID 应与 result 中的 ID 匹配"""
    with open(MOCKS / "experiment_spec_mock.yaml") as f:
        spec = yaml.safe_load(f)
    with open(MOCKS / "experiment_result_mock.json") as f:
        result = json.load(f)
    assert spec["experiment_id"] == result["experiment_id"]


def test_trajectory_references_valid_experiment():
    """轨迹数据中的 experiment_id 应与 spec 匹配"""
    with open(MOCKS / "experiment_spec_mock.yaml") as f:
        spec = yaml.safe_load(f)
    with open(MOCKS / "trajectory_mock.jsonl") as f:
        first = json.loads(f.readline())
    assert first["experiment_id"] == spec["experiment_id"]


def test_full_pipeline_data_flow():
    """端到端数据流：spec → result → trajectory 全链路 ID 一致"""
    with open(MOCKS / "experiment_spec_mock.yaml") as f:
        spec = yaml.safe_load(f)
    with open(MOCKS / "experiment_result_mock.json") as f:
        result = json.load(f)
    with open(MOCKS / "trajectory_mock.jsonl") as f:
        lines = [json.loads(l) for l in f]

    exp_id = spec["experiment_id"]
    assert result["experiment_id"] == exp_id
    assert all(l["experiment_id"] == exp_id for l in lines)


def test_trajectory_phases_complete_cycle():
    """一条完整轨迹应包含所有 6 个阶段"""
    with open(MOCKS / "trajectory_mock.jsonl") as f:
        lines = [json.loads(l) for l in f]
    phases = [l["phase"] for l in lines]
    expected = ["observe", "hypothesize", "plan", "execute", "analyze", "reflect"]
    assert phases == expected
