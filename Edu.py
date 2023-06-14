import pandas as pd
import matplotlib.pyplot as plt

# Set display option to show all columns
pd.set_option('display.max_columns', None)

# Load the data from the Excel file and get the available sheet names
df = pd.read_excel('/home/dennoh/Downloads/data.xlsx', sheet_name="Basic Statistics on Nationa")


# Create the horizontal bar graph
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Convert columns to NumPy arrays
year = df['Year'].to_numpy()
university = df['University(10K )'].to_numpy()
senior_secondary_school = df['Senior Secondary School(10K )'].to_numpy()
junior_secondary_school = df['Junior Secondary School(10K )'].to_numpy()
primary_school = df['Primary School(10K )'].to_numpy()

# Plot the bars
ax1.barh(year, university, color='blue', label='University')
ax1.barh(year, senior_secondary_school, color='green', label='Senior Secondary School')
ax1.barh(year, junior_secondary_school, color='orange', label='Junior Secondary School')
ax1.barh(year, primary_school, color='red', label='Primary School')

# Set labels and title for the first subplot
ax1.set_xlabel('Population (10K)')
ax1.set_ylabel('Year')
ax1.set_title('Education Distribution')
ax1.legend()

# Convert columns to NumPy arrays
gender_labels = ['Male', 'Female']
gender_values = [df['Male(10K )'].sum(), df['Female(10K )'].sum()]

# Create the pie chart for gender distribution
ax2.pie(gender_values, labels=gender_labels, colors=['blue', 'pink'], wedgeprops=dict(width=0.4))

# Add a circle at the center to create a donut chart
circle = plt.Circle((0, 0), 0.3, color='white')
ax2.add_artist(circle)

# Set aspect ratio to be equal so that the pie is drawn as a circle
ax2.axis('equal')

# Set title for the second subplot
ax2.set_title('Gender Distribution')

plt.tight_layout()
plt.show()
