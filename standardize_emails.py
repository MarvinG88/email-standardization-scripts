# Python Script to Standardize Email Addresses to Lowercase in a Database
# Author: Marvin G. Mazibuko
# Company: YHOsoul (Pty) Ltd
# Email: webmaster@yhosoul.co.za
# Website: https://www.yhosoul.co.za
# License: MIT License
# Created: February 2025
# Description: This script connects to a database and converts all email addresses to lowercase to ensure consistency.

import sqlite3  # You can switch to your preferred database (e.g., MySQL, PostgreSQL)

# Database connection (update with your actual database details)
conn = sqlite3.connect('your_database.db')  # Replace with MySQL or PostgreSQL connection as needed
cursor = conn.cursor()

# Select all emails to process
cursor.execute("SELECT id, email FROM users")
rows = cursor.fetchall()

# Process and update each email to lowercase
for row in rows:
    user_id, email = row
    lowercase_email = email.lower()  # Convert to lowercase

    # Update the email in the database
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (lowercase_email, user_id))

# Commit changes and close the connection
conn.commit()
conn.close()

print("All emails have been converted to lowercase.")
