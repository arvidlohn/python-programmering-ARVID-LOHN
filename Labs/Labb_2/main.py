import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


#Sökvägen för filen så att datan kan hittas. 
path_datapoint = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
path_testpoint = path_datapoint + r"/testpoints.txt"
path_datapoint = path_datapoint + r"/datapoints.txt"
counter = 0
pichu = 0


data = np.loadtxt(path_datapoint, skiprows=1, delimiter=",")
testdata = np.empty((0, 2), dtype=float)

### Läser in testdata
with open(path_testpoint, 'r', encoding='utf-8') as testdata_read:
    for line in testdata_read:
        if "(" in line and ")" in line:
            value = line.split('(', 1)[1].strip()
            value = value.split(')', 1)[0].strip()
            valuex = value.split(',', 1)[0].strip()
            valuey = value.split(',', 1)[1].strip()
            testdata = np.append(testdata, [[valuex, valuey]], axis=0)

testdata = testdata.astype(float)
data = data.astype(float)

data_2d = data[:, :2]


### Plottar alla punkter! 
plt.scatter(x=data[:, 0], y=data[:, 1], c=(data[:, 2] == 0.), label='Pichu', cmap="coolwarm")
plt.scatter(x=data[:, 0], y=data[:, 1], c=(data[:, 2] == 1.), label='Pikachu', cmap="coolwarm")


plt.title("Pikachu or Pichu")
plt.xlabel("Width")
plt.ylabel("Height")
plt.legend()
plt.show()


#Räknar ut avstädet från träningpunkter och testpunkterna.
distance = np.sqrt(np.sum((data_2d[:, None, :] - testdata[None, :, :])**2, axis=2))
distance_min_index = np.argmin(distance, axis=0)

for i in data[distance_min_index]:
    if i[2] == 1:
        print(f"Sample with (width, height): ({testdata[counter,0]}, {testdata[counter,1]}) classified as Pikachu")
    elif i[2] == 0:
        print(f"Sample with (width, height): ({testdata[counter,0]}, {testdata[counter,1]}) classified as Pichu")
    counter += 1



### Inamtning av värden samt felhantering!
while True:
    user_input_width = input("Enter a test point width: ")
    user_input_height = input("Enter a test point height: ")

    try:
        user_input_width = float(user_input_width)
        user_input_height = float(user_input_height)

        input_array = np.empty((0,2), dtype=float)

        if float(user_input_width) < 0 or float(user_input_height) < 0:
            raise ValueError("Neagtiva tal är inte tillåtna!")
        
    except ValueError as e:
        print(f"\n------------------------\n"
              f"Please enter only a number! \nError message: {e}"
               "\n------------------------\n")
    else:
        input_array = np.append(input_array, [[user_input_width, user_input_height]], axis=0)   


        #Räknar ut distansen!
        distance_input = np.sqrt(np.sum((data_2d[:, None, :] - input_array[None, :, :])**2, axis=2))
        distance_input_min_index = np.argmin(distance_input, axis=0)
        
        counter = 0
        for i in data[distance_input_min_index]:
            if i[2] == 1:
                print(f"Sample with (width, height): ({input_array[counter,0]}, {input_array[counter,1]}) classified as Pikachu")
            elif i[2] == 0:
                print(f"Sample with (width, height): ({input_array[counter,0]}, {input_array[counter,1]}) classified as Pichu")
            counter += 1

        ## 10 Närmaste punkterna med mest marioritet.
        nearest_10_points_index = np.argsort(distance_input, axis=0)[:10]
        
        antal_pikachu = np.count_nonzero(data[nearest_10_points_index][:,0,2] == 1)
        antal_pichu = np.count_nonzero(data[nearest_10_points_index][:,0,2] == 0)

        if antal_pikachu > antal_pichu:
            print(f"Sample with (width, height): ({input_array[0,0]}, {input_array[0,1]}) classified as Pikachu out of 10 points.")
        elif antal_pikachu < antal_pichu:
             print(f"Sample with (width, height): ({input_array[0,0]}, {input_array[0,1]}) classified as Pichu out of 10 points.")
        elif antal_pikachu == antal_pichu:
            print(f"Sample with (width, height): ({input_array[0,0]}, {input_array[0,1]}) classified as Pichu and Pikachu out of 10 points.")
        break

