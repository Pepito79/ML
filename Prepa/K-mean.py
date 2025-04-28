import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Lire le fichier CSV
df = pd.read_csv("Live.csv")

# Supprimer les colonnes inutiles
df.drop(["status_id", "status_published", "Column1", "Column2", "Column3", "Column4"], axis=1, inplace=True)

# Initialiser le LabelEncoder et encoder la colonne "status_type"
le = LabelEncoder()
df["status_type"] = le.fit_transform(df["status_type"])

# Initialiser le MinMaxScaler
scaler = MinMaxScaler()

# Appliquer le MinMaxScaler uniquement aux colonnes numériques
columns_to_scale = df.select_dtypes(include=['float64', 'int64']).columns  # Sélectionner les colonnes numériques
df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

# Choisir le nombre de clusters en fonction de l'inertie
inertia = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    cluster = kmeans.fit_predict(df)
    inertia.append(kmeans.inertia_)

# Afficher le graphique de l'inertie pour déterminer le nombre optimal de clusters
plt.plot(range(2, 11), inertia, marker='o')
plt.xlabel('Nombre de clusters')
plt.ylabel('Inertie')
plt.title('Méthode du coude')
plt.show()

# Appliquer KMeans avec le nombre de clusters choisi (par exemple 4)
kmeansf = KMeans(n_clusters=4, random_state=42)
clus = kmeansf.fit_predict(df)
df["cluster"] = clus  # Ajouter les résultats des clusters au DataFrame

# Visualiser les clusters
print(df.head())
