#import library
import pandas as pd


#import dataset
df = pd.read_csv('starbucks.csv')


#check dataset detail
'''
df.head()
df.info()
df.columns
'''

#check duplicate, NaN, NULL and fill value
'''
df.isna().any()
df.isnull().any()
df.duplicated().any()
'''
df['Caffeine (mg)'] = df['Caffeine (mg)'].fillna('0')


#remove column 
remove_column = []
for i in df.columns:
    remove_column.append(i) if '%' in i else None
df = df.drop(columns=remove_column)


#change milligram -> gram
miligram_column = []
for i in df.columns:
    if '(mg)' in i:
        df[i] = pd.to_numeric(df[i], errors='coerce').fillna(0) * 0.001
    else:
        continue



#rename column
df.rename(columns={'Beverage_category': 'Category', 'Beverage_prep': 'Size',
                   ' Total Fat (g)': 'Fat', 'Trans Fat (g) ': 'Trans Fat',
                   'Saturated Fat (g)': 'Saturated Fat', ' Sodium (mg)': 'Sodium',
                   ' Total Carbohydrates (g) ': 'Carbohydrate', 'Cholesterol (mg)': 'Cholesterol',
                   ' Dietary Fibre (g)': 'Fiber', ' Sugars (g)': 'Sugar',
                   ' Protein (g) ': 'Protein', 'Caffeine (mg)': 'Caffeine'}, inplace=True)

#check type
'''
df.dtypes
'''
df['Fat'] = pd.to_numeric(df['Fat'], errors='coerce')
