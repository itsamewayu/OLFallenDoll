import subprocess
import sys

def test_verify_nep_issue():
    # Run the script with the test user and creator
    result = subprocess.run(
        [sys.executable, "support_tools/verify_nep_issue.py", "--email", "ykqnb666@gmail.com", "--creator", "ProjectH"],
        capture_output=True,
        text=True,
    )
    output = result.stdout

    assert "Verification report for user 'ykqnb666@gmail.com' and creator 'ProjectH':" in output
    assert "- Active orders: 0" in output
    assert "- Pending orders: 0" in output
    assert "- Rewards delivered: No" in output
    assert "- Bonus coins delivered: No" in output
    assert "No active or pending orders found" in output
    assert "Rewards have not been delivered" in output
    assert "Bonus coins not delivered" in output
