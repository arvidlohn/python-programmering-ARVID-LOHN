import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Task A
df = pd.read_csv("unlabelled_data.csv", header=None)

plt.scatter(x=df[0], y=df[1])
plt.xlabel("X")
plt.ylabel("Y")

## Task B
x = df[0]
y = df[1]
k, m = np.polyfit(df[0], df[1], 1)
y_line = k*x + m

## 'k-' står för vilken färg det ska vara på linjen!
plt.plot(x, y_line, 'k-')
plt.show()


## Här börjar koden som skall lämnas in!

#Task C

def calculate_point(x, y, k, m, eps=1e-9):
    
    y_line = k * x + m
    
    if y > y_line + eps:
        return "Ovanför"
    elif y < y_line + eps:
        return "Nedanför"


#Task D and E
data = pd.DataFrame(columns=["x", "y", "label"])
for i, a in zip(x,y):
    answer = calculate_point(i, a, k, m)

    if answer == "Ovanför":
        data.loc[len(data)] = [i, a, 1]
    elif answer == "Nedanför":
        data.loc[len(data)] = [i, a, 0]

data.to_csv('labelled_data.csv', index=False)

# Task F
df_label = pd.read_csv("labelled_data.csv")

plt.scatter(x=df_label.loc[df_label['label'] == 1.0, "x"], 
            y=df_label.loc[df_label['label'] == 1.0, "y"],
            color='red', label='Ovanför')
plt.scatter(x=df_label.loc[df_label['label'] == 0.0, "x"], 
            y=df_label.loc[df_label['label'] == 0.0, "y"],
            color='blue', label='Nedanför')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.plot(x, y_line, 'k-')
plt.show()

