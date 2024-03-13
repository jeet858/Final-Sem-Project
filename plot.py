import pandas as pd
import os
import matplotlib.pyplot as plt



def plot_data(sub_folder_path, sub_folder_name):
    for file_name in os.listdir(sub_folder_path):
        if file_name.endswith('.txt'):
            df = pd.read_csv(os.path.join(subfolder_path, file_name), header=None, delimiter=' ')
            # Rename the columns for clarity
            df.columns = ['x', 'y', 'z']

            # Drop the 'z' column if you don't need it
            df.drop(columns=['z'], inplace=True)

            # Convert the DataFrame to a list of lists
            all_points = df.values.tolist()

            x_values = [point[0] for point in all_points]
            y_values = [point[1] for point in all_points]

            plt.scatter(x_values, y_values)
            plt.gca().invert_yaxis()
            plt.title('Scatter Plot of Points')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid(True)

            output_folder = os.path.join('Dataset-Images', sub_folder_name)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            output_file_path = os.path.join('Dataset-Images', sub_folder_name, file_name.replace('.txt', '.png'))
            plt.savefig(output_file_path)
            plt.close()  # Close the plot to avoid overlapping plots in memory
            del df


folderpath = 'Dataset'
c = 0
# Iterate through each subfolder in the main dataset folder
for subfolder in os.listdir(folderpath):
    subfolder_path = os.path.join(folderpath, subfolder)
    print(f'{subfolder} done, total completion {round((c / 71) * 100, 2)}%')
    c += 1
    plot_data(subfolder_path, subfolder)
