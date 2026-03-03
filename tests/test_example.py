"""Tests for ng-wc."""

import subprocess


class TestSteps:
    def test_step_one(self):
        result = subprocess.run(["ngwc", "-c", "tests/fixtures/test.txt"], capture_output=True, text=True)  # noqa: S607

        assert result.stdout.strip() == "342143 test.txt"
        assert result.returncode == 0
