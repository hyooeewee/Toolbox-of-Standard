import os


def get_desktop_path():  # 获取桌面的路径，作为默认存储路径
    home_path = os.path.expanduser("~")
    if os.name == "posix":  # macOS or Linux
        desktop_path = os.path.join(home_path, "Desktop")
    elif os.name == "nt":  # Windows
        desktop_path = os.path.join(home_path, "Desktop")
    else:
        desktop_path = None
    return desktop_path

