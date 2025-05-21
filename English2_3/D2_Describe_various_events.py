#c s f k p ch sh th gh
#บรรยายเหตุการณ์ต่างๆ
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#We need actions not words
#They were swimming when the attack took place
#Life is full of battles
#The truth is that the battle begins when we are born
#The battle against time begins การต่อสู้กับเวลาได้เริ่มขึ้นแล้ว
Describe_various_events_3_2={
'Acction':'การกระทำ',#'Act':'กระทำ/ทำ',2_11
    #I do not like his acctions
'Attack':'การโจมตี',
'Ask':'ถาม',
    #I ask for water ฉันขอน้ำ #ขอบางสิ่ง
    #I ask my sister to set this table ฉันขอให้น้องสาวตั้งโต๊ะ #ขอให้ทำ
    #Mr. Park asked me to explain the meaning of the that word
'Adventage':'ประโยชน์/ข้อได้เปรียบ/ข้อดี',

'Battle':'การต่อสู้',
'Butter':'เนย',


'C':'',


'Death':'ความตาย/การตาย',#'Die':'ตาย'2_9
    #I do not think of death
'Delivery':'การจัดส่ง',#'Deliver':'ส่ง',
    #This delivery is for the boss
'Discussion':'การอภิปราย/การสนทนา',#'Conversation':'การสนทนา',



'Either':'ทั้ง',#อันไหนก็ได้อันหนึ่ง
    '''
    I can't either ฉันรอไม่ไหวแล้ว
    either way ทางใดทางหนึ่ง
    either one อันใดอันหนึ่ง
    I can't hear them either ฉันไม่ได้ยินพวกเขาเหมือนกัน/ฉันก็ไม่ได้ยินพวกเขา
    I don't know the answer either ฉันก็ไม่รู้คำตอบ
    Either option will work for me. (ตัวเลือกไหนก็ได้ ฉันโอเคทั้งนั้น)
    Either of the books is fine. (หนังสือเล่มไหนก็ได้)
    You can either come with us or stay at home. (คุณสามารถเลือกที่จะไปกับเราหรืออยู่บ้าน)
    Either John or Mary will attend the meeting. (จอห์นหรือแมรีจะเข้าร่วมประชุม)
    I don’t like coffee, and I don’t like tea either. (ฉันไม่ชอบกาแฟ และฉันก็ไม่ชอบชาด้วย)
    Either way, we’ll be there by noon. (ไม่ว่าทางไหนก็ตาม เราจะไปถึงตอนเที่ยง)
    There are trees on either side of the road. (มีต้นไม้ทั้งสองด้านของถนน)
    '''
'Expression':'การแสดงออก/สำนวน',


'F':'',


'G':'',


'H':'',


'I':'',


'J':'',

'K':'',


'L':'',


'M':'',


'Noise':'เสียงรบกวน',
    #Do not make noise
    #I cannot sleep because of the noise
    #The drums will be noisier than the piano. กลองจะเสียงดังกว่าเปียนโน (เสียงดังรบกวน)
'Noisy':'เสียงรบกวน',
    #This area is so Noisy

'Occasion':'โอกาศ',#'Opportunity':'โอกาศ' 2_11
    #Today is a special occasion


'P':'',


'R':'',


'Start':'เริ่ม/การเริ่มต้น',
    #From the start ตั้งแต่การเริ่มต้น
    #From the starting จากจุดเริ่มต้น


'Traffic':'การจราจร',


'U':'',


'V':'',

'W':'',
}
def call():
    for k,v in Describe_various_events_3_2.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Describe_various_events_3_2.items():
       if name in k:
           print(k,"=",v)
    print("D2")
        
# _search("")
           