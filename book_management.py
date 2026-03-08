# ============================================================
# LIBRARY BOOK MANAGEMENT SYSTEM
# OOP Practice Activity — Full CRUD Version
# CREATE, READ, UPDATE, DELETE across multiple books
# ============================================================


class Book:
    """
    Represents a single book in the library.

    Attributes:
        book_id          (int)  - unique ID assigned to the book
        title            (str)  - title of the book
        author           (str)  - author of the book
        publication_year (str)  - year the book was published
        available        (bool) - availability status
    """

    def __init__(self, book_id, title, author, publication_year):
        self.book_id          = book_id
        self.title            = title
        self.author           = author
        self.publication_year = publication_year
        self.available        = True

    # --------------------------------------------------------
    # Method: borrow_book()
    # --------------------------------------------------------
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f'\n  [OK] "{self.title}" has been borrowed. Enjoy your read!')
        else:
            print(f'\n  [!] "{self.title}" is currently unavailable.')

    # --------------------------------------------------------
    # Method: return_book()
    # --------------------------------------------------------
    def return_book(self):
        if not self.available:
            self.available = True
            print(f'\n  [OK] "{self.title}" has been returned. Thank you!')
        else:
            print(f'\n  [!] "{self.title}" was not borrowed.')

    # --------------------------------------------------------
    # Method: update_info()
    # --------------------------------------------------------
    def update_info(self, title, author, publication_year):
        self.title            = title
        self.author           = author
        self.publication_year = publication_year
        print(f'\n  [OK] Book #{self.book_id} has been updated successfully.')

    # --------------------------------------------------------
    # Method: display_info()
    # --------------------------------------------------------
    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"  | {str(self.book_id).ljust(3)} | {self.title.ljust(30)} | {self.author.ljust(22)} | {self.publication_year.ljust(6)} | {status.ljust(13)} |")

    # --------------------------------------------------------
    # Method: is_available()
    # --------------------------------------------------------
    def is_available(self):
        return self.available


# ============================================================
# LIBRARY — manages the full collection of Book objects
# ============================================================

class Library:
    """Manages a collection of Book objects with full CRUD."""

    def __init__(self):
        self.books   = []
        self.next_id = 1

    # --- CREATE ---
    def add_book(self):
        print("\n  [ ADD NEW BOOK ]")
        title  = input("  Title            : ").strip()
        author = input("  Author           : ").strip()
        year   = input("  Publication Year : ").strip()

        if not title or not author or not year:
            print("\n  [!] All fields are required. Book not added.")
            return

        book = Book(self.next_id, title, author, year)
        self.books.append(book)
        print(f'\n  [OK] "{title}" added with Book ID #{self.next_id}.')
        self.next_id += 1

    # --- READ (all) ---
    def display_all(self):
        print("\n  [ ALL BOOKS ]")
        if not self.books:
            print("  No books in the library yet.")
            return
        self._print_table_header()
        for book in self.books:
            book.display_info()
        self._print_table_footer()

    # --- READ (search) ---
    def search_book(self):
        print("\n  [ SEARCH BOOK ]")
        keyword = input("  Enter title or author to search: ").strip().lower()
        results = [b for b in self.books if keyword in b.title.lower() or keyword in b.author.lower()]
        if not results:
            print(f'\n  [!] No books found matching "{keyword}".')
            return
        print(f'\n  Found {len(results)} result(s):')
        self._print_table_header()
        for book in results:
            book.display_info()
        self._print_table_footer()

    # --- UPDATE ---
    def update_book(self):
        print("\n  [ UPDATE BOOK ]")
        book = self._get_book_by_id()
        if not book:
            return
        print(f'  Editing "{book.title}" — press Enter to keep current value.')
        title  = input(f"  New Title            [{book.title}]: ").strip() or book.title
        author = input(f"  New Author           [{book.author}]: ").strip() or book.author
        year   = input(f"  New Publication Year [{book.publication_year}]: ").strip() or book.publication_year
        book.update_info(title, author, year)

    # --- DELETE ---
    def delete_book(self):
        print("\n  [ DELETE BOOK ]")
        book = self._get_book_by_id()
        if not book:
            return
        confirm = input(f'  Are you sure you want to delete "{book.title}"? (yes/no): ').strip().lower()
        if confirm == "yes":
            self.books.remove(book)
            print(f'\n  [OK] "{book.title}" has been deleted.')
        else:
            print("\n  [!] Deletion cancelled.")

    # --- BORROW ---
    def borrow_book(self):
        print("\n  [ BORROW BOOK ]")
        book = self._get_book_by_id()
        if book:
            book.borrow_book()

    # --- RETURN ---
    def return_book(self):
        print("\n  [ RETURN BOOK ]")
        book = self._get_book_by_id()
        if book:
            book.return_book()

    # --------------------------------------------------------
    # Helper: find a book by ID
    # --------------------------------------------------------
    def _get_book_by_id(self):
        try:
            book_id = int(input("  Enter Book ID: ").strip())
            for book in self.books:
                if book.book_id == book_id:
                    return book
            print(f"\n  [!] No book found with ID #{book_id}.")
            return None
        except ValueError:
            print("\n  [!] Invalid ID. Please enter a number.")
            return None

    # --------------------------------------------------------
    # Helpers: table formatting
    # --------------------------------------------------------
    def _print_table_header(self):
        print()
        print("  " + "-" * 97)
        print(f"  | {'ID'.ljust(3)} | {'Title'.ljust(30)} | {'Author'.ljust(22)} | {'Year'.ljust(6)} | {'Status'.ljust(13)} |")
        print("  " + "-" * 97)

    def _print_table_footer(self):
        print("  " + "-" * 97)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    library = Library()

    print("=" * 48)
    print("      LIBRARY BOOK MANAGEMENT SYSTEM")
    print("=" * 48)

    while True:
        print("\n  MENU")
        print("  ----")
        print("  1 - Add a new book        (CREATE)")
        print("  2 - View all books        (READ)")
        print("  3 - Search a book         (READ)")
        print("  4 - Update a book         (UPDATE)")
        print("  5 - Delete a book         (DELETE)")
        print("  6 - Borrow a book")
        print("  7 - Return a book")
        print("  8 - Exit")

        choice = input("\n  Enter your choice (1-8): ").strip()

        if   choice == "1": library.add_book()
        elif choice == "2": library.display_all()
        elif choice == "3": library.search_book()
        elif choice == "4": library.update_book()
        elif choice == "5": library.delete_book()
        elif choice == "6": library.borrow_book()
        elif choice == "7": library.return_book()
        elif choice == "8":
            print("\n  Goodbye! Happy reading!\n")
            break
        else:
            print("\n  [!] Invalid choice. Enter a number from 1 to 8.")


if __name__ == "__main__":
    main()