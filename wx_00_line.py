#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copy Right: suyibin
# CreateDate: 2017/7/1
# 画一条线
import wx


class Example(wx.Frame):
	def __init__(self, title):
		super(Example, self).__init__(None, title=title, size=(250,150))
		
		# 绑定渲染窗口的动作到OnPaint
		# 这样当resize窗口，会重新调用该函数（在未定义绑定前没有看到线，可能是跑位消失了）
		self.Bind(wx.EVT_PAINT, self.OnPaint)

		self.Centre()
		self.Show()

	def OnPaint(self, e):
		dc = wx.ClientDC(self)
		# 画一条线，参数为起始点的x,y,终点的x,y
		dc.DrawLine(50, 60, 190, 60)

		dc.DrawLines(((20,80),(100,80),(100,70),(20,70),(20,80)))

if __name__ == '__main__':
	app = wx.App()
	Example('Line')
	app.MainLoop()
