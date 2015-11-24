from Tkinter import *
import tkMessageBox
import tkSimpleDialog

import struct
import sys, glob # for listing serial ports

try:
    import serial
except ImportError:
    tkMessageBox.showerror('Import error', 'Please install pyserial.')
    raise 
