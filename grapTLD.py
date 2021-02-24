import sys

filepath = sys.argv[1]

def gettld():
    with open(filepath, 'r') as file:
        for line in file:
            tld = [".com", ".net", ".org", ".uk", ".fr", ".edu", ".de", ".eu", ".ie", ".int", ".mil", ".biz", ".io", ".jp", ".services", ".nl"]
            for tl in tld:
                if tl in line: 
                    x = line[:line.rfind("/")]
                    if "http" in x:
                        y = x.split('://')[1]
                        if "www" in y:
                            z = y.split('www.')[1]
                            print(z , end='\n', file=open("output.txt", "a"))
                        else:
                            print(y, file=open("output.txt", "a"))
                    elif "www" in x:
                        print(x.split('www.')[1], file=open("output.txt", "a"))
                    else:
                        print(x, file=open("output.txt", "a"))
                else:
                    pass

def sorting():
    with open('output.txt') as result:
            uniqlines = set(result.readlines())
            with open('output.txt', 'w') as rmdup:
                rmdup.writelines(set(uniqlines))
                print("Done!")

gettld()
sorting()
