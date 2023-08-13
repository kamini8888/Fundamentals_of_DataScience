import pandas as pd
data={
    'customer_reviews':['good','excellent','good','bad','bad'],
    'prod_name':['pen','pencil','eraser','pen','sharpner'],
    'customer_id': [1,2,3,4,5]
    }
df=pd.DataFrame(data)
print(df)
a=df['customer_reviews'].value_counts()
print("frequency distribution")
print(a)
