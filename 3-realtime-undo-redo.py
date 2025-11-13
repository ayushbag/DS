# Real-time Undo/Redo System using Stack

class TextEditor:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.text = ""

    def make_change(self, new_text):
        self.undo_stack.append(self.text)
        self.text = new_text
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
        else:
            print("Nothing to undo!")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()
        else:
            print("Nothing to redo!")

    def show(self):
        print("Current Document:", self.text)


# --- Test ---
editor = TextEditor()
editor.make_change("Hello")
editor.make_change("Hello World")
editor.make_change("Hello World!!!")
editor.undo()
editor.show()
editor.redo()
editor.show()

"""
⏱️ Time Complexity:
make_change → O(1)
undo → O(1)
redo → O(1)
show → O(1)

💾 Space Complexity: O(n) (for stored versions)
"""
