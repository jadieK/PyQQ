'''
Created on Feb 16, 2014

@author: chuan.gao
'''

import wx,os

class MainUI(wx.Frame):
    def __init__(self, parent, title, UISize, networkMgr):
        wx.Frame.__init__(self, parent, title=title, size=UISize)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.recv_message_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.send_message_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.recv_message = wx.TextCtrl(self, style = wx.TE_AUTO_SCROLL | wx.TE_MULTILINE | wx.TE_READONLY)
        self.send_message = wx.TextCtrl(self, style = wx.TE_AUTO_SCROLL | wx.TE_MULTILINE)
        self.network_mgr = networkMgr
        self.CreateStatusBar()
        
        self.send_message_button_id = wx.NewId();
        self.send_message_button = wx.Button(self, self.send_message_button_id, "Add")
        self.Bind(wx.EVT_BUTTON, self.OnSend, self.send_message_button)
        
        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit"," Terminate the program")
        #menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open file to edit")
        
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout);
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit);
        #self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self._Layout_()
        self.Show(True)
    
    def _Layout_(self):
        self.main_sizer.Add(self.recv_message_sizer,1,wx.EXPAND);
        self.main_sizer.Add(self.send_message_sizer,0,wx.EXPAND);
        
        self.recv_message_sizer.Add(self.recv_message,1,wx.EXPAND)
        self.send_message_sizer.Add(self.send_message,1,wx.EXPAND)
        self.send_message_sizer.Add(self.send_message_button)
        self.SetAutoLayout(1)
        self.SetSizer(self.main_sizer)
        self.Layout()
        
        
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "MyTestMessageBox", "AboutMessage", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self,event):
        self.Close(True)
        
    def OnSend(self,event):
        message = self.send_message.GetValue();
        self.network_mgr.AddMessage(message)
        self.send_message.Clear()