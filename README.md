# 🚀 Infrastructure Automation Simulator

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)

A Python-based infrastructure simulator that allows you to experiment with virtual machine provisioning and service deployment without the need for actual cloud resources. Perfect for learning and testing infrastructure concepts!

## ✨ Key Features

- 🖥️ **Virtual Machine Creation**
  - Custom VM naming
  - OS selection (Windows/Linux)
  - Hardware specification (CPU, RAM, Disk)
- 🛡️ **Input Validation**
  - JSON Schema validation for VM configurations
  - Error handling for invalid inputs
- 📝 **Comprehensive Logging**
  - Detailed activity tracking
  - Error logging
- 🔧 **Service Installation Simulation**
  - NGINX
  - DNS
  - SMTP
- 💾 **State Persistence**
  - JSON-based storage
  - Configuration management

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/arielsilberman/infra-automation.git>
   cd infra-automation
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Unix/MacOS
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. **Start the Simulator**
   ```bash
   python infrastructure_sim.py
   ```

2. **Create Virtual Machines**
   - Enter machine name
   - Choose OS (Windows/Linux)
   - Specify CPU count
   - Set RAM size (GB)
   - Define disk space (GB)
   - Type 'done' when finished

3. **Install Services**
   - Choose from: nginx, dns, smtp
   - Type 'done' to complete setup

## 📁 Project Structure

infra-automation/ ├── configs/ │ ├── instances.json # Stores VM configurations │ └── vm_schema.json # JSON validation schema ├── logs/ │ └── provisioning.log # Activity logging ├── scripts/ │ └── install.sh # Service installation simulator ├── src/ │ └── logger.py # Logging configuration ├── infrastructure_sim.py # Main application ├── machine.py # VM class definition └── requirements.txt # Project dependencies
