import sys
import os
import unreal

sys.path.append(os.path.dirname(__file__))
from editor import init_editor

editor, session = init_editor()

unreal.parent_external_window_to_slate(editor.winId())
