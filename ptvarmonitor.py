import pandas as pd
import numpy as np
import matplotlib as plt
import glob
from dataclasses import dataclass


class VarMonitor(object):
    def __init__(self, *args, **kawgs):
        self.config = 'config'
        self.monitor = []

        if "config_dir" in kawgs:
            self.config = kawgs["config_dir"]
        else:
            pass
    def read_config_files(self, config:str)->pd.DataFrame:
        """Reads in all configuration files from defined directory. Files are read into a custom "c-like" data
        structure, PyStruct and appended to monitor class attribute. Function returns a PANDAS DataFrame object."""

        for file in glob.glob('{config}/*.config'.format(config=config)):
            data = pd.read_csv('{file}'.format(file=file), delimiter=',').replace(' ', np.nan)
            self.monitor.append(PyStruct(data['variable_name'][0],
                           data['epics_name'][0],
                           data['upper_bound'][0],
                           data['lower_bound'][0]))
        return data

@dataclass
class PyStruct:
        name: str = ''
        epics_name: str = ''
        upper_bound: float = 0.0
        lower_bound: float = 0.0