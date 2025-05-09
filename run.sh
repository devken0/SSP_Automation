#!/bin/bash

# Function to check if a command is available
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if python3-venv is installed, if not, install it
if ! dpkg -s python3-venv >/dev/null 2>&1; then
    echo "python3-venv is not installed. Installing..."
    sudo apt update
    sudo apt install -y python3-venv
fi

# Check if xclip is installed, if not, install it
if ! dpkg -s xclip >/dev/null 2>&1; then
    echo "xclip is not installed. Installing..."
    sudo apt update
    sudo apt install -y xclip 
fi

if ! dpkg -s libdbus-1-dev libdbus-glib-1-dev python3-dbus > /dev/null 2>&1; then
    echo "python3-dbus is not installed. Installing..."
    sudo apt update
    sudo apt install -y libdbus-1-dev libdbus-glib-1-dev python3-dbus
fi

# Check if venv exists, if not, create it
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating a new one..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Check if pip is installed (it should be in the virtual environment, but let's be sure)
if ! command_exists pip; then
    echo "Pip not found. Installing pip..."
    python3 -m ensurepip --upgrade
fi

# Check if the required packages are installed from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Checking for missing Python modules in requirements.txt..."

    # Install missing modules
    pip install --upgrade -r requirements.txt
else
    echo "requirements.txt not found. Skipping package installation."
fi

# Run the Python script
echo "Running main.py..."
python main.py

