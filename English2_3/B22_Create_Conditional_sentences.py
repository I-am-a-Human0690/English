#c s f k p ch sh th gh
#สร้างประโยคเงื่อนไข
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

#Do you have light คุณมีไฟไหม
#we used to exercise (used to = เคย(ทำบ่อย ๆ))
#What if i fail
#i will be sad if you fail
#i did not want to tell him ฉันไม่ได้อยากบอกเค้า(บอกไปแล้วแต่ที่จริงไม่ได้อยากบอก)
#i do not want to tell him ฉันไม่อยากบอกเค้า(ยังไม่ได้บอก)
Create_Conditional_sentences_2_22={
'Fly':' บิน',
'Fail':'ล้มเหลว',#'Failure':'ความล้มเหลว' 2_14---

}
def call():
    for k,v in Create_Conditional_sentences_2_22.items():
        print(k)
# call()

def _search(name):
    name=name.capitalize()
    for k,v in Create_Conditional_sentences_2_22.items():
       if name in k:
           print(k,"=",v)
    print("2_22")
        
# _search("")
           