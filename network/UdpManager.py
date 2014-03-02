'''
Created on Feb 16, 2014

@author: chuan.gao
'''
import sys, socket
import thread, time

class UdpManager:
    def __init__(self, RemoteServerAddress, RemotePort):
        address_info = socket.getaddrinfo(RemoteServerAddress, RemotePort, socket.AF_INET, socket.SOCK_DGRAM)
        self.ip_info = address_info[0][4]
        self.sending_list = list()
        self.recving_list = list()
        self.sending_thread = None
        self.recving_thread = None
        self.show_thread = None
        
    def ConnectRemoteServer(self):
        self.cur_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
        #self.curSocket.bind(self.ip_info);
        self.cur_socket.connect(self.ip_info)
    
    def StartUdpService(self, UpdateInterval = 0.1):
        self.sending_thread = thread.start_new_thread(self._SendingService, (UpdateInterval,))
        self.recving_thread = thread.start_new_thread(self._RecvingService, (UpdateInterval,))
        self.show_thread = thread.start_new_thread(self._ShowService, (UpdateInterval,))
        print "Service Start ", self.sending_thread, self.recving_thread, self.show_thread
        
    def AddMessage(self, NewMessage):
        self.sending_list.append(NewMessage)
        
    def _SendingService(self, UpdateInterval):
        while True:
            if len(self.sending_list) > 0:
                cur_message = self.sending_list.pop(0)
                self.cur_socket.sendall(cur_message)
            time.sleep(UpdateInterval)
        
    def _RecvingService(self, UpdateInterval):
        while True:
            buf = self.cur_socket.recv(1024 * 10)
            if len(buf):
              self.recving_list.append(buf);
            time.sleep(UpdateInterval)
            
    def _ShowService(self, UpdateInterval):
        while True:
            if len(self.recving_list) > 0:
                cur_message = self.recving_list.pop(0)
                print "Recv Message", cur_message
            time.sleep(UpdateInterval)