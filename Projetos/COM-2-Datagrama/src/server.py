#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
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

serialName = "/dev/ttyACM1"           # Ubuntu (variacao de)
# serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
# serialName = "COM3"                  # Windows(variacao de)


def main():
    # Inicializa enlace
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    # Arquivo a ser recebido
    dadoW = "./recebido/recebido.png"

    # Log
    print("__________________________________________________")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("__________________________________________________")


    # Faz a recepção dos dados
    print("Recebendo dados .... ")
    rxBuffer = com.getData()

    # log
    #print("Lido {} bytes".format(nRx))
    # print(rxBuffer)

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
