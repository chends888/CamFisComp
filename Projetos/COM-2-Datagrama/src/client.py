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

serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
# serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
# serialName = "COM3"                  # Windows(variacao de)


def main():
    # Inicializa enlace
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    # Fazendo o arquivo a ser transmitido
    dado = "./enviar/Screenshot.png"

    # Log
    print("__________________________________________________")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("__________________________________________________")

    # Carrega imagem
    print("Arquivo para transmissão:")
    print("{}".format(dado))
    print("__________________________________________________")
    #txBuffer = open(dado, 'rb').read()
    txBuffer = open(dado, 'rb').read()
    # descobre a quantidade de bytes a ser enviada (importante porque so fará a leitura quando todos os bytes ja foram transmitidos.)
    txLen = len(txBuffer)

    # Transmite imagem
    print("Transmitindo {} bytes de payload".format(txLen))
    start = time.time() # Começa contagem do tempo de transmissão
    com.sendData(txBuffer)

    # espera o fim da transmissão
    while(com.tx.getIsBussy()):
        pass

    # Atualiza dados da transmissão
    end = time.time()
    print("Tempo real de transmissão: ", "%.2f" % (end-start), "segundos")
    
    txSize = com.tx.getStatus()
    print("Transmitido {} bytes ".format(txSize))

    # Encerra comunicação
    print("__________________________________________________")
    print("Comunicação encerrada")
    print("__________________________________________________")
    com.disable()


if __name__ == "__main__":
    main()
