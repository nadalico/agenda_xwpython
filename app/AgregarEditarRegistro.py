# -*- coding: utf-8 -*-
import commonDlgs
import controller
import wx
from AgregarEditarRegistroVista import AgregarEditarRegistroDialog as AgEdFrame

class AgregarEditar(AgEdFrame):
    def __init__(self, *args, **kargs):
        AgEdFrame.__init__(self, *args, **kargs)

    #----------------------------------------------------------------------
    def getData(self):
        """"""
        authorDict = {}
        bookDict = {}
                        
        fName = self.authorFirstTxt.GetValue()
        lName = self.authorLastTxt.GetValue()
        title = self.titleTxt.GetValue()
        isbn = self.isbnTxt.GetValue()
        publisher = self.publisherTxt.GetValue()
        
        if fName == "" or title == "":
            commonDlgs.showMessageDlg("El Autor y el título es requerido!",
                                      "Error!")
            return
            
        if "-" in isbn:
            isbn = isbn.replace("-", "")
        authorDict["first_name"] = fName
        authorDict["last_name"] = lName
        bookDict["title"] = title
        bookDict["isbn"] = isbn
        bookDict["publisher"] = publisher
        
        return authorDict, bookDict
            
    #----------------------------------------------------------------------
    def onAdd(self):
        """
        Add the record to the database
        """
        authorDict, bookDict = self.getData()
        data = ({"author":authorDict, "book":bookDict})
        controller.addRecord(data)
        
        # show dialog upon completion
        commonDlgs.showMessageDlg("Libro añadido correctamente!",
                                  "Correcto!", wx.ICON_INFORMATION)
        
        # clear dialog so we can add another book
        for child in self.GetChildren():
            if isinstance(child, wx.TextCtrl):
                child.SetValue("")
        
    #----------------------------------------------------------------------
    def onClose(self, event):
        """
        Cancel the dialog
        """
        self.Destroy()
        
    #----------------------------------------------------------------------
    def onEdit(self):
        """"""
        authorDict, bookDict = self.getData()
        comboDict = dict(authorDict.items() + bookDict.items())
        controller.editRecord(self.selectedRow.id, comboDict)
        commonDlgs.showMessageDlg("Libro Editado Satisfactoriamente!", "Correcto!",
                                  wx.ICON_INFORMATION)
        self.Destroy()
        
    #----------------------------------------------------------------------
    def onRecord(self, event):
        """"""
        if self.addRecord:
            self.onAdd()
        else:
            self.onEdit()
        self.titleTxt.SetFocus()
        
    #----------------------------------------------------------------------
    def rowBuilder(self, widgets):
        """"""
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        lbl, txt = widgets
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(txt, 1, wx.EXPAND|wx.ALL, 5)
        return sizer
            
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    dlg = AgregarEditar()
    dlg.ShowModal()
    app.MainLoop()