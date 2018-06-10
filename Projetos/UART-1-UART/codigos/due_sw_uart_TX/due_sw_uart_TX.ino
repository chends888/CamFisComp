#include "sw_uart.h"

due_sw_uart uart;

void setup() {
  // Serial.begin(9600);
  sw_uart_setup(&uart, 0, 18, 1, 8, SW_UART_EVEN_PARITY); //recepcao
  //sw_uart_setup(&uart, 0, 1, 1, 8, SW_UART_EVEN_PARITY); //envio
}

void loop() {
  test_write();
  //test_receive();
}

void test_write() {
  sw_uart_write_string(&uart,"camFisica\n");
  delay(50);
}

void test_receive() {
  char data;
  int code = sw_uart_receive_byte(&uart, &data);
  Serial.print(data);
  if(code == SW_UART_SUCCESS) {
     Serial.print(data);
  } else if(code == SW_UART_ERROR_PARITY) {
    //Serial.println("PARITY ERROR");
  } else {
    Serial.print("OTHER  -- ");
    Serial.println(code);
  }
}

