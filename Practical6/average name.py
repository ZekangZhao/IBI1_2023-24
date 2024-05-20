import matplotlib.pyplot as plt

def plot_average_day_activity(day_activities):
    """
    Create a pie chart to show the average daily time allocation for a university student.

    Parameters:
    day_activities : dict
        A dictionary containing the hours spent on various activities.
    """
    # Calculate the remaining 'other' time
    total_time_spent = sum(day_activities.values())
    other_time = 24 - total_time_spent
    day_activities['Other'] = other_time

    # Prepare data for the pie chart
    day_activity_list = list(day_activities.values())
    labels = list(day_activities.keys())

    # Plot the pie chart
    plt.figure(figsize=(8, 8))  # Adjust the size of the figure
    plt.pie(day_activity_list, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    plt.title('Average Day of a University Student')  # Add a title
    plt.show()  # Display the plot

# Example usage
day_activity = {
    "Sleeping": 8, 
    "Classes": 6, 
    "Studying": 3.5, 
    "TV": 2, 
    "Music": 1
}

plot_average_day_activity(day_activity)