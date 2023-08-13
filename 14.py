import pandas as pd
data={
    'customer_ages' :[25, 30, 40, 25, 35, 25, 40, 35, 30, 35],
    'customer_id': [1,2,3,4,5,6,7,8,9,10]
    }
df=pd.DataFrame(data)
print(df)
a=df['customer_ages'].value_counts()
print("frequency distribution")
print(a)
