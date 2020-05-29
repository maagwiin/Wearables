/*
   ------Projeto Wearables------
   
   NERA e Nu[Tec]² - IFES Serra


   Anel RGB - Primeiro Programa - Ring001.ino
   Reconhecimento de variáveis e funções

   Objetivo: Ligar todos os leds do anel, 1 a 1 de forma sequencial em uma única cor.

   Conclusões:
     - Biblioteca precisa ser usada;
     - Operação por meio de um objeto de tipo especifico, criado passando como parametro (n_de_leds, pino_de_ligação);
     - Inicialização obrigatória por meio da função OBJETO.begin();
     - Funções descobertas:
        * OBJETO.begin() : Inicializa o hardware;
        * OBJETO.clear() : Apaga todos os leds da malha;
        * OBJETO.setPixelColor(n_do_pixel, cor(em padrão próprio)) : Define uma nova cor para o pixel especificado;
        * OBJETO.Color(r, g, b) : Converte o RGB dado em um número usado como padrão de cor na função acima;
        * OBJETO.Show() : Envia a atualização de cor para o hardware.
    
   Autor: Magnu Windell Araújo Santos, Maio - 2020.

*/

#include <Adafruit_NeoPixel.h>  //Biblioteca Adafruit para controle dos leds


#define PIN 7 //Pino de comunicação com o anel
#define NUMPIXELS 16 //Número de pixels(leds) no equipamento
#define DELAYVAL 500 //Tempo de pausa


Adafruit_NeoPixel ring(NUMPIXELS, PIN); //Cria o objeto 'ring' do tipo Adafruit_NeoPixel


void setup() {
  ring.begin(); //Inicialização do objeto 'ring'
}


void loop() {
  ring.clear(); //Apaga todos os pixels(leds)
  for(int i=0; i<NUMPIXELS-1; i++) { //Para cada led
    ring.setPixelColor(i, ring.Color(0, 150, 0)); //Define a cor do led
    ring.show();   //Envia a atualização para o hardware
    delay(DELAYVAL); //Tempo de espera
  }
}
