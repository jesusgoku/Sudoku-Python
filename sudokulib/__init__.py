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

from .gen_sudoku import *
from .utilidades import *
from .printscreen import *
from .colores import *
from .persistencia import *
from .tableros import *