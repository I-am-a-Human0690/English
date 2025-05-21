#c s f k p ch sh th gh
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#I found every letter that he had written to my mother

Present_Perfect_13={
'A':'',


'B':'',


'C':'',


'D':'',


'E':'',


'F':'',


'G':'',


'H':'',


'I':'',


'J':'',

'K':'',


'L':'',


'M':'',


'N':'',


'O':'',


'P':'',


'R':'',


'S':'',


'T':'',


'U':'',


'V':'',

'W':'',
}
def call():
    for k,v in Present_Perfect_13.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Present_Perfect_13.items():
       if name in k:
           print(k,"=",v)
    print("2_13")
        
# _search("")
           