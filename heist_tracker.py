#!/usr/bin/env python3
"""
Neural Heist Protocol - Status Tracking System
Tracks cognitive load management through gamified metrics
"""

import json
import os
from datetime import datetime, timezone
from typing import Dict, Any


class HeistTracker:
    """
    Manages the Neural Heist Protocol status tracking system.
    Integrates GTA heist economics, ZyBooks progress, and cognitive load metrics.
    """
    
    def __init__(self, status_file: str = "status.json"):
        self.status_file = status_file
        self.data = self._load_status()
    
    def _load_status(self) -> Dict[str, Any]:
        """Load status from JSON file."""
        if os.path.exists(self.status_file):
            with open(self.status_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _save_status(self) -> None:
        """Save status to JSON file."""
        self.data['last_updated'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        with open(self.status_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status."""
        return self.data
    
    def update_status(self, new_status: str) -> None:
        """Update the status field."""
        self.data['status'] = new_status
        self._save_status()
    
    def update_next_action(self, next_action: str) -> None:
        """Update the next action field."""
        self.data['next'] = next_action
        self._save_status()
    
    def update_gta_balance(self, balance: int) -> None:
        """Update GTA heist balance."""
        self.data['gta_balance'] = balance
        self._save_status()
    
    def update_questions(self, questions: int) -> None:
        """Update ZyBooks questions count."""
        self.data['questions'] = questions
        self._save_status()
    
    def complete_question(self) -> int:
        """Mark a question as complete and return remaining count."""
        if self.data.get('questions', 0) > 0:
            self.data['questions'] -= 1
            self._save_status()
        return self.data.get('questions', 0)
    
    def add_gta_earnings(self, amount: int) -> int:
        """Add earnings to GTA balance and return new balance."""
        current = self.data.get('gta_balance', 0)
        self.data['gta_balance'] = current + amount
        self._save_status()
        return self.data['gta_balance']
    
    def print_status(self) -> None:
        """Print formatted status report."""
        print("=" * 60)
        print("NEURAL HEIST PROTOCOL - STATUS REPORT")
        print("=" * 60)
        print(f"Repository: {self.data.get('repo', 'N/A')}")
        print(f"Status: {self.data.get('status', 'N/A')}")
        print(f"Next Action: {self.data.get('next', 'N/A')}")
        print(f"GTA Balance: ${self.data.get('gta_balance', 0):,}")
        print(f"ZyBooks Questions: {self.data.get('questions', 0)}")
        print(f"Last Updated: {self.data.get('last_updated', 'N/A')}")
        print("=" * 60)
        if 'topics' in self.data:
            print(f"Topics: {', '.join(self.data['topics'])}")
            print("=" * 60)


def main():
    """Main entry point for CLI usage."""
    tracker = HeistTracker()
    tracker.print_status()


if __name__ == "__main__":
    main()
