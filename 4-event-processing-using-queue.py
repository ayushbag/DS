# Event Processing System using Queue

from collections import deque

class EventQueue:
    def _init_(self):
        self.queue = deque()

    def add_event(self, event):
        self.queue.append(event)

    def process_event(self):
        if self.queue:
            print("Processed:", self.queue.popleft())
        else:
            print("No events to process!")

    def display_events(self):
        print("Pending Events:", list(self.queue))

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print(f"Cancelled Event: {event}")
        else:
            print("Event not found!")


# --- Test ---
q = EventQueue()
q.add_event("User Login")
q.add_event("File Upload")
q.add_event("Payment Done")
q.display_events()
q.process_event()
q.cancel_event("File Upload")
q.display_events()

"""
⏱️ Time Complexity:
add_event → O(1)
process_event → O(1)
display_events → O(n)
cancel_event → O(n)

💾 Space Complexity: O(n)
"""
