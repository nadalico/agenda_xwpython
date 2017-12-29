# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 27 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

ID_ACERCA_DE = 1000

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
		
		categoriesChoices = [ u"Autor", u"Titulo", u"ISBN", u"Editor" ]
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
		
		self.ayuda = wx.Menu()
		self.acercaDe = wx.MenuItem( self.ayuda, ID_ACERCA_DE, u"Acerca De...", wx.EmptyString, wx.ITEM_NORMAL )
		self.ayuda.Append( self.acercaDe )
		
		self.m_menubar1.Append( self.ayuda, u"Ayuda" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.addRecordBtn.Bind( wx.EVT_BUTTON, self.onAgregarRegistro )
		self.editRecordBtn.Bind( wx.EVT_BUTTON, self.onEditarRegistro )
		self.deleteRecordBtn.Bind( wx.EVT_BUTTON, self.onEliminarRegistro )
		self.showAllBtn.Bind( wx.EVT_BUTTON, self.onMostrarTodosRegistros )
		self.search.Bind( wx.EVT_TEXT, self.onBuscar )
		self.Bind( wx.EVT_MENU, self.onQuit, id = self.salir.GetId() )
		self.Bind( wx.EVT_MENU, self.onAcercaDe, id = self.acercaDe.GetId() )
	
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
	
	def onAcercaDe( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameAcercaDe
###########################################################################

class FrameAcercaDe ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Acerca de...", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer3.Add( ( 30, 0), 1, wx.EXPAND, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"icons/icon_acerca_de.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"software Realizado por Javier Nadal", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

