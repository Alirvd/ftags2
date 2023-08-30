from tinydb import TinyDB,Query
from telebot.types import InlineKeyboardButton as btn
from telebot.types import InlineKeyboardMarkup as mak

import random,requests
conn=TinyDB("databaseor.json")
Query=Query()
from telebot import *
bot=TeleBot(input("Token : "))

def login(message):
	id=message.chat.id
	msg="""
	<strong>
حسنا ارسل الرقم الخاص بك
	</strong>"""
	mas=mak()
	open(f"filer{id}.txt","w").write("addnum")
	mas.add(btn(text="رجوع",callback_data="back"))
	gy=bot.edit_message_text(chat_id=id,text=msg,message_id=message.message_id,parse_mode="html",reply_markup=mas)
	bot.register_next_step_handler(gy,yg)
def yg(message):
	global num,ran,pid
	id=message.chat.id
	if open(f"filer{id}.txt").read()!="addnum" or open(f"filer{id}.txt").read()=="back":
		return "bacm"
	else:True
	open(f"filer{id}.txt","w").write("addcode")
	num=message.text
	ran=''.join(random.choice("qazxcndoeprohfncowuntgoyhebkfoch")for i in range(9))
	url="https://odpapp.asiacell.com/api/v1/login?lang=en"
	cook=""
	head={
"Authorization": "Bearer "+cook,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": f"fcb42a5d-ce8e-4467-b6c9-{ran}",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
	json={
"captchaCode": "",
"username": num
}
	req=requests.post(url,headers=head,json=json).text

	if '"success":true' in req:
		pid=req.split("PID=")[1].split('"')[0]
		mas=mak()
		mas.add(btn(text="رجوع",callback_data="back"))
		yy=bot.send_message(id,"<strong>حسنا ارسل الكود الذي تم ارساله الى رقمك</strong>",parse_mode="html",reply_markup=mas)
		bot.register_next_step_handler(yy,hy)
	else:
		mas=mak()
		mas.add(btn(text="رجوع",callback_data="back"))
		
		ggl=bot.send_message(id,"<strong>الرقم غير صحيح </strong>",parse_mode="html",reply_markup=mas)
		
def hy(message):
	cook=""
	id=message.chat.id
	if open(f"filer{id}.txt").read()!="addcode" or open(f"filer{id}.txt").read()=="back":
		return "vack"
	else:True
	
	head={
"Authorization": "Bearer "+cook,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": f"fcb42a5d-ce8e-4467-b6c9-{ran}",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
	code=message.text
	id=message.chat.id

	data1={
		"passcode": code,
		"PID":pid
		}
	req1=requests.post("https://odpapp.asiacell.com/api/v1/smsvalidation?lang=en",json=data1,headers=head)
	if 'access_token' in req1.text:
		access=req1.json()["access_token"]
		conn.update({"access": access},Query.id==id)
		bot.send_message(id,"<strong>تم تسجيل الدخول بنجاح الان ارسل /start</strong>",parse_mode="html")
	else:
		mas=mak()
		mas.add(btn(text="رجوع",callback_data="back"))
		bot.send_message(id,"<strong>الكود غير صحيح</strong>",parse_mode="html",reply_markup=mas)	

@bot.message_handler(commands=["start"])
def bop(message):
	text=message.text
	id=message.chat.id
	name=message.chat.first_name
	try:
			data=conn.search(Query.id==id)[0]
			access=data["access"]
	except:
			conn.insert({"id": id,"access": "no"})
			data=conn.search(Query.id==id)[0]
			access=data["access"]
	if access=="no":
				mas=mak()
				a1=btn(text="تسجيل الدخول",callback_data="login")
				mas.add(a1)
				bot.send_message(id,"<strong>هل تريد تسجيل الدخول</strong>",parse_mode="html",reply_markup=mas)
				
	else:
				head1={
"Authorization": "Bearer "+access,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": "fcb42a5d-ce8e-4467-b6c9-3c117f10e6",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
				
				req2=requests.get("https://odpapp.asiacell.com/api/v1/profile?lang=en",headers=head1).text
				if '"message":"Success"' in req2:
					numb=req2.split('"phoneNumber":"')[1].split('"')[0]
					amou=req2.split('"title":"YOUR PREPAID BALANCE","items":[{"value":')[1].split(',"')[0]
					msg=f"""
<strong>
اهلا بك عزيزي

رقمك : {numb}
رصيدك : {amou}

اختر احد الازرار تحت
</strong>
"""
					
					mas=mak()
					a1=btn(text="تعبئة كارت💳",callback_data="addcart")
					
					a3=btn(text="تحويل رصيد🔁",callback_data="transfer")
					a0=btn(text="الحصول على انترنت مجاني",callback_data="getmbf")
					a2=btn(text="تسجيل الخروج",callback_data="logout")
					mas.add(a1)
					mas.add(a3)
					mas.add(a0)
					mas.add(a2)
					bot.send_message(id,msg,parse_mode="html",reply_markup=mas)
				else:
					conn.update({"access":"no"},Query.id==id)
def trans(message):
	id=message.chat.id
	open(f"filer{id}.txt","w").write("transf")
	mas=mak()
	mas.add(btn(text="رجوع",callback_data="back"))
	msg="""<strong>
ارسل الرقم المراد تحويل الرصيد له
</strong>"""
	access=conn.search(Query.id==id)[0]["access"]
	if access=="no":
		bop(message)
		return "hello"
	gglp=bot.edit_message_text(message_id=message.message_id,chat_id=id,text=msg,parse_mode="html",reply_markup=mas)
	bot.register_next_step_handler(gglp,llorp)
def llorp(message):
	global nums
	nums=message.text
	id=message.chat.id
	access=conn.search(Query.id==id)[0]["access"]
	if access=="no":
		bop(message)
		return "hello"
	if nums[0:3]=="077":
		if open(f"filer{id}.txt").read()!="transf" or open(f"filer{id}.txt").read()=="back":
			return "back"
		open(f"filer{id}.txt","w").write("transf1")
		mas=mak()
		mas.add(btn(text="رجوع",callback_data="back"))
		msg="""<strong>
حسنا ارسل عدد الرصيد المراد تحويله
</strong>"""
		pdn=bot.send_message(id,msg,parse_mode="html",reply_markup=mas)
		bot.register_next_step_handler(pdn,ndp)
	if nums[0:5]=="/start":
		print("/start")
		bop(message)
def ndp(message):
	global amou,pid
	amou=message.text
	id=message.chat.id
	access=conn.search(Query.id==id)[0]["access"]
	if access=="no":
		bop(message)
		return "hello"
	if open(f"filer{id}.txt").read()!="transf1" or open(f"filer{id}.txt").read()=="back":
			return "back"
	open(f"filer{id}.txt","w").write("transf2")
	head={
"Authorization": "Bearer "+access,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": "fcb42a5d-ce8e-4467-b6c9-3c117f10e6",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
	
	data={
    "receiverMsisdn": nums,
    "amount": amou
    }
	req=requests.post("https://odpapp.asiacell.com/api/v1/credit-transfer/start?lang=ar",headers=head,json=data)
	
	
	if req.json()["success"]=="true" or req.json()["success"]==True or req.json()["success"]=="True":
		pid=req.json()["PID"]
		mas=mak()
		mas.add(btn(text="رجوع",callback_data="back"))
		msg="""<strong>
تم ارسال كود الى رقمك ارسله
</strong>"""
		pdnn=bot.send_message(id,msg,parse_mode="html",reply_markup=mas)
		bot.register_next_step_handler(pdnn,nndp)
	else:
		mas=mak()
		mas.add(btn(text="رجوع",callback_data="back"))
		msg=f"""<strong>
{req.json()['message']}
</strong>"""
		bot.send_message(id,msg,parse_mode="html",reply_markup=mas)
	if amou[0:5]=="/start":
		bop(message)

def nndp(message):
	code=message.text
	id=message.chat.id
	access=conn.search(Query.id==id)[0]["access"]
	if access=="no":
		bop(message)
		return "hello"
	if open(f"filer{id}.txt").read()!="transf2" or open(f"filer{id}.txt").read()=="back":
			return "back"
	head={
"Authorization": "Bearer "+access,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": "fcb42a5d-ce8e-4467-b6c9-3c117f10e6",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
	data={
	"PID":pid,
	"passcode": code
	}
	req=requests.post("https://odpapp.asiacell.com/api/v1/credit-transfer/do-transfer?lang=ar",json=data,headers=head).json()
	bot.send_message(id,req["message"])
@bot.callback_query_handler(func=lambda call : True)
def callq(call):
	message=call.message
	id=message.chat.id
	msgid=message.message_id
	cal=call.data
	if cal=="back":
		open(f"filer{id}.txt","w").write("back")
		try:
			data=conn.search(Query.id==id)[0]
			access=data["access"]
		except:
			conn.insert({"id": id,"access": "no"})
			data=conn.search(Query.id==id)[0]
			access=data["access"]
		if access=="no":
				mas=mak()
				a1=btn(text="تسجيل الدخول",callback_data="login")
				mas.add(a1)
				bot.edit_message_text(chat_id=id,text="<strong>هل تريد تسجيل الدخول</strong>",message_id=msgid,parse_mode="html",reply_markup=mas)
				
		else:
				head1={
"Authorization": "Bearer "+access,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": "fcb42a5d-ce8e-4467-b6c9-3c117f10e6",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
				
				req2=requests.get("https://odpapp.asiacell.com/api/v1/profile?lang=en",headers=head1).text
				if '"message":"Success"' in req2:
					numb=req2.split('"phoneNumber":"')[1].split('"')[0]
					amou=req2.split('"title":"YOUR PREPAID BALANCE","items":[{"value":')[1].split(',"')[0]
					msg=f"""
<strong>
اهلا بك عزيزي

رقمك : {numb}
رصيدك : {amou}

اختر احد الازرار تحت
</strong>
"""
					
					mas=mak()
					a1=btn(text="تعبئة كارت💳",callback_data="addcart")
					a3=btn(text="تحويل رصيد🔁",callback_data="transfer")
					a0=btn(text="الحصول على انترنت مجاني")
					a2=btn(text="تسجيل الخروج",callback_data="logout")
					mas.add(a1)
					
					mas.add(a3)
					mas.add(a0)
					mas.add(a2)
					bot.edit_message_text(chat_id=id,text=msg,message_id=msgid,parse_mode="html",reply_markup=mas)
				else:
					conn.update({"access":"no"},Query.id==id)
	if call.data=="transfer":
		trans(message)
	if call.data=="getmbf":
		access=conn.search(Query.id==id)[0]["access"]
		if access=="no":
			bob(message)
		else:
			head1={
"Authorization": "Bearer "+access,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": "fcb42a5d-ce8e-4467-b6c9-3c117f10e6",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
			data2={}
			mas=mak()
			mas.add(btn(text="رجوع",callback_data="back"))
			req2=requests.post("https://odpapp.asiacell.com/api/v1/spinwheel/confirm?lang=ar&theme=avocado",json=data2,headers=head1).text
			
			if 'reward' in req2:
				rewd=req2.split('"reward":')[1].split('}')[0]
				msg=f"مبروك لقد حصلت على {rewd}"
				bot.edit_message_text(chat_id=id,message_id=message.message_id,text=f"<strong>{msg}</strong>",parse_mode="html",reply_markup=mas)
			else:
				
				msg=req2.split('"message":"')[1].split('"')[0]
				bot.edit_message_text(chat_id=id,message_id=message.message_id,text=f"<strong>{msg}</strong>",parse_mode="html",reply_markup=mas)

		
	if cal=="logout":
		mas=mak()
		a1=btn(text="نعم",callback_data="aae")
		a2=btn(text="رجوع",callback_data="back")
		mas.add(a1)
		mas.add(a2)
		bot.edit_message_text(chat_id=id,text="<strong>هل انت متاكد من تسجيل الخروج</strong>",message_id=msgid,parse_mode="html",reply_markup=mas)
	if cal=="aae":
		conn.update({"access": "no"},Query.id==id)
		try:
			data=conn.search(Query.id==id)[0]
			access=data["access"]
		except:
			conn.insert({"id": id,"access": "no"})
			data=conn.search(Query.id==id)[0]
			access=data["access"]
		if access=="no":
				mas=mak()
				a1=btn(text="تسجيل الدخول",callback_data="login")
				mas.add(a1)
				bot.edit_message_text(chat_id=id,text="<strong>هل تريد تسجيل الدخول</strong>",message_id=msgid,parse_mode="html",reply_markup=mas)
				
		else:
				head1={
"Authorization": "Bearer "+access,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": "fcb42a5d-ce8e-4467-b6c9-3c117f10e6",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
				
				req2=requests.get("https://odpapp.asiacell.com/api/v1/profile?lang=en",headers=head1).text
				if '"message":"Success"' in req2:
					numb=req2.split('"phoneNumber":"')[1].split('"')[0]
					amou=req2.split('"title":"YOUR PREPAID BALANCE","items":[{"value":')[1].split(',"')[0]
					msg=f"""
<strong>
اهلا بك عزيزي

رقمك : {numb}
رصيدك : {amou}

اختر احد الازرار تحت
</strong>
"""
					
					mas=mak()
					a1=btn(text="تعبئة كارت💳",callback_data="addcart")
					a3=btn(text="تحويل رصيد🔁",callback_data="transfer")
					a2=btn(text="تسجيل الخروج",callback_data="logout")
					a0=btn(text="الحصول على انترنت مجاني")
					
					mas.add(a1)
					mas.add(a3)
					mas.add(a0)
					mas.add(a2)
					bot.edit_message_text(chat_id=id,text=msg,message_id=msgid,parse_mode="html",reply_markup=mas)
				else:
					conn.update({"access":"no"},Query.id==id)
	if call.data=="login":
		login(message)				
	if call.data=="addcart":
		open(f"filer{id}.txt","w").write("addcart")
		mas=mak()
		mas.add(btn(text="رجوع",callback_data="back"))
		msg="<strong>حسنا ارسل رقم الكارت اذا كان غير صحيح سيتم حضرك 24 ساعه</strong>"
		kol=bot.edit_message_text(message_id=msgid,text=msg,chat_id=id,reply_markup=mas,parse_mode="html")
		bot.register_next_step_handler(kol,wow)
def wow(message):
	id=message.chat.id
	if open(f"filer{id}.txt").read()!="addcart" or open(f"filer{id}.txt").read()=="back":
		return "vack"
	else:True
	access=conn.search(Query.id==id)[0]["access"]
	if access=="no":
		bob(message)
	else:
		card=message.text
		head1={
"Authorization": "Bearer "+access,
"X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
"DeviceID": "fcb42a5d-ce8e-4467-b6c9-3c117f10e6",
"X-OS-Version": "7.1.2",
"X-Device-Type": "[Android][samsung][SM-N975F 7.1.2] [N]",
"X-ODP-APP-VERSION": "3.4.0",
"X-FROM-APP": "odp",
"X-ODP-CHANNEL": "mobile",
"X-SCREEN-TYPE": "MOBILE",
"Content-Type": "application/json; charset=UTF-8",           
}
		data2={
			"msisdn": "",
			"rechargeType": 1,
			"voucher": card
			}
		mas=mak()
		mas.add(btn(text="رجوع",callback_data="back"))
		req2=requests.post("https://odpapp.asiacell.com/api/v1/top-up?lang=ar",json=data2,headers=head1).json()
		bot.send_message(id,f"<strong>{req2['message']}</strong>",parse_mode="html",reply_markup=mas)





	
			
bot.infinity_polling()			

			
		