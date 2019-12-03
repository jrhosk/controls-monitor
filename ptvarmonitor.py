import pandas as pd
import numpy as np
import matplotlib as plt

class VarMonitor(object):
    def __init__(self, *args, **kawgs):
        self.config = 'config'

        if "config_dir" in kawgs:
            self.config = kawgs["config_dir"]
        else:
            self.config = "config"
    def read_config_files(self, file):
        data = pd.read_csv('{config}/{file}'.format(config=self.config, file=file), delimiter=',')
        print(data)

class PyStruct(object):
    def __init__(self, *args, **kawgs):
        self.name = kawgs["name"]
        self.epics_name = kawgs["epics_name"]
        self.upper_bound = kawgs["upper_bound"]
        self.lower_bound = kawgs["lower_bound"]