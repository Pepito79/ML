import pandas as pd
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder, RobustScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from tf_keras.layers import Dense , Dropout
from tf_keras.models import Sequential
from tf_keras.metrics import Accuracy
from tf_keras.optimizers import Adam
import matplotlib.pyplot as plt
# Chargement des données
df = pd.read_csv("./Churn_Modelling.csv")

# Sélection de la cible et suppression des colonnes inutiles
y = df["Exited"]
df.drop(["Exited", "Surname", "CustomerId", "RowNumber"], axis=1, inplace=True)

# Encodage des variables catégorielles
col_to_encode = ["Geography", "Gender"]
le = LabelEncoder()
for col in col_to_encode:
    df[col] = le.fit_transform(df[col])

# Sélection des features (ici manuellement après chi2)
X = df[["Balance", "EstimatedSalary"]]

# Standardisation des données (avant SMOTE)
scaler = RobustScaler()
X = scaler.fit_transform(X)

# Division en train et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


model = Sequential()
model.add(Dense(10, activation="relu"))
model.add(Dropout(rate=0.1))
model.add(Dense(20 , activation="relu"))
model.add(Dropout(rate=0.1))
model.add(Dense(4 , activation="relu"))
model.add(Dropout(rate=0.1))
model.add(Dense(1 , activation="sigmoid"))


model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
history = model.fit(X_train, y_train, validation_split=0.2, validation_data=(X_test, y_test), epochs=50)



plt.figure(figsize=(12, 6))

train_loss = history.history['loss']
val_loss = history.history['val_loss']
epoch = range(1, 51)  # Utilise les 50 époques comme x-axis

# Tracer la courbe de perte d'entraînement et de validation
plt.plot(epoch, train_loss, label='Training Loss')
plt.plot(epoch, val_loss, label='Validation Loss')

# Titres et étiquettes
plt.title('Training and Validation Loss\n')
plt.xlabel('Epochs')
plt.ylabel('Loss')

# Affichage de la légende
plt.legend()

# Afficher le graphique
plt.show()