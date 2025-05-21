#Plan for the future 38
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#going to = กำลังจะ/จะ
#We are going to ask again tomorrow
#She is going to ask for water เธอจะไปขอน้ำ
#You did not tell me that you were going to arrive today
#I am going to add that i did not see pond ฉันกำลังจะบอกว่าฉันไม่เห็นปอน
#The student is going to achieve what he wants
#I am going to be a father
#Who is going to believe me
#What are you going to drink
#What would you like to drink สุภาพ
#What are you going to be drinking 
    #"At the party tonight, what are you going to be drinking?" (ถามถึงการดื่มที่จะเกิดขึ้นในช่วงเวลาหนึ่งในอนาคต)
#The dog going to be in the yard
#What book are you going to read
#My mother is not going to believe us
#His new book is going to come out next month
#Are we going to eat พวกเราจะกินไหม
#I am going to control myself
#We are going to continue eating พวกเราจะกินอาหารต่อไป
#Are you going to continue with this campaign
#We are going to finish eating
#I am going to go there
#I am going to go to school
#I am never going to forget my daughter
#We are not going to forget your voice
#We are going to leave soon
#You are going look for a house คุณกำลังมองหาบ้าน
#I think it is going to rain today
#I am going to reduce the amount of food
#We are going to think about you/We will miss you พวกเราจะคิดถึงคุณ
#We think about you all the time พวกเราคิดถึงคุณตลอดเวลา
#I am going to wait five more minutes ฉันจะรออีก 5 นาที
#I am going to want juice after i run
#I do not know what you are going to ask ฉันไม่รู้ว่าคุณจะถามอะไร
#Are you going to add more sugar
#I am going to consider you my friend ฉันจะพิจารณาคุณเป็นเพื่อนของฉัน
#Which pair of shoes are you going to put on คุณจะสวมรองเท้าคู่ไหน
#I am going to sleep late tonight
#if i do this she will fall in love with me
#She and i are not going to walk more
#I am nothink without you
Plan_for_the_future_27={
'A':'',


'Break':'หยุดพัก/แตกหัก',


'C':'',


'D':'',


'Establish':'จัดตั้ง',
    #They are going to establish a soccer team


'F':'',


'G':'',


'H':'',


'I':'',


'J':'',

'K':'',


'Look after':'ดูแล',
    #i am going to look after my sister

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
    for k,v in Plan_for_the_future_27.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Plan_for_the_future_27.items():
       if name in k:
           print(k,"=",v)
    print("2_27")
        
# _search("")
           