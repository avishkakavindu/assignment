## Service Monitoring Script

#### Overview

This Python script monitors the status of specified services _(`httpd`, `rabbitmq-server`, `postgresql`)_ on a Linux machine and generates a JSON object for each service's status. It records the application status into Elasticsearch. The application, "**rbcapp1**" is considered "**UP**" if all three services are running; otherwise, it's marked as "**DOWN**."

#### Prerequisites

This script runs on a Linux environment.
Ensure Python is installed (version 3+ recommended).
Instructions to Run the Script
Modify Host Name: Replace `your_host_name` in the script with the actual hostname where the services are being monitored.

#### Run the Script:

- Save the script with a .py extension (e.g., service_monitor.py).
- Execute the script using Python:

  > `python service_monitor.py`

- Ensure appropriate permissions to run systemctl commands if required (sudo might be necessary).

#### Script Details

###### Functions:

> `check_service_status(service)`

Checks the status of a service using the `systemctl is-active` command.
Returns **"UP"** if the service is running, otherwise **"DOWN"**.

> `create_json(service_name, service_status, host_name)`

Creates a JSON object with service **name**, **status**, and **host name**.
Writes the JSON object to a file with a unique timestamped filename in the format `{service_name}-status-{@timestamp}.json`.

#### Usage:

- The script iterates through the specified services (httpd, rabbitmq-server, postgresql).
- For each service, it checks its status and creates a corresponding JSON object.

**The JSON object contains:**
`service_name`: Name of the service being monitored.
`service_status`: Current status of the service (either "UP" or "DOWN").
`host_name`: Host name where the script is executed.
Additional Notes

- Ensure proper permissions and system access to execute the script and access service status information.
  Recorded JSON files will contain service statuses for monitoring and logging purposes.
