import numpy as np
a=[]
for i in range(0,4):
    sales = int(input("Enter the sales of the year:"))
    a.append(sales)
sales_data = np.array(a)
print(sales_data)
total_sales_for_year = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("Total sales for the year:", total_sales_for_year)
print("Percentage increase in sales from Q1 to Q4:", percentage_increase, "%")
