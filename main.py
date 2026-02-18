# 1
a = {}
print(a)

# 2
talaba = {"ism": "Ali", "yosh": 20, "shahar": "Toshkent"}
print(talaba)

# 3
a = {"ism": "ali", "yosh": 20, "shahar": "toshkent"}
print(a["ism"])

# 4
talaba = {"ism": "Malika",
          "yosh": 19,
          "shahar": "Buxoro"
          }
print(talaba)
print(talaba[])

# 5
talaba = {"ism": "Jasur",
          "yosh": 21,
          "shahar": "Namangan"
          }
print(talaba)
print
["yosh"] = 23
talaba = {"ism": "Dilnoza", "yosh": 20, "shahar": "Andijon", "kurs": 2}
print(talaba)

del talaba "shahar"
print(talaba)

# 7
meva = {"olma": 15000,
        "nok": 12000,
        "uzum": 20000,
        "shaftoli": 18000}

print(meva.keys())

# 8
meva = {"olma": 15000,
        "nok": 12000,
        "uzum": 20000,
        "shaftoli": 18000}

print(meva.values())

# 9
kitob = {"nomi": "O'tkan kunlar",
         "muallif": "Abdulla Qodiriy",
         "yil": 1925,
         "sahifa": 320}

print(kitob.items())

# 10
kitob = {"nomi": "Mehrobdan chayon",
         "muallif": "Abdulla Qahhor",
         "sahifa": 280
}
print(kitob)

if "muallif" in kitob:
    print("Muallif kaliti mavjud")
else:
    print("Muallif kaliti mavjud emas")

# 11
rang = {"qizil": "red",
        "ko'k": "blue",
        "yashil": "green",
        "sariq": "yellow",
        "qora": "black"}

print(rang)
print(len(rang))

# 12
user = {
    "ism": "Aziza",
    "yosh": 25,
    "shahar": "Farg'ona"
}

print(user.get("email", "Email topilmadi"))

# 13
mahsulot = {"nomi": "Telefon",
            "brend": "Samsung",
            "narx": 3500000,
            "rang": "qora"}
print(mahsulot)
print(mahsulot.pop('narx'))

# 14
sozlamalar = {"til": "uz",
              "rang_rejim": "tungi",
              "shrift": "14px",
              "ovoz": True}
print(sozlamalar.clear())

# 15
asl_dict = {"a": 1,
            "b": 2,
            "c": 3,
            "d": 4}

print(asl_dict.copy())

# 16
maktab = {
    "10-A": {"o'quvchilar": 25, "sinf_rahbar": "Olimova N."},
    "10-B": {"o'quvchilar": 28, "sinf_rahbar": "Karimov S."},
    "11-A": {"o'quvchilar": 22, "sinf_rahbar": "Rahimova D."}
}
print(maktab)

17
maktab = {
    "10-A": {"o'quvchilar": 25, "sinf_rahbar": "Olimova N."},
    "10-B": {"o'quvchilar": 28, "sinf_rahbar": "Karimov S."}
}
print(maktab)
print(len(maktab))

# 18
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 10, "d": 4, "e": 5}

dict3 = dict1 | dict2
print(dict3)

19
atlar = {"UZ": "O'zbekiston",
             "RU": "Rossiya",
             "US": "Amerika",
             "TR": "Turkiya"
}
print(atlar)
for kalit in atlar:
    print(kalit)

# 20
baholar = {"Matematika": 5,
           "Fizika": 4,
           "Kimyo": 5,
           "Biologiya": 4,
           "Tarix": 5}

for kalit, qiymat in baholar.items():
    print(kalit, ":", qiymat)

# # 21
shaxs = {"ism": "Jamshid",
         "yosh": 21,
         "shahar": "Xorazm"
}
print(shaxs)
shaxs.setdefault()
print(shaxs)


# # 22
dict1 = {"a": 1,
         "b": 2
}
print(dict1)
dict2 = {"c": 3,
         "d": 4
}
print(dict2)
dict3 = {"e": 5,
         "f": 6
}
print(dict3)
dict1.update(dict2)
dict1.update(dict3)
print(dict1)
#
# # 24
narxlar = {
    "Non": 3000,
    "Sut": 9000,
    "Tuxum": 18000,
    "Go'sht": 85000,
    "Yog'": 45000,
    "Sabzi": 7000
}
print(narxlar)
eng_qimmat = max(narxlar, key=narxlar.get)

print("Eng qimmat mahsulot:", eng_qimmat)

# 25
matn = "salom dunyo salom python python python dunyo"

sozlar = matn.split()
natija = {}

for soz in sozlar:
    if soz in natija:
        natija[soz] += 1
    else:
        natija[soz] = 1

print(natija)



