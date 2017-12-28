# -*- coding: utf-8 -*-

# Importamos módulos necesarios.
import wx

import controller
from ObjectListView import ObjectListView, ColumnDefn

# Importamos la vista directamente la clase MyFrame2.
from noname import BookFrame

 
class Car(object):
    """"""
 
    def __init__(self, make, model, year, color="Blue"):
        """Constructor"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color

#heredamos la vista
class PanelLibro(BookFrame):

	def __init__(self, parent, title):
		BookFrame.__init__(self, parent)

		try:
			bookResults = controller.getAllRecords()
		except:
			bookResults = []

		rows = [Car("Ford", "Taurus", "1996"),
		        Car("Nissan", "370Z", "2010"),
		        Car("Porche", "911", "2009", "Red")
		        ]
		self.list_ctrl = wx.ListCtrl(self, size=(-1,100),style=wx.LC_REPORT |wx.BORDER_SUNKEN)
		self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
		self.list_ctrl.InsertColumn(0, "Make")
		self.list_ctrl.InsertColumn(1, "Model")
		self.list_ctrl.InsertColumn(2, "Year")
		self.list_ctrl.InsertColumn(3, "Color")

		index = 0
		self.myRowDict = {}
		for row in rows:
			self.list_ctrl.InsertStringItem(index, row.make)
			self.list_ctrl.SetStringItem(index, 1, row.model)
			self.list_ctrl.SetStringItem(index, 2, row.year)
			self.list_ctrl.SetStringItem(index, 3, row.color)
			self.myRowDict[index] = row
			index += 1

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
		self.SetSizer(sizer)

	def onItemSelected(self, event):
		currentItem = event.m_itemIndex
		car = self.myRowDict[currentItem]
		print(car.make)
		print(car.model)
		print(car.color)
		print(car.year)

		

	#mostrar registros al pulsar boton "mostrar todos"
	def onShowAllRecord( self, event ):
		print "hola mundo"

	#salir de la aplicacion desde el menu
	def onQuit(self, e):
		self.Close()

# Crear app
class MyApp(wx.App):

	def OnInit(self):
		self.frame = PanelLibro(None, "App")
		self.SetTopWindow(self.frame)
		self.frame.Show(True)
		print("wxApp created.")
		return True	

if __name__ == "__main__":
	app =  MyApp(redirect=False)
	app.MainLoop()