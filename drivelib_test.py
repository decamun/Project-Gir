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

def __init__(self):
    Tk.__init__(self)
    self.title("iRobot Create 2 Tethered Drive")
    self.option_add('*tearOff', FALSE)

    self.menubar = Menu()
    self.configure(menu=self.menubar)

    createMenu = Menu(self.menubar, tearoff=False)
    self.menubar.add_cascade(label="Create", menu=createMenu)

    createMenu.add_command(label="Connect", command=self.onConnect)
    createMenu.add_command(label="Help", command=self.onHelp)
    createMenu.add_command(label="Quit", command=self.onQuit)

    self.text = Text(self, height = TEXTHEIGHT, width = TEXTWIDTH, wrap = WORD)
    self.scroll = Scrollbar(self, command=self.text.yview)
    self.text.configure(yscrollcommand=self.scroll.set)
    self.text.pack(side=LEFT, fill=BOTH, expand=True)
    self.scroll.pack(side=RIGHT, fill=Y)

    self.text.insert(END, helpText)

    self.bind("<Key>", self.callbackKey)
    self.bind("<KeyRelease>", self.callbackKey)

def sendCommandASCII(self, command):
    cmd = ""
    for v in command.split():
        cmd += chr(int(v))

    self.sendCommandRaw(cmd)

# sendCommandRaw takes a string interpreted as a byte array
def sendCommandRaw(self, command):
    global connection

    try:
        if connection is not None:
            connection.write(command)
        else:
            tkMessageBox.showerror('Not connected!', 'Not connected to a robot!')
            print "Not connected."
    except serial.SerialException:
        print "Lost connection"
        tkMessageBox.showinfo('Uh-oh', "Lost connection to the robot!")
        connection = None

    print ' '.join([ str(ord(c)) for c in command ])
    self.text.insert(END, ' '.join([ str(ord(c)) for c in command ]))
    self.text.insert(END, '\n')
    self.text.see(END)
