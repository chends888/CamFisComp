# Projeto 8: Modulação/DeModulação BPSK

## Implementação de um chat entre dois computadores com comunicação BPSK (Binary Phase Shift Keying).

## Modulação digital via BPSK:
 É  uma modulação digital utilizada neste projeto para realizar um canal de comunicação entre dois computadores por meio de ondas eletromagnéticas. Nesse esquema, as fases das portadoras representam os níveis 0 e 1. Durante a alteração de um nível 0 para o 1 e vice e versa, a fase da portadora se altera 180º em relação à que era antes.

## Implementação da modulação

 A comunicação criada para esse projeto consiste em um server, que ficará sempre preparado para o recebimento de uma mensagem e um client, que fará requisições e enviará as mensagens. Os dois são softwares desenvolvidos em Python. Há também, dois arquivos do GNURadio, um que representa o transmissor da mensagem, e o outro o receptor desta. A interface criada para a interação do usuário é bem simples, consiste em um chat onde em uma seção é possível enviar as mensagens e na outra é possível ver as mensagens já enviadas (caso do client) ou ver as mensagens recebidas (no caso do server). Para isso acontecer, a mensagem a ser enviada é primeiro modulada e então enviada pelo socket criado e especificado no arquivo. Nesse momento, o receptor da mensagem já deve ter estabelecido uma conexão com este e deve estar preparado para receber a mensagem, demodular esta e exibir os caracteres da dela, um a um.

## Frequência de transmissão e banda

 Para definir a frequência de transmissão (portadora) realizamos testes com o GNURadio para encontrar um valor adequado ao microfone e speaker utilizados, analisando a recepção e o diagrama de constelação. Para isso, alteramos o valor da frequência de modo que os pontos apresentados no diagrama se concentrassem em dois polos, indicando assim, baixa quantidade de ruído e/ou perdas no sinal. A frequência utilizada é de 2200Hz e analisando-se o gráfico de frequência, a banda ocupada pelo sinal é de aproximadamente 8kHz.

## Gráficos:

## Gráfico no tempo do sinal não codificado
![Não codificado t](https://github.com/chends888/aliens/blob/master/img/1.1%20Tx.png)
## Gráfico em frequênica do sinal não codificado
![Não codificado f](https://github.com/chends888/aliens/blob/master/img/1.2%20Tx.png)
As duas imagens acima apresentam a plotagem do sinal não codificado, sem qualquer tratamento.


## Gráfico no tempo do sinal codificado
![Codificado t](https://github.com/chends888/aliens/blob/master/img/2.1%20Tx.png)
## Gráfico em frequênica do sinal codificado
![Codificado f](https://github.com/chends888/aliens/blob/master/img/2.2%20Tx.png)
As duas imagens acima apresentam o sinal codificado, onde há a repetição das portadoras no gráfico dos sinal em frequência.

## Gráfico no tempo do sinal modulado
![Modulado t](https://github.com/chends888/aliens/blob/master/img/3.1%20Tx.png)
## Gráfico em frequênica do sinal modulado
![Modulado f](https://github.com/chends888/aliens/blob/master/img/3.2%20Tx.png)
As duas imagens acima apresentam o sinal modulado, prestes a ser enviado, onde há a "shiftagem" da portadora no sinal em frequência e suas repetições tanto no domínio positivo quanto no negativo. 

## Diagrama de constelação da transferência
![Constellation tx](https://github.com/chends888/aliens/blob/master/img/Constellation%20tx.png)
A imagem acima representa a modulação digital do sinal que é pretendido enviar, e sua concentração, mesmo que dispersa, em um foco no centro da imagem aponta que realmente é um sinal tratado (modulado).



## Gráfico no tempo do áudio recebido modulado e demodulado
Observamos aqui o gráfico dos sinais recebidos em relação à sua intensidade tanto cru (modulado) quanto demodulado, este gráfico em particular não nos diz muito sobre a onda recebida.
![rxsinais](https://github.com/chends888/aliens/blob/master/img/rxsinais.png)

## Gráfico em frequência do áudio recebido
Esté é o gráfico do sinal recebido sem nenhum tipo de transformação, representando apenas as frequências da onda recebida.
![rxfreq](https://github.com/chends888/aliens/blob/master/img/rxfreq.png)

## Gráfico em frequência do  áudio demodulado
Este gráfico representa o sinal depois de ser demodulado. Ou seja, este é o sinal que é traduzido para os sinais que formam a mensagem transmitida.
![rxfreqdemo](https://github.com/chends888/aliens/blob/master/img/rxfreqdemo.png)

## Diagrama de constelação da recepção
Aqui podemos analisar de forma visual a precisão da nossa transmissão. No caso da transmissão BPSK, temos dois símbolos que são usados na tradução/demodulação. No gráfico, teremos duas nuvens de pontos, quanto menos dispersos estes pontos estiverem entre si, maior será a confiabilidade de nossa transmissão.
![rxconstellation](https://github.com/chends888/aliens/blob/master/img/rxconstallation.png)


## Validação:
 Para validar o funcionamento desse projeto, ele terá que ser capaz de transmitir uma mensagem de um computador, por meio de uma interface de chat e ela deve ser recebida sem erros em outro computador, na mesma inteface por meio de ondas eletromagnéticas.
