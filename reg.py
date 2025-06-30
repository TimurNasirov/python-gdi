import winreg as reg

def lock_personalization_settings(disable=True):
    #by EZIKALEXANDR (https://github.com/EZIKALEXANDR/HackerDoomsday/)
    active_desktop_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\ActiveDesktop"
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, active_desktop_path, 0, reg.KEY_SET_VALUE)
    except FileNotFoundError:
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, active_desktop_path)

    reg.SetValueEx(key, "NoChangingWallPaper", 0, reg.REG_DWORD, int(disable))
    reg.SetValueEx(key, "NoChangingColor", 0, reg.REG_DWORD, int(disable))
    reg.CloseKey(key)

    explorer_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, explorer_path, 0, reg.KEY_SET_VALUE)
    except FileNotFoundError:
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, explorer_path)

    reg.SetValueEx(key, "NoThemesTab", 0, reg.REG_DWORD, int(disable))
    reg.CloseKey(key)

def set_accent_color(accent):
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\DWM", 0, reg.KEY_SET_VALUE)
    except FileNotFoundError:
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\DWM")
    reg.SetValueEx(key, "AccentColor", 0, reg.REG_DWORD, accent) # set accent color
    reg.SetValueEx(key, "ColorPrevalence", 0, reg.REG_DWORD, 1) # enable accent color using
    reg.SetValueEx(key, "ColorizationColor", 0, reg.REG_DWORD, accent) # set background color
    reg.CloseKey(key)

def set_window_transaprency(transparency: int = 50):
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\DWM", 0, reg.KEY_SET_VALUE)
    except FileNotFoundError:
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\DWM")

    reg.SetValueEx(key, "ColorizationTransparency", 0, reg.REG_DWORD, transparency)
    reg.CloseKey(key)

def set_window_bg_color(color):
    # Color format: '255 0 0'
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\Colors", 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(key, 'Window', 0, reg.REG_SZ, color)
    reg.CloseKey(key)

