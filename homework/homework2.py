from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import random
roles  = ['Villager','Villager','Werewolf','Werewolf','Seer','Gunner','Bodyguard','Fool','Serial Killer']
roles_left = []

#header
gui = Tk()
gui.title('Werewolf Game')
gui.geometry('1280x720')

#Title โปรแกรม
L1 = Label(gui,text='Werewolf Game',font=('SukhumvitSet',30),fg='black')
L1.place(x=500,y=30)

# Logo รูปหมา
FB3 = Frame(gui)
FB3.place(x=350,y=100)
image = Image.open("D:\src\python\python-uncle\homework\images\logo.png")
image = image.resize((600, 350))
photo = ImageTk.PhotoImage(image)
lbl = Label(FB3,image=photo)
lbl.pack()

def GetRoleBtn():
    global roles
    global roles_left
    try:
        chosen_role  = random.choice(roles)
        roles.remove(chosen_role)
        roles_left.append(chosen_role)
        dialog = Toplevel(gui)
        dialog.title('Roles Random')
        dialog.geometry("700x600")
        if chosen_role == 'Serial Killer':
            SKImg = Image.open("D:\src\python\python-uncle\homework\images\Serial Killer.png")
            SKphoto = ImageTk.PhotoImage(SKImg)
            image_label = Label(dialog, image=SKphoto)
            image_label.pack()
            message_label0 = Label(dialog, text="ฆ่าอย่างระมัดระวังละ เพราะคุณได้",font=('SukhumvitSet',18))
            message_label0.pack()
            message_label1 = Label(dialog, text="ฆาตกรต่อเนื่อง (Serial Killer) | ไม่ฝักใฝ่ฝ่ายใด",font=('SukhumvitSet',18))
            message_label1.pack()
            message_label2 = Label(dialog, text="ในแต่ละคืนคุณสามารถฆ่าผู้เล่นได้หนึ่งคน",font=('SukhumvitSet',18))
            message_label2.pack()
        elif chosen_role == 'Fool':
            FoolImg = Image.open("D:\src\python\python-uncle\homework\images\Fool_wwo.png")
            Foolphoto = ImageTk.PhotoImage(FoolImg)
            image_label = Label(dialog, image=Foolphoto)
            image_label.pack()
            message_label0 = Label(dialog, text="จงสวมบทบาทให้เนียนกับผู้อื่นเพราะคุณได้",font=('SukhumvitSet',18))
            message_label0.pack()
            message_label1 = Label(dialog, text="คนบ้า (Fool) | ไม่ฝักใฝ่ฝ่ายใด",font=('SukhumvitSet',18))
            message_label1.pack()
            message_label2 = Label(dialog, text="เป้าหมายของคุณคือการโดนประหาร ถ้าชาวบ้านแขวนคอประหารคุณ คุณชนะ",font=('SukhumvitSet',18))
            message_label2.pack()
        elif chosen_role == 'Seer':
            SeerImg = Image.open("D:\src\python\python-uncle\homework\images\Seer.png")
            SeerPhoto = ImageTk.PhotoImage(SeerImg)
            image_label = Label(dialog, image=SeerPhoto)
            image_label.pack()
            message_label0 = Label(dialog, text="คุณเป็นผู้มากสติปัญญา เพราะคุณได้",font=('SukhumvitSet',18))
            message_label0.pack()
            message_label1 = Label(dialog, text="ผู้หยั่งรู้ (Seer) | ฝ่ายชาวบ้าน",font=('SukhumvitSet',18))
            message_label1.pack()
            message_label2 = Label(dialog, text="ในแต่ละคืนคุณสามารถเลือกผู้เล่นเพื่อดูบทบาทของเขาได้",font=('SukhumvitSet',18))
            message_label2.pack()
        elif chosen_role == 'Werewolf':
            WerewolfImg = Image.open("D:\src\python\python-uncle\homework\images\Werewolf.png")
            Wolfphoto = ImageTk.PhotoImage(WerewolfImg)
            image_label = Label(dialog, image=Wolfphoto)
            image_label.pack()
            message_label0 = Label(dialog, text="ฆ่าอย่างระมัดระวังละ เพราะคุณได้",font=('SukhumvitSet',18))
            message_label0.pack()
            message_label1 = Label(dialog, text="มนุษย์หมาป่า (Werewolf) | ฝ่ายหมาป่า",font=('SukhumvitSet',18))
            message_label1.pack()
            message_label2 = Label(dialog, text="เลือกผู้เล่น 1 คนเพื่อฆ่าทุก ๆ คืน",font=('SukhumvitSet',18))
            message_label2.pack()
        elif chosen_role == 'Villager':
            VillagerImg = Image.open("D:\src\python\python-uncle\homework\images\Villager.png")
            Villagerphoto = ImageTk.PhotoImage(VillagerImg)
            image_label = Label(dialog, image=Villagerphoto)
            image_label.pack()
            message_label0 = Label(dialog, text="คุณเป็นแค่คนธรรมดา เพราะคุณได้",font=('SukhumvitSet',18))
            message_label0.pack()
            message_label1 = Label(dialog, text="ชาวบ้าน (Villager) | ฝ่ายชาวบ้าน",font=('SukhumvitSet',18))
            message_label1.pack()
            message_label2 = Label(dialog, text="เป็นสมาชิกฝ่ายชาวบ้าน มีความสามารถในการพูดในตอนกลางวัน รวมถึงการโหวตอีกด้วย",font=('SukhumvitSet',16))
            message_label2.pack()
        elif chosen_role == 'Gunner':
            GunnerImg = Image.open("D:\src\python\python-uncle\homework\images\Gunner.png")
            Gunnerphoto = ImageTk.PhotoImage(GunnerImg)
            image_label = Label(dialog, image=Gunnerphoto)
            image_label.pack()
            message_label0 = Label(dialog, text="ใช้ปืนอย่างระมัดระวัง เพราะคุณได้",font=('SukhumvitSet',18))
            message_label0.pack()
            message_label1 = Label(dialog, text="มือปืน (Gunner) | ฝ่ายชาวบ้าน",font=('SukhumvitSet',18))
            message_label1.pack()
            message_label2 = Label(dialog, text="เป็นผู้เล่นฝ่ายชาวบ้านที่สามารถฆ่าผู้เล่นอื่นได้ ยิงได้ 1 ครั้ง",font=('SukhumvitSet',18))
            message_label2.pack()
        elif chosen_role == 'Bodyguard':
            BodyguardImg = Image.open("D:\src\python\python-uncle\homework\images\Bodyguard.png")
            Bodyguardphoto = ImageTk.PhotoImage(BodyguardImg)
            image_label = Label(dialog, image=Bodyguardphoto)
            image_label.pack()
            message_label0 = Label(dialog, text="คุณเป็นฮีโร่ในสายตาอื่น เพราะคุณได้",font=('SukhumvitSet',18))
            message_label0.pack()
            message_label1 = Label(dialog, text="บอดี้การ์ด (Bodyguard) | ฝ่ายชาวบ้าน",font=('SukhumvitSet',18))
            message_label1.pack()
            message_label2 = Label(dialog, text="เป็นผู้เล่นฝ่ายชาวบ้านที่สามารถป้องกันผู้เล่นได้ 1 คน",font=('SukhumvitSet',18))
            message_label2.pack()
    except IndexError:
        txt = 'บทบาทได้แจกจ่ายให้ทุกคนแล้ว ไม่สามารถกดใช้ฟังก์ชั่นนี้ได้'
        messagebox.showerror('ERROR',txt)
    btnClose = ttk.Button(dialog, text='Close', command=dialog.destroy)
    btnClose.pack(ipadx=100, ipady=20)
    dialog.focus_set()
    dialog.wait_window()
def ExitBtn():
    gui.destroy()

# ปุ่มสุ่มบทบาท
FB1 = Frame(gui)
FB1.place(x=500,y=500)
b1_getrole = ttk.Button(FB1,text='Get Roles',command=GetRoleBtn)
b1_getrole.pack(ipadx=100,ipady=20)

# ปุ่ม Exit
FB2 = Frame(gui)
FB2.place(x=500,y=600)
b2_exit = ttk.Button(FB2,text='Exit',command=ExitBtn)
b2_exit.pack(ipadx=100,ipady=20)

gui.mainloop()