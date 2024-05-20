import matplotlib.pyplot as plt

# Define a dictionary with city populations for each country
cities_of_countries = {
    'UK': {
        "Edinburgh": 0.56,
        "Glasgow": 0.62,
        "Stirling": 0.04,
        "London": 9.7
    },
    'China': {
        "Haining": 0.58,
        "Hangzhou": 8.4,
        "Shanghai": 29.9,
        "Beijing": 22.2
    }
}

# Extract and sort the population data for each country
uk_population = sorted(cities_of_countries['UK'].values())
china_population = sorted(cities_of_countries['China'].values())

# Print the sorted population data
print("Sorted UK city populations:", uk_population)
print("Sorted China city populations:", china_population)

# Set up the figure and subplots for the bar charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Prepare data for the UK bar chart
categories_uk = list(cities_of_countries['UK'].keys())
uk_population = list(cities_of_countries['UK'].values())
ax1.bar(categories_uk, uk_population, color='skyblue', edgecolor='purple', label='UK')
ax1.set_title('Population of UK Cities')
ax1.set_xlabel('Cities in UK')
ax1.set_ylabel('Population (millions)')
ax1.set_xticks(range(len(categories_uk)))
ax1.set_xticklabels(categories_uk, rotation=45, ha="right")
ax1.legend()

# Prepare data for the China bar chart
categories_china = list(cities_of_countries['China'].keys())
china_population = list(cities_of_countries['China'].values())
ax2.bar(categories_china, china_population, color='orange', edgecolor='purple', label='China')
ax2.set_title('Population of China Cities')
ax2.set_xlabel('Cities in China')
ax2.set_ylabel('Population (millions)')
ax2.set_xticks(range(len(categories_china)))
ax2.set_xticklabels(categories_china, rotation=45, ha="right")
ax2.legend()

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()