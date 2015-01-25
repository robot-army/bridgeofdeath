#
# Default Settings to not edit, user changes go in settings.py
#
# Copyright 2013 Reading Makerspace Ltd.
# Licence GPL v2
# Authors: Barnaby Shearer <b@Zi.iS>
#
import datetime

EMAIL_SERVER = 'localhost'
EMAIL_FROM = 'rfid@localhost'
        
DEADLINE_OPENING = datetime.timedelta(seconds=30) #Grace prediod to open door
DEADLINE_LOCKING = datetime.timedelta(seconds=30) #before warning
DEADLINE_LOCKING_WARN = datetime.timedelta(seconds=30) #before fail

LDAP_URL = 'ldap://localhost'

SECTOR = 1

ENTER = ('PN532', '/dev/ttyAMA0', 115200)
#ENTER = ('SM130', '/dev/ttyUSBACON0', 19200)
#EXIT = ('SM130', '/dev/ttyUSB1', 19200)
#HD44780 = ('/dev/ttyACM1', 9600)

