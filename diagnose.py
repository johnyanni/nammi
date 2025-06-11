#!/usr/bin/env python
import sys
print(f"Python: {sys.version}")
print(f"Executable: {sys.executable}")

try:
    import manim
    print(f"Manim: {manim.__version__} from {manim.__file__}")
except Exception as e:
    print(f"Manim error: {e}")

try:
    import manim.__main__
    print("Manim main: OK")
except Exception as e:
    print(f"Manim main error: {e}")

try:
    from manim.cli.main import CLI
    print("Manim CLI: OK")
except Exception as e:
    print(f"Manim CLI error: {e}")