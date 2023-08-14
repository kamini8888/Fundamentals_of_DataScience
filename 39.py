import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("C:/Users/mailm/Downloads/customer_data2.csv")


df_encoded = pd.get_dummies(df, columns=['PurchaseBehavior'], drop_first=True)


X = df_encoded[['SpendingScore']].values


kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)


df['Cluster'] = kmeans.labels_


plt.figure(figsize=(8, 6))
plt.scatter(df['SpendingScore'], np.zeros(len(df)), c=df['Cluster'], cmap='viridis', s=100)
plt.xlabel('Spending Score')
plt.title('Customer Clusters')
plt.show()


print("Cluster Centers (Mean Spending Score):")
print(kmeans.cluster_centers_)
