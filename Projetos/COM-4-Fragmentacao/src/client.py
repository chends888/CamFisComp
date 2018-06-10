#!/usr/bin/env python3
# -*- coding: utf-8 -*-
####################################################
# Camada Física da Computação
# Prof. Rafael Corsi
#  Abril/2017
#  Aplicação
####################################################

from enlace import *
import time
import numpy as np

# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports

serialName = "/dev/ttyACM1"           # Ubuntu
# serialName = "/dev/tty.usbmodem1411" # Mac
# serialName = "COM3"                  # Windows


def main():
    # Inicializa enlace
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    # Fazendo o arquivo a ser transmitido
    dado = "./enviar/Screenshot.gif"

    # Log
    print("__________________________________________________")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("__________________________________________________")

    # Código handshake (msgtype):
    # Error   = 8
    # Sync 1  = 1
    # Ack 1   = 2
    # Sync 2  = 3
    # Ack 2   = 4
    # Payload = 5

    while (True):
        currpart = (1).to_bytes(1, byteorder='big')
        totalpart = (1).to_bytes(1, byteorder='big')

        print("Iniciando handshake")
        time.sleep(1)

        print("Enviando Sync 1...")
        data = (8).to_bytes(1, byteorder='big')
        msgtype = (1).to_bytes(1, byteorder='big')
        com.sendData(data, msgtype, currpart, totalpart)
        print("...enviado Sync 1\n")

        print("Esperando Ack 1")
        rxBuffer, msgtype = com.getData()
        print("Recebido Ack 1\n")

        print("Esperando Sync 2")
        rxBuffer, msgtype = com.getData()

        if msgtype == 3:
            print("Recebido Sync 2\n")
            print("Enviando Ack 2...")
            data = (8).to_bytes(1, byteorder='big')
            msgtype = (4).to_bytes(1, byteorder='big')
            com.sendData(data, msgtype, currpart, totalpart)
            print("...enviado Ack 2")
            print("Conexão estabelecida, encerrando handshake\n")
            time.sleep(2)
            break
        else:
            print("Erro, refazendo handshake...\n")
            continue
    print("__________________________________________________")

    # Carrega imagem
    print("Arquivo para transmissão:")
    print("{}".format(dado))
    print("__________________________________________________")
    dado = open(dado, 'rb').read()
    # descobre a quantidade de bytes a ser enviada
    # (importante porque so fará a leitura quando todos os bytes já foram transmitidos.)
    txLen = len(dado)




    # Transmite imagem
    print("Transmitindo {} bytes de payload".format(txLen))
    start = time.time()  # Começa contagem do tempo de transmissão
    msgtype = (5).to_bytes(1, byteorder='big')


    # Dividindo payload em partes menores
    if txLen > 1000:
        n = (txLen//1000) + 1
        totalpart = (n).to_bytes(1, byteorder='big')
        # txBuffer = np.array_split(txBuffer, n) # TxBuffer está dividido em n partes
        print("Pacote dividido em ", n, "partes")

        i = 0
        fullpack = b""
        while i < n:
            txBuffer = dado[i*1000 : (i*1000 + 1000)]
            currpart = (i).to_bytes(1, byteorder='big')
            fullpack +=  com.buildPackage(txBuffer, msgtype, currpart, totalpart)
            i += 1
        com.sendDataNoBuild(fullpack, msgtype, currpart, totalpart)
    
    else:
        n = 1
        totalpart = (n).to_bytes(1, byteorder='big')
        print("Não foi necessário dividir o payload")
        com.sendData(dado, msgtype, currpart, totalpart)

    
    

    # espera o fim da transmissão
    while(com.tx.getIsBussy()):
        pass

    # Atualiza dados da transmissão
    end = time.time()
    print("Tempo real de transmissão: ", "%.2f" % (end-start), "segundos")

    # txSize = com.tx.getStatus()
    # print("Transmitido {} bytes ".format(txSize))
    print("Pacote transmitido")

    # Encerra comunicação
    print("__________________________________________________")
    print("Comunicação encerrada")
    print("__________________________________________________")
    com.disable()


if __name__ == "__main__":
    main()
