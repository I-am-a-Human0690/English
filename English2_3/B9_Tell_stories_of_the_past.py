#บอกเล่าเรื่องในอดีต คุ้นเคยกับกริยาช่อง1
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#c, s, f, k, p, , ch, sh, th, gh
#have to ... ต้อง... เช่น  you have to do it คุณต้องทำมัน
Tell_stories_of_the_past={
'Answer':'ตอบ(คำถาม)/รับ(โทรศัพท์)',

'Born/Bornt':'เกิด',# 1เมื่อนจะใช้ได้ทุกอย่าง
'Beat':'ตี',
'Buy/Bought':'ซื้อ',#บัดทึ
    #I cannot buy her anythink

'Close':'ปิด/ใกล้',
'Change':'เปลี่ยน/เปลี่ยนแปลง/การเปลี่ยนแปลง',
'Carry':'พก/นำ/ขนส่ง',
'Carrying':'แบก/ถือ',

'Drink/Drank/Drunk':'ดื่ม',
'Drinks':'เครื่องดื่ม',
'Die':'ตาย',
'Drive/Drove/Driven':'ขับ/ขับรถ',
'Diary':'สมุดบันทึก',

'Eat/Ate/Eaten':'กิน',
'Enter':'เข้า',

'Found/Founded':'พบ/ก่อตั้ง',
'Feel/Felt':'รู้สึก',
'Finish':'เสร็จสิ้น',
'Fall/Fell/Fallen':'ล้ม/ตก',


'Go/Went/Gone':'ไป',#กอน
'Give/Gave/Given':'ให้',
    #I give you a car
    #I give a car to you ทางการกว่า
    #I alway give the last seat to people older than me
    #I alway give people the last seat older than me ไม่ถูกเพราะ older than ไปขยาย the last seat

'Hear/heard':'ได้ยิน',
'Happen':'เกิดขึ้น',
    #What happened to you
    #How did it happen
    #What do you think will happen to it
'Handwriting':'ลายมือ',

'Infrom':'แจ้ง',#0


'Know/knew/known':'รู้/รู้จัก',
'Keep/Kept':'เก็บ/เก็บรักษา/ทำต่อไป',

'Listen':'ฟัง',
'Lose/Lost':'ทำหาย',#ลูส/ลอส
'Let':'อนุญาต',#0
'Live':'อาศัย/อยู่/อาศัยอยู่/สด',
'Life':'ชีวิต',
'Learn/Learned,Learnt':'เรียนรู้',


'Perfrom':'ดำเนินการ/แสดง', 
'Put':'ใส่/วาง/บรรจุ', #0 put on/put -- on  สวม he puts his dress on 
       #We put out the fire พวกเราดับไฟ
'Pay/Paid':'จ่าย',
'Play/Played':'เล่น',

'Reach':'เข้าถึง/มาถึง/ไปถึง',
'Rent':'ให้เช่า/เช่า',
'Return':'กลับคืน',

'Speak/Spoke/Spoken':'พูด',#สโปคเคน
'See/Saw/Seen':'เห็น',
'Seem':'ดูเหมือน',
'Saw/Sawed/Sawed,Sawn':'เลื่อย',
'Say/Said':'พูด',
'Show/Showed/shown':'แสดง',#*1/23/3
'Stop/Stopped':'หยุด',
'Stay/Stayed':'อยู่/พักอาศัย',
'Swim/Swam/Swum':'วายน้ำ',
'Sleep/Slept':'นอน',
'Sell/Sold':'ขาย',
'Scare':'ทำให้ตกใจ-กลัว',#you are scared of 
'Smile':'รอยยิ้ม/ยิ้ม',#give me a smile / my smile


'Tell/Told':'บอก',
    #i told you to read the book
'Think/Thought':'คิด',#ตอตทึ
'Tire/Tired':'เหนื่อย',
'Take/Took/Taled':'นำไป/เอา', #เทลดึ
    #he is taking money from the bank เขากำลังถอนเงินจากธนาคาร
    #You take your coffee without sugar
    #I take the bus to the city center/I go by bus


'Word':'คำ',
'Write/Wrote/written':'เขียน',
    #He write this book
    #He write to me
    #He write that he loves her
    #He write me a letter
    #The first part of the test is written #เพราะเป็นคำกริยา ถ้าเป็น writing จะการเป็นกำลังเขียน
'Win/Won':'ชนะ',
'Worry':'กังวล',
'Wake/Woke/Woken':'ตื่น/ปลุก',#Wake up ตื่นนอน

'Yesterday':'เมื่อวาน',



}
# for k,v in Tell_stories_of_the_past.items():
#     print(k)

def _search(name):
    name=name.lower()
    for k,v in Tell_stories_of_the_past.items():
       k=k.lower()
       if name in k or name in v:  
           print(k,"=",v)
    print("2_9")
         
# _search()
           