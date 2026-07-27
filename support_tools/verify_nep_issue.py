"""
Support tool to verify Patreon subscription and reward delivery issues
for GitHub Issue #3111: "I did not receive the NEP".

This script simulates checking user subscription status and reward delivery
for a given creator and user email, and outputs a report for support staff.

Usage:
    python verify_nep_issue.py --email user@example.com --creator ProjectH
"""

import argparse

# Mock database of user orders and rewards for demonstration purposes
USER_ORDERS = {
    "ykqnb666@gmail.com": {
        "ProjectH": {
            "active_orders": [],
            "pending_orders": [],
            "rewards_delivered": False,
            "bonus_coins_delivered": False,
        }
    },
    # Add more users and creators as needed
}

def check_orders(email, creator):
    """Check active and pending orders for the user and creator."""
    user_data = USER_ORDERS.get(email, {})
    creator_data = user_data.get(creator, None)
    if creator_data is None:
        return None
    return creator_data

def generate_report(email, creator):
    """Generate a report based on the user's order and reward status."""
    creator_data = check_orders(email, creator)
    if creator_data is None:
        return f"No subscription data found for user '{email}' and creator '{creator}'."

    active = creator_data["active_orders"]
    pending = creator_data["pending_orders"]
    rewards = creator_data["rewards_delivered"]
    bonus_coins = creator_data["bonus_coins_delivered"]

    report_lines = []
    report_lines.append(f"Verification report for user '{email}' and creator '{creator}':")
    report_lines.append(f"- Active orders: {len(active)}")
    report_lines.append(f"- Pending orders: {len(pending)}")
    report_lines.append(f"- Rewards delivered: {'Yes' if rewards else 'No'}")
    report_lines.append(f"- Bonus coins delivered: {'Yes' if bonus_coins else 'No'}")

    if not active and not pending:
        report_lines.append("-> No active or pending orders found. Possible cause of issue.")
    if not rewards:
        report_lines.append("-> Rewards have not been delivered. Compensation or refund may be needed.")
    if not bonus_coins:
        report_lines.append("-> Bonus coins not delivered as promised.")

    return "\n".join(report_lines)

def main():
    parser = argparse.ArgumentParser(description="Verify Patreon subscription and reward issues.")
    parser.add_argument("--email", required=True, help="User email address")
    parser.add_argument("--creator", required=True, help="Creator name")
    args = parser.parse_args()

    report = generate_report(args.email, args.creator)
    print(report)

if __name__ == "__main__":
    main()
