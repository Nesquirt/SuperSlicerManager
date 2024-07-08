import subprocess
from choco_check import ChocoCheck


class SuperSlicerManaging:
    @staticmethod
    def install_superslicer():
        """Install SuperSlicer using Chocolatey."""
        try:
            subprocess.run(["choco", "install", "superslicer", "--pre"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'installazione di SuperSlicer: {e}")

    @staticmethod
    def update_superslicer():
        """Update SuperSlicer using Chocolatey."""
        try:
            subprocess.run(["choco", "upgrade", "superslicer", "--pre"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'aggiornamento di SuperSlicer: {e}")

    @staticmethod
    def uninstall_superslicer():
        """Uninstall SuperSlicer using Chocolatey."""
        try:
            subprocess.run(["choco", "uninstall", "superslicer", "--pre"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Errore durante la disinstallazione di SuperSlicer: {e}")

    @staticmethod
    def prompt_user(choco_installed):
        """Prompt the user to install, update, or uninstall SuperSlicer, and install Chocolatey if needed."""
        print("Choose an option:")
        if not choco_installed:
            print("4) Install Chocolatey")

        print("1) Install SuperSlicer")
        print("2) Update SuperSlicer")
        print("3) Uninstall SuperSlicer")
        choice = input("Insert the number of your choice: ")

        if choice == "1":
            SuperSlicerManaging.install_superslicer()
        elif choice == "2":
            SuperSlicerManaging.update_superslicer()
        elif choice == "3":
            SuperSlicerManaging.uninstall_superslicer()
        elif choice == "4" and not choco_installed:
            ChocoCheck.install_chocolatey()
        else:
            print("Scelta non valida. Per favore riprova.")


def main():
    choco_check = ChocoCheck()
    choco_installed = choco_check.is_chocolatey_installed()
    SuperSlicerManaging.prompt_user(choco_installed)


if __name__ == "__main__":
    main()
