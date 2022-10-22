import keyboard ### BIBLIOTECA QUE CONTROLA TECLADO 
import pyautogui #### PARA AUTOMAÇÃO CONTROLA TECLADO E MOUSE 
import sys,os #######  CONTROLA SISTEMA DIRETORIOS , SISTEMA ETC.....
import win32gui, win32con #### bilioteca para console , esconde telinha preta CMD )
import time ### controla tempo 
import os
import pyttsx3 ### converte texto em voz 



def fala():
    robo = pyttsx3.init()
    msg = 'seu progama mouse, estará ativo em alguns segundos!'
    robo.say(msg)
    robo.runAndWait()
    time.sleep(1)
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide , win32con.SW_HIDE)  ### esconde telinha preta(CMD) CONSOLE 

fala()


def FALAexit():
    robo = pyttsx3.init()
    msg = 'seu progama será encerrado'
    robo.say(msg)
    robo.runAndWait()
    time.sleep(1)
   


#################################### MOVIMENTA RAPIDO O MOUSE #######################


while True: ########### RODA A FUNÇÃO INFINITA VEZES
     #########################################################################################################
             ##################################### FECHA O PROGAMA ###############################
        if keyboard.is_pressed('F3'): #### SE APERTAR ESSA TECLA (F3)
                        FALAexit()
                        exit() ###################### SAI DO PROGAMA, ENCERRA O PROGAMA
        try:
            def movimenta_mouse():  ### FUNCAO MOVIMENTA O MOUSE MAIS RAPIDO
                keyboard.block_key('Tab')#### BLOQUEIA TECLA Tab
                keyboard.block_key('Alt')####  BLOQUEIA TECLA Tab
                pyautogui.FAILSAFE = False
                
                x , y = pyautogui.position()
                print(x, y)
                if keyboard.is_pressed('down'): #### SE APERTAR ESSA TECLA (down)
                    pyautogui.moveTo(x+1,y+50) #### movimenta o MOUSE para cima 
                    
                if keyboard.is_pressed('right'): #### SE APERTAR ESSA TECLA (right)
                    pyautogui.moveTo(x+50,y+0)    #### movimenta o MOUSE para direita
                    
                    
                if keyboard.is_pressed('left'):#### SE APERTAR ESSA TECLA (down)
                    pyautogui.moveTo(x-50,y+0)    #### movimenta o MOUSE esquerda
                       
                        
                        
                if keyboard.is_pressed('up'): #### SE APERTAR ESSA TECLA (down)
                   pyautogui.moveTo(x-0,y-50)       #### movimenta o MOUSE para baixo
                    
             ################## MOVIMETA DEVAGAR O MOUSE ########################
                
                
                if keyboard.is_pressed('Shift') and keyboard.is_pressed('down'):
                    pyautogui.moveTo(x+0,y+1)
                    
                if keyboard.is_pressed('Shift') and keyboard.is_pressed('right'):
                    pyautogui.moveTo(x+1,y+0)    
                    
                    
                if keyboard.is_pressed('Shift') and keyboard.is_pressed('left'):
                    pyautogui.moveTo(x-1,y+0)    
                       
                        
                        
                if keyboard.is_pressed('Shift') and keyboard.is_pressed('up'): 
                   pyautogui.moveTo(x-0,y-1)
             ##################################################################################################################
             ####################################### CLICA COM MOUSE E PARA BOTAO ESQUERDO E D PARA BOTAO DIREITO
                
                if keyboard.is_pressed('Shift') and keyboard.is_pressed('e'): 
                   pyautogui.click(button='left')
                   
                if keyboard.is_pressed('Shift') and keyboard.is_pressed('d'): 
                   pyautogui.click(button='right')   
                   
                   
                if keyboard.is_pressed('space') and keyboard.is_pressed('c'):
                   pyautogui.mouseDown()
                   
                if keyboard.is_pressed('space') and keyboard.is_pressed('v'):
                    pyautogui.mouseUp()
                   
                   
                   
            
             
                                
                
                     
        
                    
            movimenta_mouse() #### faz a chamada da função
            
            #### controla erro , porem não sei se isso é correto so que funcionou

        ############################################# SE CASO DER ERRO MACHE NOVAMENTO A FUNÇÃO#############################    
        except:
            pyautogui.FailSafeException == False
            pyautogui.FAILSAFE == False
            FloatingPointError == False
            print('erro na memoria ')
            movimenta_mouse()
            
            ########################################## fim######################################################
            
            
                  
