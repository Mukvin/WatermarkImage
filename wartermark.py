import sys

from PyQt5.QtWidgets import QApplication

from windows.window import WatermarkApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WatermarkApp()
    window.show()
    sys.exit(app.exec_())
