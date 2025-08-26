#!/usr/bin/env python
"""Local manage.py for the courses app to run management commands from the courses folder.
This delegates to the same settings module used by the project.
"""
import os
import sys
from pathlib import Path

# Make sure the project root (django_tool) is on sys.path when running manage.py
# so imports like 'app2' and project settings can be found when running from this folder.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app2.app2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
