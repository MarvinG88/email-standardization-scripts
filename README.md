# Email Standardization Scripts

**Python and SQL scripts for standardizing email addresses in databases.**  
These scripts help convert email addresses to lowercase to ensure consistency and prevent case-sensitivity issues in your database.

---

## **Scripts Included**

1. **Python Script (`standardize_emails.py`)**  
   This script connects to a database and converts all email addresses in the `users` table to lowercase. It uses SQLite by default but can be adapted for MySQL or PostgreSQL.

2. **SQL Script (`standardize_emails.sql`)**  
   This script contains SQL commands to update all email addresses to lowercase in various databases (MySQL, PostgreSQL, SQL Server, SQLite).

---

## **Usage Instructions**

### **Python Script**
1. Ensure you have Python installed on your system.
2. Update the database connection details in the script (`conn = sqlite3.connect('your_database.db')`).
3. Run the script:
   ```bash
   python standardize_emails.py
   ```
4. All emails in the `users` table will be converted to lowercase.

### **SQL Script**
1. Open your database management tool (e.g., MySQL Workbench, pgAdmin, or SQLite CLI).
2. Run the appropriate SQL command for your database type:
   ```sql
   -- For MySQL:
   UPDATE users SET email = LOWER(email);
   ```

---

## **Prerequisites**
- Python 3.x for running the Python script.
- Access to your database with sufficient permissions to update email addresses.

---

## **Author**
**Marvin G. Mazibuko**  
YHOsoul (Pty) Ltd  
📧 Email: [webmaster@yhosoul.co.za](mailto:webmaster@yhosoul.co.za)  
🌐 Website: [https://www.yhosoul.co.za](https://www.yhosoul.co.za)  

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

## **Contributing**
Feel free to submit issues or fork the repository to improve the scripts.
