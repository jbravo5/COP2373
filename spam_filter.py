"""
Spam Scoring Email Scanner (COP 2373 - Programming Exercise)
- User pastes an email message
- Program scans for 30 common spam words/phrases
- Each occurrence adds 1 point to a "spam score"
- Program prints score, likelihood rating, and triggers found

Note:
- Matching is case-insensitive
- Single-word keywords are matched as whole words (word boundaries)
- Multi-word phrases are matched as substrings
"""

from __future__ import annotations

import re
from typing import Dict, List, Tuple


def get_spam_keywords() -> List[str]:
    """Return a list of common spam words/phrases (30 items)."""
    return ['free', '100% free', 'act now', 'limited time', 'urgent', 'final notice', 'winner', 'congratulations', "you've been selected", 'claim your prize', 'click here', 'unsubscribe', 'risk-free', 'guaranteed', 'no obligation', 'earn cash', 'make money', 'work from home', 'cash bonus', 'get paid', 'low interest', 'pre-approved', 'credit card', 'verify your account', 'account suspended', 'unusual activity', 'confirm your identity', 'payment overdue', 'wire transfer', 'deal expires']


def analyze_message(message: str, keywords: List[str]) -> Tuple[int, Dict[str, int]]:
    """
    Scan message for each keyword/phrase.
    Returns (spam_score, triggers_dict) where triggers_dict maps keyword -> occurrences.
    """
    msg = message.lower()
    triggers: Dict[str, int] = {}
    score = 0

    for kw in keywords:
        kw_lc = kw.lower().strip()

        # If keyword contains spaces, treat as phrase substring
        if " " in kw_lc:
            count = msg.count(kw_lc)
        else:
            # Whole-word match for single tokens (e.g., "free")
            pattern = r"\b" + re.escape(kw_lc) + r"\b"
            count = len(re.findall(pattern, msg))

        if count > 0:
            triggers[kw] = count
            score += count

    return score, triggers


def rate_spam(score: int) -> str:
    """
    Convert a numeric score into a simple likelihood label.
    You can tune these thresholds if your instructor prefers different cutoffs.
    """
    if score <= 2:
        return "Low likelihood of spam"
    if 3 <= score <= 6:
        return "Moderate likelihood of spam"
    return "High likelihood of spam"


def read_email_message() -> str:
    """
    Read an email message from the user.
    User can paste multiple lines. Submit an empty line to finish.
    """
    print("Paste the email message below. Press ENTER on a blank line to finish.\n")

    lines: List[str] = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    return "\n".join(lines)


def main() -> None:
    keywords = get_spam_keywords()
    message = read_email_message()

    score, triggers = analyze_message(message, keywords)
    likelihood = rate_spam(score)

    print("\n--- RESULTS ---")
    print(f"Spam score: {score}")
    print(f"Rating: {likelihood}")

    if triggers:
        print("\nTriggers found (keyword -> count):")
        # Sort by most frequent, then alphabetical
        for kw, ct in sorted(triggers.items(), key=lambda x: (-x[1], x[0].lower())):
            print(f"  - {kw} -> {ct}")
    else:
        print("\nNo spam keywords/phrases found.")

    print("\n(End of analysis)\n")


if __name__ == "__main__":
    main()
