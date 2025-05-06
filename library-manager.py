import streamlit as st
import json

# Load library from file
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save library to file
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Initialize library
library = load_library()

# Streamlit UI
st.title("📚 Personal Library Manager")
menu = st.sidebar.radio("📌 Select an option", ["View library", "Add book", "Remove book", "Search book", "Save and Exit"])

# View all books
if menu == "View library":
    st.subheader("📖 Your Library")
    if library:
        st.table(library)
    else:
        st.info("Your library is empty. Add some books!")

# Add a book
elif menu == "Add book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=2021, max_value=2025, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        if title and author and genre:
            new_book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read
            }
            library.append(new_book)
            save_library()
            st.success(f"✅ Book '{title}' added successfully!")
            st.rerun()
        else:
            st.warning("Please fill in all required fields.")

# Remove a book
elif menu == "Remove book":
    st.subheader("🗑 Remove a Book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("✅ Book removed successfully!")
            st.rerun()
    else:
        st.info("No books available to remove.")

# Search for a book
elif menu == "Search book":
    st.subheader("🔍 Search for a Book")
    search_term = st.text_input("Enter title or author name")

    if st.button("Search"):
        results = [
            book for book in library
            if search_term.lower() in book["title"].lower() or
               search_term.lower() in book["author"].lower()
        ]
        if results:
            st.table(results)
        else:
            st.warning("No matching books found.")

# Save and Exit
elif menu == "Save and Exit":
    save_library()
    st.success("📋 Library saved successfully!")
