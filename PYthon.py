import pyttsx3
import os
engine = pyttsx3.init()
engine.say("Hi ..I am PY assistant...")
engine.runAndWait()
while True:
    print('Hi...This is your PY assistant....What can i do for you..???')
    u = input()
    if ((("open" in u) or ("launch" in u) or ("run" in u)) and (("notepad" in u) or ("editor" in u))):
        engine.say("opening notepad")
        engine.runAndWait()
        os.system("notepad")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and ("control panel" in u)):
        engine.say("opening control panel")
        engine.runAndWait()
        os.system("control panel")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and ("chrome" in u)):
        engine.say("opening google chrome")
        engine.runAndWait()
        os.system("chrome")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and ("firefox" in u)):
        engine.say("opening firefox")
        engine.runAndWait()
        os.system("firefox")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and (("audacity" in u) or ("Audacity" in u))):
        engine.say("opening Audacity")
        engine.runAndWait()
        os.system("audacity")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and ("paint" in u)):
        engine.say("opening paint")
        engine.runAndWait()
        os.system("mspaint")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and ("jupyter notebook" in u)):
        engine.say("opening jupyter notebook")
        engine.runAndWait()
        os.system("jupyter notebook")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and (("vlc" in u) or ("media player" in u))):
        engine.say("opening vlc media player")
        engine.runAndWait()
        os.system("vlc")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and (("microsoft edge" in u) or ("browser" in u) or ("internet explorer" in u))):
        engine.say("opening microsoft edge")
        engine.runAndWait()
        os.system("msedge")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and (("photoshop" in u) or ("Photoshop" in u))):
        engine.say("opening Photoshop CS6")
        engine.runAndWait()
        os.system("photoshopCS6")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and (("vs code" in u) or ("visual studio" in u))):
        engine.say("opening visual studio code")
        engine.runAndWait()
        os.system("code")
    elif ((("open" in u) or ("launch" in u) or ("run" in u)) and (("star uml" in u) or ("uml" in u))):
        engine.say("opening star uml")
        engine.runAndWait()
        os.system("staruml")
    elif (("exit" or "close") in u):
        engine.say("exiting")
        engine.runAndWait()
        break
    else:
        print("Oops Sorry ! I Could not understand You")
        engine.say("Oops sorry ! I Could not understand You")
        engine.runAndWait()