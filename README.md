# 🚀 Infrastructure Automation Simulator

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python-based infrastructure simulator that allows you to experiment with virtual machine provisioning and service deployment without the need for actual cloud resources. Perfect for learning DevOps concepts, testing infrastructure automation, and prototyping deployment strategies!

## ✨ Key Features

- 🖥️ **Virtual Machine Simulation**
  - Interactive VM creation with custom naming
  - Multi-OS support (Windows/Linux with flexible input formats)
  - Hardware specification (CPU cores, RAM, Disk space)
  - Persistent VM configuration storage
- 🛡️ **Robust Input Validation**
  - JSON Schema validation for VM configurations
  - Comprehensive error handling and user feedback
  - Input sanitization and format validation
- 📝 **Advanced Logging System**
  - Dual logging (console + file output)
  - Timestamped activity tracking
  - Structured error reporting in `logs/provisioning.log`
- 🔧 **Service Installation Simulation**
  - Automated service deployment simulation
  - Support for common services: NGINX, DNS, SMTP
  - Bash script integration for realistic installation flow
- 💾 **State Management**
  - JSON-based persistent storage in `configs/instances.json`
  - Configuration schema validation
  - Incremental VM addition to existing configurations

## 🛠️ Installation

### Prerequisites

- Python 3.8+ (recommended: Python 3.12)
- Git
- Bash (for service installation simulation)

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/arielsilberman/infra-automation.git
   cd infra-automation
   ```

2. **Set Up Virtual Environment** (Recommended)

   ```bash
   python -m venv .venv

   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1

   # Windows (Command Prompt)
   .venv\Scripts\activate.bat

   # Unix/MacOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   python infrastructure_sim.py
   ```

## 🎮 Usage

### Quick Start

```bash
python infrastructure_sim.py
```

### Detailed Workflow

#### 1. **Virtual Machine Creation**

The simulator will prompt you for VM specifications:

- **Machine Name**: Enter a unique identifier for your VM
- **Operating System**: Choose between:
  - Windows: `windows`, `win`, `w`
  - Linux: `linux`, `lin`, `l`
- **CPU Cores**: Specify number of virtual CPUs (minimum: 1)
- **RAM**: Memory allocation in GB (minimum: 1GB)
- **Disk Space**: Storage allocation in GB (minimum: 1GB)
- **Continue/Exit**: Type `done`, `exit`, `quit`, or `q` to finish

#### 2. **Service Installation**

After VM creation, install services:

- **Available Services**: `nginx`, `dns`, `smtp`
- **Installation**: Services are simulated via bash scripts
- **Completion**: Type `done` to exit service installation

#### 3. **Configuration Persistence**

- VM configurations are automatically saved to `configs/instances.json`
- Logs are written to `logs/provisioning.log`
- Each run appends to existing configurations

### Example Session

```
$ python infrastructure_sim.py
Select a name for the machine (or type 'done' to exit): web-server-01
Select the running OS (win or linux): linux
Select the number of CPUs desired: 4
Select the amount of memory desired (in GB): 8
Select an amount of disk for the machine (in GB): 100
Select a name for the machine (or type 'done' to exit): done
Select a service to install (nginx, dns, smtp) enter 'done' to exit: nginx
Select a service to install (nginx, dns, smtp) enter 'done' to exit: done
```

## 📁 Project Structure

```
infra-automation/
├── configs/
│   ├── instances.json      # VM configuration storage
│   └── vm_schema.json      # JSON validation schema
├── logs/
│   └── provisioning.log    # Application logs (auto-created)
├── scripts/
│   └── install.sh          # Service installation simulator
├── src/
│   ├── __init__.py         # Package initialization
│   ├── logger.py           # Logging configuration & setup
│   ├── machine.py          # VM class definition
│   └── temp4me.py          # Temporary/utility file
├── infrastructure_sim.py   # Main application entry point
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

### Key Components

- **`infrastructure_sim.py`**: Main application with user interaction and orchestration
- **`src/machine.py`**: VM class with object modeling and logging
- **`src/logger.py`**: Centralized logging setup with file & console output
- **`configs/vm_schema.json`**: JSON schema for VM configuration validation
- **`scripts/install.sh`**: Bash script for simulating service installations

## 🔧 Configuration

### VM Schema (`configs/vm_schema.json`)

The application validates VM configurations against a JSON schema:

```json
{
  "name": "string", // VM identifier
  "os": "string", // Operating system
  "cpu": "number", // CPU core count
  "ram": "number", // RAM in GB
  "disk": "number" // Disk space in GB
}
```

### Logging Configuration

- **File Logging**: `logs/provisioning.log`
- **Console Output**: Real-time status updates
- **Format**: `YYYY-MM-DD HH:MM:SS - LEVEL - MODULE - MESSAGE`

## 🧪 Testing

### Manual Testing

```bash
# Test basic functionality
python infrastructure_sim.py

# Test with invalid inputs
# Try entering negative numbers or non-numeric values

# Test service installation
# Install multiple services in sequence
```

### Validation Testing

The application includes built-in validation:

- Input sanitization for numeric values
- JSON schema validation for VM configurations
- Error handling for subprocess calls

## 🤝 Contributing

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit Changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'jsonschema'`
**Solution**: Install dependencies with `pip install -r requirements.txt`

**Issue**: Permission denied when running bash scripts
**Solution**: Ensure bash is available and executable permissions are set:

```bash
chmod +x scripts/install.sh
```

**Issue**: JSON validation errors
**Solution**: Check that all required fields (name, os, cpu, ram, disk) are provided and valid

## 🚀 Future Enhancements

- [ ] Web-based UI for VM management
- [ ] Network topology simulation
- [ ] Cloud provider integration (AWS, Azure, GCP)
- [ ] Container orchestration simulation
- [ ] Infrastructure as Code (IaC) template generation
- [ ] Multi-region deployment simulation
- [ ] Cost estimation features
- [ ] Performance monitoring simulation

## 📞 Support

For questions, issues, or contributions:

- Create an [Issue](https://github.com/arielsilberman/infra-automation/issues)
- Submit a [Pull Request](https://github.com/arielsilberman/infra-automation/pulls)
- Contact: [arielsilberman](https://github.com/arielsilberman)

---

⭐ **Star this repository if you find it helpful!**
