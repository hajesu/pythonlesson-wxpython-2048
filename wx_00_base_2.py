#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copy Right: suyibin
# CreateDate: 2017/7/1
# 实例化2
# 定义Frame子类方式，结果与wx_00_base.py一致
import wx


class Example(wx.Frame):
	def __init__(self, title):
		super(Example, self).__init__(None, title=title, size=(600,400))
		self.Centre()
		self.Show()

if __name__ == '__main__':
	app = wx.App()
	Example('Shapes')
	app.MainLoop()