mysql> CREATE DATABASE company_db;
Query OK, 1 row affected (0.24 sec)

mysql> USE company_db;
Database changed
mysql> CREATE TABLE departments (
    ->     department_id INT PRIMARY KEY AUTO_INCREMENT,
    ->     department_name VARCHAR(100) NOT NULL
    -> );
Query OK, 0 rows affected (0.44 sec)

mysql> CREATE TABLE employees (
    ->     employee_id INT PRIMARY KEY AUTO_INCREMENT,
    ->     employee_name VARCHAR(100) NOT NULL,
    ->     department_id INT,
    ->     FOREIGN KEY (department_id) REFERENCES departments(department_id)
    -> );
Query OK, 0 rows affected (0.30 sec)

mysql> INSERT INTO departments (department_name)
    -> VALUES ('HR'),
    ->        ('Engineering'),
    ->        ('Sales');
Query OK, 3 rows affected (0.40 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql>
mysql> INSERT INTO employees (employee_name, department_id)
    -> VALUES ('John Doe', 1),
    ->        ('Jane Smith', 2),
    ->        ('Alice Brown', 3),
    ->        ('Bob White', NULL);
Query OK, 4 rows affected (0.06 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> SELECT employees.employee_name, departments.department_name
    -> FROM employees
    -> INNER JOIN departments
    ->     ON employees.department_id = departments.department_id;
+---------------+-----------------+
| employee_name | department_name |
+---------------+-----------------+
| John Doe      | HR              |
| Jane Smith    | Engineering     |
| Alice Brown   | Sales           |
+---------------+-----------------+
3 rows in set (0.17 sec)

mysql> SELECT employees.employee_name, departments.department_name
    -> FROM employees
    -> LEFT JOIN departments
    ->     ON employees.department_id = departments.department_id;
+---------------+-----------------+
| employee_name | department_name |
+---------------+-----------------+
| John Doe      | HR              |
| Jane Smith    | Engineering     |
| Alice Brown   | Sales           |
| Bob White     | NULL            |
+---------------+-----------------+
4 rows in set (0.00 sec)