from ptsmtplib import Chaldea
from ptvarmonitor import VarMonitor
from ptvarmonitor import PyStruct as struct

if __name__ == '__main__':
    mail = Chaldea('jrh4dy@virginia.edu')
    monitor = VarMonitor(config_dir='config')
    data = monitor.read_config_files('config')

    #message = "Hey there, python test."
    #mail.send_message(message)
