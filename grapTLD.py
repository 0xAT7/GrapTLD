import sys

filepath = sys.argv[1]

with open(filepath, 'r') as file:
    for line in file:
        if ".com" in line or ".net" in line or ".org" in line or ".uk" in line or ".fr" in line or ".edu" in line or ".de" in line or ".eu" in line or ".ie" in line or ".int" in line or ".mil" in line or ".biz" in line or ".io" in line or ".jp" in line or ".services" in line or ".nl" in line:
            x = line[:line.rfind("/")]
            if "http" in x:
                y = x.split('://')[1]
                if "www" in y:
                    z = y.split('www.')[1]
                    print(z , end='\n')
                else:
                    print(y)
            elif "www" in x:
                print(x.split('www.')[1])
            else:
                print(x)
        else:
            pass
