"""Tests for ng-wc."""

import subprocess

TESTFILE_PATH = "tests/fixtures/test.txt"


class TestSteps:
    def test_step_one(self):
        result = subprocess.run(["ngwc", "-c", TESTFILE_PATH], capture_output=True, text=True)  # noqa: S603, S607

        assert result.stdout.strip() == "342143 test.txt"
        assert result.returncode == 0

    def test_step_two(self):
        result = subprocess.run(["ngwc", "-l", TESTFILE_PATH], capture_output=True, text=True)  # noqa: S603, S607

        assert result.stdout.strip() == "7143 test.txt"
        assert result.returncode == 0
