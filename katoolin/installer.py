"""Installer module for Katoolin tool management."""
import os


def run_command(cmd_str):
    """Executes a system shell command."""
    return os.system(cmd_str)


def install_package(package_name):
    """Installs a specific package via apt-get."""
    if not package_name or not isinstance(package_name, str):
        raise ValueError("Invalid package name")
    cmd = f"apt-get install -y {package_name}"
    return run_command(cmd)
