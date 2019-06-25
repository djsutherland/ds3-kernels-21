#!/usr/bin/env python
import json
import sys

nb = json.load(sys.stdin)
for cell in nb["cells"]:
    if "execution_count" in cell:
        cell["execution_count"] = None
    if "outputs" in cell:
        cell["outputs"] = []

json.dump(nb, sys.stdout, sort_keys=1, indent=1, separators=(",", ": "))
