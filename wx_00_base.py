#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copy Right by suyibin
# CreateDate: 2017/7/1


import wx

# 每个wxPython的程序必须有一个wx.App对象
app = wx.App()

# 实例化一个frame
'''
None: 当前窗口的父窗口parent,如果当前窗口是最顶层的话，则parent=None,如果不是顶层窗口，则他的值为所属frame的名字
-1: id值，-1的话程序会自动产生一个id
pos: 位置
size: 宽，高大小
还有⻛风格参数style,不填默认是这样几几个的组合
wx.MAXIMIZE_BOX| wx.MINIMIZE_BOX| wx.RESIZE_BORDER|wx.SYSTEM_MENU| wx.CAPTION|
wx.CLOSE_BOX
你可以去掉几几个看看效果,比比如
style = wx.SYSTEM_MENU| wx.CAPTION| wx.CLOSE_BOX
'''
frame = wx.Frame(None, -1, title='wx_00_base.py', size=(600,400))	# pos=(300,400),
panel = wx.Panel(frame)
label = wx.StaticText(panel, label='Hello World', pos=(100,100))

# 居中处理
frame.Centre()

# 显示frame
frame.Show()

print "hello world"
print "fff"

# 进入循环，等待窗口响应
app.MainLoop()
