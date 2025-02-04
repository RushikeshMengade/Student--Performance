import os
import sys
from pathlib import Path

configuration={
    f"notbook/data",
    f"src/components/__init__.py",
    f"src/pipeline/__init__py",

}

for locations in configuration:
    os.makedirs(os.path.dirname(locations),exist_ok=True)
    os.path.join(locations)
    