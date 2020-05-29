/*
   ------Projeto Wearables------
   
   NERA e Nu[Tec]² - IFES Serra


   Anel RGB - Sinalização Wearable - Ring003.ino
   Integração com projeto

   Objetivo: Implementar rotinas de sinalização para projeto wearables.

   Conclusões:
     - Tempo de inicialização grande, ajustar de acordo com calibração dos sensores MQ;
     - Número de repetições fictício, apenas para testes, o blink deve permanecer até a mudança de estado.
    
   Autor: Magnu Windell Araújo Santos, Maio - 2020.

*/

#include <Adafruit_NeoPixel.h>  //Biblioteca Adafruit para controle dos leds

#define PIN 7 //Pino de comunicação com o anel
#define NUMPIXELS 16 //Número de pixels(leds) no equipamento
#define DELAYVAL 500 //Tempo de pausa

Adafruit_NeoPixel ring(NUMPIXELS, PIN); //Cria o objeto 'ring' do tipo Adafruit_NeoPixel

void setup() {
  ring.begin(); //Inicialização do objeto 'ring'
  ring.clear(); //Apaga todos os leds
  ring.show();  //Envia atualização para o hardware

  starting();   //Executa rotina de inicialização
}

void loop() {
  normal();
  delay(30000);
  co();
  normal();
  delay(10000);
  lpg();
  normal();
  delay(10000);
  co_lpg();
  normal();
}

void starting() {
  int rpt = 12;   //Repetição da rotina
  int del = 75;   //Tempo de delay entre acionamento dos leds 
  for(int i=0; i<rpt; i++){ //Em cada repetição
    colorWipe(ring.Color(150, 150, 150), del); //Wipe em branco
    colorWipe(ring.Color(150, 0, 0), del);     //Wipe em vermelho
    colorWipe(ring.Color(0, 150, 0), del);     //Wipe em verde
    colorWipe(ring.Color(0, 0, 150), del);     //Wipe em azul
  }
  ring.clear();  //Apaga todos os leds
  ring.show();   //Envia atualização para o hardware
}

void colorWipe(uint32_t color, int wait) {
  for(int k=0; k<ring.numPixels(); k++) { //Para cada led
    ring.setPixelColor(k, color);         //Define a cor do led
    ring.show();                          //Envia atualização para o hardware
    delay(wait);                          //Tempo de espera
  }
}

void normal(){
  colorFill(ring.Color(150, 150, 150));
}

void co(){
  for(int j=0; j<=20; j++){
    colorFill(ring.Color(0, 150, 0));
    ring.show();
    delay(DELAYVAL);
    ring.clear();
    ring.show();
    delay(DELAYVAL);
  }
}

void lpg(){
  for(int j=0; j<=20; j++){
    colorFill(ring.Color(0, 0, 150));
    ring.show();
    delay(DELAYVAL);
    ring.clear();
    ring.show();
    delay(DELAYVAL);
  }
}

void co_lpg(){
  for(int j=0; j<=20; j++){
    colorFill(ring.Color(150, 0, 0));
    ring.show();
    delay(DELAYVAL);
    ring.clear();
    ring.show();
    delay(DELAYVAL);
  }
}

void colorFill(uint32_t color) {
  ring.fill(color, 0, NUMPIXELS);
  ring.show();
}
