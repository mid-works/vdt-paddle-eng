# main.py
from PyQt6.QtWidgets import QApplication
import sys
from database.session import get_session
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow(session_factory=get_session)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()