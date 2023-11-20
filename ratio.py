import pandas as pd
import os
from collections import Counter

# List to store the counts for each file
counts_list = []


# Iterate through each file in the folder
def ratio(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # Read the file into a DataFrame
            df = pd.read_csv(file_path, header=None, names=['x', 'y', 'z'], delimiter=' ')
            # Count occurrences of '0' in the 'z' column and append to the list
            diff_x = round(df['x'].max() - df['x'].min(), 2)
            diff_y = round(df['y'].max() - df['y'].min(), 2)
            res = round(diff_x / diff_y, 2)

    # Print or use the counts_list as needed

    # Use the most_common(1) method to get the most common element
    return res


def store_data(folder_name, folder_path, c):
    data = ratio(folder_path)
    stra = f'{folder_name}: {data}'
    file_path = 'ratio.txt'
    with open(file_path, 'a') as file:
        file.write(stra + '\n')
    print(f'{folder_name} done, total completion {round((c / 71) * 100,2)}%')


# store_data()
folderpath = 'Dataset'
c = 0
for subfolder in os.listdir(folderpath):
    c += 1
    subfolder_path = os.path.join(folderpath, subfolder)
    store_data(subfolder, subfolder_path, c)



