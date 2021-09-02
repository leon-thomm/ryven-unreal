import ryvencore_qt as rc
from nodes.basic import export_nodes as nodes_basic

from os.path import abspath, dirname, join

import unreal

from PySide2.QtWidgets import QWidget, QHBoxLayout
from PySide2.QtCore import Qt


class Editor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.session = rc.Session()
        self.session.design.load_from_config(
            abspath(join(dirname(__file__), 'styling/design_config.json'))
        )
        self.session.register_nodes(
            nodes_basic
        )
        self.script = self.session.create_script(
            title='main',
            create_default_logs=False,
            flow_view_size=[10000, 10000],
        )

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.session.flow_views[self.script])
