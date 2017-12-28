# -*- coding: utf-8 -*-

# Importamos módulos necesarios.
import AgregarEditarRegistro
import commonDlgs
import controller
import wx
from ObjectListView import ObjectListView, ColumnDefn
# Importamos directamente la clase MyFrame2.
from ListadoLibrosVista import BookPanel,BookFrame

###################
# Panel principal #
###################

class PanelLibro(BookPanel):
    def __init__(self):
        pass
        """try:
            self.bookResults = controller.getAllRecords()
            print controller.getAllRecords()
        except:
            self.bookResults = []

        self.bookResultsOlv = ObjectListView(self, style=wx.LC_REPORT
                                                        |wx.SUNKEN_BORDER)
        self.bookResultsOlv.SetEmptyListMsg("Registros no encontrados")
        self.setBooks()"""

    
    #----------------------------------------------------------------------

    #evento para mostrar registro
    """def onShowAllRecord(self, event):
       
        #Updates the record list to show all of them
       
        wx.MessageBox("Has hecho click en botón ACEPTAR","",wx.OK)
        #print self.showAllRecords()

    def setBooks(self):
        self.bookResultsOlv.SetColumns([
            ColumnDefn("Título", "left", 350, "title"),
            ColumnDefn("Autor", "left", 150, "author"),
            ColumnDefn("ISBN", "right", 150, "isbn"),
            ColumnDefn("Editor", "left", 150, "publisher")
        ])
        self.bookResultsOlv.SetObjects(self.bookResults)

    def showAllRecords(self):
        
        #Show all records in the object list view control
        
        print "prueba"
        self.bookResults = controller.getAllRecords()
        self.setBooks()"""

class Frame(BookFrame):
        pass

if __name__ == "__main__":
    app = wx.App()
    frame = BookFrame() # llamamos a la clase de la vista
    app.MainLoop()