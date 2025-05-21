#c s f k p ch sh th gh
#บ่งบอกคุณลักษณะ
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#May the force be with you
#Quality is more important than quantity
#This problem is of great importance
#This problem is very important ใช้ในภาษาที่เป็นกันเอง
#This method offers two advantages
#What is the advantage of this techology
#This meat is of bad quality ดูเป็นทางการเกินไป
    #This meat is poor quality.
    #This meat is not good quality.
    #This meat is bad.
#You give too much importance to what he says
#His personality is great / He has a great personality
#The quality of this wine is good / This wine is of good quality
#I wish everyone good luck

Indicates_3_3={
'Air Force':'กองทัพอากาศ',


'Beautiful':'สวย',
'Beauty':'ความสวย',
    #Beauty is not everything
    #Her new bicycle is a beauty รถคันใหม่ของเธอสวย/รถคันใหม่ของเธอมีความสวย


'C':'',


'Difference':'ความแตกต่าง',
    #There is a difference
    #Can you see the difference
'Different':'แตกต่าง',
    #My friends come from different cultures
    #This book is different from that one. (หนังสือเล่มนี้แตกต่างจากเล่มนั้น)
    #My car is different to yours. (รถของฉันต่างจากรถของคุณ)
    #The weather today is different than yesterday. (อากาศวันนี้ต่างจากเมื่อวาน)


'E':'',


'Force':'บังคับ/กำลัง/แรง',


'G':'',


'H':'',


'Identity':'ตัวตน',
'Identity card':'ประชาชน',
'Importance':'ความสำคัญ',
    #It has a lot of importance     
'Important':'สำคัญ',
    #It is very importan

'J':'',

'K':'',


'Luck':'โชค',


'M':'',


'N':'',


'O':'',


'Power':'พลัง/อำนาจ',
    #This man has more power ผู้ชายคนนี้มีอำนาจมากกว่า
'Personality':'บุคลิก', #'Personal':'ส่วนตัว', 2_10

'Quality':'คุณภาพ',
    #Is the quality good
'Quantity':'ปริมาณ',

'R':'',


'Start':'เริ่มต้น',


'T':'',


'U':'',


'V':'',

'W':'',
}
def call():
    for k,v in Indicates_3_3.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Indicates_3_3.items():
       if name in k:
           print(k,"=",v)
    print("D3")
        
# _search("")
           