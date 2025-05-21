#c s f k p ch sh th gh
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

#You're right. I need to clean my room more often
#I don't enjoy cleaning up by myself
#My dog broke this vase, so I'm responsible for cleaning it up
#If we clean up together, we'll finish faster
#I put a soft rug on the floor. Now my feet feel warm and comfortable
#Where is the rug? It should be on the floor here
#Let's move the rug and mop the floor
E5_Talk_about_the_chores={
'A':'',


'Blanket':'ผ้าห่ม',


'Closet':'ตู้เสื้อผ้า',
'Carpet':'พรม',#พรมขนาดใหญ่ที่ปูคลุมพื้นทั้งหมดหรือเกือบทั้งหมดของห้อง #มักจะ ติดตั้งแบบถาวร โดยยึดติดกับพื้นห้อง


'Dish':'จาน/ชาม/ถ้วย',
    #พหูพจน์ I wash dishes
'Dishwasher':'เครื่องล้างจาน',
    #he dishwasher is broken
'Dislike':'ไม่ชอบ',


'E':'',


'F':'',


'Garbage':'ขยะ',
    #ขยะที่เป็น ของเปียกหรือเน่าเปื่อยได้ เช่น เศษอาหาร เปลือกผัก ผลไม้ หรือของเหลือจากการทำอาหาร
    #Garbage is something you throw out because it is not useful
    #Yes, it's in the garbage with your old socks


'Housework':'งานบ้าน',
    #I helped her with her housework
'Heater':'เครื่องทำความร้อน',
    #During cold winters, I use a heater to keep my room warm

'I':'',


'J':'',

'K':'',


'Loud':'ดัง',


'Messy':'ยุ่งเหยิง',
    #Your side of the room is messier than mine
'Mop':'ถู',
'Make/Made':'ทำ/สร้าง',
    #When Mom make me clean the house, I cannot say no. Mom's the boss around here
    #He make me vacuum my room

'Neat':'ประณีต/เรียบร้อย',
    #If you want your house to be neat, you have to clean it often
'Neatly':'อย่างเรียบร้อย',


'O':'',


'Plate':'จาน',
    #"I need a clean plate."
'Push':'ดัน',#Poosh
    #Turn on the vacuum and push it over the dust. It's loud, but it cleans the floor.
'Pot':'หม้อ',
    #When you make pasta or rice, you start with a pot full of water

'Q':'',


'Rug':'พรม',#พรมขนาดเล็กหรือกลางที่สามารถ เคลื่อนย้ายได้


'Sock':'ถุงเท้า',
'Shelf':'ชั้นวาง',
'Stove':'เตา',
'Soft':'นุ่ม/เบา',


'Toilet':'ห้องน้ำ',
'Toilet paper':'กระดาษชำระ',
'Throw':'ขว้าง/โยน/ทิ้ง',
'Trash':'ขยะ',
    #ขยะทั่วไปที่มักเป็น สิ่งของแห้ง เช่น กระดาษ พลาสติก กล่อง หรือสิ่งที่ไม่ใช้แล้ว


'U':'',


'Vaccuum':'ดูดฝุ่น',
    #Oh Vacuuming is much fater #การดูดฝุ่น
'Vase':'แจกัน',

'Wash':'ซัก/ล้าง',
'Water':'น้ำ',
    #I water thos plants

'X':'',

'Y':'',

'Z':'',
}
def call():
    for k,v in E5_Talk_about_the_chores.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in E5_Talk_about_the_chores.items():
       if name in k:
           print(k,"=",v)
    print("E5")
        
# _search("")
           