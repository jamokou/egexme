# Program Name : egexme
# Programmer   : The Alpha
# Credits      : Iranpython.blog.ir
# Version      : 0.9(Beta Version)
# Linted By    : Pyflakes
# Info         : This tool can bind exe files with images by a click !
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os

class EgexMe(QDialog):
	def __init__(self):
		QDialog.__init__(self)

		self.setWindowTitle("egeXme 1.0")

		layout = QGridLayout()

		self.result_label = QLabel()
		self.result_label.setText("<i><h1>Image & Exe file MUST be in the same folder</h1></i>")

		photo_label = QLabel("<b>Photo :</b>")
		self.photo_line_edit = QLineEdit()
		self.photo_browse = QPushButton("Browse")

		exe_label = QLabel("<b>Exe :</b>")
		self.exe_line_edit = QLineEdit()
		self.exe_browse = QPushButton("Browse")

		save_path_label = QLabel("<b>Save Path :</b>")
		self.save_path_line_edit = QLineEdit()
		self.save_path_browse = QPushButton("Browse")


		start_button = QPushButton("Start")
		exit_button = QPushButton("Exit")

		self.setLayout(layout)
		
		layout.addWidget(photo_label, 0, 0)
		layout.addWidget(self.photo_line_edit, 0, 1)
		layout.addWidget(self.photo_browse, 0,3)

		layout.addWidget(exe_label, 1, 0)
		layout.addWidget(self.exe_line_edit, 1, 1)
		layout.addWidget(self.exe_browse, 1, 3)

		layout.addWidget(save_path_label, 3, 0)
		layout.addWidget(self.save_path_line_edit, 3, 1)
		layout.addWidget(self.save_path_browse, 3, 3)

		layout.addWidget(self.result_label, 10, 0)

		layout.addWidget(start_button, 11, 3)
		layout.addWidget(exit_button, 12, 3)

		self.photo_line_edit.setPlaceholderText("Image File Path")
		self.exe_line_edit.setPlaceholderText("Executable File Path")
		self.save_path_line_edit.setPlaceholderText("Save Location")

		self.photo_browse.clicked.connect(self.photobrowser)
		self.exe_browse.clicked.connect(self.exebrowser)
		self.save_path_browse.clicked.connect(self.savePathBrowser)
		start_button.clicked.connect(self.binder)
		exit_button.clicked.connect(self.close)
		self.setFocus()
			



	def photobrowser(self):
		open_photo = QFileDialog.getOpenFileName(self, caption="Select your photo", directory='../', filter="Images (*.jpg *.jpeg *.png)")
		self.photo_line_edit.setText(open_photo)

	def exebrowser(self):
		open_exe = QFileDialog.getOpenFileName(self, caption="Open Executable File", directory='../', filter="Executable File (*.exe)")
		self.exe_line_edit.setText(open_exe)

	def savePathBrowser(self):
		save_final = QFileDialog.getSaveFileName(self, caption="Save As Picture", directory='../', filter="Images (*.jpg *.jpeg *.png)")
		self.save_path_line_edit.setText(save_final)



	def binder(self):
		t1 = self.photo_line_edit.text().replace("/", "\\")
		l1 = self.exe_line_edit.text().replace("/", "\\")
		l2 = self.save_path_line_edit.text().replace("/", "\\")
		command = "copy/b "+t1+" + "+l1+" "+l2 
		
		if os.system(command) == 0:
			self.result_label.setText("<b>Binding Completed</b>")
		else:
			self.result_label.setText("<b>Binding Failed</b>")

		self.photo_line_edit.setText("")
		self.exe_line_edit.setText("")
		self.save_path_line_edit.setText("")

app = QApplication(sys.argv)
dialog = EgexMe()
dialog.show()
app.setWindowIcon(QIcon('092.ico'))
app.exec_()
