import sys
from PySide6.QtWidgets import QApplication
from Boundaries.MainWindow import MainWindow


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())


#----------------------команда: pyside6-uic filename.ui -o filename.py --------------------