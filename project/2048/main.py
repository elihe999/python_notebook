#/usr/local/bin/python3
# -*- coding: utf-8 -*-


"""
None: top parent
-1: id
pos:
size: X Y
/usr/local/Cellar/python/3.7.2_1/bin/python3
"""

import wx

app = wx.App()

frame = wx.Frame(None, -1, title="base", pos=(320, 450), size=(200, 150))

frame.Show(True)
app.MainLoop()

