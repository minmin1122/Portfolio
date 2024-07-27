from gtts import gTTS
import pyaudio
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import tkinter

rec = sr.Recognizer()
def enter():
    with sr.Microphone() as source:
        print("listening...")
        l1["text"] = "listening..."
        l1.update()
        voice = rec.listen(source)
        voice_text = rec.recognize_google(voice, language="ja-JP")
        l1["text"] = voice_text
        if voice_text in "敦盛" or "東大出身":
            if voice_text in "敦盛":
                word = "敦盛"
            elif voice_text in "東大出身":
                word = "学歴自慢"
            output_text = "申し訳ございません。"+ word + "が出てしまいました。"
            output = gTTS(text=output_text, lang="ja")
            output.save("output.mp3")
            l1["text"] = output_text
            l1.update()
            play(AudioSegment.from_mp3("output.mp3"))
        else:
            pass

root = tkinter.Tk()
root.title("謝罪代行プログラム")
root.geometry("640x480")
l1 = tkinter.Label(root, text="出力画面")
l1.pack()
b1 = tkinter.Button()
b1["text"] = "実行"
b1["command"] = enter
b1.pack()
root.mainloop()