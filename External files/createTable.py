import pandas

df = pandas.DataFrame([[1,2,3],[10,20,30],[100,200,300]])
print(df)

df1 = pandas.DataFrame([[200,15,10000],[400,20,42000],[500,34,322]],columns=["Price","Age","Value"],index=["First","Second","Third"])
print(df1)
df1max = df1.Price.max()
print(df1max)



df2 = pandas.DataFrame([{"Name:Jack","Surname:Doe"},{"Name:John"}])
print(df2)

