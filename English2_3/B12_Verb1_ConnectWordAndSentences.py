#c s f k p ch sh th gh
#ใช้กริยาช่อง1 เชื่อมคำและประโยค
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Verb1_ConnectWordAndSentences_12={
'Apply':'ใช้/นำไปใช้/สมัคร',
    #We are going to apply for that job
    #We are going to apply it พวกเราจะนำมันไปใช้
'Accept':'ยอมรับ',
'Avoid':'หลีกเลี่ยง',
'Achieve':'บรรลุ',
'Affect':'มีผลกระทบ/ส่งผลกระทบ',
'Analyze':'วิเคราะห์',
'Adult':'ผู้ใหญ่',


'Build/Built':'สร้าง',#Building ตึก2_5_2
'Belong':'เป็นของ',#Belong to 


'Choose/Chose/Choosen':'เลือก',
'Cover/Coveren':'ปิดบัง/คลุม/ครอบคลุม',
    #Cover your nose
'Consider':'พิจารณา/ถือว่าเป็น',
'Cookbook':'หนังสือสอนทำอาหาร',


'Define':'นิยาม/กำหนด',
'Dish':'จาน',


'Exist':'มีอยู่/ดำรงอยู่',


'Forget/Forgot':'ลืม',


'Good job':'เก่งมาก',


'Increase':'เพิ่ม/เพิ่มขึ้น',
'Improve':'ปรับปรุง/ทำให้ดีขึ้น/แก้ไข',


'Prevent':'ป้องกัน/ขัดขวาง',
    #Are you going to prevent the conflict
'Pepper':'พริกไทย',


'Repeat':'ทำซ้ำ/ทวน',
'Recover':'ฟื้นตัว/กู้คืน',
'Recipe':'สูตรอาหาร',


'Suffer':'ทุกข์ทรมาน',
'Shut':'ปิด/หุบ',#0
'Secret':'ความลับ',


'Though':'แม้ว่า/ถึงแม้ว่า',#โดวว/โดวโอ่


'Understand/Understood':'เข้าใจ',



}
def call():
    for k,v in Verb1_ConnectWordAndSentences_12.items():
        print(k)
# call()

def _search(name):
    name=name.lower()
    for k,v in Verb1_ConnectWordAndSentences_12.items():
       k=k.lower()
       if name in k or name in v:
           print(k,"=",v)
    print("B_12")
        
# _search("")
           