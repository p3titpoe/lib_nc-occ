import os
import sys

if __name__ == "__main__":
    from pip._internal.cli.main import main as _main

    sys.exit(_main())
