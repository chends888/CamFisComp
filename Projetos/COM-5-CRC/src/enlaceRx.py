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


class RX(object):
    # This class implements methods to handle the reception
    # data over the p2p fox protocol

    def __init__(self, fisica):
        # Initializes the TX class

        self.fisica = fisica
        self.buffer = bytes(bytearray())
        self.threadStop = False
        self.threadMutex = True
        self.READLEN = 1024

    def thread(self):
        # RX thread, to send data in parallel with the code
        while not self.threadStop:
            if(self.threadMutex == True):
                rxTemp, nRx = self.fisica.read(self.READLEN)
                if (nRx > 0):
                    self.buffer += rxTemp
                time.sleep(0.001)

    def threadStart(self):
        # Starts RX thread (generate and run)
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def threadKill(self):
        # Kill RX thread

        self.threadStop = True

    def threadPause(self):
        # Stops the RX thread to run

        # This must be used when manipulating the Rx buffer
        self.threadMutex = False

    def threadResume(self):
        # Resume the RX thread (after suspended)
        self.threadMutex = True

    def getIsEmpty(self):
        # Return if the reception buffer is empty

        if(self.getBufferLen() == 0):
            return(True)
        else:
            return(False)

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

    def getBufferLen(self):
        # Return the total number of bytes in the reception buffer
        return(len(self.buffer))

    def getBuffer(self, nData):
        # Remove n data from buffer

        self.threadPause()
        pack = self.buffer[0:nData]

        eop = self.buffer.find(b'888888888888')  # Search for end of package
        idealcrc = self.buffer[0:4]
        size = self.buffer[3:7]  # Get header from buffer
        msgtype = self.buffer[7:8]  # Get message type
        currpart = self.buffer[8:9] # Get number of current package
        totalpart = self.buffer[9:10] # Get number of total packages
        
        totalpart = int.from_bytes(totalpart, byteorder='big')
        msgtype = int.from_bytes(msgtype, byteorder='big')
        payload = b""

        rescrc = -1
        if totalpart == 1:
            payload = pack[10:eop]
        else:
            # Process to join packages and check CRC
            i = 0
            while i < totalpart:
                temppayload = pack[((1015*i) + 10) : ((1015*i) + 1010)]
                if i == totalpart - 1:
                    temppayload = temppayload[:-5]
                calccrc = self.crc16(temppayload)
                calccrc = (calccrc).to_bytes(4, byteorder='big')
                idealcrc = pack[(1015*i) : ((1015*i) + 4)]
                if calccrc != idealcrc:
                    rescrc = i
                payload += temppayload
                i += 1
        if msgtype == 5:
            print("Recebido pacote dividido em", totalpart, "parte(s)")

        self.clearBuffer()
        self.threadResume()

        return(payload, msgtype, rescrc)

    def getNData(self):
        # Read N bytes of data from the reception buffer

        # This function blocks until the number of bytes is received

        self.clearBuffer()
        tamanho = 0

        start = time.time()  # Começar timer

        while (self.getBufferLen() > tamanho or self.getBufferLen() == 0):
            tamanho = self.getBufferLen()
            time.sleep(0.5)

            end = time.time()  # Stop timer
            print("%.2f" % (end-start), '/ 10 seg')

            if (end - start) > 10:
                return ()

        return(self.getBuffer(tamanho))

    def clearBuffer(self):
        # Clear the reception buffer

        self.buffer = b""
