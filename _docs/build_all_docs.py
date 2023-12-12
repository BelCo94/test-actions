import sys
import os


_DIR = os.path.dirname(os.path.realpath(__file__))

INDEX_TEXT = """
Test doc
=========================================
"""


def main():
  os.makedirs(os.path.join(_DIR, "source"), exist_ok=True)
  with open(os.path.join(_DIR, "source", "index.rst"), "w") as f:
    f.write(INDEX_TEXT)

if __name__ == "__main__":
  sys.exit(main())
