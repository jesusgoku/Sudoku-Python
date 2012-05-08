from random import shuffle
from random import randint
import time
import re
import os
import sys

try:
    import cPickle as pickle
except ImportError:
    pickle

from .sudoku import *
from .utilidades import *
from .printscreen import *
from .colores import *
from . import gen_sudoku