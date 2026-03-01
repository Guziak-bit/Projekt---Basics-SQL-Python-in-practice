import sqlite3
import pandas as pd 
import openpyxl

# Connection to local data base
conn = sqlite3.Connection("northwind2000-simplified.sqlite")

# SQL query that provide data for DataFrame
sql_query = """
    SELECT OrderDetails.Quantity, OrderDetails.UnitPrice, OrderDetails.Discount, Orders.OrderID, Employees.EmployeeID, Employees.LastName
    FROM Orders JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
    JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID

    """
# Creating DataFrame
df = pd.read_sql_query(sql_query, conn)

# Creating a new column in memory with business logic
df['Revenue'] = df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'])
# Sorting data to make it clear for business
ranking = df.groupby('LastName')['Revenue'].sum().sort_values(ascending=False)

report_name = "Excel_raport.xlsx"

# Transfer DataFrame to Excel file with 2 sheets with sorted information and overall
with pd.ExcelWriter(report_name) as writer:
    ranking.to_excel(writer, sheet_name='Ranking_Sprzedawców')
    df.to_excel(writer, sheet_name='Dane_Szczegółowe', index= False)