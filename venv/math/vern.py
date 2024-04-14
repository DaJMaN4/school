
vern = [10, 13, 15, 16, 20, 25, 32, 40, 50, 56, 63, 80, 100, 120]

verni = [10, 13, 16, 20, 25, 32, 40, 50, 63, 80, 100, 120]

tversnittcu = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70]
tversnittal = [16, 25, 35, 50, 70]

forlegninsmåter = ["a1","a2","b1","b2","c","d2","e"]

Iz = {"a1":{"CU PVC":[14.5,19.5,26,34,46,61,80,99,119,151], "AI PVC": [48,63,77,93], "CU PEX":[19,26,35,45], "AI PEX": [64,84,103,125]},
      "a13":{"CU PVC":[13.5,18,24,31,42,56,73,89,108,136], "AI PVC": [43,57,70,84], "CU PEX":[17,23,31,40], "AI PEX": [58,76,94,113]},
      "a2":{"CU PVC":[14,18.5,25,32,43,57,75,92,110,139], "AI PVC": [44,58,71,86], "CU PEX":[18.5,25,33,42], "AI PEX": [60,78,96,115]},
      "a23":{"CU PVC":[13,17.5,23,29,39,52,68,83,99,125], "AI PVC": [41,53,65,78], "CU PEX":[16.5,22,30,38], "AI PEX": [55,71,87,104]},
      "b1":{"CU PVC":[17.5,24,32,41,57,76,101,125,151,192], "AI PVC": [60,79,97,118], "CU PEX":[23,31,42,54], "AI PEX": [79,105,130,157]},
      "b13":{"CU PVC":[15.5,21,28,36,50,68,89,110,134,171], "AI PVC": [53,70,86,104], "CU PEX":[20,28,37,48], "AI PEX": [71,93,116,140]},
      "b2":{"CU PVC":[16.5,23,30,38,52,69,90,111,133,168], "AI PVC": [54,71,86,104], "CU PEX":[22,30,40,51], "AI PEX": [72,94,115,138]},
      "b23":{"CU PVC":[15,20,27,34,46,62,80,99,118,149], "AI PVC": [48,62,77,92], "CU PEX":[19.5,26,35,44], "AI PEX": [64,84,103,124]},
      "c":{"CU PVC":[19.5,27,36,46,63,85,112,138,168,213], "AI PVC": [66,83,103,125], "CU PEX":[23,33,45,58], "AI PEX": [84,101,126,154]},
      "c3":{"CU PVC":[17.5,24,32,41,57,76,96,119,144,184], "AI PVC": [59,73,90,110], "CU PEX":[22,30,40,52], "AI PEX": [76,90,112,136]},
      "d2":{"CU PVC":[22,28,38,48,64,83,110,132,156,192], "AI PVC": [63,82,98,117], "CU PEX":[27,35,46,58], "AI PEX": [76,90,112,136]},
      "d23":{"CU PVC":[19,24,33,41,54,70,92,110,130,162], "AI PVC": [53,69,83,99], "CU PEX":[23,30,39,49], "AI PEX": [64,82,98,117]},
      "e":{"CU PVC":[22,30,40,51,70,94,119,148,180,232], "AI PVC": [73,89,111,135], "CU PEX":[26,36,49,63], "AI PEX": [91,108,135,164]},
      "e3":{"CU PVC":[18.5,25,34,43,60,80,101,126,153,196], "AI PVC": [61,78,96,117], "CU PEX":[23,32,42,54], "AI PEX": [77,97,120,146]}
      }

temp = {10:[1.22,1.15,1.10,1.07],
        15:[1.17,1.12,1.05,10.4],
        20:[1.12,1.08,1,1],
        25:[1.06,1.04,0.95,0.96],
        30:[1,1,0.89,0.93],
        35:[0.94,0.96,0.84,0.89],
        40:[0.87,0.91,0.77,0.85],
        45:[0.79,0.87,0.71,0.8],
        50:[0.71,0.82,0.63,0.76],
        55:[0.61,0.76,0.55,0.71],
        60:[0.5,0.71,0.45,0.65]
        }

ak = {1:[1,0.8,0.7,0.65,0.6,0.57,0.5,0.45,0.41,0.38],
      2:[1,0.85,0.79,0.75,0.73,0.72,0.7,0.7,0.7,0.7],
      3:[0.95,0.81,0.72,0.68,0.66,0.64,0.61,0.61,0.61,0.61],
      4:[1,0.88,0.82,0.79,0.77,0.76,0.73,0.73,0.73,0.73],
      5:[1,0.87,0.82,0.8,0.8,0.79,0.78,0.78,0.78,0.78]
      }

vern1 = []
iz = 0
m = ""
ale = 0
tv = None
fm = None
while True:
    if input("Regn Iz? y/n ") == "y":

        while forlegninsmåter.__contains__(fm) == False:
            fm = input("forlegninsmåte: ")

        while m != "cu" and m != "al":
            m = input("Metall cu/al: ")
            if m != "cu" and m != "al":
                print("Skriv inn cu eller al")

        if m == "cu":
            m = "CU"
        elif m == "al":
            m = "AI"

        while ale != "2" and ale != "3":
            ale = input("Antall ledere: ")
            if ale != "2" and ale != "3":
                print("Det kan være 2/3 ledere")

        if m == "AI":
            while tversnittal.__contains__(tv) == False:
                tv = float(input("tversnitt: "))

        else:
            while tversnittcu.__contains__(tv) == False:
                tv = float(input("tversnitt: "))
        iso = input("PVC? y/n ")

        if ale != "2":
            fm = fm + "3"
        if iso != "y":
            m = m + " PEX"
        else:
            m = m + " PVC"

        if m[0] == "C":
            if tversnittcu.__contains__(tv):
                for x in range(10):
                    if tv == tversnittcu[x]:
                        tv = x
                        break
            else:
                raise Exception("Feil tversnitt")
        else:
            if tversnittal.__contains__(tv):
                for x in range(10):
                    if tv == tversnittal[x]:
                        tv = x
                        break
            else:
                print(m, "waiuhuwfa")
                raise Exception("Feil tversnitt")

        iz = Iz.get(fm).get(m)[tv]
        print("Iz er ",iz)

        if input("Trenges korreksjon for omgivelser y/n ") == "y":
            if input("Trenges korreksjon for omgivelsetemperatur y/n ") == "y":
                te = int(input("Utgi temperatur "))
                if m[5] == "C":
                    iz = iz * temp.get(te)[0]
                    print("ny Iz = ", iz)
                elif m[5] == "X":
                    z = iz * temp.get(te)[1]
                    print("ny Iz = ", iz)

            if input("Trenges korreksjon for nærføring av flere kabler y/n ") == "y":
                te = int(input("Velg hvilken type korreksjon vil du ha                           \n"
                               "Kabler i bunt i luft, på en overflate, innstøpt ller innkapslet (1) \n"
                               "Enkelt lag på vegg, gult eller uperforert bro                   (2) \n"
                               "Enkelt lag festet direkte under himmling/tak                    (3) \n"
                               "Enkelt lag på en horisontal eller vertikal perforert bro        (4) \n"
                               "Enkelt lag på kabelstige, knekter eller lignande                (5) \n:"))
                ll = int(input("Hvor mange ledere ligger ved siden av hveradnre? :"))
                if ll <= 6:
                    pass
                elif 7 <= ll < 9:
                    ll = 7
                elif 9 <= ll < 12:
                    ll = 8
                elif 12 <= ll < 16:
                    ll = 9
                elif 16 < ll:
                    ll = 10

                print(ll)
                iz = iz * ak.get(te)[ll - 1]
                print("ny Iz = ", iz)

    if input("Finne ut vern? y/n ") == "y":

        Ib = float(input("Ib = "))

        if iz == 0:
            iz = float(input("Iz = "))

        bolig = input("bolig? y/n ")

        if bolig == "y":
            for x in vern:
                if Ib <= x <= iz and x * 1.45 <= iz:
                    vern1.append(x)
        else:
            for x in vern:
                if Ib <= x <= iz:
                    vern1.append(x)

        print("alle vern som passer: ", vern1)

        print("")

        input("Trykk hvilke som helst knapp for å starte på nytt")
        iz = 0
        print("\n\n\n")



