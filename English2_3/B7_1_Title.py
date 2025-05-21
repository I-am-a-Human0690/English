#วางแผนการเดินทาง, รู้จักคำนำหน้านาม
Title={
'Every':'ทุก',#แอปวี่ #อยู่หน้าอะไร อันไม่ต้องต้องเปลี่ยนรูป(เช่นไม่ต้องเติม s)
'Everybody':'ทุกคน',
    #Everybody is going to wait
    # Is everybody tired มีใครเหนื่อยไหม
'Everyone':'ทุกคน',#เป็นทางการกว่า ใช้ is เพราะนับเป็น เอกพจ
'Everything':'ทุกสิ่ง/ทุกอย่าง',
'Any':'ใดๆ/เลย',
'Anybody':'ใครก็ได้',#Is anybody with you มีใครอยู่กับคุณไหม
'Anything':'อะไรก็ได้',
'Nobody':'ไม่มีใคร/ไม่มีใครเลยสักคน',
'No one':'ไม่มีใคร/ไม่มีใครเลยสักคน',
'Something':'บางอย่าง/บางสิ่ง',
'Someone':'บางคน/ใครคนหนึ่ง',
'Notthing':'ไม่มีอะไร',
'ALL':'ทั้งหมด',
'Each':'แต่ละ',
'Those':'เหล่านั้น/พวกนั้น',#the ใช้ได้ทั้งเอกและพหุแต่จะใช้แค่สิ่งที่อยู่ใกล้ แต่ those ใช่กับพหุเท่านั้น ไกล
'These':'เหล่านี้',
'You all':'พวกคุณทุกคน',
'None':'ไม่มี/ไม่มีเลย',#None of them
'Both':'ทั้งสอง/ทั้งคู่',#Both of you
'Such':'ดังกล่าว',
'Other':'อื่นๆ',
'Know each other':'รู้จักกัน',
'Another':'อีกหนึ่ง/อีกครั้ง',
    #I won't wait for another minute
    #Another drink เครื่องดื่มอีกไหม
    #There is another thing to consider
'But':'แต่',
'No place':'ไม่มีที่ไหน',
'Terrible':'แย่มาก',#เทริบเบิล #เทเลอเบิล
'Argue':'โต้เถียง',
'Interesting':'น่าสนใจ',
'Yuck':'แหวะ',
'Complain':'บ่น',
'Side':'ด้านข้าง/ด้าน/ข้าง/ฝ่าย/สนับสนุน/เข้าข้าง',
'Other Side':'อีกด้าน',
'Faster':'เร็วขึ้น',
'Potatoes':'มันฝรั่ง',
}

def call():
    for k,v in Title.items():
        print(k)
# call()

def _search(name):
    name=name.lower()
    for k,v in Title.items():
       k=k.lower()
       if name in k or name in v: 
           print(k,"=",v)
    print("2_7_1")
           
# _search("Meter")