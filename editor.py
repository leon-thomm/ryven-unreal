from PySide2.QtWidgets import QApplication

import ryven
import sys
from os.path import dirname, normpath, abspath, join


def init_editor():

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    editor = ryven.run_ryven(
        qt_app=app,
        qt_api='pyside2',
        show_dialog=False,
        gui_parent=None,
        window_title='Ryven Unreal',
        window_theme_name='dark',
        flow_theme='pure dark',
    )
    session = editor.session

    loc = dirname(normpath(__file__))
    p = join(loc, 'unreal_nodes')
    editor.import_nodes(path=p)

    session.create_script('main')

    return editor, session
