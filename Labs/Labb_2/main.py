import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


#Sökvägen för filen så att datan kan hittas. 
path_datapoint = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
path_testpoint = path_datapoint + r"/testpoints.txt"
path_datapoint = path_datapoint + r"/datapoints.txt"

data = pd.read_csv(path_datapoint, sep=",", header=None, names=["x", "y", "pokemon", "none"])
test = pd.read_csv(path_testpoint, sep=",")


data.drop("none", inplace=True, axis=1)
data.drop(0, inplace=True, axis=0)
data = data.astype(float)


plt.scatter(x=data["x"], y=data["y"], c=data["pokemon"], cmap="coolwarm")



plt.title("Pikachu or Pichu")
plt.xlabel("Width")
plt.ylabel("Height")
plt.legend(title="Pokemon", loc="upper right")
plt.show()