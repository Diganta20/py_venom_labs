import pandas as pd
data= {
    'Name':['A','B','C'], 'Score':[7,8,9]
}
df= pd.DataFrame(data)
print('Data Frame')
print(df)
print('\nNames:')
print(df['Name'])                                #Task for tommorow search for why : in line 3 outside of var Name is so imp
# Check why name needs [] for printing
avg_score = df['Score'].mean()
print('\navg_score', avg_score)