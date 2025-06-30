import win32gui
import win32con
import math
import ctypes
def get_user32():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    return user32

def get_size(user32):
    return [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

def get_pos(user32):
    return [user32.GetSystemMetrics(76), user32.GetSystemMetrics(77)]

def get_hdc():
    return win32gui.GetDC(0)

def get_window_hdc():
    return win32gui.GetWindowDC(win32gui.GetDesktopWindow())

def get_gdi_data():
    size = get_size(get_user32())
    return get_window_hdc(), size[0], size[1]

def shake(angle: int = 0, size: int = 1, speed: int = 5):
    """shake/pan your screen"""
    hdc, w, h = get_gdi_data()
    dx = dy = 1
    angle = angle
    size = size
    speed = speed
    
    while True:
        win32gui.BitBlt(hdc, 0, 0, w, h, hdc, dx, dy, win32con.SRCCOPY)
        dx = math.ceil(math.sin(angle) * size * 10)
        dy = math.ceil(math.cos(angle) * size * 10)
        angle += speed / 10
        if angle > math.pi :
            angle = math.pi * -1
        print(dx, dy, angle)
shake()