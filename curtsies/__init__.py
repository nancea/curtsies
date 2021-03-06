"""Terminal-formatted strings"""
__version__='0.3.2'

from .window import FullscreenWindow, CursorAwareWindow
from .input import Input
from .termhelpers import Nonblocking, Cbreak, Termmode # add docstrings
from .formatstring import FmtStr, fmtstr
from .formatstringarray import FSArray, fsarray
