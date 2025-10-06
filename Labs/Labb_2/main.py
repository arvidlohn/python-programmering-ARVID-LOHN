import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path_datapoint = r"D:\IT_högskolan\01_Python_programming\python-programmering-ARVID-LOHN\Labs\Labb_2\datapoints.txt"
path_testpoint = r"D:\IT_högskolan\01_Python_programming\python-programmering-ARVID-LOHN\Labs\Labb_2\testpoints.txt"
data = pd.read_csv(path_datapoint, sep=",")
test = pd.read_csv(path_testpoint, sep=",")

#data.groupby(' label (0-pichu').plot(kind="scatter", x="(width (cm)", y=" height (cm)",
 #                                    alpha=0.7)
colors = {"0":"blue", "1":"red"}

for pokemon in ["0","1"]:
    subset = data[data[' label (0-pichu'] == pokemon]
    plt.scatter(subset["(width (cm)"], subset[" height (cm)"],
                c=colors[pokemon], label="Pokemon", alpha=0.7)



plt.legend()
plt.show()
