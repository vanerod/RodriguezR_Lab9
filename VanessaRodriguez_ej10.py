import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal


datos=pd.read_csv('https://hub.mybinder.org/user/computociencias-fisi2029-201910-wj943fh0/files/Seccion_1/Fourier/Datos/transacciones2008.txt')
datos["date [AST]"]=pd.to_datetime(datos["date [AST]"],format='%Y%m%d %H:%M:%S')
datos.set_index(["date [AST]"],inplace=True)