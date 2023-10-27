import psutil
import time

def main():
    print("Hello, World!")
    
    while True:
        print_usage()
        time.sleep(10)

def print_usage():
    cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage as a percentage
    mem = psutil.virtual_memory()  # Get memory usage information

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage - Total: {mem.total} bytes, Available: {mem.available} bytes, Percent: {mem.percent}%")

if __name__ == "__main__":
    
        main()
