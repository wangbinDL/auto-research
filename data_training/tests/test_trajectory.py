"""数据质检模块单元测试"""

import json
from pathlib import Path

MOCKS_DIR = Path(__file__).parent.parent.parent / "mocks"


def test_trajectory_mock_valid_jsonl():
    traj_path = MOCKS_DIR / "trajectory_mock.jsonl"
    lines = traj_path.read_text().strip().split("\n")
    assert len(lines) == 6

    for i, line in enumerate(lines):
        obj = json.loads(line)
        assert obj["step_index"] == i
        assert obj["phase"] in ["observe", "hypothesize", "plan", "execute", "analyze", "reflect"]
        assert "content" in obj


def test_trajectory_has_required_fields():
    traj_path = MOCKS_DIR / "trajectory_mock.jsonl"
    first_line = json.loads(traj_path.read_text().strip().split("\n")[0])
    required = ["trajectory_id", "experiment_id", "timestamp", "step_index", "phase", "content"]
    for field in required:
        assert field in first_line, f"Missing required field: {field}"
