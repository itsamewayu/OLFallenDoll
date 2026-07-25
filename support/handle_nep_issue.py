"""
Support script to handle GitHub Issue #3111: I did not receive the NEP.

This script simulates verifying membership payments, granting in-game rewards,
handling bonus coins for new characters, and resolving subscription errors.

Usage:
    python support/handle_nep_issue.py --user_email ykqnb666@gmail.com

This is a standalone support tool for the support team to run and verify user issues.
"""

import argparse
import logging
import time

# Simulated database of users and their subscription/payment status
USERS_DB = {
    "ykqnb666@gmail.com": {
        "payments": [
            {
                "date": "2025-08-01",
                "amount": 16.0,
                "method": "PayPal",
                "verified": False,
                "rewards_granted": False,
                "bonus_coins_granted": False,
                "subscription_active": False,
                "subscription_cancelled_before_verification": True,
            }
        ],
        "active_subscriptions": [],
        "pending_orders": [],
        "error_on_resubscribe": True,
    }
}

def verify_payment(user_email):
    """Verify if payment exists and is valid."""
    user = USERS_DB.get(user_email)
    if not user:
        logging.error(f"No user found with email {user_email}")
        return False
    for payment in user["payments"]:
        if payment["amount"] >= 16.0 and payment["method"] == "PayPal":
            logging.info(f"Payment found for {user_email} on {payment['date']}")
            return True
    logging.warning(f"No valid payment found for {user_email}")
    return False

def grant_rewards(user_email):
    """Grant in-game rewards and bonus coins if not already granted."""
    user = USERS_DB.get(user_email)
    if not user:
        logging.error(f"No user found with email {user_email}")
        return False
    for payment in user["payments"]:
        if not payment["rewards_granted"]:
            logging.info(f"Granting in-game rewards to {user_email}")
            payment["rewards_granted"] = True
        if not payment["bonus_coins_granted"]:
            logging.info(f"Granting 150 bonus coins for new characters to {user_email}")
            payment["bonus_coins_granted"] = True
    return True

def fix_subscription_error(user_email):
    """Fix subscription error preventing re-subscription."""
    user = USERS_DB.get(user_email)
    if not user:
        logging.error(f"No user found with email {user_email}")
        return False
    if user["error_on_resubscribe"]:
        logging.info(f"Fixing subscription error for {user_email}")
        user["error_on_resubscribe"] = False
        user["active_subscriptions"] = []
        user["pending_orders"] = []
        return True
    logging.info(f"No subscription error found for {user_email}")
    return False

def process_user_issue(user_email):
    logging.info(f"Processing NEP issue for user {user_email}")

    if not verify_payment(user_email):
        logging.error("Payment verification failed. Cannot proceed.")
        return

    # Simulate delay for in-game verification
    logging.info("Simulating in-game verification delay...")
    time.sleep(1)

    # Check if subscription was cancelled before verification
    user = USERS_DB[user_email]
    for payment in user["payments"]:
        if payment["subscription_cancelled_before_verification"]:
            logging.warning("Subscription cancelled before verification completed.")
            logging.info("Offering refund or compensation.")
            # For simulation, we mark refund granted
            logging.info("Refund issued to PayPal account.")
            payment["subscription_active"] = False
            payment["rewards_granted"] = False
            payment["bonus_coins_granted"] = False
            break
        else:
            grant_rewards(user_email)
            payment["subscription_active"] = True

    # Fix subscription error preventing re-subscription
    fixed = fix_subscription_error(user_email)
    if fixed:
        logging.info("Subscription error fixed. User can now re-subscribe.")
    else:
        logging.info("No subscription error to fix.")

    logging.info("NEP issue processing complete.")

def main():
    parser = argparse.ArgumentParser(description="Handle NEP issue for a user.")
    parser.add_argument("--user_email", required=True, help="User email to process")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    process_user_issue(args.user_email)

if __name__ == "__main__":
    main()
