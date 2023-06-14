import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
df = pd.read_excel('/home/dennoh/Downloads/data.xlsx', sheet_name="Basic Statistics on Nationa")

# Convert columns to NumPy arrays
year = df['Year'].values
total_family_households = df['Total Family Households\n(10K)'].values
average_size_family_households = df['Average Size of \nFamily Households'].values
total_population = df['Total Population\n(10K )'].values

# Create the figure and axes objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the Total Population (10K) as a bar graph
ax1.bar(year, total_population, color='blue', alpha=0.5)
ax1.set_xlabel('Year')
ax1.set_ylabel('Total Population (10K)', color='blue')
ax1.tick_params('y', colors='blue')

# Create a twin axes object for the line graph
ax1_twin = ax1.twinx()

# Plot the Total Family Households (10K) as a line graph
ax1_twin.plot(year, total_family_households, marker='o', color='red', label='Total Family Households (10K)')
ax1_twin.set_ylabel('Total Family Households (10K)', color='red')
ax1_twin.tick_params('y', colors='red')

# Plot the Average Size of Family Households as a line graph
ax1_twin.plot(year, average_size_family_households, marker='s', color='green', label='Average Size of Family Households')
ax1_twin.set_ylabel('Average Size of Family Households', color='green')
ax1_twin.tick_params('y', colors='green')

# Set the title and legend
ax1.set_title('Population of Zhejiang Province')
ax1.legend(loc='upper left')

# Combine Urban and Rural population
total_population = df['Urban(10K )'] + df['Rural(10K )']

# Plot the horizontal bars
ax2.barh(df['Year'], df['Urban(10K )'], color='blue', label='Urban')
ax2.barh(df['Year'], df['Rural(10K )'], color='green', label='Rural')

# Set labels and title
ax2.set_xlabel('Population (10K)')
ax2.set_ylabel('Year')
ax2.set_title('Urbanization')
ax2.legend()

plt.tight_layout()
plt.show()
