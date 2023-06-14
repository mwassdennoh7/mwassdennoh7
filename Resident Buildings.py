import pandas as pd
import matplotlib.pyplot as plt

# Set display option to show all columns
pd.set_option('display.max_columns', None)

# Load the data from the Excel file
df = pd.read_excel('/home/dennoh/Downloads/data.xlsx', sheet_name="People's Material and Cultu")


# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Convert columns to NumPy arrays
year = df['Year'].to_numpy()
urban = df['Urban Areas Per Capita Floor Space\nof Residents Buildings(m²)'].to_numpy()
rural = df['Rural Areas Per Capita Floor Space\nof Residents Buildings(m²)'].to_numpy()

# Create the divided bar graph
ax1.bar(year, urban, color='yellow', label='Urban')
ax1.bar(year, rural, bottom=urban, color='purple', label='Rural')

# Set labels and title for ax1
ax1.set_xlabel('Year')
ax1.set_ylabel('Floor Space (m²)')
ax1.set_title('Resident Buildings Distribution')
ax1.legend()

# Convert columns to NumPy arrays
doctors_per_1000 = df['Number of Doctors Per\n1000 Persons'].to_numpy()
hospital_beds_per_1000 = df['Number of Hospital Beds\nPer 1000 Persons'].to_numpy()

# Create the double bar graph
bar_width = 0.35

ax2.bar(year, doctors_per_1000, width=bar_width, color='blue', label='Doctors per 1000')
ax2.bar(year + bar_width, hospital_beds_per_1000, width=bar_width, color='orange', label='Hospital Beds per 1000')

# Set labels and title for ax2
ax2.set_xlabel('Year')
ax2.set_ylabel('Count (per 1000 population)')
ax2.set_title('Medical Resource')
ax2.legend()

# Adjust the x-axis ticks
ax1.set_xticks(year)
ax2.set_xticks(year)

plt.tight_layout()
plt.show()
