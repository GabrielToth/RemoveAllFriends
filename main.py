import pyautogui
import time

def friend_list_search(list_heigh):
    img_pos = pyautogui.locateOnScreen(friend_list)
    pyautogui.click(img_pos)

    time.sleep(0.5)
    pyautogui.click(1700, list_heigh)

    time.sleep(1)

def friend_list_close():
    x_pos = pyautogui.locateOnScreen(x)
    pyautogui.click(x_pos)
    
    time.sleep(0.5)
    
def find_unfriend_button():
    friend_button_pos = pyautogui.locateOnScreen(friend_button)
    pyautogui.click(friend_button_pos)
    time.sleep(0.5)
    
    unfriend_pos = pyautogui.locateOnScreen(unfriend)
    pyautogui.click(unfriend_pos)

def confirm_unfriend():
    confirm_pos = pyautogui.locateOnScreen(confirm)
    pyautogui.click(confirm_pos)
    time.sleep(0.5)

friend_list = 'friend_list.png'
friend_button = 'friend_button.png'
unfriend = 'unfriend.png'
x = 'x.png'
confirm = 'confirm.png'

list_heigh = 375

i = 0
j = 0

while j < 10:
    try:
        friend_list_search(list_heigh)
        
        try:
            friend_list_close()
            
            try:
                find_unfriend_button()
                
                try:
                    confirm_unfriend()
                except:
                    print('Não achei o botão de confirmação, pelo amor de @God da seus pulos que quero trabalhar.')
            except:
                print('Amigo não encontrado')
                time.sleep(1)
        except:
            print('Aba amigos fechada')
    except:
        print('Pipipi, pópópó, pani nu systema')

    
    
    i += 1
    
    list_heigh = list_heigh + 44
    
    if (i % 9 == 0) :
        list_heigh = 375
        pyautogui.hotkey('Ctrl','f5')
        time.sleep(7)
        j += 1
    