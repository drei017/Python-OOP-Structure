# 📚 Library Book Management System

A simple terminal-based Library Book Management System built with Python using Object-Oriented Programming (OOP). This program supports full **CRUD** operations — Create, Read, Update, and Delete — across multiple books.

---

## 🗂 Files

| File | Description |
|------|-------------|
| `book_management.py` | Main program — terminal/console version |
| `library_tracker_gui.py` | PyQt6 GUI version of the library tracker |
| `ANSWERS.txt` | Reflection answers for the OOP activity |
| `README.md` | This file |

---

## ⚙️ Requirements

- Python 3.x
- PyQt6 *(only for the GUI version)*

Install PyQt6 with:
```bash
pip install PyQt6
```

---

## ▶️ How to Run

**Terminal version:**
```bash
python book_management.py
```

**GUI version:**
```bash
python library_tracker_gui.py
```

---

## 🧩 OOP Structure

### `Book` Class
Represents a single book with the following attributes and methods:

**Attributes**
- `book_id` — unique ID auto-assigned to each book
- `title` — title of the book
- `author` — author of the book
- `publication_year` — year the book was published
- `available` — availability status (True/False)

**Methods**
- `borrow_book()` — marks the book as unavailable
- `return_book()` — marks the book as available again
- `update_info()` — updates title, author, and publication year
- `display_info()` — prints the book's details in table format
- `is_available()` — returns the current availability status

### `Library` Class
Manages the full collection of `Book` objects.

**Methods**
- `add_book()` — creates and adds a new book (CREATE)
- `display_all()` — shows all books in a formatted table (READ)
- `search_book()` — searches books by title or author keyword (READ)
- `update_book()` — edits an existing book's details (UPDATE)
- `delete_book()` — removes a book with confirmation (DELETE)
- `borrow_book()` — borrows a book by ID
- `return_book()` — returns a book by ID

---

## 📋 Menu Options

```
1 - Add a new book        (CREATE)
2 - View all books        (READ)
3 - Search a book         (READ)
4 - Update a book         (UPDATE)
5 - Delete a book         (DELETE)
6 - Borrow a book
7 - Return a book
8 - Exit
```

---

## 💡 Sample Output

```
================================================
      LIBRARY BOOK MANAGEMENT SYSTEM
================================================

  MENU
  ----
  1 - Add a new book        (CREATE)
  ...

  [ ALL BOOKS ]

  -------------------------------------------------------------------------------------------------
  | ID  | Title                          | Author                 | Year   | Status        |
  -------------------------------------------------------------------------------------------------
  | 1   | The Alchemist                  | Paulo Coelho           | 1988   | Available     |
  | 2   | 1984                           | George Orwell          | 1949   | Not Available |
  -------------------------------------------------------------------------------------------------
```

---

## 🎓 OOP Concepts Applied

| Concept | Where |
|--------|-------|
| **Class** | `Book`, `Library` |
| **Attributes** | `title`, `author`, `publication_year`, `available`, `book_id` |
| **Methods** | `borrow_book()`, `return_book()`, `update_info()`, `display_info()`, etc. |
| **Object Instantiation** | Each book added is a new `Book` object |
| **Encapsulation** | Book state managed through its own methods |
