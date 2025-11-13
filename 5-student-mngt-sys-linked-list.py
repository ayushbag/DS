# Student Record Management System using Linked List

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete_student(self, roll):
        temp = self.head
        if temp and temp.roll == roll:
            self.head = temp.next
            return
        prev = None
        while temp and temp.roll != roll:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def update_student(self, roll, name=None, marks=None):
        temp = self.head
        while temp:
            if temp.roll == roll:
                if name:
                    temp.name = name
                if marks:
                    temp.marks = marks
                return
            temp = temp.next

    def search_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"Found: {temp.roll} {temp.name} {temp.marks}")
                return
            temp = temp.next
        print("Student not found!")

    def sort_by_marks(self):
        arr = []
        temp = self.head
        while temp:
            arr.append((temp.roll, temp.name, temp.marks))
            temp = temp.next
        arr.sort(key=lambda x: x[2])
        for rec in arr:
            print(rec)

    def display(self):
        temp = self.head
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next


# --- Test ---
s = StudentList()
s.add_student(1, "Sneha", 85)
s.add_student(2, "Rahul", 92)
s.add_student(3, "Priya", 78)
print("All Students:")
s.display()
print("\nAfter Sorting by Marks:")
s.sort_by_marks()
print("\nSearch:")
s.search_student(2)

"""
⏱️ Time Complexity:
Add → O(n)
Delete → O(n)
Update → O(n)
Search → O(n)
Sort → O(n log n)

💾 Space Complexity: O(n)
"""
