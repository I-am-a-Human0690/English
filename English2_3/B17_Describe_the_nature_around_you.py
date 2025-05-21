#c s f k p ch sh th gh
#บรรยายธรรมชาติรอบตัว #28
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Describe_the_nature_around_you_2_17={
'Air':'อากาศ',


'Climate':'ภูมิอากาศ/อากาศ',
'Crop':'พืชผล',


'Down':'ลง',
'Dust':'ฝุ่น',
    #Why is there dust everywhere


'Earth':'โลก/พื้นโลก',


'Flower':'ดอกไม้',
'Fire':'ไฟ',
'Field':'สนาม',
'Forest':'ป่า',


'Grass':'หญ้า',


'Heat':'ความร้อน',


'Land':'ที่ดิน/ลงจอด',
'Leaf/leaves':'ใบไม้',
'Landscape':'ทิวทัศน์/ภูมิประเทศ',
'Light':'แสงสว่าง',#สว่าง=อ่อน


'Mood':'ดวงจันทร์',
'Mountain':'ภูเขา',
'Material':'วัสดุ/วัตถุ/ผ้า',


'Nature':'ธรรมชาติ/ลักษณะ',



'Planet':'ดาวเคราะห์',
'Plant':'พืช',


'Rain':'ฝน/ฝนตก',
'River':'แม่น้ำ',#ริบเวอร์
'Rose':'ดอกกุหลาบ',


'Sea':'ทะเล',
'Sky':'ท้องฟ้า',
'Sun':'ดวงอาทิตย์',
'Star':'ดาว',
'Stone':'หิน/ก้อนกิน',
'Smoke':'ควัน',
'Soil':'ดิน',
'Sand':'ทราย',


'Tree':'ต้นไม้',


'Universe':'จักรวาล',
'Up':'ขึ้น',


'Volcano':'ภูเขาไฟ',

'Wood':'ไม้',
'Wooden':'ที่ทำด้วยไม้',#วูดดิด wooden spoon
'Weather':'อากาศ',
'Wind':'ลม',
}
def call():
    for k,v in Describe_the_nature_around_you_2_17.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Describe_the_nature_around_you_2_17.items():
       if name in k:
           print(k,"=",v)
    print("2_17")
        
# _search("")
           