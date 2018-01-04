import wx
from ObjectListView import ObjectListView, ColumnDefn
 
########################################################################
class Results(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, tin, zip_code, plus4, name, address):
        """Constructor"""
        self.tin = tin
        self.zip_code = zip_code
        self.plus4 = plus4
        self.name = name
        self.address = address
 
 
########################################################################
class DCPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
 
        mainSizer = wx.BoxSizer(wx.VERTICAL)
 
        self.test_data = [Results("123456789", "50158", "0065", "Patti Jones",
                                  "111 Centennial Drive"),
                          Results("978561236", "90056", "7890", "Brian Wilson",
                                  "555 Torque Maui"),
                          Results("456897852", "70014", "6545", "Mike Love", 
                                  "304 Cali Bvld")
                          ]
        self.resultsOlv = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.resultsOlv.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onDoubleClick)
 
        self.setResults()
 
        mainSizer.Add(self.resultsOlv, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(mainSizer)
 
    #----------------------------------------------------------------------
    def onDoubleClick(self, event):
        """
        When the item is double-clicked or "activated", do something
        """
        print "in onDoubleClick method"
 
    #----------------------------------------------------------------------
    def setResults(self):
        """"""
        self.resultsOlv.SetColumns([
            ColumnDefn("TIN", "left", 100, "tin"),
            ColumnDefn("Zip", "left", 75, "zip_code"),
            ColumnDefn("+4", "left", 50, "plus4"),
            ColumnDefn("Name", "left", 150, "name"),
            ColumnDefn("Address", "left", 200, "address")
            ])
        self.resultsOlv.CreateCheckStateColumn()
        self.resultsOlv.SetObjects(self.test_data)
 
 
########################################################################
class DCFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Double-click Tutorial")
        panel = DCPanel(self)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = DCFrame()
    frame.Show()
    app.MainLoop()