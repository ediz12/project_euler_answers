nLetter = {
"1":"one",
"2":"two",
"3":"three",
"4":"four",
"5":"five",
"6":"six",
"7":"seven",
"8":"eight",
"9":"nine",
"10":"ten",
"11":"eleven",
"12":"twelve",
"13":"thirteen",
"14":"fourteen",
"15":"fifteen",
"16":"sixteen",
"17":"seventeen",
"18":"eighteen",
"19":"nineteen",
"20":"twenty",
"30":"thirty",
"40":"forty",
"50":"fifty",
"60":"sixty",
"70":"seventy",
"80":"eighty",
"90":"ninety",
}
from datetime import datetime
startTime = datetime.now()
total = 0
for i in range(1,1001):
    stri = str(i)
    if len(stri) == 1:
        total += len(nLetter[stri])
        print nLetter[stri]
    elif len(stri) == 2:
        if int(stri[0]) == 1:
            total += len(nLetter[stri])
            print nLetter[stri]
        elif int(stri[0]) > 1:
            total += len(nLetter[stri[0]+"0"])
            print nLetter[stri[0]+"0"],
            if int(stri[1]) != 0:
                total += len(nLetter[stri[1]])
                print nLetter[stri[1]]
    elif len(stri) == 3:
        total += len(nLetter[stri[0]] + "hundred")
        print nLetter[stri[0]] + "hundred",
        if int(stri[1]) > 0 or int(stri[2]) > 0:
            total += len("and")
            print "and",
            if int(stri[1:]) < 20:
                if int(stri[1]) == 0:
                    total += len(nLetter[stri[2]])
                    print nLetter[stri[2]]
                else:
                    total += len(nLetter[stri[1:]])
                    print nLetter[stri[1:]]
            else:
                total += len(nLetter[stri[1] + "0"])
                print nLetter[stri[1] + "0"],
                if int(stri[2]) != 0:
                    total += len(nLetter[stri[2]])
                    print nLetter[stri[2]]
    elif len(stri) == 4:
        total += len("onethousand")
print total
print(datetime.now()-startTime)
                
            
