# -*- coding: utf-8 -*- 
# addModRecord.py

import wx

########################################################################
class AgregarEditarRegistroDialog(wx.Dialog):
    """
    Add / Modify Record dialog
    """

    #----------------------------------------------------------------------
    def __init__(self, row=None, title="Añadir", addRecord=True):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="%s Registro" % title)
        self.addRecord = addRecord
        self.selectedRow = row
        if row:
            bTitle = self.selectedRow.title
            fName = self.selectedRow.first_name
            lName = self.selectedRow.last_name
            isbn = self.selectedRow.isbn
            publisher = self.selectedRow.publisher
        else:
            bTitle = fName = lName = isbn = publisher = ""
        size = (80, -1)
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD) 
        
        # create the sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        authorSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                
        # create some widgets
        
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD) 
        titleLbl = wx.StaticText(self, label="Título:", size=size)
        titleLbl.SetFont(font)
        self.titleTxt = wx.TextCtrl(self, value=bTitle)
        mainSizer.Add(self.rowBuilder([titleLbl, self.titleTxt]), 
                      0, wx.EXPAND)
        
        authorLbl = wx.StaticText(self, label="Autor:", size=size)
        authorLbl.SetFont(font)
        authorSizer.Add(authorLbl, 0, wx.ALL, 5)
        self.authorFirstTxt = wx.TextCtrl(self, value=fName)
        authorSizer.Add(self.authorFirstTxt, 1, wx.EXPAND|wx.ALL, 5)
        self.authorLastTxt = wx.TextCtrl(self, value=lName)
        authorSizer.Add(self.authorLastTxt, 1, wx.EXPAND|wx.ALL, 5)
        mainSizer.Add(authorSizer, 0, wx.EXPAND)
        
        isbnLbl = wx.StaticText(self, label="ISBN:", size=size)
        isbnLbl.SetFont(font)
        self.isbnTxt = wx.TextCtrl(self, value=isbn)
        mainSizer.Add(self.rowBuilder([isbnLbl, self.isbnTxt]),
                      0, wx.EXPAND)
        
        publisherLbl = wx.StaticText(self, label="Editor:", size=size)
        publisherLbl.SetFont(font)
        self.publisherTxt = wx.TextCtrl(self, value=publisher)
        mainSizer.Add(self.rowBuilder([publisherLbl, self.publisherTxt]),
                      0, wx.EXPAND)
        
        okBtn = wx.Button(self, label="%s Libro" % title)
        okBtn.Bind(wx.EVT_BUTTON, self.onRecord)
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        cancelBtn = wx.Button(self, label="Cerrar")
        cancelBtn.Bind(wx.EVT_BUTTON, self.onClose)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)
        
        mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(mainSizer)
        
    