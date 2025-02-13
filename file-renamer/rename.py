import os
import sys
import shutil
import time
import subprocess
import pkg_resources

# Define the network share path (modify this)
NETWORK_SHARE = r"X:\\"  # Update to your actual mapped drive path

# Required Python packages
REQUIRED_PACKAGES = ["pywin32"]

def install_missing_packages():
    """Ensure required Python packages are installed."""
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    for package in REQUIRED_PACKAGES:
        if package not in installed_packages:
            print(f"Installing missing package: {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_network_share():
    """Check if the network share is accessible."""
    if not os.path.exists(NETWORK_SHARE):
        print(f"Error: The network share '{NETWORK_SHARE}' is not accessible.")
        sys.exit(1)

def move_and_rename_files():
    """Move all files from subdirectories to the root and rename them sequentially."""
    print(f"Scanning and moving files in {NETWORK_SHARE}...")

    files_moved = 0
    for root, _, files in os.walk(NETWORK_SHARE):
        if root == NETWORK_SHARE:
            continue  # Skip the root folder itself

        for file in files:
            old_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1]  # Preserve file extension
            new_filename = f"file_{files_moved + 1}{ext}"
            new_path = os.path.join(NETWORK_SHARE, new_filename)

            # Ensure unique filenames
            while os.path.exists(new_path):
                files_moved += 1
                new_filename = f"file_{files_moved + 1}{ext}"
                new_path = os.path.join(NETWORK_SHARE, new_filename)

            try:
                shutil.move(old_path, new_path)
                print(f"Moved: {old_path} -> {new_path}")
                files_moved += 1
            except Exception as e:
                print(f"Failed to move {old_path}: {e}")

    print(f"Completed! Moved {files_moved} files.")

if __name__ == "__main__":
    # Install missing dependencies if necessary
    install_missing_packages()

    # Check if the network share is accessible
    check_network_share()

    # Move and rename files
    move_and_rename_files()
