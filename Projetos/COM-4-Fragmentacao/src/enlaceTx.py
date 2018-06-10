#!/usr/bin/env python3
# -*- coding: utf-8 -*-
####################################################
# Camada Física da Computação
# Prof. Rafael Corsi
#  Abril/2017
#  Camada de Enlace
####################################################

# Importa pacote de tempo
import time

# Threads
import threading

# Class


class TX(object):
    # This class implements methods to handle the transmission
    # data over the p2p fox protocol

    def __init__(self, fisica):
        # Initializes the TX class
        self.fisica = fisica
        self.buffer = bytes(bytearray())
        self.transLen = 0
        self.empty = True
        self.threadMutex = False
        self.threadStop = False

    def thread(self):
        # TX thread, to send data in parallel with the code
        while not self.threadStop:
            if(self.threadMutex):
                self.transLen = self.fisica.write(self.buffer)
                self.threadMutex = False

    def threadStart(self):
        # Starts TX thread (generate and run)
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def threadKill(self):
        # Kill TX thread
        self.threadStop = True

    def threadPause(self):
        # Stops the TX thread to run
        # This must be used when manipulating the tx buffer
        self.threadMutex = False

    def threadResume(self):
        # Resume the TX thread (after suspended)
        self.threadMutex = True

    # Package building function
    def buildDataPackage(self, data, msgtype, currpart, totalpart):
        head = (len(data)).to_bytes(7, byteorder='big')
        head += msgtype
        head += currpart
        head += totalpart
        
        eop = (888888888888).to_bytes(5, byteorder='big')
        pack = head + data + eop

        msgtype = int.from_bytes(msgtype, byteorder='big')
        currpart = int.from_bytes(currpart, byteorder='big')
        totalpart = int.from_bytes(totalpart, byteorder='big')


        if (msgtype == 5) and (currpart == totalpart-1):
            overhead = totalpart * len(pack)/len(data)
            troughput = (len(data)/len(pack))*115200
            print("__________________________________________________")
            print("Tamanho do payload: ", len(data))
            print("Overhead: ", "%.5f" % overhead)
            print("Troughput: ", "%.3f" % troughput, "bits de payload/seg")
            print("Tempo esperado da transmissão: ", "%.2f" %
                  ((len(pack)/(115200/8))), "segundos")
            print("__________________________________________________")

        return pack

    def sendBuffer(self, data, msgtype, currpart, totalpart):
        # Write a new data to the transmission buffer
        # This function is non blocked.

        # This function must be called only after the end
        # of transmission, this erase all content of the buffer
        # in order to save the new value.

        self.transLen = 0
        self.buffer = self.buildDataPackage(data, msgtype, currpart, totalpart)
        self.threadMutex = True

    def sendBufferNoBuild(self, data, msgtype, currpart, totalpart):
        # Write a new data to the transmission buffer
        # This function is non blocked.

        # This function must be called only after the end
        # of transmission, this erase all content of the buffer
        # in order to save the new value.

        self.transLen = 0
        self.buffer = data
        self.threadMutex = True

    def getBufferLen(self):
        # Return the total size of bytes in the TX buffer
        return(len(self.buffer))

    def getStatus(self):
        # Return the last transmission size
        return(self.transLen)

    def getIsBussy(self):
        # Return true if a transmission is ongoing
        return(self.threadMutex)
