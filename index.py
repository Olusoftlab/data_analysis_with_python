import pandas as pd
import matplotlib.pyplot  as plt


pd_1=pd.read_csv("laptop_price.csv")


pd_1.dropna(inplace=True)

print(pd_1.head())
print(pd_1.describe())

pd_2=pd_1[["Company", "Product", "Weight (kg)", "Price (Euro)"  ]]

pd_3=pd_2.groupby("Product")["Price (Euro)"].mean().reset_index()

plt.bar(pd_3["Product"], pd_3["Price (Euro)"]  )

plt.xlabel("product")

plt.ylabel("Mean per product")

plt.show()

# product, cpu type, ram and cpu frequency

pd_4=pd_1[["Product", "CPU_Type", "CPU_Frequency (GHz)", "RAM (GB)" ]]

pd_5=pd_4["CPU_Type"].value_counts()
print(pd_5)
print(pd_4.columns)
print(pd_4)




 




  



