## @package win32gui,win32api,win32con,time,win32clipboard,sys
#  Documentation for this module.
#  
#  轰炸微信的好友
#  deluging your friend on Wechat with python
#  More details.
import win32gui
import win32api
import win32con
import time
import win32clipboard
import sys


## Documentation for a function.
#
# 设置和粘贴剪贴板
def ClipboardText(aString):
    # 设置剪贴板
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(aString, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    time.sleep(0.3)
    # 将剪贴板文本进行粘贴
    # ctrl键位码是17
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    # v键位码是86
    win32api.keybd_event(ord('V'), 0, 0, 0)
    # 释放CTRL按键
    win32api.keybd_event(win32con.VK_CONTROL, 0,
                         win32con.KEYEVENTF_KEYUP, 0)
    # 释放V键
    win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_KEYUP, 0)

## Documentation for a function.
#
# 搜索微信好友或者微信群
def search(wxname):
    if win != 0:
        # 获取控制
        win32gui.SetForegroundWindow(win)
        # 模拟按下Ctrl+F快捷键,ctrl+f搜索
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        win32api.keybd_event(ord('F'), 0, 0, 0)
        win32api.keybd_event(ord('F'), 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(win32con.VK_CONTROL, 0,
                             win32con.KEYEVENTF_KEYUP, 0)
        ClipboardText(wxname)
        time.sleep(0.5)
        # 模拟按下Enter键
        win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
        win32api.keybd_event(win32con.VK_RETURN, 0,
                             win32con.KEYEVENTF_KEYUP, 0)
    else:
        # 模拟按下Enter键
        print(f'请注意：找不到【{wxname}】这个人（或群）！')
        exit()

## Documentation for a function.
#
# 模拟发送动作,alt+s键发送
def SendMsg():
    # Alt键位码18,win32con.VK_MENU键位码代表ALT键
    win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)
    win32api.keybd_event(ord('S'), 0, 0, 0)  # s键位码83
    win32api.keybd_event(win32con.VK_MENU, 0,
                         win32con.KEYEVENTF_KEYUP, 0)  # 释放ALT按键
    win32api.keybd_event(ord('S'), 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放S按键

## Documentation for a function.
#
# 发送文本
def sendText(chatrooms, text,max):
    for chatroom in chatrooms:
        search(chatroom)
        # 文字首行留空，防止带表情复制不完全
        for i in range(0,max):
            ClipboardText(text)
            SendMsg()
    print(f'微信消息:{text} 已发送至:{chatroom}')


## Documentation for a function.
#
# 使用示例:
# python boom_reply.py 备注 消息内容 迭代次数
#
# For example:
# python boom_reply.py zhanggao hello,zhanggao 3
if __name__=="__main__":
    win = win32gui.FindWindow("WeChatMainWndForPC", '微信')# 获取微信主窗口句柄
    title = win32gui.GetWindowText(win)
    className=win32gui.GetClassName(win)
    print(f'找到{className}{title}主窗口句柄:{win}')
    chatrooms = [sys.argv[1]]
    text = sys.argv[2]
    sendText(chatrooms, text, int(sys.argv[3]))