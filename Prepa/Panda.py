import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('telco_churn.csv')
copy =df
# #Pour avoir le type on fait : df.dtypes (the types)
# df.dtypes

# #Pour connaitre les colonnes
# col = df.columns
# #Pour avoir des info globales
# df.describe()

# colonnes= ['State', 'Account length', 'Area code', 'International plan',
#        'Voice mail plan', 'Number vmail messages', 'Total day minutes',
#        'Total day calls', 'Total day charge', 'Total eve minutes',
#        'Total eve calls', 'Total eve charge', 'Total night minutes',
#        'Total night calls', 'Total night charge', 'Total intl minutes',
#        'Total intl calls', 'Total intl charge', 'Customer service calls',
#        'Churn']

# #Pour accéder aux colonnes : df [[ col1, col2 , ..... , coln]]
# taget = df['Churn']

# #Pour voir ce qui est unique
# (df.Churn.unique())  

# #Pour mmanipuler des lignes
# df [ (df ['Churn'] == True ) & ( df['International plan'] == 'No') ]

# #Slicer ses rows utiliser indexloc : iloc
# df.iloc[0:24]

# #Dropper des lignes avec na / inplace dit de modifier directement le df de base
# df.dropna(inplace= True)

# # Drop les colonnes 

# #Pour appliquer une fonction : .apply()
# df["Binary Churn"] = df["Churn"].apply(lambda x: 1 if x == True else 0)
# df[df["Binary Churn"] == 1].sum()["Churn"]


col = ['State', 'Account length', 'Area code', 'International plan',
       'Voice mail plan', 'Number vmail messages', 'Total day minutes',
       'Total day calls', 'Total day charge', 'Total eve minutes',
       'Total eve calls', 'Total eve charge', 'Total night minutes',
       'Total night calls', 'Total night charge', 'Total intl minutes',
       'Total intl calls', 'Total intl charge', 'Customer service calls']


target = copy["Churn"]

copy.hist()
plt.show()