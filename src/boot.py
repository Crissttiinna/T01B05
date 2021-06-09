# boot.py - - runs on boot-up
#este código serve para configurar os comandos referentes ao sensor de som
from machine import UART, Pin
from utime import sleep_ms

S=0x7E #start bit
VER=0XFF #version information
LEN=0X06 #numero de bits depois de len (exceto os checksum)
FB=0X01 #01 se quero feedback, 00 se não quero feedback
END=0XEF #end bit
check1=0xFF #acumulation
check2=0xE6 #verification


#definir inicialização
def inicial(self,pin_tx,pin_rx):
    uart = UART(1)
    uart.init(baudrate=9600, bits=8, parity=0, stop=1, tx=pin_tx, rx=pin_rx)
    self.cmd(0x3F,0x00,0x00) #comando para inicialização de parametros
    self.volume_esp=15

#defino a minha linha de comandos onde envio a informação ao sensor
def cmd(self,comando,par1,par2):
    linha=bytes([S,VER,LEN,comando,FB,par1,par2,check1,check2,END]) #defino a minha linha de comandos que quero mandar para o sensor via UART
    self.uart.write(linha)

#DEFINIR OS COMANDOS

#PARAR
def stop(self):
    self.cmd(0x0E,0x00,0x00)

#RETIRAR DA PAUSA
def play(self):
    self.cmd(0x0D,0X00,0X00)

#REPETIR TRACK
def repete(self):
    self.cmd(0x11,0x00,0x00)

#AVANÇAR, RECUAR E ESPECIFICAR TRACK
def avançar(self):
    self.cmd(0x01,0x00,0x00)

def recuar(self):
    self.cmd(0x02,0x00,0x00)

def escolher(self,par1,par2):
    self.cmd(0x03,par1,par2)

#DEFINIR O VOLUME (AUMENTAR,DIMINUIR E ESPECIFICAR)
def volume_up(self):  #esta função permite me aumentar o volume
    self.cmd(0x04,0x00,0x00)

def volume_down(self): #esta função permite me diminuir o volume
    self.cmd(0x05,0x00,0x00)

def volume_esp(self,par1,par2): #esta função permite me especificar o volume
    self.cmd(0x06,par1,par2)

#HARDWARE
def module_sleep(self): #esta função permite me o sensor entrar em low loss
    self.cmd(0x0A,0x00,0x00)

def module_wake(self): #esta função permite por aa funcioona lo normalmente
    self.cmd(0x0B,0x00,0x00)

def module_reset(self): #esta função permite me ativar o módulo de reset
    self.cmd(0x0C,0x00,0x00)


musica=inicial(pin_tx=23,pin_rx=18)
musica.volume_esp(par1=0x00,par2=0x0F) #especifico o volume que quero para a música
musica.escolher(par1=0x00,par2=0x01) #especifico o file que quero passar
