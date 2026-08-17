from library import (
    Book,
    BookNotAvailableError,
    BookNotFoundError,
    DuplicateEntryError,
    Library,
    Member,
    MemberNotFoundError,
    load_library,
    save_library,
)

DATA_FILE = "library.json"


def print_menu():
    print(
        """
1. Add book
2. Remove book
3. Add member
4. Search books
5. List all books
6. Borrow book
7. Return book
8. Save library
9. Exit
"""
    )


def prompt_required(label):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print(f"{label} cannot be empty. Please try again.")


def main():
    library = Library()
    load_library(library, DATA_FILE)

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = prompt_required("Title")
                author = prompt_required("Author")
                isbn = prompt_required("ISBN")
                library.add_book(Book(title, author, isbn))

            elif choice == "2":
                isbn = prompt_required("ISBN to remove")
                library.remove_book(isbn)

            elif choice == "3":
                name = prompt_required("Member name")
                member_id = prompt_required("Member ID")
                library.add_member(Member(name, member_id))

            elif choice == "4":
                keyword = prompt_required("Search keyword")
                results = library.search_books(keyword)
                for book in results:
                    print("-", book)

            elif choice == "5":
                for book in library.list_books():
                    print("-", book)

            elif choice == "6":
                member_id = prompt_required("Member ID")
                isbn = prompt_required("ISBN")
                library.borrow_book(member_id, isbn)

            elif choice == "7":
                member_id = prompt_required("Member ID")
                isbn = prompt_required("ISBN")
                library.return_book(member_id, isbn)

            elif choice == "8":
                save_library(library, DATA_FILE)
                print("Library saved.")

            elif choice == "9":
                save_library(library, DATA_FILE)
                print("Goodbye!")
                break

            else:
                print("Invalid option, please choose 1–9.")

        except (
            BookNotFoundError,
            MemberNotFoundError,
            BookNotAvailableError,
            DuplicateEntryError,
            ValueError,
        ) as error:
            print("Error:", error)

        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Saving and exiting...")
            save_library(library, DATA_FILE)
            break


if __name__ == "__main__":
    main()