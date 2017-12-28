# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 27 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

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
		
		self.editRecordBtn = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.editRecordBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.deleteRecordBtn = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.deleteRecordBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.showAllBtn = wx.Button( self, wx.ID_ANY, u"Mostrar Todos", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.showAllBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		btnSizer.Add( bSizer9, 1, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER, 5 )
		
		categoriesChoices = [ u"Autor", u"Título", u"ISBN", u"Editor" ]
		self.categories = wx.ComboBox( self, wx.ID_ANY, u"Autor", wx.DefaultPosition, wx.DefaultSize, categoriesChoices, 0 )
		btnSizer.Add( self.categories, 0, wx.ALL, 5 )
		
		self.search = wx.SearchCtrl( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search.ShowSearchButton( True )
		self.search.ShowCancelButton( False )
		btnSizer.Add( self.search, 0, wx.ALL, 5 )
		
		
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
		self.addRecordBtn.Bind( wx.EVT_BUTTON, self.onAgregarRegistro )
		self.editRecordBtn.Bind( wx.EVT_BUTTON, self.onEditarRegistro )
		self.deleteRecordBtn.Bind( wx.EVT_BUTTON, self.onEliminarRegistro )
		self.showAllBtn.Bind( wx.EVT_BUTTON, self.onMostrarTodosRegistros )
		self.search.Bind( wx.EVT_TEXT, self.onBuscar )
		self.Bind( wx.EVT_MENU, self.onQuit, id = self.salir.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onAgregarRegistro( self, event ):
		event.Skip()
	
	def onEditarRegistro( self, event ):
		event.Skip()
	
	def onEliminarRegistro( self, event ):
		event.Skip()
	
	def onMostrarTodosRegistros( self, event ):
		event.Skip()
	
	def onBuscar( self, event ):
		event.Skip()
	
	def onQuit( self, event ):
		event.Skip()
	

