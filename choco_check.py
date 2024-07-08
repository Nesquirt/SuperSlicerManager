import subprocess
import os


class ChocoCheck:
    @staticmethod
    def is_chocolatey_installed():
        """Check if Chocolatey is installed by executing `choco -v` and capturing the output."""
        try:
            result = subprocess.run(["choco", "-v"], capture_output=True, text=True, shell=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False

    @staticmethod
    def install_chocolatey():
        """Install Chocolatey using the provided PowerShell command."""
        install_command = (
            "Set-ExecutionPolicy Bypass -Scope Process -Force; "
            "[System.Net.ServicePointManager]::SecurityProtocol = "
            "[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; "
            "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
        )
        try:
            print(f"Executing command: {install_command}")
            process = subprocess.Popen(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", install_command],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # Clear console
            os.system('cls' if os.name == 'nt' else 'clear')

            # Print stderr output (errors)
            if stderr:
                print(f"Error output:\n{stderr.decode('utf-8')}")
            # Print stdout output (standard)
            if stdout:
                print(f"Standard output:\n{stdout.decode('utf-8')}")

            # Wait for user input before continuing
            input("Press ENTER to continue...")

            if process.returncode != 0:
                print(f"Error installing Chocolatey.")
            else:
                print("Chocolatey has been installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing Chocolatey: {e}")
