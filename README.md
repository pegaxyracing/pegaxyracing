<img hspace="3" alt="Logo" src="https://raw.githubusercontent.com/pegaxyracing/pegaxyracing/master/res/logo.png" height=84/>


[español](https://github.com/pegaxyracing/pegaxyracing/blob/master/res/README_es.md) | [português](https://github.com/pegaxyracing/pegaxyracing/blob/master/res/README_pt_BR.md)

### About it:

This is a fork from [pega-racing-bot](https://github.com/GabrielZulian/pegaxy-racing-bot). This bot, developed in Python, is to automate races in pegaxy.
The game developers do not allow the use of bots. It was developed for study purposes only, not responsible for any penalties that may be incurred for using it. Use it at your own risk.


The software is free and open source and should not be used for commercial purposes. Pull requests are welcome.


### How to install it:



1 - Download Python from official website [here](https://www.python.org/downloads/).

2 - Install Python on your OS. (Remeber to add PYTHON to path)

<img src="https://raw.githubusercontent.com/pegaxyracing/pegaxyracing/master/res/path.png">
	
3 - Open your terminal (Command prompt).
	
4 - Go to bot folder using following command:

```
cd c:/pegaxy-runner-bot
```
	
	
Here i recommend you installing virtualenv as a good practice,
so you don't fill your computer with packages that you won't use later, 
or cause bug with other python applications. The processes below 
are not required. Remember if you do that will always have to activate
it before using the bot.
	
	
To install virtualenv use pip:
	
```
pip install virtualenv
```
	
To create a new virtualenv named venv:
	
```
pip install virtualenv
```
	
	
To activate virtualenv:
	
```
.\venv\Scripts\activate
```
	
You can see now a (venv) that is the name of virtualenv you created. 

5 - Install all requeriments using following command:

```
pip install -r requirements.txt
```
	
or you can install it manually using following commands:
	
```
pip install pillow
```
```
pip install opencv-python
```
```
pip install pyautogui
```
```
pip install mss
```
```
pip install colorama
```
	

6 - Recommend you take all screenshots from folder screenshots using [LightShot](https://app.prntscr.com/pt-br/download.html)


7 - Run bot using following command:

Remember that you must be on the pegaxy's website with your metamask connected.

```	
python main.py
```
	

8 - Use CTRL + C to STOP script.


### To do 🎯:
	
```
- Organize code.
- Solve start buttom bug.
- Solve expected bug if user has less than three horses (IndexError).
- Make code smarter, work only if energy != 0/0.
- Take horses name.
- Save race data by horse.
```



### Found a bug or questions?

	Feel free to open an issue.


### Do you like it ? Buy me a coffee or a horse! Wallet (Polygon / BSC):

```
0xEEf8F8023C3d24276Bd807705C213d6994c064b6
```
