"""
seçenek >>

# eğer kullanıcı 1 seçerse kullanıcıdan sese çevrilecek metni isteyin
# mesela
    sese çevrilecek metni gir: 
    
# eğer kullanıcı 2 seçerse aşağıdaki uyarı ile son mp3 kaydını oynat
    ses çalınıyor...
    
# eğer kullanıcı 3 seçerse aşağıdaki mesajı gösterip programı sonlandır
    uygulamamızı kullandığınız için teşekkürler
    bye...
    
"""
from gtts import gTTS
import os

menu = """
1) Yeni Ses Kaydı
2) Son Kaydı Oynat
------------------
0) Çıkış

"""

while True:
    print(menu)
    secim = int(input("Seçiminiz >> "))
    if secim == 0:
        print("Uygulamamızı kullandığınız için teşekkürler")
        break
    elif secim == 1:
        metin = input("Sese çevrilecek metni gir: ")
        ses = gTTS (metin, lang = "tr")
        ses.save("engelsiz.mp3")
    elif secim == 2:
        os.system("engelsiz.mp3")
    else :
        print("Hatalı seçim yaptınız. Tekrar deneyiniz...") 
	
    ##input("çıkış için bir tuşa basınız >>> ")