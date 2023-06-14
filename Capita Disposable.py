import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
df = pd.read_excel('/home/dennoh/Downloads/data.xlsx', sheet_name=' Income of Urban and Rural ')
print(df)


# Convert columns to NumPy arrays
year = df['Year'].to_numpy()
rural = df['Rural Households Per Capita \nDisposable \nIncome(yuan)'].to_numpy()
urban = df['Urban Households Per Capita\nDisposable \nIncome(yuan)'].to_numpy()

# Create the line graph
plt.figure(figsize=(10, 6))

# Plot Rural Households Per Capita Disposable Income
plt.plot(year, rural, marker='o', label='Rural')

# Plot Urban Households Per Capita Disposable Income
plt.plot(year, urban, marker='o', label='Urban')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Per Capita Disposable Income (yuan)')
plt.title('Capita Disposable Income')
plt.legend()

plt.tight_layout()
plt.show()