import psutil
import time

# Set the threshold for power-draining apps (in percentage)
POWER_THRESHOLD = 20;


# Monitor power usage and detect power-draining apps
def monitor_power_usage():
    while True:
        battery = psutil.sensors_battery()
        if battery.power_plugged:
            # Skip monitoring when the device is plugged in
            time.sleep(60)
            continue

        # Get a list of running processes and their CPU percentages
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            processes.append(proc.info)

        # Identify power-draining apps
        power_draining_apps = []
        for proc in processes:
            if proc['cpu_percent'] > POWER_THRESHOLD:
                power_draining_apps.append(proc['name'])

        if power_draining_apps:
            # Notify the user about power-draining apps
            print("Power-draining apps detected:")
            for app in power_draining_apps:
                print(app)
            print("Consider closing these apps to optimize battery life.")

        time.sleep(5)  # Wait for 60 seconds before checking again


# Start monitoring power usage
monitor_power_usage()
