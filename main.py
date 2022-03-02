import cv2 as cv2
import numpy
import pyautogui
import mss
import time
from os import listdir
import colorama
from colorama import Fore, Back, Style
from datetime import datetime
import pygetwindow


now = datetime.now()

colorama.init()

horseName = ""
countRace = 0


logo0 = """
 _______   _______   _______   _______   _    _   _    _
|  ___  | |  _____| |  _____| |  ___  | \ \  / / \ \  / /
| |___| | | |____   | | ____  | |   | |  \ \/ /   \ \/ /
|  _____| |  ____|  | ||__  | | |___| |   >  <     \  /
| |       | |_____  | |___| | |  ___  |  / /\ \    / /
|_|       |_______| |_______| |_|   |_| /_/  \_\  /_/        

"""


logo1 = """
           _                     _          
          |_)  _.  _ o ._   _   |_)  _ _|_  
          | \ (_| (_ | | | (_|  |_) (_) |_
                            _|         
"""


logo2 = """
            /\                       /\                         
            \ \                     / /
          __/_/,,;;;`;       ;';;;,,\_\__        
       ,~(  )  , )~~\|       |/~~( ,  (  )~;
       ' / / --`--,             .--'-- \ \ `
        /  \    | '             ` |    /  \      
"""

logo3 = """
        #####################################
        #            Opensource             #
        #####################################   
"""

logo4 = """
        #####################################
        #    Press CTRL + C to stop bot     #
        #####################################   
"""

print(Fore.MAGENTA + logo0 + Style.RESET_ALL)

print(Fore.CYAN + logo1 + Style.RESET_ALL)

print(Fore.YELLOW + logo2 + Style.RESET_ALL)

print(logo3)
print(Fore.RED + logo4 + Style.RESET_ALL)
print('Starting pegaxy racing bot...')
print('\n')
time.sleep(5)

"""
to get window name:

window = pygetwindow.getWindowsWithTitle('Pegaxy')[0]
print(window)

"""


window = pygetwindow.getWindowsWithTitle('Pegaxy - Mozilla Firefox')[0]
time.sleep(2)
window.maximize()
time.sleep(5)

def print_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        sct_img = numpy.array(sct.grab(monitor))

        # Grab the data
        return sct_img[:, :, :3]

def locate_coordinates(img, threshold=0.8):
    print = print_screen()
    result = cv2.matchTemplate(print, img, cv2.TM_CCOEFF_NORMED)
    w = img.shape[1]
    h = img.shape[0]

    yloc, xloc = numpy.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles
    

def move_cursor(x, y, t):
    pyautogui.moveTo(x, y, t, pyautogui.easeInOutQuad)
    
def load_screenshots(dir_path='./screenshots/'):

    file_names = listdir(dir_path)
    targets = {}
    for file in file_names:
        path = 'screenshots/' + file
        targets[file.removesuffix('.png')] = cv2.imread(path)

    return targets


def already_race_menu():
    matches = locate_coordinates(images['racing_menu_on'])
    return len(matches[0]) > 0


def do_click(img, timeout=3, threshold=0.8):

    start = time.time()
    has_timed_out = False
    while(not has_timed_out):
        matches = locate_coordinates(img, threshold)

        if(len(matches[0]) == 0):
            has_timed_out = time.time()-start > timeout
            continue

        x, y, w, h = matches[0][0]
        pos_x = x + w / 2
        pos_y = y + h / 2
        move_cursor(pos_x, pos_y, 1)
        pyautogui.click(clicks=2)
        return True

    return False
    
    
def workbot():

    global images
    images = load_screenshots()



    while True:
        print('Pressing start...')
        do_click(images['start'])
        do_click(images['start'])
        do_click(images['start'])
        do_click(images['start'])
        do_click(images['start'])

        if (do_click(images['empty_energy'], 0.7)):

            print(Fore.RED + f'{horseName} horse without energy...' + Style.RESET_ALL)

            print('Refreshing page...')
            pyautogui.hotkey('ctrl', 'f5')
            time.sleep(5)
            break
        else:

            
            while True:
                print('Waiting metamask sign...')
                do_click(images['sign'], 30)
                time.sleep(3)
                if (do_click(images['find_another'])):
                    print(Fore.YELLOW + 'Fail to start race, searching for another...' + Style.RESET_ALL)
                else:
                    print('Starting race...')
                    global countRace
                    countRace = countRace + 1
                    print(Fore.GREEN + f'{horseName} horse running the race number {countRace}, please wait...' + Style.RESET_ALL)
                    time.sleep(100)
                    do_click(images['next_match'], 300)
                    print('Next race...')
                    break
            
        
    time.sleep(3)
    
images = load_screenshots()

 
print('Acessing racing menu...')
do_click(images['racing_menu'])

print('Picking the pegaxy...')
do_click(images['pick_a_pega'])
time.sleep(2)
print("\nCounting horses, please wait...")


# Takes a screen shot and saves the file in the specified location
loc1 = (r'Capture.png')
pyautogui.screenshot(loc1)

# Reads the screen shot and loads the image it will be compared too
img_rgb = cv2.imread(loc1)
count = 0

# Reads the file
template_file_ore = r"horse.png"
template_ore = cv2.imread(template_file_ore)
w, h = template_ore.shape[:-1]

# Compares screen shot to given image, gives error thresh hold
res = cv2.matchTemplate(img_rgb, template_ore, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = numpy.where(res >= threshold)


# Puts red box around matched images and counts horses
for pt in zip(*loc[::-1]):
    loc1 = (r'Capture.png')
    pyautogui.screenshot(loc1)


 # Reads the file
    template_file_ore = r"horse.png"
    template_ore = cv2.imread(template_file_ore)
    w, h = template_ore.shape[:-1]

 # Compares screen shot to given image, gives error thresh hold
    res = cv2.matchTemplate(img_rgb, template_ore, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = numpy.where(res >= threshold)


  # Reads the screen shot and loads the image it will be compared too
    img_rgb = cv2.imread(loc1)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    count = count + 1
    

        
    print(f"Horse {count} found.")

horses = locate_coordinates(template_ore)


horse1x =  horses[0][0][0]
horse1y= horses[0][0][1]



horse2x =  horses[0][1][0]
horse2y= horses[0][1][1]




horse3x =  horses[0][2][0]
horse3y= horses[0][2][1]


while True:
    pyautogui.hotkey('ctrl', 'f5')
    horseName= "First"
    print(f"Clicking {horseName} horse")
    time.sleep(3)
    pyautogui.click(horse1x,  horse1y)
    time.sleep(3)
    workbot()

    horseName= "Second"
    print(f"Clicking {horseName} horse")
    time.sleep(3)
    pyautogui.doubleClick(horse2x,  horse2y)
    time.sleep(3)
    workbot()

    horseName= "Third"
    print(f"Clicking {horseName} horse")
    time.sleep(3)
    pyautogui.click(horse3x,  horse3y)
    time.sleep(3)
    workbot()
    
    sleepMinutes = 60
    sleepScript = sleepMinutes*60
    nowHour = now.strftime("%H:%M:%S")
    nowDate = now.strftime("%d/%m/%Y")
    nowString = nowHour + " - " + nowDate
    print(Back.CYAN + Fore.RED + f'Sleeping {sleepMinutes} minutes after {countRace} race(s).  {nowString}' + Style.RESET_ALL)
    time.sleep(sleepScript)



