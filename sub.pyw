from gtts import gTTS
import codecs,sys,os,main
from pydub import AudioSegment

url = 'https://notify-api.line.me/api/notify'
token = 'OAOqdzcOWdZxh3IlBg2mwNOVuSzzI2Lz5UDrOJPSSRc'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
'''-------------audio-----------'''
def merge(au1,au2):
    song1 = AudioSegment.from_mp3('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+au1+'.mp3')
    song2 = AudioSegment.from_mp3('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+au2+'.mp3')
    silen = AudioSegment.silent(duration=1500)
    final = song1 + silen + song2
    final.export('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+au1+'.mp3',format='mp3', codec="libmp3lame")
    os.remove('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+au2+".mp3")

'''--------------tts------------'''
def speak(x,file_):
    for i in range(len(x)):
        if i%2 == 0:
            language = 'ko'
        elif i%2 != 0:
            language = 'th'

        tts = gTTS(x[i], lang = language)
        tts.save('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+str(i)+'.mp3')
        if i != 0:
            song1 = AudioSegment.from_mp3('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+str(i-1)+'.mp3')
            song2 = AudioSegment.from_mp3('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+str(i)+'.mp3')
            silen = AudioSegment.silent(duration=1500)
            final = song1 + silen + song2
            final.export('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+str(i)+'.mp3',format='mp3', codec="libmp3lame")
            os.remove('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+str(i-1)+".mp3")
    os.rename('C:/Users/pk/Downloads/เกาหลี V.3/audio/'+str(len(x)-1)+'.mp3','C:/Users/pk/Downloads/เกาหลี V.3/audio/'+file_+'.mp3')
    
def text(first):
    x=[]
    y = first.split('\n')
    for i in y:
        if i != '':
            a = i.split()
            x.extend(a)
    speak(x)
    
def file(file_):
    x = []
    f = codecs.open('C:/Users/pk/Downloads/เกาหลี V.3/txt/'+file_+'.txt','r','utf-8')
    fl = f.readlines()
    for i in fl:
        i = i.rstrip('\n').split()
        x.extend(i)
    f.close()
    speak(x,file_)

def create(write_,file):
    x=[]
    x = write_.split()
    write__ = ''
    for i in x:
        if x.index(i)%2 == 0:
            write__ += i + ' '
        elif x.index(i)%2 == 1:
            if i != x[-1]:
                write__ += i + '\n'
            else:
                write__ += i
    f = codecs.open(file+'.txt','w','utf-8')
    f.write(write__)
    f.close()
