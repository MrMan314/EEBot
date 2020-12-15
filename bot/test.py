import random as rd
equals = open('eq', 'r')
Lines = equals.readlines()
dat = []
for line in Lines:
    dat.append(line.strip().split("±"))
for data in dat:
    if data[0].split("·").__contains__(message):
        print(rd.choice(data[1].split("·")))
