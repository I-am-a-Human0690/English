#c s f k p ch sh th gh
#จับเข่าคุยการเมือง 37
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#Nothing is as important as peace ไม่มีอะไรสำคัญเท่าความสงบสุข
#I do not want to take the blame for something that I did not do
#The students are making progress นักเรียนมีความก้าวหน้า/กำลังพัฒนา
#I made my decision ฉันตัดสินใจแล้ว
#She loves him because of his wealth เน้นที่เหตุผลเน้นเพื่ออธิบาย /She loves him for his wealth อันนี้ใช้ในชีวิตประจำวัน
#Thank you for your piece of advice / Thank you for your advice
#He is the leader of the century
#The candidate gave a speech last Monday
Talking_About_Politics_26={
'Advice':'คำแนะนำ',
'Army':'กองทัพ/กองทัพบก',
'Argument':'ความขัดแย้ง/การโต้เถียง',
'Arrest':'จับ/การจับคุม',
    #I will arrest him
    #Is he under arrest


'Blame':'การกล่าวโทษ/การติเตียน/การตำหนิ',


'Court':'ศาล',#โค้ด
'Crime':'อาชญากรรม',
'Campaign':'การหาเสียง/การรณรงค์/การเผยแพร่',
'Congress':'รัฐสภา(อเมริกา)',
'Conflict':'ความขัดแย้ง',
'Candidate':'ผู้สมัคร',
    #He like the other candidates more
'Crisis':'วิกฤต',
'Cause':'สาเหตุ/ต้นเหตุ',
    #There are many causes for this problem


'Debt':'หนี้สิน',
    #I am in debt to you ฉันติดหนี้คุณ
'Debt Crises':'วิกฤตหนี้สิน',
'Decision':'การตัดสินใจ',#Did you make a decision
'Decide':'ตัดสินใจ',#I decided to do it


'Economy':'เศรษฐกิจ',
'Election':'การเลือกตั้ง',
    #There are elections every four years

'Freedom':'เสรีภาพ',


'Government':'รัฐบาล',
'Governor':'ผู้ว่าการ/ผู้ว่าราชการ(จังหวัด)',


'H':'',


'Investment':'การลงทุน',


'J':'',

'King':'พระราชา',


'Law':'กฦหมาย',
'Leader':'ผู้นำ',


'Mayor':'นายยกเทศมนตรี',


'National':'ระดับชาติ',
    #The next week is the national wine week
'Navy':'กองทัพเรือ',
'Navy blue':'สีน้ำเงินเข้ม',


'Opinion':'ความคิดเห็น',
    #We have different opinion


'President':'ประธานาธิบดี',
'Progress':'ความคืบหน้า/ความก้าวหน้า',
    #The work is now in progress งานกำลังดำเนินอยู่ตอนนี้ Now ไม่ค่อยใส่กัน
'Peace':'ความสงบสุข/สันติภาพ',
'Parliament':'รัฐสภา',
'Prince':'เจ้าชาย',
'Plan':'แผน/วางแผน/โครงการ/ตั้งใจทำ',
    #Dad didn't plan to break both arms พ่อไม่ได้ตั้งใจทำแขนทั้งสองหัก


'Queen':'พระราชินี',

'R':'',


'Security':'ความปลอดภัย',
    #We have two dogs for security
'Satety':'ความปลอดภัย',
    #Your father think about your safety
'Society':'สังคม',#โซไซเอที้
    #He has an important role in society
'Strategy':'กลยุทธ์',#สแตดเอจี้
    #What is the stategy of his campaign
    #Hope is not a stategy
'Speech':'การปราศรัย/การพูด',
    #Free speech เสรีการพูด
'Strike':'หยุดงานประท้วง',
    #There is a Strike today
    #The strike happend with no violence การประท้วงนี้ได้เกิดขึ้นโดยไม่มีความรุนแรง
'Senator':'วุฒิสมาชิก/วุฒิสภา',


'Tax':'ภาษี',


'U':'',


'Vote':'การออกเสียง/การลงคะแนน',
'Violence':'ความรุนแรง',

'War':'สงคราม',
'Wealth':'ความรวย/ความมั่งคั่ง',#เวลฟู่
    #Nature is the wealth of this country
'Weapon':'อาวุธ',
}
def call():
    for k,v in Talking_About_Politics_26.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Talking_About_Politics_26.items():
       if name in k:
           print(k,"=",v)
    print("2_26")
        
# _search("")
           