import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(data_path):
    # Carga de datos simulada
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    y = df['target']

    # Split y entrenamiento
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model
