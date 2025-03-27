import pandas as pd

df = pd.read_csv(r"C:\Users\alper\.cache\kagglehub\datasets\johnsmith88\heart-disease-dataset\versions\2\heart.csv")

print("\nVeri Setinini İlk 5 satırı:")
print(df.head())

print("\nEksik Değerlerin Sayısı:")
print(df.isnull().sum())

print("\nİstatistiksel Özet:")
print(df.describe())
