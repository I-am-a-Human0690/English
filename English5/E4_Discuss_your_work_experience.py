#c s f k p ch sh th gh
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#"What's something you're good at?" (มีอะไรที่คุณทำได้ดีบ้าง?)
#"I'm good at playing the piano."(ฉันเก่งในการเล่นเปียโน)
#Sorry, I can't meet you tonight because i didn't finish my resume
#(I've always)มาโดยตลอด been interested in physics
#it could be one or more jobs
#How long have you worked as a guide
#American bosses give workers pay and benefits like vacation time and lower prices (at the doctor's / on health's benefit)
#หัวหน้างานชาวอเมริกันให้ค่าจ้างและสวัสดิการแก่พนักงาน เช่น วันลาพักร้อนและราคาที่ถูกลงเมื่อไปพบแพทย์
#The pay is too low, so I'm not going to accep this job
#Benefits include over ten days of vacation
#An airline is a company that flies airplanes and sells plane tickets สายการบินคือบริษัทที่ให้บริการบินด้วยเครื่องบินและขายตั๋วเครื่องบิน
#My kind of thing ประเภทของฉัน/แนวของฉัน
#When the boss is away, please ask customers to call again later
#To make a decision is to decide
#If you are happy with the pay, hours, and boss, then you should accept the job ถ้าคุณพอใจกับค่าจ้าง ชั่วโมงทำงาน และหัวหน้า คุณก็ควรรับงานนี้
#How long have you worked as a singer / Actually, I've just begun giving concerts
#Were you a reponsible student/ I was I always did my homework and was never late
#It's a full-time job, so forty hours a week.
#  it doesn't have to be Monday (through ผ่าน) Friday, 9 to 5. You can work at other times if you want
#I've had my part-time job for five months. I've worked as a chef since I moved to Italy
#i don't have strong feelings about the job ฉันไม่ได้รู้สึกอะไรมากนักเกี่ยวกับงานนี้ / ฉันรู้สึกเฉยๆ กับงานนี้
#Your resume looks great, Ben! It isn't too long or too short, and you 
# (have ถ้าไม่มีจะไม่แสดงถึงการเชื่อมโยงถึงปัจจุบัน) described your work history and job skills well
#You have done a great job on your resume.They're going to love you
#To answer your question เพื่อตอบคำถามของคุณ
#I've always understood math. It was my favorite subject in school
#I was a taxi driver, but then I changed careers ฉันเคยเป็นคนขับแท็กซี่ แต่หลังจากนั้นฉันก็เปลี่ยนอาชีพ
#I've begun learning Spanish too
#i worked as a part-time singer from 2016 to 2018 and I've been a chef since 2020
#(I'd:would) love to work here at the city museum #I would like อยาก I would love อยากมาก ๆ
#I'm interested in a music career ทำไหมต้องเติม a "career" เป็นคำนามนับได้
#I get great benefits from my job, so my doctor's visits are cheap
#It sounds like you were really into him ฟังดูเหมือนคุณชอบเขามากจริง ๆ
#In the past ten years, I have quit ten ในช่วงสิบปีที่ผ่านมา
#I've wanted to work for your airline since I became a pilot
#He's(He has) been happy since he contacted her
#Can you please give us your email
#Has our boss contacted you yet
#I can't decide I've never understood how other people make decisions so quickly 80
#"Lisa is maybe going to work for them" "ลิซ่าอาจจะไปทำงานให้พวกเขา"
#"To get a job" เพื่อให้ได้งาน 
#I've decided to quit as well   as well คล้ายกับคำว่า "too" หรือ "also"
#I added more information to my resume yesterday
#What time does he leave for the office
#I have only gone to one school, so the education part of my resume is short
    #"I attended only one school, so the education section of my resume is brief."
#Your company sounds like a fun place to work! I've heard good things
#No but it doesn't sound like my kind of thing
#I am not being so nervous since i took my exams  ฉันไม่ค่อยรู้สึกประหม่าเลยตั้งแต่ฉันสอบเสร็จ ไม่ปกติ
    #"I haven't been so nervous since I took my exams." 
#"I don't know if I want the job" "ฉันไม่รู้ว่าฉันอยากได้งานนี้หรือเปล่า" or I am sure that I want the job
#I've understood English most of my life "ฉันเข้าใจภาษาอังกฤษเกือบตลอดชีวิตของฉัน"
E4_Discuss_your_work_experience={
'A':'',


'Biology':'ชีววิทยา',


'Careful':'ระมัดระวัง',
'Career':'อาชีพ',
'Congratulations':'ยินดีด้วย',


'D':'',


'E':'',


'Friendly':'เป็นกันเอง',
    #We're looking for friendly receptionist


'Graduate':'ได้รับใบปริญญา/เรียนจบ',#กริยา
'Graudation':'การสำเร็จการศึกษา',


'H':'',


'I':'',


'J':'',

'K':'',


'L':'',


'Mess':'ความยุ่งเหยิง',
'Manager':'ผู้จัดการการ',


'N':'',


'O':'',


'Pilot':'นักบิน',

'Quit':'ล้มเลิก/ลาออก',#I quit my job ฉันออกจากงานของฉัน0


'Resume':'เรซุเม',
'Receptionist':'พนักงานต้อนรับ',


'Skill':'สกิล',


'Timely':'ทันเวลา',


'Useful':'มีประโยชน์',
    #her skills will be very useful in our workplace

'Unfortunately':'น่าเสียดาย/โชคไม่มี',
    #Unfortunately, the boss is away till next week

'V':'',

'W':'',

'X':'',

'Y':'',

'Z':'',
}
def call():
    for k,v in E4_Discuss_your_work_experience.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in E4_Discuss_your_work_experience.items():
       if name in k:
           print(k,"=",v)
    print("E4")
        
# _search("")
           