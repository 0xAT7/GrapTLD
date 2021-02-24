import sys

filepath = sys.argv[1]

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
                        print(z , end='\n')
                    else:
                        print(y)
                elif "www" in x:
                    print(x.split('www.')[1])
                else:
                    print(x)
            else:
                pass
