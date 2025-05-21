#พูดถึงสถานที่ เรียกชื่อสิ่งของทั่วไป
Things={
'Spoon':'ช้อน',
'Fork':'ส้อม',
'Chair':'เก้าอี้',
'Magazine':'นิตยสาร',
'Snack':'อาหาร',
'Blanket':'ผ้าห่ม',
'Blowl':'ถ้วย / ชาม',
'Cup':'ถ้วย',
'Table':'โต๊ะ',
'Bottle':'ขวด',
'Window':'หน้าต่าง',
'Clock':'นาฬิกา',
'Mirror':'กระจก',
'Radio':'วิทยุ',
'Computer':'คอมพิวเตอร์',
'Cellphone':'มือถือ/โทรศัพท์',
'Telephone':'โทรศัพท์',
'Phone':'โทรศัพท์',
'TV':'ทีวี/โทรทัศน์',
'Television':'ทีวี/โทรทัศน์',
'Sofa':'โซฟา',
    #ทางการกว่า มักใช้เฟอร์นิเจอร์ที่เป็นโซฟาชัดเจนหรือหรู
'couch':'โซฟา',
    #ไม่ค่อยทางการ มักใช้สิ่งที่นั่งได้นอนได้คล้ายโซฟาแต่อาจไม่ชัดว่าเป็น
'Basket':'ตะกร้า',
'Lamp':'โคมไฟ',
'Desk':'โต๊ะ,โต๊ะทำงาน',
'Battery':'แบตเตอรี่',
'Soap':'สบู่',
'Watch' :'จับตาดู/นาฬิกาข้อมือ',
'Door':'ประตู',
'Wallet':'กระเป๋าเงิน',
'Box':'กล่อง',
'Bedsheet':'ผ้าปูที่นอน',
    #What color are your bedsheets
'Screen':'จอภาพ',
'Razor':'มีดโกน',
'Floor':'พื้น/ชั้น',#twenty floors = 20 ชั้น
'Umbrella':'ร่ม',
'Bag':'กระเป๋า',
'Wall':'กำแพง',
'Toothbrush':'แปลงสีฟัน',
'Toothpaste':'ยาสีฟัน',
'Wheel':'ล้อ',
'Key':'กุญแจ',
'Letter':'จดหมาย',
'Mail':'จดหมาย',
    #International mail ไปรษณีย์ระหว่างประเทศ
'Envelope':'ซองจดหมาย',
'Post':'โพสต์',
'Postman':'บุรุษไปรษณีย์',
    #The post office sends and receives mail
'Pool':'สระน้ำ',
'Sponge':'ฟองน้ำ -สปอจ/สปั้น',
'Cabinet':'ตู้ ',#แคบบิเน็ท
'Roof':'หลังคา',
'Paper':'กระดาษ',
'Bell':'ระฆัง',
'Scissors':'กรรไกร',
'Pan':'กระทะ',
'Glasses':'แว่นตา',
'Glass':'กระจก/แก้ว',# two Glasses
'String':'ดาย/เชือก/เส้น',
'Motor':'เครื่องยนต์',
'Engine':'เครื่องยนต์',
'Machine':'เครื่องจักร',
'Sheet':'แผ่น',
'Object':'วัตถุ',
'Piece':'ชิ้น',
'Comb':'หวี',#โคม
'Root':'ราก',
'Through':'ผ่าน',#ธูรร
    #I see you through the window
'Powder':'แป้ง',
'Milk powder':'นมผง',
'Flag':'ธง',
'Chain':'โซ่',
'Novel':'นิยาย/นวนิยาย',
'Knife/Knives':'มีด',
"Thing":'สิ่ง, สิ่งของ',
'Refrig/Refrigerator':'ตู้เย็น', #รีฟริจ จะเรเทอะ
}
def call():
    for i in Things.keys():
        print(i,"\n")
# call()


def _search(name):
    name=name.lower()
    for k,v in Things.items():
       k=k.lower()
       if name in k or name in v: 
           print(k,"=",v)
    print("2_5_1")
           
# _search("Knife")
