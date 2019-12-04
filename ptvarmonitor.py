import pandas as pd
import numpy as np
import matplotlib as plt
import glob
from dataclasses import dataclass


class VarMonitor(object):
    def __init__(self, *args, **kawgs):
        self.config = 'config'

        if "config_dir" in kawgs:
            self.config = kawgs["config_dir"]
        else:
            self.config = "config"
    def read_config_files(self, config):
        for file in glob.glob('{config}/*.config'.format(config=config)):
            data = pd.read_csv('{file}'.format(file=file), delimiter=',')
            print(data)
@dataclass
class PyStruct(object):
        name: str
        epics_name: str
        upper_bound: float
        lower_bound: float