from Files_preparation import *
from Files_reading import *
from Files_define import *
from Files_writing import *
from Clean import *
from Function_define import *
from Charts_show import *


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Package your_project initialized")

__version__ = "1.0.0"
__author__ = "Waller Tsai"
__time__="2024-07-03"
