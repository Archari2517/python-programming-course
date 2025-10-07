"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():
    temp = []
    for i in range(1,8):
        temperatures = float(input(f"Enter temperatures {i} :"))
        temp.append(temperatures)
    return temp

def analyze_temps(temp_list):
    avg_temp = 0
    highest_temp = max(temp_list)
    lowest_temp = min(temp_list)
    sum = 0
    for temp in temp_list:
        sum += temp
    avg_temp = sum / len(temp_list)
    return (avg_temp, highest_temp, lowest_temp)

def display_analysis(avg, high, low):
        print("Temperature Analysis for the Week:")
        print(f"Average: {avg:.2f}")
        print(f"Highest: {high:.2f}")
        print(f"Lowest: {low:.2f}")

my_temp = get_temperatures()
analyze_temp = analyze_temps(my_temp)
display_analysis(analyze_temp[0],analyze_temp[1],analyze_temp[2])