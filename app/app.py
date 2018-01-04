# -*- coding: utf-8 -*-
import wx
#import AgregarEditarRegistro
#import commonDlgs
#import controller

#clases UI
from mygui import *
from ObjectListView import ObjectListView, ColumnDefn

import AgregarEditarRegistro
import commonDlgs
import controller

"""
Clase panel libros que hereda del UI panel libros
"""
class PanelLibro(PanelLibrosUI):
  def __init__(self,parent):
    PanelLibrosUI.__init__(self,parent)
    self.parent = parent

    try:
        self.bookResults = controller.getAllRecords()
    except:
        self.bookResults = []

    #listado libros sin crear objeto desde la interfaz grafica
    self.bookResultsOlv = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.TE_CENTRE, size=(850,250))
    self.bookResultsOlv.SetEmptyListMsg("Registros no encontrados")
    self.setBooks()

  #####################
  # eventos al pulsar #
  #####################

  def onAgregarRegistro( self, event ):
      """
      Añadimos registro en la base de datos
      """
      dlg = AgregarEditarRegistro.AgregarEditar()
      dlg.ShowModal()
      dlg.Destroy()
      self.mostrarTodosRegistros()

  #evento para mostrar ventana editar registro
  def onEditarRegistro(self, event):
      """
      Editar registro
      """
      selectedRow = self.bookResultsOlv.GetSelectedObject()
      if selectedRow == None:
          commonDlgs.showMessageDlg("Fila no seleccionada!", "Error")
          return
      dlg = AgregarEditarRegistro.AgregarEditar(selectedRow, title="Modificar",
                                         addRecord=False)
      dlg.ShowModal()
      dlg.Destroy()
      self.mostrarTodosRegistros()

  #evento para borrar registro
  def onEliminarRegistro(self, event):
      selectedRow = self.bookResultsOlv.GetSelectedObject()
      if selectedRow == None:
          commonDlgs.showMessageDlg("Fila no seleccionada!", "Error")
          return
      controller.deleteRecord(selectedRow.id)
      self.mostrarTodosRegistros()

  #mostrar registros al pulsar boton "mostrar todos"
  def onMostrarTodosRegistros( self, event ):
      self.mostrarTodosRegistros()

  #evento para buscar
  def onBuscar(self, event):
      """
      Searches database based on the user's filter choice and keyword
      """
      print "entramos en onbuscar"
      filterChoice = self.categories.GetValue()
      print filterChoice
      keyword = self.search.GetValue()
      print "%s %s" % (filterChoice, keyword)
      self.bookResults = controller.searchRecords(filterChoice, keyword)
      self.setBooks()

  def onBtnAtras(self,event):
    parentShow = PanelPrincipal(parent=self.parent)
    parentShow.Show()
    self.Destroy()

  #########################
  # Fin eventos al pulsar #
  #########################

  def setBooks(self):
      self.bookResultsOlv.SetColumns([
          ColumnDefn("Título", "left", 350, "title"),
          ColumnDefn("Autor", "left", 150, "author"),
          ColumnDefn("ISBN", "right", 150, "isbn"),
          ColumnDefn("Editor", "left", 150, "publisher")
      ])
      self.bookResultsOlv.SetObjects(self.bookResults)

  def mostrarTodosRegistros(self):
          
      #Show all records in the object list view control
      
      self.bookResults = controller.getAllRecords()
      self.setBooks()

"""
Clase panel pag dos
"""
class PanelPaginaDos(PanelPag2UI):
  def __init__(self,parent):
    PanelPag2UI.__init__(self, parent)
    self.parent = parent

  def onBtnAtras( self, event ):
    print "prueba"
    parentShowDos = PanelPrincipal(parent=self.parent)
    parentShowDos.Show()
    self.Destroy()

"""
Clase que hereda componentes de la UI del panel principal de la aplicacion
"""
class PanelPrincipal(MainPanelUI):
  def __init__(self,parent):
    MainPanelUI.__init__(self, parent)

    self.parent=parent

    ###########
    # Eventos #
    ###########

  def onPanelLibros( self, event ):
    
    panellibros = PanelLibro(parent=self.parent)
    #panellibros.Centre()
    panellibros.Show()
    self.Hide()

  def onPanelPag2(self,event):
    panelpagdos = PanelPaginaDos(parent=self.parent)
    panelpagdos.Show()
    self.Hide()
    

"""
Clase que hereda componentes de la UI de la ventana principal
"""
class MainApp(MainFrame):
    def __init__(self, *args, **kargs):
        MainFrame.__init__(self, *args, **kargs)

        """
          Cargamos panel principal de la aplicacion al iniciarla
        """
        mainpanel = PanelPrincipal(parent=self)
        #panellibros.Centre()
        mainpanel.Show()

    ###################
    # Menu aplicacion #
    ###################

    #salir de la aplicacion desde el menu
    def onQuit(self, e):
        self.Close()

    def onAcercaDe(self, e):
        print "acerca de"
        aframe = FrameAcercaDe(None)
        aframe.Centre()
        aframe.Show()

    #######################
    # Fin Menu aplicacion #
    #######################
 

"""
  Cargamos ventana principal de la aplicacion
"""

if __name__ == '__main__':

    app = wx.App()
    frame = MainApp(None)
    frame.Show()
    app.MainLoop()  