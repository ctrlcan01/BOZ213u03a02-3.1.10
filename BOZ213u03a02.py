bitki = input("Bir bitki adı giriniz: ")

if bitki == "Spathiphyllum":
    print("Evet, Spathiphyllum en güzel bitkidir!")
elif bitki == "spathiphyllum":
    print("Hayır, büyük harfle Spathiphyllum yazmanı istiyorum!")
else:
    print("Spathiphyllum! Bu değil, " + bitki + "!")
