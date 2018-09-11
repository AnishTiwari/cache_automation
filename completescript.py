import glob
import os
import shutil
import time

source_dir = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Media Cache"
# noinspection PyRedeclaration
dst = 'D:/saavn'  # Path you want to move your files to
files = glob.iglob(os.path.join(source_dir, "f_*"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, dst)
        print("1111111111")

from subprocess import Popen  # /test.py file(for calling batch file for merging mp3 files)

p = Popen("mergemp3.bat", cwd=r'D:/saavn', shell=True)
stdout, stderr = p.communicate()
print("2222222222")

source_dir = "D:/saavn"  # Path where your files are at the moment   MOVING THE MP3 TO SONGS FOLDER
dst = 'D:/saavn/songs'  # Path you want to move your files to
files = glob.iglob(os.path.join(source_dir, "*.mp3"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, dst)

for f in glob.glob("C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Media Cache\\f_*"):
    os.remove(f)

for f in glob.glob("D:/saavn/f_*"):
    os.remove(f)

for f in glob.glob("D:/saavn/*.mp3"):
    os.remove(f)

print("Your Song is Saved!!!")

for f in glob.glob("D://saavn//songs//myFile.txt"):
    os.remove(f)

for f in glob.glob("C:\\Users\\admin\\Downloads\\myFile*.txt"):
    os.remove(f)
