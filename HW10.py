from gtts import gTTS
import playsound

tts = gTTS("안녕하세요 지구환경시스템과학부 석사 1학기 202455122 이진형입니다.", lang='ko')
tts.save("HW10_202455122_이진형.mp3")
playsound.playsound("HW10_202455122_이진형.mp3", True)
