#c s f k p ch sh th gh
#ใช้กริยาช่อง1 เชื่อมคำและประโยค 40
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#We live in the age of technology พวกเราอยู่ในยุคของเทคโนโลยี
#He is still full of energy
#Do you have a smaller size
#At what speed does he run
#Sometimes a mass will change to energy
#Everything has a reason
#The second cycly รอบที่สอง
#What is the total weight
#Size is important to us
Talk_about_science_28={
'Article':'บทความ',
'Analysis':'การวิเคราะห์/ผลการวิเคราะห์',
    #What was his analysis ผลการวิเคราะห์ของเขาเป็นอย่างไร
    #Her analyses are good
'Alcohol':'แอลกอฮอล์',


'B':'',


'Chemistry':'วิชาเคมี/เคมี',
'Concept':'แนวคิด',
'Cycle':'รอบ/วงจร/วัฎจักร',#circle = วงกลม 2_14
    # i am studying the life cycly of the spider
'Conclusion':'บทสรุป',


'Details':'ลายละเอียด',
'Distance':'ระยะทาง',
    #What is the distance to your house
'Definition':'คำนิยาม',#define = นิยาม/กำหนด(กริยา) 2_12
    #That is the Definition นั้นคือคำนิยาม
'Depth':'ความลึก',#'Deep':'ลึก/ลึกซึ้ง',2_10
    #The depth is important
    #What is the depth of the pool
'Discovery':'การค้นพบ',
    #The discovery of that medicine was important
'Discover':'ค้นพบ',#กริยา
'Dot':'จุด',
    #I see a dot on your shirt
'Decrease':'ลด',
    #They decrease the speed of the car

'Energy':'พลังงาน',
'Edition':'ฉบับพิมพ์',
'Electric':'ไฟฟ้า/เกี่ยวกับไฟฟ้า',


'Formula':'สูตร',


'Geography':'ภูมิศาสตร์',


'Height':'ความสูง',


'Investigation':'การสอบสวน',



'J':'',

'K':'',


'Line':'เส้น/แถว',
    #We are wainting in line พวกเรากำลังรอในแถว/พวกเรากำลังเข้าแถว
'Length':'ความยาว',
    #What is the length of that bridge
    #How long is that bridge
'Limit':'ขอบเขต',
    #Science has no limit
'Laboratory':'ห้องทดลอง',#แลบเบอทอรี่
'Landline':'โทรศัพท์บ้าน',


'Method':'วิธี',#เมดเธด
'Mass':'มวล',
    #Heat has no mass
'Measure':'มาตรการ',#เมเชอร
    #All three measures


'N':'',


'O':'',


'Project':'โครงการ',
'Publication':'สิ่งพิมพ์',
'Philosophy':'ปรัชญา',

'Quantity':'จำนวน',
    #My daughter likes to eat bread in large quantities


'Research':'การวิจัย/งานวิจัย',
'Reason':'เหตุผล',
    #I have my own reasons


'Size':'ขนาด',
'Science':'วิทยาศาสตร์',
'Sample':'ตัวอย่าง',
    #The sample is not pure enough
    #Here is a sample
'Scale':'ตาชั่ง/มาตรส่วน/ขนาด',
'Surface':'พื้นผิว',
'Scientist':'นักวิทยาศาสตร์',


'Theory':'ทฤษฎี',
'Task':'งาน/ภาระ/ภารกิจ',
    #my boss has a new task for me
'Technique':'เทคนิค',
'Temperature':'อุณหภูมิ',
    #The temperature will be the same tomorrow

'Unit':'หน่วย',
    #The second is a unit of time


'Volume':'ระดับเสียง/ปริมาณ/ปริมาตร',
    #The water volume is not enough
    #He turns up the volume เขาเพิ่มเสียง

'Weight':'น้ำหนัก',
}
def call():
    for k,v in Talk_about_science_28.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Talk_about_science_28.items():
       if name in k:
           print(k,"=",v)
    print("2_28")
        
# _search("")
           