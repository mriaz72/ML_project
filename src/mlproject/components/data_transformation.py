import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import os


@dataclass
class DataTranformstionConfig:
    preprocessor_obj_file_path  = os.join('artifacts', 'preprocessor.pkl')
    