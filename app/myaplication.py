# -*- coding: utf-8 -*-
import wx
import AgregarEditarRegistro
import commonDlgs
import controller
from mygui import BookFrame
from ObjectListView import ObjectListView, ColumnDefn

class MyApplication(BookFrame):
    def __init__(self, *args, **kargs):
        BookFrame.__init__(self, *args, **kargs)

        ##**put here all your Bind()**

        try:
            self.bookResults = controller.getAllRecords()
        except:
            self.bookResults = []

        #listado libros sin crear objeto desde la interfaz grafica
        self.bookResultsOlv = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER, size = wx.Size( 912,300 ),)
        self.bookResultsOlv.SetEmptyListMsg("Registros no encontrados")
        self.setBooks()

    #####################
    # eventos al pulsar #
    #####################

    def onAgregarRegistro( self, event ):
        """
        Añadimos registro en la base de datos
        """
        dlg = AgregarEditarRegistro.AgregarEditarRegistroDialog()
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
        dlg = AgregarEditarRegistro.AgregarEditarRegistroDialog(selectedRow, title="Modificar",
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
        filterChoice = self.categories.GetValue()
        keyword = self.search.GetValue()
        print "%s %s" % (filterChoice, keyword)
        self.bookResults = controller.searchRecords(filterChoice, keyword)
        self.setBooks()

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

    #salir de la aplicacion desde el menu
    def onQuit(self, e):
        self.Close()


if __name__ == '__main__':

    app = wx.PySimpleApp()
    frame = MyApplication(None)
    frame.Show()
    app.MainLoop()   