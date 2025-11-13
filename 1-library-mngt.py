# 📘 Library Borrowing Records Management

class Library:
    def __init__(self):
        self.records = {}  # {member_name: no_of_books_borrowed}
        self.book_borrow_count = {}  # {book_name: borrow_count}

    def add_record(self, member, books):
        self.records[member] = books

    def add_book_borrow(self, book_name, count):
        self.book_borrow_count[book_name] = count

    def average_books_borrowed(self):
        total = sum(self.records.values())
        avg = total / len(self.records)
        return avg

    def highest_lowest_borrowed_book(self):
        highest = max(self.book_borrow_count, key=self.book_borrow_count.get)
        lowest = min(self.book_borrow_count, key=self.book_borrow_count.get)
        return highest, lowest

    def members_with_zero_borrow(self):
        count = sum(1 for x in self.records.values() if x == 0)
        return count

    def most_frequently_borrowed_book(self):
        mode = max(self.book_borrow_count, key=self.book_borrow_count.get)
        return mode


# --- Test the program ---
lib = Library()
lib.add_record("Sneha", 5)
lib.add_record("Rahul", 2)
lib.add_record("Priya", 0)
lib.add_record("Amit", 3)

lib.add_book_borrow("Python Basics", 10)
lib.add_book_borrow("C Programming", 5)
lib.add_book_borrow("Data Science", 12)
lib.add_book_borrow("AI Intro", 3)

print("Average books borrowed:", lib.average_books_borrowed())
high, low = lib.highest_lowest_borrowed_book()
print("Most borrowed book:", high)
print("Least borrowed book:", low)
print("Members with 0 borrowed books:", lib.members_with_zero_borrow())
print("Most frequently borrowed book:", lib.most_frequently_borrowed_book())
