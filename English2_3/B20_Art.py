#c s f k p ch sh th gh
#ชื่อชมงานศิลปะ 31
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Art2_20={
'Art':'ศิลปะ',
'Audience':'ผู้ฝัง/ผู้ชม',
'Actress':'นักแสดงหญิง',


'Band':'วงดนตรี',


'Camera':'กล้องถ่ายรูป',
'Concert':'การแสดงดนตรี',
'Contest':'การประกวด/การแข่งขัน(ประกวด)',


'Dance':'การเต้นรำ',




'Flute':'ขุ่ย',
'Film':'หนัง',
'Fashion':'ความนิยม/แฟชั่น',



'Instrument':'เครื่องดนตรี/อุปกรณ์',


'Literature':'วรรณกรรม/วรรณคดี',


'Movie':'ภาพยนตร์',
'Music':'ดนตรี/เพลง',
'Musical':'ดนตรี/เพลง',#adjective musical talent




'Photo':'ภาพถ่าย',
'Picture':'รูปภาพ',
'Photography':'การถ่ายภาพ',
'Poetry':'บทกวี',#โพเออทรี
'Paint':'สี/ทาสี/ระบายสี/วาดภาพ',
'Painting':'จิตกรรม/ภาพวาดจิตกรรม/ภาพศิลปะ/การทาสี',

'Song':'เพลง',
'Style':'รูปแบบ/สไตล์',
'Sound':'เสียง',
    #No but it doesn't sound like my kind of thing
    #That sounds good

'Theater':'โรงละคร',

'Violin':'ไวโลลิน',
}
def call():
    for k,v in Art2_20.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Art2_20.items():
       if name in k:
           print(k,"=",v)
    print("2_20")
        
# _search("")
           