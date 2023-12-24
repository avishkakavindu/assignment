This Ansible playbook performs various actions based on the provided variable action. Ensure Ansible is installed on your machine before proceeding.

### Steps to Run the Playbook

#### Prerequisites:

Ensure Ansible is installed on your local machine or the control node.
Update the hosts file to reflect your target servers' details and credentials.
Execution Commands:

#### Verify Install:

> `ansible-playbook playbook.yml -i inventory.ini -e "action=verify_install"`
> This action checks if services like httpd, rabbitMQ, or postgresql are installed. If not, it installs the missing service(s).

#### Check Disk Usage:

> `ansible-playbook playbook.yml -i inventory.ini -e "action=check-disk"`
> This action checks disk usage on specified servers and sends an email alert if usage exceeds 80%.

#### Check Application Status:

> `ansible-playbook playbook.yml -i inventory.ini -e "action=check-status"`
> This action retrieves the application status from the specified API endpoints and checks for any down services.

#### Ansible Playbook Structure

The playbook is structured into different tasks based on the provided action. Here's a brief overview:

#### Verify Installation of Services:

Checks if specified services are installed and installs them if missing.
**Check Disk Usage:**

Retrieves disk space information and triggers an email alert if usage exceeds 80%.
**Check Application Status:**

Calls specific API endpoints to fetch application status and lists down services.

#### Inventory Configuration

Ensure your inventory file (inventory.ini) is correctly configured.
Replace <user>, <port>, and paths with your actual server details and configurations.
