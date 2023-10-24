
'''
lloyd = {
 "name": "Lloyd",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}
alice = {
 "name": "Alice",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}
tyler = {
 "name": "Tyler",
 "homework": [0.0, 87.0, 75.0, 22.0],
 "quizzes": [0.0, 75.0, 78.0],
 "tests": [100.0, 100.0]
}
def getav(lis):
    summed = sum(lis)
    totality = float(summed)/float(len(lis))
    return totality
stud = [lloyd,alice,tyler]
intt = 0
for i in stud:
    print(i["name"])
    print(i["homework"])
    print(i["quizzes"])
    print(i["tests"])
    print("")
    intt1= sum(i["homework"])
    intt2= sum(i["quizzes"])
    intt3= sum(i["tests"])
    tes = getav(i["tests"])
    qu = getav(i["quizzes"])
    h = getav(i["homework"])
    print("average test: ", tes)
    print("average quiz: ", qu)
    print("average home: ", h)
    print("")
    print("tes result:")
    if tes >= 90:
        print("Tes get: A")
    elif tes >= 80 and tes < 90:
        print("Tes get: b")
    elif tes >= 70 and tes < 80:
        print("Tes get: c")
    elif tes >= 60 and tes < 70:
        print("Tes get: d")
    elif tes < 60:
        print("fail")
    print("")
    print("quiz result:")
    if qu >= 90:
        print("quiz get: A")
    elif qu >= 80 and tes < 90:
        print("quiz get: b")
    elif qu >= 70 and tes < 80:
        print("quiz get: c")
    elif qu >= 60 and tes < 70:
        print("quiz get: d")
    elif qu < 60:
        print("fail")
    print("")
    print("tes result:")
    if h >= 90:
        print(" get: A")
    elif h >= 80 and tes < 90:
        print("homework get: b")
    elif h >= 70 and tes < 80:
        print("homework get: c")
    elif h >= 60 and tes < 70:
        print("homework get: d")
    elif h < 60:
        print("fail")
    print("")

'''
#task2
'''cl={
"COP 2510" :"Programming Concepts",
"EGN 3000L" :"Foundations of Engineering Lab",
"MAC 2281" :'Calculus',
"MUH 3016" :"Survey of Jazz",
"PHY 2048" :"General Physics I"
}

c = {
"COP 2510" :"Z. Beasley",
"EGN 3000L" :"J. Anderson",
"MAC 2281":"A. Makaryus",
"MUH 3016" :"A. Wilkins",
"PHY 2048" :"G. Pradhan"
}

i = {
    "COP 2510" :"MW 1230pm – 1:45pm",
"EGN 3000L" :"TR 1100am – 12:15pm",
"MAC 2281" :"MW 9:30am – 10:45am",
"MUH 3016 ":"online asynchronous",
"PHY 2048" :"TR 5:00pm – 6:15pm"
}
classthing = input("hpls input class")
print(cl[classthing])
print(c[classthing])
print(i[classthing])
'''
#task3
'''lizie = []

class sale():
    def __init__(self,moday,tuesday,wednesday,thursday,friday):
        self.moday = moday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
someguy= sale(0,0,0,0,0)
someguy.moday= input("pls input for manday: ")
someguy.tuesday= input("pls input for tuesday: ")
someguy.wednesday= input("pls input for wednesday: ")
someguy.thursday= input("pls input for thursday: ")
someguy.friday= input("pls input for friday: ")


lizie.append(someguy.moday)
lizie.append(someguy.tuesday)
lizie.append(someguy.wednesday)
lizie.append(someguy.thursday)
lizie.append(someguy.friday)
hanxo = []
news = []
for stri in lizie:
    stri = str(stri)
    for a in stri:
        if a.isnumeric():
            hanxo.append(a)
        elif a.isalpha():
            pass
    nes= ''.join(hanxo)
    hanxo.clear()
    news.append(nes)
print(hanxo)
print(news)


'''
#task4
thecode = ""
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..'
}

listwo = []
userin = input("pls input str to convert into moarse: ")
userin = userin.upper() #i mostly got this mthod from dennis i actually first thought i had to convert a moarse into a str but i will try my best to put my twist into it so credit to dennis
listwo.append(userin)
for word in listwo:
    for w in word:
        if w in morse_code:
            thecode = thecode+ morse_code[w] + " "
        else:
            pass
print(thecode)
