import os, sys, random, time, threading

# --- OTOMATİK KÜTÜPHANE YÜKLEYİCİ ---
def kutuphane_kontrol():
    try:
        import requests
    except ImportError:
        print("🚀 Kütüphane eksik, patron için otomatik yükleniyor... Lütfen bekle.")
        os.system(sys.executable + " -m pip install requests")
        print("✅ Yükleme bitti! Oyun başlıyor...")
        time.sleep(1)

kutuphane_kontrol()
import requests # Artık yüklendiği için hata vermez

# --- AYARLAR ---
TOKEN = "8584511756:AAER422sp3V_qvhTEIZJkb1G_VvlQthqYjw"
# Botuna bu TOKEN ile bağlanıyoruz patron.

# --- DEĞİŞKENLER ---
bakiye = 100
asa_hakki = 0
borc = 0
last_id = 0

def ekran_yenile():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\n" + " ✨ " + "═"*45 + " ✨ ")
    print(f"   💰 SERVET: {bakiye:,} TL | 📉 BORÇ: {borc} TL")
    print(f"   🔮 ASA HAKKI: {asa_hakki} | 🧠 MATEMATİK: ÖLÜMCÜL")
    print(" " + "═"*49)
    print("   [ENTER] YAZI/TURA | [1] MARKET | [3] BORÇ AL")
    print("   [4] SORU BİL PARA KAZAN (RİSK!)")
    print("   [Q] OYUNDAN ÇIK")
    print(" " + "═"*49)
    print(" >>> BOT AKTİF! Bakiye için bota sayı yaz patron.")
    sys.stdout.write(" >>> Seçimin: ")
    sys.stdout.flush()

def bakiye_motoru():
    """Bot üzerinden bakiye çekme sistemi"""
    global bakiye, last_id
    while True:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_id + 1}&timeout=1"
            r = requests.get(url, timeout=2).json()
            if r.get("ok") and r.get("result"):
                for up in r["result"]:
                    last_id = up["update_id"]
                    msg = up.get("message", {}).get("text", "")
                    if msg.isdigit():
                        bakiye = int(msg)
                        ekran_yenile()
        except:
            pass
        time.sleep(1)

# Arka planda botu dinlemeye başla
threading.Thread(target=bakiye_motoru, daemon=True).start()

ekran_yenile()

while True:
    if borc > 0: bakiye -= 100
    
    try:
        secim = input().lower().strip()
        if secim == "q": break
        
        # --- [4] ÖLÜMCÜL MATEMATİK ---
        if secim == "4":
            os.system('clear')
            print("\n 🧠 RİSKLİ MATEMATİK")
            try:
                hedef = int(input(" Kaç para kazanmak istiyorsun?: "))
                if hedef < 100:
                    a, b = random.randint(10, 99), random.randint(10, 99)
                    soru, cevap = f"{a} + {b}", a + b
                elif hedef < 999:
                    a, b = random.randint(15, 60), random.randint(6, 18)
                    soru, cevap = f"{a} x {b}", a * b
                else: # 999+ İMKANSIZ MOD
                    a, b, c = random.randint(100, 999), random.randint(15, 45), random.randint(200, 800)
                    soru, cevap = f"({a} x {b}) - {c}", (a * b) - c
                
                print(f"\n ❓ SORU: {soru} = ?")
                tahmin = int(input(" Cevabın: "))
                if tahmin == cevap:
                    bakiye += hedef
                    print(" ✅ BİLDİN!")
                else:
                    bakiye = 0
                    print(f" 💀 BİLEMEDİN! Cevap: {cevap}. Servet sıfırlandı!")
            except: pass
            time.sleep(2); ekran_yenile(); continue

        if secim == "1": # MARKET
            os.system('clear')
            print("\n [A] Kadim Asa (30.000 TL) - 3 Hak")
            m = input(" Seçim: ").lower()
            if m == "a" and bakiye >= 30000:
                bakiye -= 30000; asa_hakki += 3
            ekran_yenile(); continue

        if secim == "3": # BORÇ
            if borc == 0: borc = 500; bakiye += 500
            ekran_yenile(); continue

        if secim == "": # YAZI TURA
            z = random.choice(["yazı", "tura"])
if asa_hakki > 0: print(f" 🔮 ASA: {z.upper()}!"); asa_hakki -= 1
            t = input(" y/t?: ").lower()
            if t in ["yazı", "tura"]:
                try:
                    m = int(input(" Bahis: "))
                    if 0 < m <= bakiye:
                        bakiye -= m
                        if t == z: bakiye += m*2; print(" 🎯 KAZANDIN!")
                        else: print(" 💀 KAYBETTİN!")
                    time.sleep(1)
                except: pass
            ekran_yenile()
    except: break
