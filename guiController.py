# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Лабораторная 10", pos = wx.DefaultPosition, size = wx.Size( 328,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 328,300 ), wx.Size( 328,300 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.wxStaticTextUslovie = wx.StaticText( self, wx.ID_ANY, u"Найти максимальный элемент второй строки.\nЕсли он больше первого элемента третьей строки,\nто поменять элементы местами.", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.wxStaticTextUslovie.Wrap( -1 )

		self.wxStaticTextUslovie.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.wxStaticTextUslovie, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.wxGridMyArray = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,120 ), 0 )

		# Grid
		self.wxGridMyArray.CreateGrid( 4, 5 )
		self.wxGridMyArray.EnableEditing( True )
		self.wxGridMyArray.EnableGridLines( True )
		self.wxGridMyArray.EnableDragGridSize( False )
		self.wxGridMyArray.SetMargins( 0, 0 )

		# Columns
		self.wxGridMyArray.SetColSize( 0, 60 )
		self.wxGridMyArray.SetColSize( 1, 60 )
		self.wxGridMyArray.SetColSize( 2, 60 )
		self.wxGridMyArray.SetColSize( 3, 60 )
		self.wxGridMyArray.SetColSize( 4, 60 )
		self.wxGridMyArray.EnableDragColMove( False )
		self.wxGridMyArray.EnableDragColSize( True )
		self.wxGridMyArray.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.wxGridMyArray.SetRowSize( 0, 30 )
		self.wxGridMyArray.SetRowSize( 1, 30 )
		self.wxGridMyArray.SetRowSize( 2, 30 )
		self.wxGridMyArray.SetRowSize( 3, 30 )
		self.wxGridMyArray.EnableDragRowSize( True )
		self.wxGridMyArray.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.wxGridMyArray.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.wxGridMyArray.SetDefaultCellFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.wxGridMyArray.SetDefaultCellAlignment( wx.ALIGN_RIGHT, wx.ALIGN_CENTER )
		bSizer1.Add( self.wxGridMyArray, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.wxStaticTextMaxItem = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.wxStaticTextMaxItem.Wrap( -1 )

		bSizer1.Add( self.wxStaticTextMaxItem, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.wxButtonRandom = wx.Button( self, wx.ID_ANY, u"Случайные\nчисла", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.wxButtonRandom, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.wxButtonSolver = wx.Button( self, wx.ID_ANY, u"Решить\nзадачу", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.wxButtonSolver, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.myFrameOnActivate )
		self.Bind( wx.EVT_CLOSE, self.myFrameOnClose )
		self.wxButtonRandom.Bind( wx.EVT_BUTTON, self.wxButtonRandomOnButtonClick )
		self.wxButtonSolver.Bind( wx.EVT_BUTTON, self.wxButtonSolverOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def myFrameOnActivate( self, event ):
		event.Skip()

	def myFrameOnClose( self, event ):
		event.Skip()

	def wxButtonRandomOnButtonClick( self, event ):
		event.Skip()

	def wxButtonSolverOnButtonClick( self, event ):
		event.Skip()


