import time
import sys

# التأكد من دعم الصوت حسب نظام التشغيل (Windows أو Mac/Linux)
try:
    import winsound
    def play_tone(frequency, duration):
        winsound.Beep(frequency, duration)
except ImportError:
    import os
    def play_tone(frequency, duration):
        # بديل الصوت لأنظمة Linux و Mac
        os.system('play -n synth %s sin %s' % (duration/1000, frequency))

def print_animated(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def celebrate():
    print("\n" + "="*50)
    print_animated("  ❤️ ✨ Happy Birthday My Love ✨ ❤️  ", 0.08)
    print("="*50 + "\n")
    
    time.sleep(0.5)
    print_animated("كل سنة وأنتِ أجمل وحتة من قلبي..", 0.06)
    print_animated("كل عام وأنتِ سر سعادتي وبطلة قصتي! 🎉", 0.06)
    print_animated("أتمنى لكِ سنة جديدة مليئة بالحب والنجاح والفرح. ❤️\n", 0.06)

    input("👉 اضغطي على Enter لبدء الاحتفال الموسيقي...")
    print("\n🎵 استمعي للنغمة...\n")

    # النوتات الموسيقية لأغنية Happy Birthday (التردد بالـ Hz، المدة بالـ ms)
    notes = [
        (262, 300), (262, 300), (294, 500), (262, 500), (349, 500), (330, 800),
        (262, 300), (262, 300), (294, 500), (262, 500), (392, 500), (349, 800),
        (262, 300), (262, 300), (523, 500), (440, 500), (349, 500), (330, 500), (294, 800),
        (466, 300), (466, 300), (440, 500), (349, 500), (392, 500), (349, 800)
    ]

    # رسم احتفالي أثناء عزف الموسيقى
    heart_art = [
        "   ******       ******   ",
        " **      **   **      ** ",
        "**          ***          **",
        "**                       **",
        " **                     ** ",
        "   **                 **   ",
        "     **             **     ",
        "       **         **       ",
        "         **     **         ",
        "           ** **           ",
        "             *             "
    ]

    # عزف النغمات
    for i, (freq, duration) in enumerate(notes):
        play_tone(freq, duration)
        if i < len(heart_art):
            print(f"   \033[91m{heart_art[i]}\033[0m")
        time.sleep(0.05)

    print("\n🎉 🥳 🎉 Happy Birthday! 🎉 🥳 🎉\n")

if __name__ == "__main__":
    celebrate()