#วางแผนการเดินทาง, รู้จักคำนำหน้านาม
Plan_a_trip={
'Exciting':'น่าตื่นเต้น',
'Excited':'ตื่นเต้น',
    #I am so excited
'Tennis':'เทนนิส',
'Tennis racket':'ไม้เทนนิส',
'basketball':'บาสเก็ตบอล',
'ball':'บอล',
'Ballet':'การเต้นบัลเลต์',
'Problem':'ปัญหา',
'Dance':'เต้น',
'Bus':'รถประจำทาง/รถเมล์',
'Bus stop':'ป้ายรถเมล์',
'Car':'รถยนต์',
'Train':'รถไฟ',
'Bicycle':'รถจักรยาน',
'Suitcase':'กระเป๋าเดินทาง',
'Travel':'เดินทาง',
'Boat':'เรือ',
'Airplane':'เครื่องบิน',
'Plane':'เครื่องบิน',
'Backpack':'เป้/กระเป๋าเป้',
'Motorcycle':'มอเตอร์ไซค์',
'Visit':'เยี่ยม',
'Drive':'ขับ',
'Guide':'ผู้นำเที่ยว/ไกด์',
'Road':'ถนน',
'Map':'แผนที่',
'Transportation':'การขนส่ง',
'Transport':'ขนส่ง',
    #We are going to transport milk to the school
'Vehicle':'ยานพาหนะ/พาหนะ/รถ',
'Ship':'เรือลำใหญ่',
'Spanish':'ภาษาสเปน',
'Portuguese':'คนโปรตุเกส',#โปรตุกี
'Bridge':'สะพาน',#บิจ
'Flight':'เที่ยวบิน',
'Adventure':'การผจญภัย',
'Journey':'การเดินทาง',
'Trip':'การเดินทาง',
'France':'ประเทศฝรั่งเศล',
'French':'ภาษาฝรั่งเศล/คนฝรั่งเศล',
'Italian':'ภาษาอิตาลี',#อิทแทลเลียน
'Subway':'รถไฟใต้ดิน',
'Departure':'การจากไป',
'German':'ภาษาเยอรมัน/คนเยอรมัน',
'America':'อเมริกา',
'tourist':'นักท่องเที่ยว',
'South':'ใต้',
'Abroad':'ต่างประเทศ',
'China':'ประเทศจีน',
'Chinese':'คนจีน/ภาษาจีน',
'Europe':'ทวีปยุโรป',
'European':'คนยุโรป',
'Passport':'หนังสือเดินทาง',
'Turn':'เปลี่ยน/กลับ/หัน/เลี่ยว/หมุน',
    #You turn right here/Take a right turn here ใช่สั่ง
    #You take a right turn here ใช้เพื่ออธิบาย เช่นวิธีที่คุณต้องไปคือเลี้ยวขวาตรงนี้
'Turn off':'ปิด',
'Around':'รอบ/ประมาณ',
'International':'นานาชาติ',
'Dinosaurs':'ไดโนเสาร์',
'Apartment':'อพาร์ตเมนต์',
'Popular':'เป็นที่นิยม/นิยม',
'blog':'เว็บล็อค',
'Right':'ใช่ไหม/ขวา',
'Well':'ดี',
}
# for k,v in Plan_a_trip.items():
#     print(k)


def _search(name):
    name=name.lower()
    for k,v in Plan_a_trip.items():
       k=k.lower()
       if name in k or name in v: 
           print(k,"=",v)
    print("2_7_2")
           
# _search("Meter")