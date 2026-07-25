import subprocess
import sys

def test_handle_nep_issue_script_runs():
    """Test that the support script runs and processes the user without errors."""
    result = subprocess.run(
        [sys.executable, "support/handle_nep_issue.py", "--user_email", "ykqnb666@gmail.com"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Processing NEP issue for user ykqnb666@gmail.com" in result.stdout
    assert "NEP issue processing complete." in result.stdout
