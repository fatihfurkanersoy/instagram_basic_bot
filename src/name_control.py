file = open("file/photo_likes.txt" , "r").readlines() #sayafadan çektiğimiz

filecontrol = open("file/just_1_name.txt" , "a") #isim teke düşer
count = 0
Sadece1isim = []

for line in file :
    if line not in Sadece1isim:
        filecontrol.write(line)
        Sadece1isim.append(line)
