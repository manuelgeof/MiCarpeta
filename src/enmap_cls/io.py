import numpy as np
import rasterio

NODATA = -32768
SCALE = 10000.0


def read_l2a(path):
    """Lee SPECTRAL_IMAGE.TIF de EnMAP L2A.

    Devuelve (cubo float32 [filas, columnas, bandas] en reflectancia 0-1 con NaN
    en nodata, perfil rasterio, longitudes de onda en nm si están en los tags).
    """
    with rasterio.open(path) as src:
        data = src.read().astype("float32")
        profile = src.profile
        wavelengths = [
            float(src.tags(i).get("wavelength", "nan")) for i in range(1, src.count + 1)
        ]
    data[data == NODATA] = np.nan
    cube = np.moveaxis(data / SCALE, 0, -1)
    return cube, profile, np.array(wavelengths)
