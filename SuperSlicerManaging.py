import subprocess
import os
import time
from ChocoCheck import ChocoCheck


class SuperSlicerManaging:
    @staticmethod
    def install_superslicer():
        SuperSlicerManaging.run_command('choco install superslicer --pre')

    @staticmethod
    def update_superslicer():
        SuperSlicerManaging.run_command('choco upgrade superslicer --pre')

    @staticmethod
    def uninstall_superslicer():
        SuperSlicerManaging.run_command('choco uninstall superslicer --pre')

    @staticmethod
    def run_command(command):
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' failed with exit status {e.returncode}. Error: {e.stderr}")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    while True:
        clear_console()
        print("1) Install SuperSlicer")
        print("2) Update SuperSlicer")
        print("3) Uninstall SuperSlicer")
        if not ChocoCheck.is_choco_installed():
            print("4) Install Chocolatey")

        choice = input("Select an option: ")

        if choice == '1':
            SuperSlicerManaging.install_superslicer()
        elif choice == '2':
            SuperSlicerManaging.update_superslicer()
        elif choice == '3':
            SuperSlicerManaging.uninstall_superslicer()
        elif choice == '4' and not ChocoCheck.is_choco_installed():
            ChocoCheck.install_choco()
        else:
            print("Invalid option. Please try again.")

        input("Press Enter to return to the menu...")


if __name__ == '__main__':
    main_menu()
