import subprocess

class ChocoCheck:
    @staticmethod
    def is_choco_installed():
        try:
            subprocess.check_call(['choco', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False
        except FileNotFoundError:
            return False

    @staticmethod
    def install_choco():
        install_command = ("Set-ExecutionPolicy Bypass -Scope Process -Force; "
                           "[System.Net.ServicePointManager]::SecurityProtocol = "
                           "[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; "
                           "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
        try:
            subprocess.check_call(['powershell', '-Command', install_command])
            print("Chocolatey installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during Chocolatey installation: {e}")

