import numpy as np
from sklearn.ensemble import RandomForestClassifier


def train_rf(X, y, **kwargs):
    """X: [muestras, bandas], y: etiquetas."""
    clf = RandomForestClassifier(n_estimators=300, n_jobs=-1, random_state=0, **kwargs)
    return clf.fit(X, y)


def predict_cube(clf, cube):
    """Clasifica un cubo [filas, columnas, bandas]; píxeles con NaN -> 0."""
    rows, cols, bands = cube.shape
    flat = cube.reshape(-1, bands)
    valid = ~np.isnan(flat).any(axis=1)
    out = np.zeros(flat.shape[0], dtype="uint8")
    out[valid] = clf.predict(flat[valid])
    return out.reshape(rows, cols)
