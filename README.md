### UnrealEngine 4 Python Plugin for Ryven-like nodes editor

This repo provides a Python plugin to integrate a simple Ryven-like editor, but there are not any nodes yet. **If you know the Unreal Python API, or want to get into it, please consider contributing by creating nodes**.

### setup

Using Unreal Engine's Python installation (probably located in `<UE4 path>/<version>/Engine/Binaries/ThirdParty/Python3/<your OS>/`), install [`ryvencore-qt`](https://github.com/leon-thomm/ryvencore-qt)

```
<UE4 Python location> > python.exe Scripts\pip.exe install ryvencore-qt
```

Alternatively you can create your own virtual env and link UR4's Python to this env's side-packages, but I didn't try that.

Then you just need to execute `__init__.py` from the Unreal Editor via `File > Execute Python Script...`. This should open a new instance of the editor. Do not close this window if you want to keep the content.
