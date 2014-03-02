'''
Created on Feb 16, 2014

@author: chuan.gao
'''
import wx
from network import *
from wxUI import *

if __name__ == '__main__':
    udp_mgr = UdpManager.UdpManager('bj-chuangao-w',12366)
    udp_mgr.ConnectRemoteServer()
    udp_mgr.StartUdpService();
    
    app = wx.App(False)
    frame = wxUIMain.MainUI(None, 'Test', (200,100), udp_mgr)
    app.MainLoop()
    #udp_mgr.AddMessage("MyTest")
    