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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplicacion", pos = wx.DefaultPosition, size = wx.Size( 912,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
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
		self.Bind( wx.EVT_MENU, self.onQuit, id = self.salir.GetId() )
		self.Bind( wx.EVT_MENU, self.onAcercaDe, id = self.acercaDe.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onQuit( self, event ):
		event.Skip()
	
	def onAcercaDe( self, event ):
		event.Skip()
	

###########################################################################
## Class MainPanelUI
###########################################################################

class MainPanelUI ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 912,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer53 = wx.BoxSizer( wx.VERTICAL )
		
		self.PanelPrincipal = wx.StaticText( self, wx.ID_ANY, u"Panel Principal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PanelPrincipal.Wrap( -1 )
		bSizer53.Add( self.PanelPrincipal, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer53, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.PanelLibros = wx.Button( self, wx.ID_ANY, u"Panel Libros", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		bSizer10.Add( self.PanelLibros, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.PanelPag2UI = wx.Button( self, wx.ID_ANY, u"Panel Página 2", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		bSizer10.Add( self.PanelPag2UI, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer8.Add( bSizer10, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer11, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		# Connect Events
		self.PanelLibros.Bind( wx.EVT_BUTTON, self.onPanelLibros )
		self.PanelPag2UI.Bind( wx.EVT_BUTTON, self.onPanelPag2 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onPanelLibros( self, event ):
		event.Skip()
	
	def onPanelPag2( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelLibrosUI
###########################################################################

class PanelLibrosUI ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 912,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer50 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Panel Libros", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer50.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer6.Add( bSizer50, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7.SetMinSize( wx.Size( -1,650 ) ) 
		
		bSizer7.Add( ( 0, 450), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer7, 1, wx.ALL|wx.EXPAND, 1 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.addRecordBtn = wx.Button( self, wx.ID_ANY, u"Añadir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addRecordBtn.SetMinSize( wx.Size( -1,40 ) )
		
		bSizer54.Add( self.addRecordBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.editRecordBtn = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.editRecordBtn.SetMinSize( wx.Size( -1,40 ) )
		
		bSizer54.Add( self.editRecordBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.deleteRecordBtn = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.deleteRecordBtn.SetMinSize( wx.Size( -1,40 ) )
		
		bSizer54.Add( self.deleteRecordBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.showAllBtn = wx.Button( self, wx.ID_ANY, u"Mostrar Todos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.showAllBtn.SetMinSize( wx.Size( -1,40 ) )
		
		bSizer54.Add( self.showAllBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer54, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		categoriesChoices = [ u"Autor", u"Titulo", u"ISBN", u"Editor" ]
		self.categories = wx.ComboBox( self, wx.ID_ANY, u"Autor", wx.DefaultPosition, wx.DefaultSize, categoriesChoices, 0 )
		self.categories.SetMinSize( wx.Size( -1,30 ) )
		
		bSizer4.Add( self.categories, 0, wx.ALL, 5 )
		
		self.search = wx.SearchCtrl( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search.ShowSearchButton( True )
		self.search.ShowCancelButton( False )
		self.search.SetMinSize( wx.Size( 200,30 ) )
		
		bSizer4.Add( self.search, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer4, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAtras = wx.Button( self, wx.ID_ANY, u"Atras", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		bSizer55.Add( self.btnAtras, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer9.Add( bSizer55, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer9, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		# Connect Events
		self.addRecordBtn.Bind( wx.EVT_BUTTON, self.onAgregarRegistro )
		self.editRecordBtn.Bind( wx.EVT_BUTTON, self.onEditarRegistro )
		self.deleteRecordBtn.Bind( wx.EVT_BUTTON, self.onEliminarRegistro )
		self.showAllBtn.Bind( wx.EVT_BUTTON, self.onMostrarTodosRegistros )
		self.search.Bind( wx.EVT_TEXT, self.onBuscar )
		self.btnAtras.Bind( wx.EVT_BUTTON, self.onBtnAtras )
	
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
	
	def onBtnAtras( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelPag2UI
###########################################################################

class PanelPag2UI ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer56.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Pagina Dos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer17.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer15.Add( bSizer17, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BtnAtras = wx.Button( self, wx.ID_ANY, u"Atras", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.BtnAtras, 0, wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, 5 )
		
		
		bSizer15.Add( bSizer18, 0, wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer56.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer56 )
		self.Layout()
		
		# Connect Events
		self.BtnAtras.Bind( wx.EVT_BUTTON, self.onBtnAtras )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onBtnAtras( self, event ):
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
	

