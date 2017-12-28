# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# ListadoLibros.py
#
# Author: Javier Nadal
# Contact: jnadalico@outlook.es
#
# This program demonstrates how to work with a SQLite database
# using wxPython and SqlAlchemy. It is also an example of MVC
# concepts and how to put together a fully working wxPython
# application.
# ------------------------------------------------------------

import AgregarEditarRegistro
import commonDlgs
import controller
import wx
from ObjectListView import ObjectListView, ColumnDefn

########################################################################
class BookPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        """try:
            self.bookResults = controller.getAllRecords()
        except:
            self.bookResults = []"""
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        searchSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD) 
        
        # widget selector buscador
        cat = ["Autor", "Título", "ISBN", "Editor"]
        searchByLbl = wx.StaticText(self, label="Buscar por:")
        searchByLbl.SetFont(font)
        searchSizer.Add(searchByLbl, 0, wx.ALL, 5)
        
        self.categories = wx.ComboBox(self, value="Autor", choices=cat)
        searchSizer.Add(self.categories, 0, wx.ALL, 5)
        #widget buscador
        self.search = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.search.Bind(wx.EVT_TEXT_ENTER, self.onSearch)
        searchSizer.Add(self.search, 0, wx.ALL, 5)
        
        self.bookResultsOlv = ObjectListView(self, style=wx.LC_REPORT
                                                        |wx.SUNKEN_BORDER)
        """self.bookResultsOlv.SetEmptyListMsg("Registros no encontrados")
        self.setBooks()"""
        
        # Botón añadir con evento "onAddRecord"
        addRecordBtn = wx.Button(self, label="Añadir")
        addRecordBtn.Bind(wx.EVT_BUTTON, self.onAddRecord)
        btnSizer.Add(addRecordBtn, 0, wx.ALL, 5)
        
        # Botón Editar con evento "onEditRecord"
        editRecordBtn = wx.Button(self, label="Editar")
        editRecordBtn.Bind(wx.EVT_BUTTON, self.onEditRecord)
        btnSizer.Add(editRecordBtn, 0, wx.ALL, 5)
        
        # Botón Eliminar con evento "onDelete"
        deleteRecordBtn = wx.Button(self, label="Eliminar")
        deleteRecordBtn.Bind(wx.EVT_BUTTON, self.onDelete)
        btnSizer.Add(deleteRecordBtn, 0, wx.ALL, 5)
        
        # Botón mostrar todo con evento "onShowAllRecord"
        """showAllBtn = wx.Button(self, label="Mostrar Todo")
        showAllBtn.Bind(wx.EVT_BUTTON, self.onShowAllRecord)
        btnSizer.Add(showAllBtn, 0, wx.ALL, 5)"""
        # Connect Events
        self.showAllBtn = wx.Button( self, wx.ID_ANY, u"Mostrar Todos", wx.DefaultPosition, wx.DefaultSize, 0 )
        btnSizer.Add( self.showAllBtn, 0, wx.ALL, 5 )
        self.showAllBtn.Bind( wx.EVT_BUTTON, self.onShowAllRecord )
        
        mainSizer.Add(searchSizer)
        mainSizer.Add(self.bookResultsOlv, 1, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(mainSizer)

    def __del__( self ):
        pass
        
    #----------------------------------------------------------------------

    #evento para mostrar ventana añadir registro
    def onAddRecord(self, event):
        """
        Add a record to the database
        """
        dlg = AgregarEditarRegistro.AgregarEditarRegistroDialog()
        dlg.ShowModal()
        dlg.Destroy()
        self.showAllRecords()
        
    #----------------------------------------------------------------------

    #evento para mostrar ventana editar registro
    def onEditRecord(self, event):
        """
        Edit a record
        """
        selectedRow = self.bookResultsOlv.GetSelectedObject()
        if selectedRow == None:
            commonDlgs.showMessageDlg("No row selected!", "Error")
            return
        dlg = AgregarEditarRegistro.AgregarEditarRegistroDialog(selectedRow, title="Modify",
                                           addRecord=False)
        dlg.ShowModal()
        dlg.Destroy()
        self.showAllRecords()
        
    #----------------------------------------------------------------------

    #evento para borrar registro
    def onDelete(self, event):
        """
        Delete a record
        """
        selectedRow = self.bookResultsOlv.GetSelectedObject()
        if selectedRow == None:
            commonDlgs.showMessageDlg("No row selected!", "Error")
            return
        controller.deleteRecord(selectedRow.id)
        self.showAllRecords()
        
    #----------------------------------------------------------------------

    #evento para buscar
  
    def onSearch(self, event):
        
        #Searches database based on the user's filter choice and keyword
        
        filterChoice = self.categories.GetValue()
        keyword = self.search.GetValue()
        print "%s %s" % (filterChoice, keyword)
        #self.bookResults = controller.searchRecords(filterChoice, keyword)
        #self.setBooks()
     
    #----------------------------------------------------------------------
    # Virtual event handlers, overide them in your derived class
    def onShowAllRecord( self, event ):
        event.Skip()

    #evento para mostrar registro
    """def onShowAllRecord(self, event):
      
        #Updates the record list to show all of them
        
        self.showAllRecords()
    """    
    #----------------------------------------------------------------------
    """def setBooks(self):
        self.bookResultsOlv.SetColumns([
            ColumnDefn("Título", "left", 350, "title"),
            ColumnDefn("Autor", "left", 150, "author"),
            ColumnDefn("ISBN", "right", 150, "isbn"),
            ColumnDefn("Editor", "left", 150, "publisher")
        ])
        #self.bookResultsOlv.SetObjects(self.bookResults)"""
        
    #----------------------------------------------------------------------
    """def showAllRecords(self):
        
        #Show all records in the object list view control
        
        self.bookResults = controller.getAllRecords()
        self.setBooks()"""
        
########################################################################
class BookFrame(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="APP Libros",
                          size=(800, 600))
        panel = BookPanel(self)
        
        self.Show()
        
#----------------------------------------------------------------------
"""if __name__ == "__main__":
    app = wx.App(False)
    frame = BookFrame()
    app.MainLoop()"""