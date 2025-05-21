#c s f k p ch sh th gh
#คุยเฟื่องเรื่องกีฬา 30
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#tennis racket Ping pong racket
Sport_2_19={
'Athlete':'นักกีฬา/นักกรีฑา',


'Ball':'ลูกบอล',
'Basketball':'บาสเก็ตบอล',


'Coach':'ผู้ฝึก',



'Goal':'เป้าหมาย/ประตู(บอล)',
'Game':'เกม',
'Gym':'ยิม',


'Jump':'กระโดด',

'Kick':'เตะ',


'Marathon':'มาราธอน',


'Player':'ผู้เล่น',
'Path':'เส้นทาง/ทาง',
'Point':'คะแนน/จุด',


'Sport':'กีฬา',
'Step':'ขั้นตอน/ระดับ',
'Score':'คะแนน/ทำคะแนน',#i scored four point


'Team':'ทีม',


'Volleyball':'บอลเลย์บอล',

'Work out':'ออกกำลังกาย',
}
def call():
    for k,v in Sport_2_19.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Sport_2_19.items():
       if name in k:
           print(k,"=",v)
    print("2_19")
        
# _search("")
           