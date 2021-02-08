import re
from pathlib import Path

def filter_file(file_path):
    """Return True if file_path is a .xlsx or .xlsm file

    :file_path: (str) file path detected by watchdog 
    :returns: (bool) if file is .xlsx or .xlsm
    """
    return bool(re.search(r'\.xls[mx]$', file_path))
