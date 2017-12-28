# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 27 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class BookFrame
###########################################################################

class BookFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 912,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		btnSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.addRecordBtn = wx.Button( self, wx.ID_ANY, u"Añadir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.addRecordBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.list_ctrl = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.list_ctrl, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button5, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button6, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.showAllBtn = wx.Button( self, wx.ID_ANY, u"Mostrar Todos", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.showAllBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		btnSizer.Add( bSizer9, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( btnSizer )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.inicio = wx.Menu()
		self.salir = wx.MenuItem( self.inicio, wx.ID_EXIT, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
		self.inicio.Append( self.salir )
		
		self.m_menubar1.Append( self.inicio, u"Inicio" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.showAllBtn.Bind( wx.EVT_BUTTON, self.onShowAllRecord )
		self.Bind( wx.EVT_MENU, self.onQuit, id = self.salir.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onShowAllRecord( self, event ):
		event.Skip()
	
	def onQuit( self, event ):
		event.Skip()
	

