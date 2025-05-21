#c s f k p ch sh th gh
#บอกเรื่องสมมุติในอดีต 26
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#Would have
#She would have been a teacher
#We would have had children
#We would have written the piece lastyear
#We would have had to live with my sister พวกเราคงตะได้ใช่ชีวิตกับน้องสาวของฉัน
#I would not have come to this school ฉันคงจะได้มาโรงเรียนนี้แล้ว
#They would have had to go there
#I'm too embarrased
#Though she loves him ถึงแม้ว่าเธอรักเขา
#pass me the sugar please
#This is the watch that i had lost
#more wowen that previously ผู้หญิงเยอะกว่าเมื่อก่อน
#Five years have passed since that day
'''
https://www.trueplookpanya.com/dhamma/content/88286/-laneng-lan-
Modal verb คือกริยาช่วยรูปหนึ่งที่มีความหมายในตัวมันเองด้วย โดยปกติกริยาช่วยจะมีหน้าที่ทำให้ประโยคสมบูรณ์เท่านั้นไม่ได้มีความหมายในตัว Modal verb มีดังนี้ Can/Could = สามารถ, Will/Would = จะ, Shall/Should = ควรจะ, May/Might = อาจจะ, Must = ต้อง, Ought to = ควรจะ โดยครั้งนี้จะเน้นวิธีการใช้ Modal verb ในรูปอดีตว่ามีการใช้และความหมายอย่างไร

Modal + Verb + participle (verb ช่อง3)
Would have = Past unreal action หรือการกระทำในอดีตที่ไม่ได้เกิดขึ้นจริง เช่น ถ้าสิ่งนั้นเกิดขึ้น เราจะทำอย่างนั้น (แต่จริง ๆ แล้วไม่ได้เกิดขึ้น) เช่น

If I knew we have nothing left to eat, I would have brought some foods. 
(ถ้าฉันรู้ว่าเราไม่มีอะไรเหลือเลย ฉันก็จะซื้ออะไรเข้ามากินละ)

If I knew his decision, I would have known what to do. 
(ถ้าฉันรู้ว่าเขาจะตัดสินใจอย่างไร ฉันก็คงจะรู้ละว่า ต้องทำอย่างไรต่อไป) **แต่นี่คือฉันไม่รู้

ข้อควรจำ : Would have มักจะใช้ร่วมกันกับประโยคก่อนหน้าที่เป็นการใช้ verb ช่อง 2 เสมอ


Could have = Past unreal ability หรือความสามารถหรือการกระทำอะไรบางอย่างในอดีตที่ไม่ได้เกิดขึ้นจริง เช่น
They could have attended the conference. 
(จริง ๆ แล้วพวกเขาเข้าร่วมประชุมได้) **แต่ในความเป็นจริงพวกเขาไม่ได้เข้าร่วม

I could have taken the flight. 
(ฉันควรจะนั่งเครื่องบินไปแล้ว) **แต่จริง ๆ ฉันไม่ได้นั่ง เพราะอาจจะตกเครื่อง ไปไม่ทันเครื่องออก


May have = Past unreal possibility หรือความเป็นไปได้ในอดีตที่ไม่ได้เกิดขึ้นจริง เช่น
She may has passed the exam if she studied harder. 
(เธอน่าจะสอบผ่านถ้าเธอตั้งใจเรียนกว่านี้) **แต่จริง ๆ แล้วเธอสอบไม่ผ่าน เพราะไม่ได้ตั้งใจเรียน

We may have missed the bus. Luckily, we spare enough time getting here. 
(นี่พวกเราอาจจะตกรถแล้วนะเนี่ย ยังโชคดีที่เผื่อเวลาเอาไว้พอ) **ถ้าเผื่อเวลาไม่พอ ต้องตกรถแน่ๆ


should have = Past unreal recommendation หรือข้อแนะนำจากอีกฝ่ายในอดีตที่ไม่ได้เกิดขึ้นจริง เช่น
You should have listened better. 
(เธอน่าจะฟังให้ดีกว่านี้) **แต่จริง ๆ แล้วเธอสอบฟังมาไม่ดี ก็เลยอาจจะจับใจความมาผิด ๆ

You should have brought them; they are so cheap! 
(เธอน่าจะซื้อมันมานะ มันถูกมาก) **แต่น่าเสียดายเธอไม่ได้ซื้อมา


Must have = Past unreal assumption หรือข้อสันนิษฐานในอดีตที่ไม่ได้เกิดขึ้นจริง เช่น
They must have been crazy!  
(พวกเขาต้องบ้าไปแล้วแน่ ๆ!) **เป็นการเปรียบเทียบจากการกระทำที่เห็น แต่พวกเขาอาจจะไม่ได้บ้าจริง ๆ)
'''
B15_Tell_a_hypothetical_story_from_the_past={
'A':'',


'B':'',


'C':'',


'D':'',


'E':'',


'F':'',


'G':'',


'H':'',


'I':'',


'J':'',

'K':'',


'L':'',


'M':'',


'N':'',


'O':'',


'P':'',


'R':'',


'S':'',


'T':'',


'U':'',


'V':'',

'W':'',
}
def call():
    for k,v in B15_Tell_a_hypothetical_story_from_the_past.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in B15_Tell_a_hypothetical_story_from_the_past.items():
       if name in k:
           print(k,"=",v)
    print("B15")
        
# _search("")
           