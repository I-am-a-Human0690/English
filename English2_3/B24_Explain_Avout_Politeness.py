#c s f k p ch sh th gh
#อธิบายเกี่ยวกับสุขภาพ 35
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#i have never had so much money ฉันไม่เคยมีเงินมากขนานนี้มาก่อน
#she found the key to my heart เธอพบกุญแจสู่หัวใจของผม
#out of sight out of mind รักแท้แพ้ระยะทาง
#my diet is not a choice it is a treatment การควบอาหารของฉันไม่ใช่ทางเลือก แต่มันคือการรักษา
#she goes to school by foot
#i eat with the hands
#my mother will also be sick
#this treatment works วิธีการบำบัดนี้ได้ผล
#in case of emercency
#i will be back
#i am back ฉันกลับมาแล้ว
#i go back home
Explain_Avout_Politeness_24={
'Ambulance':'รถพยาบาล',#แอมบิวแลซ
'Arm':'แขน',
'Accident':'อุบัติเหตุ',
    #he had an accident on the job
'Appointment':'การนัดหมาย/การแต่งตั้ง',
    #i have an Appointment with him at six


'Body':'ร่างกาย/ศพ',
'Blood':'เลือด',#บัด
'Brain':'สมอง',#he has cancer in the brain
'Back':'หลัง',


'Care':'ห่วงใย/การดูแล',
    #i care about you so much ฉันเป็นห่วงคุณมาก
    #i take care of my dad
    #i am taking good care of my dad ฉันกำลังดูแลพ่อของฉันเป็นอย่างดี
'Cancer':'โรคมะเร็ง',#he died of cancer
'Chest':'อก',#i have a pain in my chest
'Condition':'เงื่อนไข/สภาวะ',
    #the Condition in this agreement are good for us


'Disease':'โรค',#เดิสซีอิส #ดิซีด #what disease dose he have
'Diet':'อาหาร/โภชนาการ',#she is on a diet เธอกำลังลดน้ำหนัก
'Dream':'ฝัน/ความฝัน',#my dreams


'Eye':'ตา',
'Emergency':'เหตุฉุกเฉิน',
'Ear':'หู',


'Face':'ใบหน้า',
'Foot':'เท้า',
'Feet':'เท้า/ฟุต',#i am six feet tall ฉันสูงหกฟุต / feet up ยกเท้าขึ้น
'Finger':'นิ้ว',


'G':'',


'Hand':'มือ',
'Health':'สุขภาพ',#เฮลฟู่ คำนาม
'Healthy':'สุขภาพดี',#adjective #her health
    #Healthy food
    #it's very healthy! And it tastes good, too
'Head':'หัว',
'Heart':'หัวใจ',
'Hospital':'โรงพยาบาล',
'Health insurance':'ประกันสุขภาพ',


'Illness':'อาการป่วย/โรค/โรคภัยไข้เจ็บ',
    #what illness do i have ฉันป่วยเป็นอะไร
    #this illness make him weak อาการเจ็บป่วยนี้ทำให้เขาอ่อนแอ
'Ill':'ป่วย',#he is Ill


'J':'',

'K':'',


'Lips':'ริมฝีปาก',


'Medicine':'ยา',#she took that medicine เธอกินยานั้น
'Mouth':'ปาก',


'Neck':'คอ',
'Nose':'จมูก',
'Nurse':'พยาบาล',


'Operation':'การผ่าตัด',#ออบเปอร์เรชั่น
    #his Operation took eight hours
    #it took eight hours to do the Operation การผ่าตัดใช้เวลาไปแปดชัวโมง
    #he decided to have the Operation เขาตัดสินใจผ่าตัด


'Patient':'อดทน/ผู้ป่วย',#เพเชียนทึ
'Pain':'ความเจ็บปวด',# i have a pain here ฉันเจ็บตรงนี้


'R':'',


'Sick':'ป่วย',
'Skin':'ผิวหนัง',#she has light skin เธอมีผิวสีอ่อน
'Sight':'สายตา',


'Treatment':'การบำบัด/การรักษา',
'Tongue':'ลิ้น',#ธ่อง
    #Spanish is her mother tongue ภาษาสเปนเป็นภาษาแม่
'Teeth':'ฟัน',#ทีฟฟู่


'U':'',


'Virus':'เชื้อไวรัส',
'Vision':'สายตา/ทัศนวิสัย//การมองเห็น',

'W':'',
}
def call():
    for k,v in Explain_Avout_Politeness_24.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Explain_Avout_Politeness_24.items():
       if name in k:
           print(k,"=",v)
    print("B24")
        
# _search("")
           