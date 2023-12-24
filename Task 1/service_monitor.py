import subprocess
import json
from datetime import datetime

# List of services to monitor
services = ["httpd", "rabbitmq-server", "postgresql"]

# Replace 'your_host_name' with the actual host name where services are being monitored
host_name = "your_host_name"

def check_service_status(service):
    """ Function to check the status of a service using systemctl is-active command """

    try:
        # Run the systemctl is-active command for the service
        subprocess.run(['systemctl', 'is-active', service], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "UP"  # If the command runs without error, service is UP
    except subprocess.CalledProcessError:
        return "DOWN"  # If an error occurs, service is considered DOWN

def create_json(service_name, service_status, host_name):
    """Function to create a JSON object and write it to a file"""
   
    # Get current timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    data = {
        "service_name": service_name,
        "service_status": service_status,
        "host_name": host_name
    }
    # Create the filename based on service name and timestamp
    filename = f"{service_name}-status-{timestamp}.json"
   
    # Write JSON data to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
  
    # Print a message confirming the creation of JSON object for the service
    print(f"JSON object created for {service_name}")

for service in services:
    status = check_service_status(service)
    # Create a JSON object for reach service
    create_json(service, status, host_name)


