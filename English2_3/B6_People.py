#ถกประเด็นเรื่องผู้คนม นับเลข
Number={
'Baby':'เด็กทารก',
'Public':'สาธารณะ',#The Public = มหาชน
'Friend':'เพื่อน',
'Girlfriend':'แฟนสาว',
'Boyfriend':'แฟนหนุ่ม',
'Person':'คน/บุคคล',
'Ennemy/Enemies':'ศัตรู',#เอนเนมิส
'Youth':'เยาวชน',
'Human':'มนุษย์',
'Committee':'คณะกรรมการ',
'Foundation':'มูลนิธิ',
'Population':'ประชากร/ผลเมือง',
'Citizen':'ผลเมือง',#ซิดิเซน
'Conference':'งานสัมมนา',
'Rome':'โรม(เมืองหลวงของอิตาลี)',
'Culture':'วัฒนธรรม',#เคาเจอร์
'People':'ผู้คน',#a few 
'Village':'หมู่บ้าน',
'Individual':'บุคคล',#อินดิวิดดอล
'Couple':'คู่รัก/คู่/แฟน',
'Relationship':'ความสัมพันธ์',
'Victim':'เหยื่อ',
'Lady/Ladies':'สุภาพสตรี',
'One hundred':'100',
'Thousand':'1000',
'Some':'บางส่วน',#Some books หนังสือบางเล่ม
'Third':'ลำดับที่สาม/ที่สาม',
'Fourth':'ลำดับที่สี่/ที่สี่',
'Last':'ที่แล้ว/สุดท้าย',
'Million':'ล้าน',
'Amount':'จำนวน/ปริมาณ',
'Sum':'ผลรวม',
'Per':'ต่อ',#per meal - ต่อมื้อ
'Half':'ครี่ง',
'Pair':'คู่',
'Meter':'เมตร',
'Average':'ค่าเฉลี่ย/ธรรมดา',
'Majority':'ส่วนใหญ่/เสียงส่วนมาก/คนส่วนมาก',
'Total':'ทั้งหมด',
'Social meaia':'สื่อสังคมออนไลน์',
'Meeting':'ประชุม',
'Other':'อื่นๆ',
'Ugh':'เอ่อ!',
'Here is':'นี้คือ',
'Wait':'รอ/เดี่ยว/เดี่ยวก่อน',
    #i wait for you
    #i will wait for you to finish
'Oops':'อุ้ย',#อูบ
'Reservation':'การจอง',#Reserve จอง 2_8
'Strange':'แปลก',
'Stranger':'คนแปลก',
'Jacket':'เสื้อแจ็คเก็ต',
'Shower':'อาบน้ำ',
}

def call():
    for k,v in Number.items():
        print(k,"\n")
# call()


def _search(name):
    name=name.lower()
    for k,v in Number.items():
       k=k.lower()
       if name in k or name in v: 
           print(k,"=",v)
    print("2_6")
           
# _search("secretary")