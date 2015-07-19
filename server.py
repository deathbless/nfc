import pythoncom
import pyHook
import win32gui
import win32api
import win32con

Lcontrol_press = False
Lmenu_press = False
Left_press = False
def OnKeyboardEvent(event):
    global Lcontrol_press
    global Lmenu_press
    global Left_press
    print 'Keydown:',event.Key
    if event.Key == "Lcontrol":
        Lcontrol_press = True
    elif event.Key == "Lmenu":
        Lmenu_press = True
    elif event.Key == "P":
        Left_press = True
    handle_key()
    return True

def OnKeyboardEventreset(event):
    global Lcontrol_press
    global Lmenu_press
    global Left_press
    print 'Keyup:',event.Key
    if event.Key == "Lcontrol":
        Lcontrol_press = False
    elif event.Key == "Lmenu":
        Lmenu_press = False
    elif event.Key == "P":
        Left_press = False
    handle_key()
    return True

def handle_key():
    global Lcontrol_press
    global Lmenu_press
    global Left_press
    if Lmenu_press and Lcontrol_press and Left_press:
        Lcontrol_press = False
        Lmenu_press = False
        Left_press = False
        win32api.keybd_event(0xB0, win32con.VK_MEDIA_NEXT_TRACK, 0, 0)

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.KeyUp = OnKeyboardEventreset
hm.HookKeyboard()
pythoncom.PumpMessages()




# from pymouse import PyMouse
# m = PyMouse()
#
# t = m.position()
# print t
# m.move(500, 500)
# t = m.position()
# print t
# m.click(1000, 500)
# from ctypes import *
# import time
#
# class POINT(Structure):
#      _fields_ = [("x", c_ulong),
#      ("y", c_ulong)]
# orig = POINT()
# windll.user32.GetCursorPos(byref(orig))
# print 'Orig Pos:', orig.x, orig.y
# print 'Move to center of the screen'
# windll.user32.SetCursorPos(1023/2, 767/2)
# time.sleep(1)
# windll.user32.SetCursorPos(orig.x, orig.y)