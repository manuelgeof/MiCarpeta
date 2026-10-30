# Clasificación de imágenes hiperespectrales EnMAP (L2A)

Clasificación de escenas EnMAP nivel L2A (reflectancia de superficie, 224 bandas, 30 m).

## Estructura

- `src/enmap_cls/`: código reutilizable (lectura, preprocesado, clasificación)
- `notebooks/`: exploración
- `data/`: escenas y muestras de entrenamiento (no se versionan)
- `outputs/`: mapas y métricas (no se versionan)

## Uso

```bash
pip install -r requirements.txt
```

```python
from enmap_cls.io import read_l2a
cube, profile, wavelengths = read_l2a("data/<escena>/ENMAP01-...-SPECTRAL_IMAGE.TIF")
```

Las escenas L2A se descargan del portal EOC Geoservice del DLR.
