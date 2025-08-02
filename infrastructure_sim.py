import json                                          # for json files
import subprocess                                    # for running bash scripts in python
from src.logger import setup_logger                  # logging module imported from local
from jsonschema import validate, ValidationError     # module for json error handling


with open("configs/vm_schema.json") as f:
    vm_schema = json.load(f)

def usr_input():
    machines = []
    while True:    # Getting the name input from user and making an exit for him
        name = input("Select a name for the machine (or type 'done' to exit): ")
        if name.lower() == 'done':
            break
        while True:    # Getting the Os from user and making sure that it accepts all forms of os alias
            os = input("Select the running OS (win or linux): ").lower()
            if os in ["windows", 'win', 'w']:
                os = "Windows"
                break
            elif os in ["Linux", "linux", 'lin', 'l']:
                os = "Linux"
                break
            else:
                print("Please select a valid and supported OS")
        while True:
            cpu = input("Select the number of CPUs desired: ")
            if not cpu.isdigit() or int(cpu) < 1:   # Making sure the user input is valid for the machine creation
                print("Please enter a valid number of CPUs.")
            else:
                cpu = f"{cpu}vCPU"
                break
        while True:
            ramv = input("Select the amount of memory desired (in GB): ")
            if not ramv.isdigit() or int(ramv) < 1:  # Making sure the user input is valid for the machine creation
                print("Invalid value for the memory, please enter a number higher than zero.")
            else:
                ram = f"{ramv}GB"
                break
        while True:
            diskv = input("Select an amount of disk for the machine (in GB): ")
            if not diskv.isdigit() or int(diskv) <1: # Making sure like line 35 for a valid and useful input from user.
                print("Invalid value for the memory, please enter a number higher than zero.")
            else:
                disk = f"{diskv}GB"
                break

        instance_data = {
            "name": name,
            "os": os,
            "cpu": float(cpu.replace("vCPU", "")),
            "ram": float(ram.replace("GB", "")),
            "disk": float(disk.replace("GB", ""))
        }

        try:
            validate(instance=instance_data, schema=vm_schema)
            instance_data["cpu"] = f"{int(instance_data['cpu'])}vCPU"
            instance_data["ram"] = f"{int(instance_data['ram'])}GB"
            instance_data["disk"] = f"{int(instance_data['disk'])}GB"
            log_message(f"VM created successfully: {instance_data}")

        except ValidationError as err:
            print(f"An error has happened, please try again later. Error: {err.message}")

            log_message(f"Validation error: {err.message}", level="error")
        machines.append(instance_data)

    return machines


def setup_script(service_name):
    try:
        subprocess.run(["bash", "scripts/install.sh", service_name], check=True)
        log_message(f"{service_name} installed.")
    except subprocess.CalledProcessError as e:
        log_message(f"An error has happened while installing {service_name}, please try again later. Error: {e}")

logger = setup_logger()
def log_message (message, level="info"):
    if level == "error":
        logger.error(message)
    else:
        logger.info(message)


def main():
    try:
        log_message("Provisioning initiated")

        instances = usr_input()
        with open("configs/instances.json", "r") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []

        existing_data.extend(instances)

        with open("configs/instances.json", "w") as f:
            json.dump(existing_data, f, indent=4)

        log_message("Provisioning done.")

        while True:
            service = input("Select a service to install (nginx, dns, smtp) enter 'done' to exit: ")
            if service == 'done':
                break
            setup_script(service)
            log_message(f"{service} installed")

    except KeyboardInterrupt:
        log_message("User interrupted the VM creation...", level="error")

if __name__ == '__main__':
    main()