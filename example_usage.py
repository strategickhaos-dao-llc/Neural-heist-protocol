#!/usr/bin/env python3
"""
Example usage of the Neural Heist Protocol tracking system
Demonstrates how to interact with the status tracking system
"""

from heist_tracker import HeistTracker


def demo_workflow():
    """Demonstrate a typical workflow through the system."""
    
    print("\n🎮 NEURAL HEIST PROTOCOL - Example Workflow\n")
    
    # Initialize tracker
    tracker = HeistTracker()
    
    print("📊 Initial Status:")
    tracker.print_status()
    
    # Simulate completing a ZyBooks question
    print("\n✅ Completing a ZyBooks question...")
    remaining = tracker.complete_question()
    print(f"   Questions remaining: {remaining}")
    
    # Simulate earning GTA money from productivity
    print("\n💰 Adding GTA earnings for completed work...")
    new_balance = tracker.add_gta_earnings(50000)
    print(f"   New balance: ${new_balance:,}")
    
    # Update status to in progress
    print("\n🔄 Updating status to IN_PROGRESS...")
    tracker.update_status("IN_PROGRESS")
    
    # Set next action
    print("📝 Setting next action to ZYBOOKS_QUESTION...")
    tracker.update_next_action("ZYBOOKS_QUESTION")
    
    # Show final status
    print("\n📊 Updated Status:")
    tracker.print_status()
    
    # Reset to original state for demo purposes
    print("\n🔄 Resetting to original state...")
    tracker.update_status("AWAITING_CONFIRMATION")
    tracker.update_gta_balance(341920)
    tracker.update_questions(18)
    tracker.update_next_action("ZYBOOKS_QUESTION")
    
    print("\n✅ Demo complete! System reset to original state.")


if __name__ == "__main__":
    demo_workflow()
