import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.logger.logging import logging
from src.exception.exception import customexception

from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error