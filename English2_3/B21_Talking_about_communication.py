#พูดถึงการสื่อสาร 32
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Talking_about_communication_21={
'Access':'เข้า/เข้าถึง/ทางเข้า/สิทธ์เข้าถึง',#i have access to his library



'Channel':'ช่อง',#She works for Channel Five
'Comment':'ความคิดเห็น',
'Communication':'การสื่อสาร',




'Information':'ข้อมูล',
'Internet':'อินเตอร์เน็ต',


'Journalist':'นักข่าว',



'Language':'ภาษา',


'Message':'ข้อความ',#This message is for both of you


'Network':'เครือข่าย',
'News':'ข่าว',



'Press':'กด/บรรดาหนังสือพิมพ์/สื่อ', #Press here กดที่นี้ #Press once กดครั้งเดียว
'Postcard':'โปสการ์ด/ไปรษณียบัตร',
'Post':'โพสต์',


'Story':'เรื่องราว',
'Search':'การค้นหา',# I am in search of a new house
'Stamp':'ตรา/แสตมป์',
'Search engine':'โปรแกรมค้นหา',


'Text':'ข้อความ',
}
def call():
    for k,v in Talking_about_communication_21.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Talking_about_communication_21.items():
       if name in k:
           print(k,"=",v)
    print("2_21")
        
# _search("")
           