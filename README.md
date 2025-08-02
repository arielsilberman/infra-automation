Infra Automation Simulator 

This project is a mock infrastructure provisioning tool built in Python.
It allows you to create virtual machine (VM) instances, validate inputs with JSON Schema,
and simulate service installation through Bash scripts — all without touching real cloud resources.

Project Overview
Accepts user inputs for creating virtual machines:

Name

Operating System (Windows or Linux)

CPU count (vCPUs)

RAM size (GB)

Disk size (GB)

Validates inputs against a JSON schema to prevent bad data.

Logs all activity (success and errors) in logs/provisioning.log.

Saves VM instances to configs/instances.json for persistence.

Simulates service installation (nginx, dns, smtp) via Bash script.

Project Structure

infra-automation/

│
├── configs/

│ ├── instances.json

│ └── vm_schema.json 


│
├── logs/

│ └── provisioning.log

│

├── scripts/

│ └── install.sh

│

├── src/

│ └── logger.py

│

├── infrastructure_sim.py

├── machine.py

├── README.md

└── requirements.txt

bash

Copy

Edit

git clone <your_repo_link_here>

cd infra-automation

Create a virtual environment (recommended)

bash

Copy

Edit

python -m venv .venv

source .venv/bin/activate

.venv\Scripts\activate

Install dependencies


bash

Copy

Edit

pip install -r requirements.txt

Usage


Run the simulator:

bash

Copy

Edit

python infrastructure_sim.py

Follow the prompts to add VMs.


Enter done when you’ve finished adding machines.

Optionally install services like nginx, dns, or smtp.

Check configs/instances.json for saved instances and logs/provisioning.log for logs.