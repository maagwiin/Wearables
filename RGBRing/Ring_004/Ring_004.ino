/*
   ------Projeto Wearables------
   
   NERA e Nu[Tec]² - IFES Serra


   Anel RGB - Estados de atmosfera - Ring004.ino
   Integração com projeto

   Objetivo: Implementar troca de estado por meio de dado recebido - Serial.

   Conclusões:
     - Usando dados vindos da comunicação serial em 9600;
     - Apresenta uma pequena latência na troca de estados.
    
   Autor: Magnu Windell Araújo Santos, Maio - 2020.

*/

#include <Adafruit_NeoPixel.h>  //Biblioteca Adafruit para controle dos leds

#define PIN 7 //Pino de comunicação com o anel
#define NUMPIXELS 16 //Número de pixels(leds) no equipamento
#define DELAYVAL 200 //Tempo de pausa

int recebido = 0; //Dado recebido por serial
int dado = 0;     //Dado para comutação de estado

Adafruit_NeoPixel ring(NUMPIXELS, PIN); //Cria o objeto 'ring' do tipo Adafruit_NeoPixel

void setup() {
  ring.begin(); //Inicialização do objeto 'ring'
  ring.clear(); //Apaga todos os leds
  ring.show();  //Envia atualização para o hardware
  Serial.begin(9600); //Inicia comunicação serial
  starting();   //Executa rotina de inicialização
  normal();     //Chama rotina para ambiente normal
}

void loop() {
  if(Serial.available()){             //Tem dado na serial?
    recebido = Serial.parseInt();     //Converte o dado em inteiro
    change();                         //Chama rotina de mudança de estado
   }
}

void starting() {
  int rpt = 2;   //Repetição da rotina
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


void change(){
  if(Serial.available()){ 
    recebido = Serial.parseInt();
   }
  if(recebido > 0 && recebido < 5 && recebido != dado){     //Avalia o dado recebido
      dado = recebido;                                      //Armazena recebido na variável de comutação
    }
     switch(dado){   //Testa a variável de comutação
      case 1:        //Atmosfera normal
        normal();
        change();
        break;
      case 2:        //CO presente
        co();
        change();
        break;
      case 3:        //GLP presente
        lpg();
        change();
        break;
      case 4:       //CO e LPG presentes
        co_lpg();
        change();
        break;
      default:      //Segurança
        normal();
        change();
        break;
    }
}

void normal(){    //Rotina de atmosfera normal
  if(Serial.available()){
      change();
    }
  colorFill(ring.Color(150, 150, 150)); //Troca cor dos leds para branco
  ring.show();
}

void co(){        //Rotina de atmosfera contaminada com CO  --- Blink leds em verde
    if(Serial.available()){
      change();
    }
    colorFill(ring.Color(0, 150, 0));
    ring.show();
    delay(DELAYVAL);
    ring.clear();
    ring.show();
    delay(DELAYVAL);
}

void lpg(){       //Rotina de atmosfera contaminada com LPG  --- Blink leds em azul
    if(Serial.available()){
      change();
    }
    colorFill(ring.Color(0, 0, 150));
    ring.show();
    delay(DELAYVAL);
    ring.clear();
    ring.show();
    delay(DELAYVAL);
}

void co_lpg(){    //Rotina de atmosfera contaminada com CO e LPG  --- Blink leds em vermelho
  while(dado == 4){
    if(Serial.available()){
      change();
    }
    colorFill(ring.Color(150, 0, 0));
    ring.show();
    delay(DELAYVAL);
    ring.clear();
    ring.show();
    delay(DELAYVAL);
  }
}

void colorFill(uint32_t color) { //Rotina de preenchimento de leds
  ring.fill(color, 0, NUMPIXELS);
  ring.show();
}
