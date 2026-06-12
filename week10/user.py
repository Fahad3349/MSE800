import sqlite3
import hashlib
from datetime import datetime

DB_NAME = "project_system.db"


# ---------------- DATABASE SECTION ----------------
def connect_db():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------------- SECURITY SECTION ----------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ---------------- USER ACCOUNT MANAGEMENT ----------------
def register_user():
    print("\n--- User Registration ---")

    full_name = input("Enter Full Name: ")
    date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
    email = input("Enter Email: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")

    if not full_name or not date_of_birth or not email or not username or not password:
        print("All fields are required.")
        return

    if not validate_date(date_of_birth):
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    if password != confirm_password:
        print("Passwords do not match.")
        return

    hashed_password = hash_password(password)

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (full_name, date_of_birth, email, username, password)
            VALUES (?, ?, ?, ?, ?)
        """, (full_name, date_of_birth, email, username, hashed_password))

        conn.commit()
        conn.close()

        print("Registration successful!")

    except sqlite3.IntegrityError:
        print("Email or username already exists.")


def login_user():
    print("\n--- User Login ---")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed_password = hash_password(password)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ? AND password = ?
    """, (username, hashed_password))

    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"\nLogin successful. Welcome, {user[1]}!")
        user_dashboard(user)
    else:
        print("Invalid username or password.")


def forgot_password():
    print("\n--- Forgot Password ---")

    email = input("Enter your registered email: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if user:
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")

        if new_password != confirm_password:
            print("Passwords do not match.")
            conn.close()
            return

        hashed_password = hash_password(new_password)

        cursor.execute("""
            UPDATE users
            SET password = ?
            WHERE email = ?
        """, (hashed_password, email))

        conn.commit()
        print("Password reset successful.")
    else:
        print("Email not found.")

    conn.close()


def view_profile(user):
    print("\n--- User Profile ---")
    print(f"Full Name: {user[1]}")
    print(f"Date of Birth: {user[2]}")
    print(f"Email: {user[3]}")
    print(f"Username: {user[4]}")


def user_dashboard(user):
    while True:
        print("\n--- User Dashboard ---")
        print("1. View Profile")
        print("2. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_profile(user)
        elif choice == "2":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice.")


# ---------------- MAIN MENU ----------------
def main_menu():
    create_tables()

    while True:
        print("\n===== PROJECT SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()