from os import path
import os
from pydub import AudioSegment
import pandas as pd

df1 = pd.read_csv("XXX/WorkSpace/AI_Projects/voices/cv-corpus-7.0-2021-07-21/ar/genderClassification/train_gend.csv")
df2 = pd.read_csv("XXX/WorkSpace/AI_Projects/voices/cv-corpus-7.0-2021-07-21/ar/genderClassification/test_gend.csv")
df = df1.append(df2)
df = df[['path','gender']]


directory_src = "XXX/WorkSpace/AI_Projects/voices/cv-corpus-7.0-2021-07-21/ar/clips"

directory_dst = "XXX/WorkSpace/AI_Projects/voices/cv-corpus-7.0-2021-07-21/ar/wav"


# files 


for f in os.listdir(directory_src):
    src = directory_src+os.sep+f
    dst = directory_dst+"/"+f[:-4]+".wav"
    if os.path.isfile(dst):
        print(f+" already converted")
    else :
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        print(f+" is converted")

print("the convertion is done successfully ! Congratulations ! ")
    