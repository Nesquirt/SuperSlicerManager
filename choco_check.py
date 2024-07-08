import subprocess

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
            subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", install_command], check=True)
            print("Chocolatey è stato installato con successo.")
        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'installazione di Chocolatey: {e}")
