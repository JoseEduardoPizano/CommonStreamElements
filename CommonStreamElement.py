import re
def CommonStreamElement(msg1,msg2):
    msg1 = re.sub(r'[.,"\'-?:!;]', "", msg1)
    msg2 = re.sub(r'[.,"\'-?:!;]', "", msg2)
    x = msg1.split()
    y = msg2.split()

    print("Mensaje 1")
    print(x)
    print("Mensaje 2")
    print(y)
    l3=[]
    n = 0
    for list in x:
        for list2 in y:
            if list == list2:
                l3.insert(n,list2)
                n = n+1
    return l3

txt = "Nota: cuando se especifica maxsplit, la lista contendrá el número especificado de elementos más uno"
txt2 = "Divida la cadena, usando una coma, seguida de un espacio, como separador"




x = CommonStreamElement(txt,txt2)
print("Coincidencias")
print(x)
