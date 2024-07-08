import subprocess
import os
from choco_check import ChocoCheck


class SuperSlicerManaging:
    @staticmethod
    def install_superslicer():
        """Install SuperSlicer using Chocolatey."""
        try:
            install_command = ["choco", "install", "superslicer", "--pre", "-y"]
            print(f"Executing command: {' '.join(install_command)}")
            process = subprocess.Popen(install_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE, shell=True)

            # Read and print stdout and stderr in real-time
            for stdout_line in iter(process.stdout.readline, b''):
                print(stdout_line.decode('utf-8').strip())
            process.stdout.close()

            # Wait for the process to complete
            process.wait()

            # Clear console
            os.system('cls' if os.name == 'nt' else 'clear')

            if process.returncode != 0:
                print(f"Error installing SuperSlicertry to install Chocolately first, or try to delete folder Chocolately.")
            else:
                print("SuperSlicer has been installed successfully.")

            # Wait for user input before continuing
            input("Press ENTER to continue...")

        except subprocess.CalledProcessError as e:
            print(f"Error installing SuperSlicer,try to install Chocolately first, or try to delete folder Chocolately: {e}")

    @staticmethod
    def update_superslicer():
        """Update SuperSlicer using Chocolatey."""
        try:
            update_command = ["choco", "upgrade", "superslicer", "--pre", "-y"]
            print(f"Executing command: {' '.join(update_command)}")
            process = subprocess.Popen(update_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE, shell=True)

            # Read and print stdout and stderr in real-time
            for stdout_line in iter(process.stdout.readline, b''):
                print(stdout_line.decode('utf-8').strip())
            process.stdout.close()

            # Wait for the process to complete
            process.wait()

            # Clear console
            os.system('cls' if os.name == 'nt' else 'clear')

            if process.returncode != 0:
                print(f"Error updating SuperSlicer.")
            else:
                print("SuperSlicer has been updated successfully.")

            # Wait for user input before continuing
            input("Press ENTER to continue...")

        except subprocess.CalledProcessError as e:
            print(f"Error updating SuperSlicer: {e}")

    @staticmethod
    def uninstall_superslicer():
        """Uninstall SuperSlicer using Chocolatey."""
        try:
            uninstall_command = ["choco", "uninstall", "superslicer", "--pre", "-y"]
            print(f"Executing command: {' '.join(uninstall_command)}")
            process = subprocess.Popen(uninstall_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE, shell=True)

            # Read and print stdout and stderr in real-time
            for stdout_line in iter(process.stdout.readline, b''):
                print(stdout_line.decode('utf-8').strip())
            process.stdout.close()

            # Wait for the process to complete
            process.wait()

            # Clear console
            os.system('cls' if os.name == 'nt' else 'clear')

            if process.returncode != 0:
                print(f"Error uninstalling SuperSlicer.")
            else:
                print("SuperSlicer has been uninstalled successfully.")

            # Wait for user input before continuing
            input("Press ENTER to continue...")

        except subprocess.CalledProcessError as e:
            print(f"Error uninstalling SuperSlicer: {e}")

    @staticmethod
    def prompt_user(choco_installed):
        """Prompt the user to install, update, or uninstall SuperSlicer, and install Chocolatey if needed."""
        while True:
            # Clear console at the beginning of each loop
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\nChoose an option:")
            print("1) Install SuperSlicer")
            print("2) Update SuperSlicer")
            print("3) Uninstall SuperSlicer")
            if not choco_installed:
                print("4) Install Chocolatey")

            choice = input("Enter the number of your choice: ")

            if choice == "1":
                SuperSlicerManaging.install_superslicer()
            elif choice == "2":
                SuperSlicerManaging.update_superslicer()
            elif choice == "3":
                SuperSlicerManaging.uninstall_superslicer()
            elif choice == "4" and not choco_installed:
                ChocoCheck.install_chocolatey()
                choco_installed = True  # Chocolatey is now installed, so update the flag
            else:
                print("Invalid choice. Please try again.")


def main():
    choco_check = ChocoCheck()
    choco_installed = choco_check.is_chocolatey_installed()
    SuperSlicerManaging.prompt_user(choco_installed)


if __name__ == "__main__":
    main()
