#พูดถึงสถานที่ม เรียกชื่อสิ่งของทั่วไป
location={
    'Location':'สถานที่',
    'Castle':'ปราสาท',
    'Place':'สถานที่/ตำแหน่ง/ที่พัก/วาง/ใส่',
        #i like this place a lot
        #Where are you going to place it
        #She is going to place the flower on the table
    'Site':'สถานที่/เว็บไซด์',
    'District':'เขต',
    'Zone':'เขต/บริเวณ',
    'Border':'ชายแดน/เขตแดน',
    'Bathroom':'ห้องน้ำ',
    'Yard':'สนาม',
    'Kitchen':'ห้องครัว',
    'Hotel':'โรงแรม',
    'retaurant':'ร้านอาหาร',
    'House':'บ้าน',
    'Neighborhood':'แถวบ้าน/ละแวกบ้าน',
    'Neighbor':'เพื่อนบ้าน',
    'Beach':'หาด',
    'Rest':'พักผ่อน',
        #You need to get some rest
    'City':'เมือง',
    'Area':'พื้นที่',
    'Church':'โบสถ์',
    'Street':'ถนน',
    'Airport':'สนามบิน',
    'Port':'ท่า', #ท่าเรือ
    'Italy':'อิตาลี',
    'Country':'ประเทศ',
    'Vienna':'เวียนนา/เมืองหลวงของออสเตรีย',
    'Office':'สำนักงาน',
    'Center':'ศูนย์กลาง',
    'Into':'เข้าไป',
    'Building':'ตึก/อาคาร',
    'Room':'ห้อง',
    'Department':'แผนก',
    'Park':'สวนสาธารณะ/สวน/จอดรถ',
    'Garden':'สวน',
    'Market':'ตลาด',
    'Address':'ที่อยู่',
    'Property':'ทรัพย์สิน/คุณสมบัติ',
    'Bar':'บาร์',
    'Island':'เกราะ',
    'Bank':'ธนาคาร',
    'Region':'ภูมิภาค',
    'Front':'ข้างหน้า',
        #There is a bus stop in front of the hotel
    'Inside':'ภายใน',
    'Station':'สถานี',
    'Coast':'ชายฝั่ง',
    'Ground':'พื้นดิน',
    'Valley':'หุบเขา',
    'Museun':'พิพิธภัณฑ์',
    'Route':'เส้นทาง',
    'Avenue':'ถนน/ถนนใหญ่/วิธีการ',
    'Corner':'มุม/หัวมุม',
    'Cinema':'โรงภาพยนตร์/โรงหนัง',
    'Tower':'ตึกสูง',
    'Town':'เมือง',
    'Capital':'เมืองหลวง',
    'Community':'ชุมชน',
    'Spain':'ประเทศสเปน',
    'Rights':'สิทธิ',
    'Palace':'พระราชวัง',
    'Prison':'คุก',
    'North':'ทิศเหนือ',
    'West':'ตะวันตก',
    'Farm':'ฟาร์ม',
    'Zoo':'สวนสัตว์',
    'Square':'ลานกว้าง',
    'Currently':'ปัจจุบัน/ขณะนี้',
  
}

def call():
    for i in location.keys():
        print(i,"\n")

# call()


def _search(name):
    name=name.lower()
    for k,v in location.items():
       k=k.lower()
       if name in k or name in v: 
           print(k,"=",v)
    print("2_5_2")
           
# _search("zoo")
