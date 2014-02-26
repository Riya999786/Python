__author__ = 'Joel Santiago'

# __all__ = ["Battle", "DangerousPath", "Death", "Engine", "Map", "NoPath", "Player", "SafePath"]

import os
import glob
__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]