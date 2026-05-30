
max_temperature = 0;
min_temperature = 0;
avg_temperature = 0;

def calculate_statistics(temperatures):
    max_temperature = max(temperatures)
    min_temperature = min(temperatures)
    avg_temperature = sum(temperatures) / len(temperatures)
    report_log = f"=== SENSOR REPORT ===\n Max temperature: {max_temperature}\n Min temperature: {min_temperature}\n Avg temperature: {avg_temperature:.2f}"
    print(report_log)
    return report_log

with open("sensor_data.txt", "r") as file:
    lines = file.read().splitlines()
    temperatures = [int(line) for line in lines]
    report_log = calculate_statistics(temperatures)

with open("report.txt", "w") as file:
    file.write(report_log)

with open("data.csv", "r") as file:
    next(file)  # Skip the header line
    lines = file.read().splitlines()
    temperatures = []
    for line in lines:
        temperature = int(line.split(",")[1])  # Assuming temperature is the second column
        temperatures.append(temperature)
        
    report_log = calculate_statistics(temperatures)
