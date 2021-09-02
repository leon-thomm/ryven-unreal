import sys
import os
import unreal

sys.path.append(os.path.dirname(__file__))
from editor import Editor
from styling.window_theme import apply_stylesheet

from PySide2.QtWidgets import QDialog, QHBoxLayout, QApplication


class EditorWindow(QDialog):
    # I have to define the below instantiated window here to prevent the garbage
    # collector from removing it immediately; which it does when the class is
    # imported.
    # so I just keep the window here but the actual editor widget is in editor.py

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Ryven Editor')

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(Editor())


app = None
if not QApplication.instance():
    app = QApplication(sys.argv)

# I could not find any Qt-compatible stylesheets of the UE4 editor frontend
apply_stylesheet('dark')

editor_window = EditorWindow()
editor_window.show()
unreal.parent_external_window_to_slate(editor_window.winId())
