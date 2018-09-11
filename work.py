from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import os
import subprocess

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Media Cache")
w = webdriver.Chrome(executable_path="C:\\Python27\\chromedriver.exe")

w.get('https://www.saavn.com/')

while(1):
    path_to_watch = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Media Cache"
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while True:
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added:
            print "Added1111: ", ", ".join(added)
            time.sleep(10)
            print "Added: ", ", ".join(added)
            w.execute_script("javascript:var x=document.getElementById('player-track-name');  var textToSave = x.firstChild.innerHTML; var hiddenElement = document.createElement('a'); hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave); hiddenElement.target = '_blank'; hiddenElement.download = 'myFile.txt'; hiddenElement.click();")
            subprocess.call(['python', 'completescript.py'])
        if removed: print "Removed: ", ", ".join(removed)
        before = after