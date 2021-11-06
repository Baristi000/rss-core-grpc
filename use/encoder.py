from setting import settings
import numpy as np


def encode(data):
    return np.array(settings.encode([data]), dtype="f")
