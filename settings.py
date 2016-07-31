import os 
from os.path import join


class GLOBAL_DIR:
    ROOT_DIR = os.getcwd()
    DATA_DIR = join(ROOT_DIR, "data")
    PROCESSED_DIR = join(ROOT_DIR, "processed")

class CONFIG:
    MIN_TRACK_QUARTERS = 4
    TARGET = "foreclosure_status"
    NON_PREDICTORS = [TARGET, "id"]
    CV_FOLDS = 5

