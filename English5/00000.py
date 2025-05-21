#c s f k p ch sh th gh
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
D3_Describe_a_day_in_college={
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

'Q':'',


'R':'',


'S':'',


'T':'',


'U':'',


'V':'',

'W':'',

'X':'',

'Y':'',

'Z':'',
}
def call():
    for k,v in D3_Describe_a_day_in_college.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in D3_Describe_a_day_in_college.items():
       if name in k:
           print(k,"=",v)
    print("D4")
        
# _search("")
           