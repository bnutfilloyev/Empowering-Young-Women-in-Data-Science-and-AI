# Bu - misol modul fayli (my_module.py)

def salomlashish(ism):
    """Salomlashish funksiyasi"""
    return f"Salom, {ism}!"

def hisoblash(a, b, amal="qo'shish"):
    """Matematik amallar"""
    if amal == "qo'shish":
        return a + b
    elif amal == "ayirish":
        return a - b
    elif amal == "ko'paytirish":
        return a * b
    elif amal == "bo'lish":
        if b != 0:
            return a / b
        else:
            return "Nolga bo'lish mumkin emas!"
    else:
        return "Noma'lum amal!"


class Shaxs:
    """Shaxslar haqida ma'lumot saqlash uchun klass"""
    
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
    
    def tanishtir(self):
        return f"Mening ismim {self.ism} va yoshim {self.yosh}."
    
shaxs = Shaxs("Ali", 30)

# O'zgaruvchilar
PI = 3.14159
AUTHOR = "Python o'quvchisi"

# Modulni import qilganda ishlaydigan kod
if __name__ == "__main__":
    print("Bu modul to'g'ridan-to'g'ri ishga tushirilmoqda!")
    print(salomlashish("Dasturchi"))
else:
    print(f"'{__name__}' moduli import qilindi!")