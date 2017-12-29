import wx
 
class bFrame(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, size=(353,270))
        self.parent = parent
 
        mainButton = wx.Button(self, -1, '&Back to Main',pos=(100,100),size=(-1,30))
        self.Bind(wx.EVT_BUTTON, self.backMain,mainButton)
 
    def backMain (self, event):
        self.parent.panel.Show()
        self.Destroy()
 
class aFrame(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(353,270))
 
        self.parent=parent
 
        mainButton = wx.Button(self, -1, '&Back to Main',pos=(100,100),size=(-1,30))
        self.Bind(wx.EVT_BUTTON, self.backMain,mainButton)
 
        bButton= wx.Button(self, -1, 'b',pos=(100,10),size=(-1,30))
        self.Bind(wx.EVT_BUTTON, self.b,bButton)
 
    def backMain (self, event):
        self.parent.panel.Show()
        self.Destroy()
 
    def b(self,event):
        bframe = bFrame(parent=self.parent)
        bframe.Centre()
        bframe.Show()
        self.Destroy()
 
class MainFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Title',size=(353,270),style=wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.MINIMIZE_BOX)
        self.panel = wx.Panel(self)
 
        aButton= wx.Button(self.panel, -1, 'a',pos=(10,10),size=(-1,30))
        self.Bind(wx.EVT_BUTTON, self.a,aButton)
 
    def a(self,event):
        aframe = aFrame(parent=self)
        aframe.Centre()
        aframe.Show()
        self.panel.Hide()
 
if __name__ == '__main__':
    app=wx.App()
    frame=MainFrame(parent=None,id=999)
    frame.Centre()
    frame.Show()
    app.MainLoop()