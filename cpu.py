import psutil
import time


def monitor_cpu_threshold(threshold):
    while True:
        cpu_percent = psutil.cpu_percent(interval=get_monitoring_interval())
        if cpu_percent > threshold:
            send_notification(f"CPU usage is above {threshold}%")
        time.sleep(1)


def get_monitoring_interval():
    cpu_percent = psutil.cpu_percent(interval=0.1)
    if cpu_percent < 40:
        return 500  # Lower CPU usage, monitor every 500 seconds
    elif cpu_percent < 60:
        return 300  # Moderate CPU usage, monitor every 300 seconds
    else:
        return 60  # High CPU usage, monitor every 60 second


def send_notification(message):
    # Implement your notification logic here
    # This function should send a notification to the user (e.g., via email, SMS, or a push notification)
    # You can use external libraries or services to send notifications

    print(message)  # For demonstration purposes, print the message to the console


if __name__ == '__main__':
    threshold = 80
    monitor_cpu_threshold(threshold)
