import rasterio
import numpy as np

def calculate_ndvi_from_tif(red_path, nir_path):
    with rasterio.open(red_path) as red_src:
        red = red_src.read(1).astype('float32')

    with rasterio.open(nir_path) as nir_src:
        nir = nir_src.read(1).astype('float32')

    ndvi = (nir - red) / (nir + red + 1e-10)
    ndvi = np.clip(ndvi, -1, 1)
    ndvi_norm = ((ndvi + 1) / 2 * 255).astype('uint8')  # Normalize to 0-255

    return ndvi, ndvi_norm
