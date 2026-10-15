#!/usr/bin/env python3
"""Print Berean Standard Bible text for references: python3 tools/verse.py "John 3:16" "Romans 8:38–39" """
import sys, importlib.util, os
spec = importlib.util.spec_from_file_location("b", os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_cards.py"))
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
bible = b.load_bible()
for r in sys.argv[1:]:
    try: print(r, "|", b.scripture(r, bible))
    except Exception as ex: print("ERROR", ex)
