#c s f k p ch sh th gh
#เข้าใจสรรพนามสะท้อน
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z


B16_Understanding_reflexive_pronouns={
'A':'',


'B':'',


'C':'',


'D':'',


'E':'',


'F':'',


'G':'',


'Himself':'ตัวเขา',
    #He love himself
    #He made his breakfast by himself

'Itself':'ตัวมันเอง',
    #The dog hears itself
    #The problem is the machine itself


'J':'',

'K':'',


'L':'',


'Myself':'ตัวเอง',
    #I see myself
    #I have not seen myself in the mirror today

'N':'',


'Ourselves':'ตัวพวกเราเอง',
    #We love ourselves

'P':'',

'Q':'',

'R':'',


'S':'',


'Themselves':'ตัวพวกเขาเอง',
    #Many people like to travel by themselves
    #He makes everyone feel good about themselve


'U':'',


'V':'',

'W':'',

'X':'',

'Yourselves':'ตัวคุณเอง',
    #What do you think of yourselves
    #You have to believe in yourself
    #Go tell him yourself
    #Did you go by yourselves

'Z':'',
}
def call():
    for k,v in B16_Understanding_reflexive_pronouns.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in B16_Understanding_reflexive_pronouns.items():
       if name in k:
           print(k,"=",v)
    print("B16")
        
# _search("")
           