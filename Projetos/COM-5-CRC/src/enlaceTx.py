#!/usr/bin/env python3
# -*- coding: utf-8 -*-
####################################################
# Camada Física da Computação
# Prof. Rafael Corsi
#  Abril/2017
#  Camada de Enlace
####################################################

import numpy as np
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



    def crc16(self, data: bytes):
        '''
        CRC-16-CCITT Algorithm
        '''
        data = bytearray(data)
        poly = 0x8408
        crc = 0xFFFF
        for b in data:
            cur_byte = 0xFF & b
            for _ in range(0, 8):
                if (crc & 0x0001) ^ (cur_byte & 0x0001):
                    crc = (crc >> 1) ^ poly
                else:
                    crc >>= 1

                cur_byte >>= 1

        crc = (~crc & 0xFFFF)
        crc = (crc << 8) | ((crc >> 8) & 0xFF)

        return crc

    # Package building function
    def buildDataPackage(self, data, msgtype, currpart, totalpart):
        # https://gist.github.com/oysstu/68072c44c02879a2abf94ef350d1c7c6
        calccrc = self.crc16(data)

        head = (calccrc).to_bytes(4, byteorder='big')
        head += (len(data)).to_bytes(3, byteorder='big')
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
            print("Troughput: ", "%.3f" % troughput, "bits de payload/seg\n")
            # print("Tempo esperado da transmissão: ", "%.2f" %
            #       ((len(pack)/(115200/8))), "segundos\n")
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

    def sendBufferNoBuild(self, fullpack):
        # Write a new data to the transmission buffer
        # This function is non blocked.

        # This function must be called only after the end
        # of transmission, this erase all content of the buffer
        # in order to save the new value.        

        self.transLen = 0
        self.buffer = fullpack
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
