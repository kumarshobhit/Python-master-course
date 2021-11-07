import cv2
import pandas as pd
import numpy as np

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
print(ser)