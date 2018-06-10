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

# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports

serialName = "/dev/ttyACM0"           # Ubuntu
# serialName = "/dev/tty.usbmodem1411" # Mac
# serialName = "COM3"                  # Windows


def main():
    # Inicializa enlace
    com = enlace(serialName)

    # Ativa comunicação
    com.enable()

    # Arquivo a ser recebido
    dadoW = "./recebido/recebido.gif"

    # Log
    print("__________________________________________________")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("__________________________________________________")

    print("Iniciando handshake")

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

        print("Esperando sync 1...")

        rxBuffer, msgtype = com.getData()
        # msgtype = int.from_bytes(msgtype, byteorder='big')

        if msgtype == 1:
            print("Recebido Sync 1\n")
            print("Enviando Ack 1...")
            data = (8).to_bytes(1, byteorder='big')
            msgtype = (2).to_bytes(1, byteorder='big')
            com.sendData(data, msgtype, currpart, totalpart)
            print("...enviado Ack 1\n")

            time.sleep(2)

            print("Enviando Sync 2...")
            data = (8).to_bytes(1, byteorder='big')
            msgtype = (3).to_bytes(1, byteorder='big')
            com.sendData(data, msgtype, currpart, totalpart)
            print("...enviado Sync 2\n")
        else:
            print("Erro, refazendo handshake...\n")
            continue

        print("Esperando Ack 2...")

        rxBuffer, msgtype = com.getData()
        # msgtype = (int.from_bytes(msgtype, byteorder='big'))

        if msgtype == 4:
            print("Ack 2 recebido\n")
            print("Conexão estabelecida, encerrando handshake\n")
            break
        else:
            print("Erro, refazendo handshake...\n")
            continue
    print("__________________________________________________")

    # Faz a recepção dos dados
    print("Recebendo pacote com payload... ")
    rxBuffer, msgtype = com.getData()

    # Salva o dado recebido em arquivo
    print("__________________________________________________")
    print("Salvando dados no arquivo :")
    print("{}".format(dadoW))
    f = open(dadoW, 'wb')
    f.write(rxBuffer)

    # Fecha arquivo de imagem
    f.close()

    # Encerra comunicação
    print("__________________________________________________")
    print("Comunicação encerrada")
    print("__________________________________________________")
    com.disable()


if __name__ == "__main__":
    main()
