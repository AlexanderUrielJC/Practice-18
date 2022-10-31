#Reporte de solución/análisis de caso práctico, aplicando la librería SEABORN. (Alexander Uriel JC)

import numpy as np
import pandas as pdb
import seaborn as sns
from sklearn.datasets import load_iris

t = np.arange(0, 2, 0.01)
seno = np.sin(2*np.pi*t)
coseno = np.cos(2*np.pi*t)

sns.lineplot(t, seno)
sns.lineplot(t, coseno)
