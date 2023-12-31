import pandas as pd

data = {
    'product_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product B', 'Product A', 'Product G'],
    'quantity_sold': [100, 80, 70, 50, 120, 90, 60]
}
sales_data = pd.DataFrame(data)
product_sales = sales_data.groupby('product_name')['quantity_sold'].sum()
sorted_product_sales = product_sales.sort_values(ascending=False)
top_5_products = sorted_product_sales.head(5)
print("Top 5 products sold the most in the past month:")
print(top_5_products)


