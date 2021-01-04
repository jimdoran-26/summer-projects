#https://www.youtube.com/watch?v=vmEHCJofslg
import pandas as pd

###Whys Pandas?
#Flexibility compared to Excel
#allows you to work with larger datasets

##load data into DataFrame
df = pd.read_csv('pokemon_data.csv')

##access different data pointtts
#print(df.head(3))
#print(df.tail(3))

#print df.columns
#print df[['Name','Type 1','Legendary']][0:9]

#print df.iloc[1:3]
#print df.iloc[2,1]

#for loop printing out stattts
#for index, row in df.iterrows():
#    print(index,row['Name'])

#print df.loc[df['Type 1'] =='Fire']['Name']

##sorting/describing data
#print df.describe()
#print df.sort_values(['Speed', 'Name'],ascending = [0,0])[['Name','Speed']][0:10]

##making changes to data
##create column that is total of stats
#df['Total'] = df['HP']+df['Attack'] + df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
#print df[['Name','Total']][0:9]

df['Total'] = df.iloc[:,4:10].sum(axis=1)
#print df.head(3)

cols = list(df.columns.values)
df = df[cols[0:4]+[cols[-1]]+cols[4:12]]
#print df.head(5)

df.to_csv('modified.csv', index = 'False', sep = '\t')

##filtering data
#print df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')]
new_df= df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')& (df['HP']>70)]
new_df=new_df.reset_index(drop = True)
#print new_df

##filter out mega
import regex as re
#print df.loc[~df['Name'].str.contains('Mega')] #can pass regex in contains
#print df.loc[df['Type 1'].str.contains('Fire|Grass')][0:10] #can pass regex in contains
#re.I = ignore case 


##Conditional Changes
df.loc[df['Type 1']=='Fire', 'Type 1']= 'Flamer'
df.loc[df['Type 1']=='Flamer', 'Type 1']= 'Fire'
#print df.head(10)
##Can use 1 parameter to set another (making all fire types legendary)

#df.loc[df['Total']>500,['Generation','Legendary']]='TEST VALUE'
#print df


##Aggregate Statistics

#print df.groupby(['Type 1']).mean().sort_values('Legendary', ascending = False)
df['count']=1
#print df.groupby(['Type 1','Type 2']).count()['count']


##Large Datasets

df2 = pd.read_csv('pokemon_data.csv', chunksize=5)
#print df2

new_df = pd.DataFrame(columns = df.columns)
for df in pd.read_csv('pokemon_data.csv', chunksize = 5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df,results])

#print new_df
