#c s f k p ch sh th gh
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#it's cloudy and cool, but it's not rainy ท้องฟ้ามีเมฆครึ้มและอากาศเย็นสบาย แต่ฝนไม่ได้ตก
#I don't go to the office on rainy days
#Aren't you slower than me? ใช่ไหม
#ls it too late to join the meeting
#If your internet speed is slow, this file will take a long time to download
#How fast something is
#I'm going to a cafe. Would you like to come too/I'm too busy to go out right
#You use them to listen to music or to an online meeting
#Why aren't they joining us
#Why aren't you at the office
#After (having) hidden the cabbage, he ate dessert / After having stolen the spoons, she left the party
#At the end of the day, the sunset paints the evening sky pink and purple. it can be very beautiful
#Sunsets here are amazing Have you ever been to Barcelona / Never, but I'd love to go
#Isn't ใช่ไหม ใช้ isn't เพื่อแสดงคำถามที่มีน้ำเสียงคาดหวังหรือสมมติฐานว่าคำตอบควรจะเป็น "ใช่"
#"It's hot in Paris today! Isn't it sunny over there too?"(วันนี้ปารีสร้อนมาก! ที่นั่นก็แดดออกเหมือนกันใช่ไหม) 
    #แสดงถึงความคาดหวังหรือสมมติฐานว่าที่อีกที่หนึ่งก็น่าจะมีแดดออกเช่นกัน (เหมือนกับปารีส)
    #Is it sunny over there too? นี้คือเหตุผลที่ไม่ใช้
#It's a beautiful day, isn't it
#The sunsets here are beautiful at this time of year
#In the moring after a cold, rainy night, the roads are usually icy
#It's too cold outside, and the roads look icy / So, are you going to work from home today
#Aren't you having a meeting with ben today? Isn't that in the office
#We need to discuss a couple of questions
#First, you start. Then, you continue. Finally, you finish /First = Before anything else
#We have a lot of thing on the agenda. What do you want to start with
#I've worked for six different airlines
#I see that you're wearing a sweater, Maria. ls the weather getting cooler where you live? It's still hot here. Summer isn't over yet
#My hair looks awful this morning, so I've hidden it under a hat
#My laptop is too old to work without a charger
#I can hear my colleagues better ฉันสามารถได้ยินเพื่อนร่วมงานได้ดีขึ้น
#Sound is turned off
#Sorry about my outfit. I was just exercising at the gym, and I didn't have time to change
#The weather is getting cool here, so we've started wearing warm jackets
#When is the best season to visit
#I can't hear you guys
#It's just too dangerous to drive ใช้เพื่อแสดงความรู้สึกของผู้พูดที่ต้องการบอกว่า "มันอันตรายมากๆ จริงๆ"
#There are a couple of thing that I'd like to talk about
#Days are shorter in the fall, so yes, it's already sunset วันจะสั้นลงในฤดูใบไม้ร่วง ใช่แล้ว เป็นเวลาพระอาทิตย์ตกแล้ว

E6_Talk_in_online_meeting={
'Agenda':'กำหนดการ/วาระการประชุม',


'Below':'ด้านล่าง',
    #If i hide my legs below the camera nobody will know i'm wearing short

'Charger':'ที่ชาร์จ',
'Cabbage':'กะหลึ่า',
'Cloudy':'เมฆ',
    #It's cloudy and cool but it's not rainy
'Colleagues':'เพื่อนร่วมงาน',
'Curtains':'ผ้าม่าน',

'Drawer':'ลิ้นชัก',
    #in


'E':'',


'Figure':'ตัวเลข/รูป',
    #You have a good figure คุณมีรูปร่างที่ดี
    #In our meeting, we discussed the sales figures from last year


'G':'',


'Headphone':'หูฟัง',
'Hide/Hid/Hidden':'ซ่อน',
'Hopefully':'หวังว่า',#adverb
    #it everything goes well
    #Hopefully, they’ll understand our point of view.มุมมอง
'Heavily':'หนักงาน',


'Icy':'น้ำแช็ง',
    #The road are really icy

'J':'',

'K':'',


'Lazy':'บ้า',
    #My dog is lazier than me
'Loud':'เสียงดัง',
    #If there is a storm, you may hear some loud thunder

'M':'',


'N':'',


'Outfit':'ชุด',


'Printer':'เครื่องปริ้น',
    #We only sold a few printers

'Q':'',


'Rainy':'ฝนตก',
    #On rainy days,rain falls from clouds in the sky
    #It's a rainy day today.
    #rainy weather
    #During the rainy season
    #The fall here is very rainy
'Raincoat':'เสื้อกันฝน',
'Road':'ถนน',
    #Roads look icy

'Speed':'ความเร็ว',
'Steal/Stole/Stolen':'ขโมย',
'Snow':'หิมะ',
    #The roads were icy this morning because it snowed yesterday
'Storm':'พายุ',
    #a winter storm
'Sweater':'เสื้อกันหนาว',


'Thunder':'ฟ้าเสียง',


'U':'',


'V':'',

'Wet':'เปียก',
    #I don't want to get wet
    #it's all wet
'X':'',

'Y':'',

'Z':'',
}
def call():
    for k,v in E6_Talk_in_online_meeting.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in E6_Talk_in_online_meeting.items():
       if name in k:
           print(k,"=",v)
    print("E6")
        
# _search("")
           