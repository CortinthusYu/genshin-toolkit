from pathlib import Path


root=Path('.')
if not (root/'Output').exists():
    (root/'Output').mkdir()
if not root.joinpath('Output','dataparser').exists():
    root.joinpath('Output','dataparser').mkdir()