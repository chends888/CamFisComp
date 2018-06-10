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
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
#serialName = "COM3"                  # Windows(variacao de)

def main():
    # Inicializa enlace
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    # # Fazendo o arquivo a ser transmitido
    # dado = list(range(0,256))
    # print(dado)
    # print(type(dado[1]))

    # dado = bytes(dado)

    # print(dado)


    #Arquivo a ser recebido
    dadoW = "./recebido/recebido.png"

    # Endereco do arquivo a ser salvo
    #dado = "./imgs/dado.txt"

    # Log
    print("__________________________________________________")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("__________________________________________________")

    # # Carrega imagem
    # print ("Carregando dado para transmissão :")
    # print (" - {}".format(dado))
    # print("-----------------------------------------------")
    # #txBuffer = open(dado, 'rb').read()
    # txBuffer = dado
    # txLen    = len(txBuffer)  #descobre a quantidade de bytes a ser enviada (importante porque so fará a leitura quando todos os bytes ja foram transmitidos.)
    # print(txLen)

    # # Transmite imagem
    # print("Transmitindo .... {} bytes".format(txLen))
    # com.sendData(txBuffer)

    # espera o fim da transmissão
    # while(com.tx.getIsBussy()):
    #     pass

    # # Atualiza dados da transmissão
    # txSize = com.tx.getStatus()
    # print ("Transmitido       {} bytes ".format(txSize))

    # Faz a recepção dos dados
    print ("Recebendo dados .... ")
    rxBuffer, nRx = com.getData(1)

    # log
    print ("Lido              {} bytes ".format(nRx))
    print (rxBuffer)

    # Salva o dado recebido em arquivo
    print____________________________
    print ("Salvando dados no arquivo :")
    print (" - {}".format(dadoW))
    f = open(dadoW, 'wb')
    f.write(rxBuffer)

    # Fecha arquivo de imagem
    f.close()

    # Encerra comunicação
    print____________________________
    print("Comunicação encerrada")
    print____________________________
    com.disable()

if __name__ == "__main__":
    main()