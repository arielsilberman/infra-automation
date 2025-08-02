from logger import setup_logger

logger = setup_logger()


class Machine:
    def __init__(self, name, os, cpu, ram, disk):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
        self.disk = disk

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram,
            "disk": self.disk
        }

    def log_creation(self):
        logger.info(f"Setting up {self.name}: {self.os} OS, {self.cpu}vCPUs, {self.ram}GB RAM, {self.disk}GB Disk")
        print(f"Setting up {self.name}: {self.os} OS, {self.cpu}vCPUs, {self.ram}GB RAM, {self.disk}GB Disk")