from datetime import datetime
import time
name = input("Enter Customer Name : ")
# Get user input
# Check if the input contains only alphabets
if name.isalpha():
    print("Name accepted.")
else:
    print("Wrong input. You entered non-alphabetic characters.")
    time.sleep(0.5)
print("="*60)
time.sleep(0.6)
print("\t\t\t\t𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐓𝐚𝐝𝐢𝐩𝐚𝐭𝐫𝐢 𝐒𝐮𝐩𝐞𝐫𝐌𝐚𝐫𝐤𝐞𝐭")
print(" "*17,"-"*28)
time.sleep(0.7)
print("\t\t\tＴｏｄａｙ Ａｖａｉｌａｂｌｅ Ｇｒｏｃｅｒｉｅｓ ")
print("="*60)
lists = """
         Rice                  Rs . : 80/Kg
         Redgram Dal           Rs . : 120/Kg
         Wheat Flour           Rs . : 224/Kg
         Maggi                 Rs . : 50/Pack
         Corn Flour            Rs . : 30/Kg
         Milk                  Rs . : 40/Litre
         Rotis                 Rs . : 70/Pack
         Rasam Powder          Rs . : 200/Kg
         Sugar                 Rs . : 40/Kg
         Salt                  Rs . : 10/Kg
         Ice cream             Rs . : 500/Kg
         Onion                 Rs . : 80/Kg                 
         Sunflower Oil         Rs . : 140/Kg
         Colgate               Rs . : 40/Pack
         Lays Chips            Rs . : 10/Pack
         Bread                 Rs . : 140/Kg
         Coffee Powder         Rs . : 1000/Kg
         Tomatoes              Rs . : 120/Kg
          """
#Declare lists
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist=[]
qlist=[]
plist=[]
#items rates
items = {'rice':80,
         'redgram dal': 120,
         'wheat flour': 224,
        'maggi': 50,
        'corn flour': 30,
         'milk': 40,
         'rotis': 70,
         'rasam powder': 200,
         'sugar': 40,
         'salt' : 10,
         'ice cream': 500,
         'onion': 80,
         'sunflower oil': 140,
         'colgate' : 40,
         'lays' : 10,
         'bread' : 140,
         'coffee powder': 1000,
         'tomatoes': 120}
option = input("꧁٭𝙳𝚘 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚜𝚎𝚎 𝚊𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚒𝚝𝚎𝚖𝚜 (𝚜𝚊𝚢 𝚢𝚎𝚜)٭꧂:")
if option.lower() =="yes":
    print(lists)
for i in range(len(items)):
    print("︿" * 60)
    inp1 = int(input("۩ 𝐈𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐁𝐔𝐘 𝐩𝐫𝐞𝐬𝐬 𝟏 𝐨𝐫 𝐩𝐫𝐞𝐬𝐬 𝟐 𝐟𝐨𝐫 𝐄𝐗𝐈𝐓:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("𝙀𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙞𝙩𝙚𝙢𝙨 : ")
        quantity = int(input("𝐄𝐧𝐭𝐞𝐫 𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲 𝐢𝐧 (𝐊𝐠/ 𝐏𝐞𝐫𝐏𝐚𝐜𝐤): "))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice = totalprice+price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst =  (totalprice*5)/100
            finalamount = gst+totalprice
        else:
            time.sleep(0.8)
            print("𝙔𝙤𝙪𝙧 𝙚𝙣𝙩𝙚𝙧𝙚𝙙 𝙞𝙩𝙚𝙢/𝙞𝙩𝙚𝙢𝙨 𝙞𝙨 𝙣𝙤𝙩 𝙖𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 𝙉𝙤𝙬..𝘝𝘪𝘴𝘪𝘵 𝘛𝘰𝘮𝘮𝘰𝘳𝘳𝘰𝘸 𝘪𝘧 𝘮𝘢𝘺 𝘣𝘦 𝘈𝘷𝘢𝘪𝘭𝘢𝘣𝘭𝘦")
    else:
        print("You have Entered wrong Number")
    bill = input("𝑨𝒓𝒆 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒕𝒐 𝑩𝒊𝒍𝒍𝒊𝒏𝒈 𝒕𝒉𝒊𝒔 𝒊𝒕𝒆𝒎𝒔: [𝒔𝒂𝒚 𝒀𝒆𝒔 𝒐𝒓 𝑵𝒐]: ")
    if bill.lower()=="yes":
        pass
        if finalamount!=0:
            print("="*25,"𝐓𝐚𝐝𝐢𝐩𝐚𝐭𝐫𝐢 𝐒𝐮𝐩𝐞𝐫𝐌𝐚𝐫𝐤𝐞𝐭","="*25)
            # print("="*28,"Tadipatri","="*28)
            print("𝑵𝒂𝒎𝒆 :",name,""*30,""*10, "𝑫𝒂𝒕𝒆:",datetime.now() )
            print("-"*75)
            print("𝐒𝐧𝐨"," "*9,"𝐈𝐭𝐞𝐦𝐬"," "*9,"𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲"," "*4,"𝐏𝐫𝐢𝐜𝐞")
            for i in range(len(pricelist)):
                print(i,"",9*" ",ilist[i],7*" ",qlist[i]," "*5,plist[i])
            print("-"*75)
            print(" "*50,"𝗧𝗼𝘁𝗮𝗹 𝗔𝗺𝗼𝘂𝗻𝘁: ","Rs:",totalprice)
            print("𝐆𝐬𝐭 :"," "*50,"Rs. :",gst)
            print("-"*75)
            time.sleep(1)
            print(" "*50," 𝐅𝐢𝐧𝐚𝐥 𝐀𝐦𝐨𝐮𝐧𝐭:", "𝗥𝘀. :",finalamount)
print("-"*75)
time.sleep(0.8)
print(" "*10,"✿◉●• 𝑻𝒉𝒂𝒏𝒌 𝒀𝒐𝒖 𝑭𝒐𝒓 𝑽𝒊𝒔𝒊𝒕𝒊𝒏𝒈 𝑻𝒂𝒅𝒊𝒑𝒂𝒕𝒓𝒊 𝑺𝒖𝒑𝒆𝒓 𝑴𝒂𝒓𝒌𝒆𝒕 ✿◉●•◦")
print("-"*75)



