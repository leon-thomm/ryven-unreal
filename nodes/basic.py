from ryvencore_qt import *


class NodeBase(Node):
    identifier_prefix = 'basic'


class ValNode(NodeBase):
    title = 'val'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Data(size='s'))
    ]
    init_outputs = [
        NodeOutputBP()
    ]
    style = 'small'

    def place_event(self):
        self.set_display_title('')
        self.update()

    def update_event(self, inp=-1):
        self.set_output_val(0, self.input(0))


export_nodes = [
    ValNode,
]
