from re import I, T
import re
from traceback import print_tb


size = {"S":20,"M":40,"L":60}
taste = ["	รสชาติ","วนิลา","ช๊อคโกแลต","สตรอเบอรี่",
			"บลูเบอรี่","ชาเขียว","ชาไทย",
			"กะทิ","โอริโอ้","มะม่วง",
			"ช๊อคโกแลตชิพ","ทุเรียน","เผือก",
		 	"มิ้นช๊อคโกแลตชิพ","คาปูชิโน","เอสเปสโซ",
            "เรนโบ","มะนาว","โอวันติน"]
taste1 = [" Taste","Vanilla","Chocolate","Strawberry",
            "Blueberry","Green Tea","Thai Tea",
            "Coconut milk","Oreo","Mango",
            "Chocolate Chip","Durian","Taro",
            "Mint Chocolate Chip","Cappuccino","Espresso",
            "Rainbo","Lime","Ovantin"]
rec_taste = ["1.รสช็อคโกแลต","2.รสวนิลา","3.รสช็อคโกแลตชิพ"]
rec_taste1 = ["1.Chocolate","2.Vanilla","3.Chocolate Chip"]
topping_fivebaht = ["	Topping 5 Baht",
                    "เยลลี่แดง","คอนเฟรก","โอริโอ้",
				    "โกโก้ครั้น","เกล็ดเรนโบว์","วุ้นมะพร้าว",
				    "ข้างเหนียว","ไวช๊อคโกแลต","มินิคุกกี้",
				    "เยลลี่","ขนมปัง"]
topping_fivebaht1 = ["	Topping 5 Baht",
                    "Red Jelly","Cornflakes","Oreo",
                    "Koko Krunch","Rainbow Flakes","Coconut Jelly",
                    "Sticky Rice","White Chocolate","Mini Cookies",
                    "Jelly","Bread"]
topping_tenbaht = ["	Topping 10 Baht","แอลมอนด์","บราวนี่","เม็ดมะม่วงหิมพานต์","เอมแอนเอม"]
topping_tenbaht1 = ["	Topping 10 Baht","Almond","Brownie","Cashew Nut","m&m's"]
rec_top = ["1.โอริโอ้","2.เยลลี่แดง","3.บราวนี่"]
rec_top1 = ["1.Oreo","2.Red Jelly","3.Brownie"]
syrup = ["  ไซรัป","ช๊อคโกแลต","นมข้น","สตรอเบอรี่",
         "คาราเมล","น้ำผึ้ง","ชาเขียว"]
syrup1 = [" Syrup","Chocolate","Condensed Milk","Strawberry",
            "Caramel","Honey","Green Tea"]
rec_sauce = ["1.ช็อคโกแลต","2.นมข้น","3.คาราเมล"]
rec_sauce1 = ["1.Chocolate","2.Condensed milk","3.Caramel"]
od=[]

def changelang():
    while True:
        try:
            print("\n [Choose Your Language เลือกภาษาที่คุณต้องการ]")
            print("พิมพ์ 1 [Thai ภาษาไทย]")
            print("Type 2 [English ภาษาอังกฤษ]")
            lg = int(input("Language ภาษา(1/2):"))
            if lg==1:
                print("\n คุณเลือก ภาษาไทย")
                return lg
            elif lg==2:
                print("\n You Choose English")
                return lg
            else:
                print("--------------------------")
                print("คุณควรใช้เลข 1 ไม่ก็เลข 2 \nYou should use number 1 or number 2.")
                pass
        except ValueError:
            print("--------------------------")
            print("คุณควรใช้เลข 1 ไม่ก็เลข 2 \nYou should use number 1 or number 2.")


def name(lg):
    if lg == 1:
        name1= input("\nกรุณากรอกชื่อของคุณ: ")
        return name1
    elif lg == 2:
        name1= input("\nPlease input your name: ")
        return name1

def welcome(lg,name1):
    if lg == 1:
        print(f"\n ***ยินดีต้อนรับคุณ {name1} สู่ร้าน คัมมีไอศครีม***")
    elif lg == 2:
        print(f"\n ***Welcome {name1} to Kummee Ice Cream***")


def main_menu(lang):
    while True:
        try:
            if lang == 1 :
                print("\n [เมนูหลัก]")
                print("1.เมนูทั้งหมด")
                if od==[]:
                    print("2.เริ่มสั่งไอศครีม")
                elif od!=[]:
                    print("2.สั่งไอศครีมใหม่")
                print("3.เช็คคำสั่งซื้อของคุณ")
                print("0.ออกจากโปรแกรม")
            elif lang == 2:
                print("\n [Main Menu]")
                print("1.All menu")
                if od==[]:
                    print("2.Start ordering ice cream")
                elif od!=[]:
                    print("2.Order new ice cream")
                print("3.Check your order")
                print("0.Exit Program")
            if lang==1:
                work = int(input("เลือกเมนูทำงาน: "))
            elif lang ==2:
                work = int(input("Select work menu: "))
            if work == 0:
                farewell(lang)
                break
            elif work == 1:
                all_menu(lang)
            elif work == 2:
                start_order(lang)
            elif work == 3 :
                check_order()
            else :
                if lang == 1:
                    print("กรุณาเลือกเฉพาะเมนูทำงานที่มี")
                elif lang ==2:
                    print("Please select only the available menu items.")
                pass
        except ValueError:
            print("--------------------------")
            if lang == 1:
                print("กรุณาใช้แต่ตัวเลข")
            elif lang==2:
                print("Please use only numbers")
    

def all_menu(lang):
    if lang == 1:
            print("\n [เมนูทั้งหมด]")
            print("1.แนะนำ!!!")
            print("2.รสชาติทั้งหมด")
            print("3.ท็อปปิ้งทั้งหมด")
            print("4.ไซรัปทั้งหมด")
            print("9.ย้อนกลับ")
            print("--------------------------")
    elif lang == 2 :
            print("\n [All Menu]")
            print("1.Recommend!!!")
            print("2.Taste")
            print("3.Topping")
            print("4.Syrup")
            print("9.Back")
            print("--------------------------")
    while True:
        try:
            if lang == 1:
                am = int(input("เลือกเมนูทำงาน: "))
            elif lang == 2:
                am = int(input("Select work menu: "))
            if am == 1:
                recommend_ic(lang)
            elif am == 2:
                if lang == 1:
                    print('\n'.join(map(str,taste)))
                    print("\n [เมนูทำงาน]")
                    print("1.แนะนำ!!!")
                    print("3.ท็อปปิ้งทั้งหมด")
                    print("4.ไซรัปทั้งหมด")
                    print("9.กลับเมนูหลัก")
                    print("--------------------------")
                elif lang == 2:
                    print('\n'.join(map(str,taste1)))
                    print("\n [Work Menu]")
                    print("1.Recommend!!!")
                    print("3.Topping")
                    print("4.Syrup")
                    print("9.Main Menu")
                    print("--------------------------")
            elif am == 3:
                if lang == 1:
                    print('\n'.join(map(str,topping_fivebaht)))
                    print('\n'.join(map(str,topping_tenbaht)))
                    print("\n [เมนูทำงาน]")
                    print("1.แนะนำ!!!")
                    print("2.รสชาติทั้งหมด")
                    print("4.ไซรัปทั้งหมด")
                    print("9.กลับเมนูหลัก")
                    print("--------------------------")
                elif lang == 2:
                    print('\n'.join(map(str,topping_fivebaht1)))
                    print('\n'.join(map(str,topping_tenbaht1)))
                    print("\n [Work Menu]")
                    print("1.Recommend!!!")
                    print("2.Taste")
                    print("4.Syrup")
                    print("9.Main Menu")
                    print("--------------------------")
            elif am == 4:
                if lang == 1:
                    print('\n'.join(map(str,syrup)))
                    print("\n [เมนูทำงาน]")
                    print("1.แนะนำ!!!")
                    print("2.รสชาติทั้งหมด")
                    print("3.ท็อปปิ้งทั้งหมด")
                    print("9.กลับเมนูหลัก")
                    print("--------------------------")
                elif lang == 2:
                    print('\n'.join(map(str,syrup1)))
                    print("\n [Work Menu]")
                    print("1.Recommend!!!")
                    print("2.Taste")
                    print("3.Topping")
                    print("9.Main Menu")
                    print("--------------------------")
            elif am == 9:
                main_menu(lang)
            else:
                if lang ==1:
                    print("--------------------------")
                    print("คุณควรใช้เลขที่มีอยู่ในเมนู")
                elif lang ==2:
                    print("--------------------------")
                    print("You should use the numbers available in the menu.")
                pass
        except ValueError:
            print("--------------------------")
            if lang == 1:
                print("กรุณาใช้แต่ตัวเลข")
            elif lang==2:
                print("Please use only numbers")

def recommend_ic(lang):
    if lang==1:
        print("\n [รสชาติแนะนำ]")
        print('\n'.join(map(str,rec_taste)))
        print(" [ท็อปปิ้งแนะนำ]")
        print('\n'.join(map(str,rec_top)))
        print(" [ไซรัปแนะนำ]")
        print('\n'.join(map(str,rec_sauce)))
        print("\n [เมนูทำงาน]")
        print("2.เริ่มสั่งไอศครีม")
        print("9.ย้อนกลับ")
        print("-------------------------- ")
    elif lang==2:
        print("\n [Recommend Taste]")
        print('\n'.join(map(str,rec_taste1)))
        print("\n [Recommend Topping]")
        print('\n'.join(map(str,rec_top1)))
        print("\n [Recommend Syrup]")
        print('\n'.join(map(str,rec_sauce1)))
        print("\n [Work Menu]")
        print("2.Start ordering ice cream")
        print("9.Back")
        print("-------------------------- ")
    while True:
        try:
            if lang == 1:
                rc = int(input("เลือกเมนูทำงาน: "))
            elif lang == 2:
                rc = int(input("Select work menu: "))
            if rc == 2:
                start_order()
            elif rc == 9:
                all_menu(lang)
            else:
                if lang ==1:
                    print("--------------------------")
                    print("คุณควรใช้เลขที่มีอยู่ในเมนู")
                elif lang ==2:
                    print("--------------------------")
                    print("You should use the numbers available in the menu.")
                pass
        except ValueError:
            print("--------------------------")
            if lang == 1:
                print("กรุณาใช้แต่ตัวเลข")
            elif lang==2:
                print("Please use only numbers")
    

def start_order(lang):
    global cs,odp,ct,ctp,sum_tp,csr
    cs,odp =choose_size(lang)
    od.append(cs)
    ct=choose_taste(lang,cs)
    ctp,sum_tp =choose_topping(lang)
    csr=choose_syrup(lang)
    return cs,odp,ct,ctp,sum_tp,csr

def choose_size(lang):
    cs=[]
    odp=0
    while True:
        for key in size:
            if lang == 1:
                print("ขนาด ",key," ราคา ",size[key]," บาท")
            elif lang ==2:
                print("Size ",key," Price ",size[key]," Baht")
        if lang == 1:
            cs = input("เลือกขนาดของถ้วยไอศครีมที่คุณต้องการ: ")
            print("-------------------------- ")
        elif lang ==2:
            cs = input("Choose your Ice Cream size: ")
            print("-------------------------- ")
        if cs.upper() in size.keys():
            odp = size.get(cs.upper())
            return cs,odp
        else:
            if lang == 1:
                print("ไม่มีขนาดที่ท่านต้องการ กรุณาเลือกใหม่")
            elif lang == 2:
                print("Don't have the size you want.Please select a new one")
            pass

def choose_taste(lang,cs):
    ct=[]
    a=1
    while True:
        if lang == 1:
            if cs in ['s','S']:
                print("\nท่านสามารถเลือกรสชาติได้ 1 รสชาติ")
                i = 1
            elif cs in ['m','M']:
                print("\nท่านสามารถเลือกรสชาติได้ 2 รสชาติ")
                i = 2
            elif cs in ['l','L']:
                print("\nท่านสามารถเลือกรสชาติได้ 3 รสชาติ")
                i = 3
        elif lang == 2:
            if cs in ['s','S']:
                print("You can choose 1 flavor.")
                i = 1
            elif cs in ['m','M']:
                print("You can choose 2 flavor.")
                i = 2
            elif cs in ['l','L']:
                print("You can choose 3 flavor.")
                i = 3
        while a!=i+1:
            if lang == 1:
                print('\n'.join(map(str,taste)))
                print("\n [รสชาติแนะนำ]")
                print('\n'.join(map(str,rec_taste)))
                print("--------------------------")
                ict = input("เลือกรสชาติไอศครีมที่ท่านต้องการทานรสที่ "+str(a)+" : ")
            elif lang == 2:
                print('\n'.join(map(str,taste1)))
                print("\n [Recommend Taste]")
                print('\n'.join(map(str,rec_taste1)))
                print("--------------------------")
                ict = input("Flavor "+str(a)+" : ")
            if ict in taste:
                ct.append(ict)
                a+=1
            elif ict in taste1:
                ct.append(ict)
                a+=1
            else:
                if lang == 1:
                    print("--------------------------")
                    print("ไม่มีรสชาติที่ท่านต้องการ กรุณาเลือกใหม่")
                elif lang == 2:
                    print("--------------------------")
                    print("There is no flavor you want. Please select a new one")
                pass
        if lang==1:
            print("\n รสชาติไอศครีมของท่านคือ",ct)
            print("--------------------------")
        elif lang == 2:
            print("\n Your ice cream flavor is",ct)
            print("--------------------------")
        return ct
        
def choose_topping(lang):
    if lang ==1:
        print("ฟรีท็อปปิ้ง 10 บาท หลังจากนั้นคิดเงิน")
    elif lang == 2:
        print("Free topping 10 baht, after that charge")
    ictp =''
    ctp=[]
    sum_tp=0
    while ictp not in ['stop','พอ']:
        if lang == 1:
            print('\n'.join(map(str,topping_fivebaht)))
            print('\n'.join(map(str,topping_tenbaht)))
            print(" [ท็อปปิ้งแนะนำ]")
            print('\n'.join(map(str,rec_top)))
            print("พิมพ์ (พอ) เมื่อไม่ต้องการท็อปปิ้งเพิ่มแล้ว")
            print("--------------------------")
            ictp = input("เลือกท็อปปิ้ง:")
        elif lang == 2:
            print('\n'.join(map(str,topping_fivebaht1)))
            print('\n'.join(map(str,topping_tenbaht1)))
            print("\n [Recommend Topping]")
            print('\n'.join(map(str,rec_top1)))
            print("Type (stop) when no more toppings are needed.")
            print("--------------------------")
            ictp = input("Choose topping:")
        if ictp in topping_fivebaht:
            ctp.append(ictp)
            sum_tp=sum_tp+5
        elif ictp in topping_fivebaht1:
            ctp.append(ictp)
            sum_tp=sum_tp+5
        elif ictp in topping_tenbaht:
            ctp.append(ictp)
            sum_tp=sum_tp+10
        elif ictp in topping_tenbaht1:
            ctp.append(ictp)
            sum_tp=sum_tp+10
        else:
            if ictp not in ['stop','พอ']:
                if lang == 1:
                    print("ไม่มีท็อปปิ้งที่ท่านเลือก กรุณาเลือกใหม่")
                elif lang ==2:
                    print("There is no topping you selected, please select again.")
        if lang == 1:
            print("ท็อปปิ้งของคุณมี",ctp)
        elif lang ==2:
            print("Your topping is",ctp)
    return ctp,sum_tp
            

def choose_syrup(lang):
    csr=[]
    while True:
        if lang == 1:
            print('\n'.join(map(str,syrup)))
            print(" [ไซรัปแนะนำ]")
            print('\n'.join(map(str,rec_sauce)))
            print("พิมพ์ (ไม่) เพื่อไม่เอาไซรัป")
            print("--------------------------")
            icsr = input("กรุณาเลือกไซรัปที่ท่านต้องการ:")
        elif lang == 2:
            print('\n'.join(map(str,syrup1)))
            print("\n [Recommend Syrup]")
            print('\n'.join(map(str,rec_sauce1)))
            print("Type (no) for no syrup")
            print("--------------------------")
            icsr = input("Please select the syrup you want:")
        if icsr in syrup:
            csr.append(icsr)
        elif icsr in syrup1:
            csr.append(icsr)
        elif icsr in['no','ไม่']:
            csr=[]
        else:
            if lang == 1:
                print("ไม่มีไซรัปที่ท่านต้องการ กรุณาเลือกใหม่")
            elif lang ==2:
                print("There is no syrup you need. Please select a new one")
            pass
        return csr

def check_order():
    while True:
        if od==[]:
            if lang == 1:
                print("\nคุณยังไม่ได้สั่งไอศครีม")
                print("-------------------------- ")
                main_menu(lang)
            elif lang == 2:
                print("\nYou haven't ordered ice cream.") 
                print("-------------------------- ")
                main_menu(lang)
        else:
            if lang == 1:
                print("[ออร์เดอร์ของท่าน]")
                print("ขนาดไอศครีม:",cs," ",odp," บาท")
                print("รสชาติ:",ct)
                print("ท็อปปิ้ง:",ctp," ",sum_tp," บาท")
                print("ไซรัป:",csr)
                if ctp!=[]:
                    sum=odp+sum_tp-10
                    print("ราคาทั้งหมด:",sum)
                else:
                    sum=odp+sum_tp
                    print("ราคาทั้งหมด:",sum)
            elif lang == 2:
                print("[Your order]")
                print("Ice cream size: ",cs," ",odp," Baht")
                print("Taste: ",ct)
                print("Topping: ",ctp,"Total topping price: ",sum_tp," Baht")
                print("Syrup: ",csr)
                if ctp!=[]:
                    if ctp in topping_tenbaht:
                        sum=odp+sum_tp-10
                    elif ctp in topping_tenbaht1:
                        sum=odp+sum_tp-10
                    else:
                        sum=odp+sum_tp-5
                    print("Total Price: ",sum," Baht")
                else:
                    sum=odp+sum_tp
                    print("Total Price: ",sum," Baht")
        break

def farewell(lang):
    while True:
        if lang == 1:
            print("ขอบคุณที่ใช้บริการ")
        elif lang == 2:
            print("Thank you for using the service.")
        break
#main program
lang=changelang()
name1=name(lang)
welcome(lang,name1)
main_menu(lang)