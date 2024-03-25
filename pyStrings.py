# import string 

# strings radix=d file

def get_Strings(name,exclude=False):
    output=[]
    file = open(name,"rb").read()
    pc = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126, 32, 9, 10, 13, 11, 12]
    # this xcan be used if you dont mind importing a lib
    # pc = list(map(ord,string.printable))
    out=""
    start=0
    last=0
    for index,char in enumerate(list(file)):
        if char in pc:
            if last+1!=index:
                if len(out)>4:
                    if exclude:
                        output.append((start,start+len(out)))
                    else:
                        output.append((start,start+len(out),repr(out)))
                out=chr(char)
                start=index
            else:
                out+=chr(char)
            last=index
    return output

if __name__ == "__main__":
    from pprint import pprint
    pprint(get_Strings("out.bin"))
