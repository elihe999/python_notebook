# -*- coding: utf-8 -*-

"""
None: top parent
-1: id
pos:
size: X Y

"""

import wx

app = wx.App()

frame = wx.Frame(None, -1, title="base", pos=(320, 450), size=(200, 150))

frame.Show(True)
app.MainLoop()

