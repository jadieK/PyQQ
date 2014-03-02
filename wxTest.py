import wx,os
class MyFrame(wx.Frame):
    def __init__(self,parent, title):
        wx.Frame.__init__(self,parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        
        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit"," Terminate the program")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open file to edit")
        
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout);
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit);
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Show(True)
        
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "MyTestMessageBox", "AboutMessage", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self,event):
        self.Close(True)
        
    def OnOpen(self,event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
app = wx.App(False)
frame = MyFrame(None, 'Test')
app.MainLoop()