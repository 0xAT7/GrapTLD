import sys

try:
    def gettld(filepath, output):
        with open(filepath, 'r') as file:
            for line in file:
                tld = [".com", ".net", ".org", ".uk", ".fr", ".edu", ".de", ".eu", ".ie", ".int", ".mil", ".biz", ".io", ".jp", ".services", ".nl"]
                for tl in tld:
                    if tl and tl + "/" in line:
                        x = line[:line.rfind("/")]
                        if "http" in x:
                            y = x.split('/')[2]
                            if "www." in y:
                                z = y.split('www.')[1]
                                print(z , end='\n', file=open(output, "a"))
                            else:
                                print(y, file=open(output, "a"))
                        elif "www." in x:
                            print(x.split('www.')[1], file=open("output", "a"))
                        else:
                            x = line.split('/')[0]
                            print(x, file=open(output, "a"))
                    elif tl in line:
                        if "http" in line:
                            a = line.split('://')[1]
                            if "www." in a:
                                b = a.split('www.')[1]
                                print(b , end='\n', file=open(output, "a"))
                            else:
                                print(a , end='\n', file=open(output, "a"))
                        elif "www." in line:
                            print(line.split('www.')[1], file=open(output, "a"))
                        else:
                            print(line, file=open(output, "a"))
                    else:
                        pass

    def sorting(output):
        with open(output) as result:
                uniqlines = set(result.readlines())
                delemptylines = filter(lambda x: not x.isspace(), uniqlines)
                with open(output, 'w') as final_file:
                    final_file.writelines(set(delemptylines))

    gettld(sys.argv[1] , sys.argv[2])
    sorting(sys.argv[2])
    print("Done! Check your file: " + sys.argv[2])

except:
    print("Usage: python3 grapTLD.py list.txt output.txt")
