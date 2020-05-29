/*
   ------Projeto Wearables------
   
   NERA e Nu[Tec]² - IFES Serra


   Anel RGB - Aprofundamento - Ring002.ino
   Demais funções

   Objetivo: Implementar rotina de inicialização e verificação

   Conclusões:
     - Usando 1 minuto para inicialização a partir do produto entre 'rpt' e 'del', rpt = repetição da rotina, del = tempo de espera entre os leds:
        * Para 1 minuto:
            *   RPT ------- DEL
            *    12 ------- 75
            *     6 ------- 150
            *     3 ------- 300
            *     1 ------- 900
           
     - Funções descobertas:
        * OBJETO.fill(cor(em padrão próprio), led_inicial, led_final): Preenche os leds do range especificado com a cor especificada; 
        * OBJETO.setBrightness(0<->255): Configura o nível do brilho dos leds;
        * OBJETO.getPixelColor(pixel): Retorna a cor definida para o led específico;
    
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
