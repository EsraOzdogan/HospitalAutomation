from tkinter import *
import os

import PIL.Image, PIL.ImageTk


from PIL import ImageTk,Image


def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()
def delete6():
    screen7.destroy()

def login_success():
    screen2.destroy()
    
    global screen3
    screen3 = Toplevel(screen)
    w, h = screen3.winfo_screenwidth(), screen3.winfo_screenheight()
    screen3.geometry("%dx%d+0+0" % (w, h))
    
    Label(screen3, text = "").pack()

    global patient_tc
    global patient_tc_entry
    global patient_name
    global patient_name_entry
    global patient_last_name
    global patient_last_name_entry
    global patient_clinic
    global patient_clinic_entry
    global patient_dr
    global patient_dr_entry
    global patient_saat
    global patient_saat_entry
    
    
    
    patient_name = StringVar()
    patient_tc = StringVar()
    patient_last_name = StringVar()
    patient_clinic = StringVar()
    patient_saat = StringVar()


    
    Label(screen3, text = "").pack()
    image = Image.open('C:\\Users\\admin\\Desktop\\Hospital Automation\\img\\logo-2.png')
    photo1 = ImageTk.PhotoImage(image)
    label2 = Label(screen3,image=photo1)
    label2.image = photo1 # keep a reference!
    label2.pack()
    Label(screen3, text = "Lütfen hasta bilgilerini giriniz:", fg="#222", font = "Arial 20", pady="5").pack()
    
   
    Label(screen3, text = "TC Kimlik No", fg="#222",font = "Arial 10").pack()
    patient_tc_entry = Entry(screen3, textvariable = patient_tc)
    patient_tc_entry.pack()
    
    
    Label(screen3, text = "Ad", fg="#222",font = "Arial 10").pack()
    patient_name_entry = Entry(screen3, textvariable = patient_name)
    patient_name_entry.pack()

    Label(screen3, text = "Soyad", fg="#222",font = "Arial 10").pack()
    patient_last_name_entry = Entry(screen3, textvariable = patient_last_name)
    patient_last_name_entry.pack()

    def randevuSec(value):
       
        global patient_saat
        global patient_saat_entry
       
        if value == "Prof.Dr. Hakan PEKESEN" or "Op.Dr. Canan KARATAY " or "Doç.Dr. Nicki MINAJ" or "Prof.Dr. İbrahim Adnan SARAÇOĞLU":
            
            Label(screen3, text = "Saat Seçiniz",font = "Arial 10").pack()
            patient_saat_entry = Entry(screen3, textvariable = patient_saat, width = 2)
            patient_saat_entry.pack()
            Label(screen3, text = "  ").pack()
            

            Button(screen3, text = "Kaydet", bg = "#fff", fg = "#222", width = 10, height = 1, command=HastaKaydet).pack()
            
    inpt=[]
    inpt2=[]
    inpt3=[]
    inpt4=[]
    
    def RandevuSaatleri():
        global screen6
        screen6 = Toplevel(screen)
        w, h = screen6.winfo_screenwidth(), screen6.winfo_screenheight()
        screen6.geometry("%dx%d+0+0" % (w, h))

        Label(screen6, text = "").pack()
        Label(screen6, text = "").pack()
        Label(screen6, text = "--Randevulu Hastalar--", fg="#222", font = "Arial 20", pady="5").pack()
        Label(screen6, text = "").pack()
        Label(screen6, text = "").pack()
        
        i= 0
        while i < 30:
            Label(screen6, text="Tc: "+inpt2[i]+"  Ad: " + inpt3[i]+ "  Soyad: "+inpt4[i], fg="#222",font = "Arial 18",pady="5").pack()            
            i += 1

        Label(screen6, text = "").pack()
        image = Image.open('C:\\Users\\admin\\Desktop\\Hospital Automation\\img\\logo-2.png')
        photo1 = ImageTk.PhotoImage(image)
        label2 = Label(screen6,image=photo1)
        label2.image = photo1 # keep a reference!
        label2.pack()
        Label(screen6, text = "Lütfen hasta bilgilerini giriniz:", fg="#222", font = "Arial 20", pady="5").pack()
            
    def HastaDizisi():
        patient_saat_info = patient_saat.get()
        patient_tc_info = patient_tc.get()
        patient_name_info = patient_name.get()
        patient_last_name_info = patient_last_name.get()

        inpt.append(patient_saat_info)
        inpt2.append(patient_tc_info)
        inpt3.append(patient_name_info)
        inpt4.append(patient_last_name_info)
        #print(inpt)

    def HastaGoster():
        
        #print("Hastalar =", inpt)

        #sorted = sorted(inpt)

        root = inpt[0]
        inpt.remove(root)

        tree = [root, [], []]

        def sol_root(this_tree):
            if len(this_tree) == 1:
                this_tree[1].append([],[])
            elif len(this_tree) == 2:
                this_tree[1].append([])

            return this_tree[1]

        def sag_root(this_tree):
            if len(this_tree) == 1:
                this_tree[2].append([],[])
            elif len(this_tree) == 2:
                this_tree[2].append([])

            return this_tree[2]

        def is_empty(this_tree):
          return this_tree == []

        def is_leaf(thistree):
            return sol_root(this_tree) == [] and sag_root(this_tree) == []

        def count_leaves(this_tree):
          if is_empty(this_tree):
            return 0
          if is_leaf(this_tree):
            return 1
          else:
            return count_leaves(sol_root(this_tree)) + count_leaves(sag_root(this_tree))

        def root_ne(this_tree):
            return this_tree[0]

        def sum_tree(this_tree):
            if is_empty(this_tree):
                return 0
            return root_ne(this_tree) + sum_tree(left(tree)) + sum_tree(right(tree))

        def make_tree(tree):
            tmp_tree = tree
            for number in inpt:
                tmp_tree = tree
                finish = False
                while finish == False:
                    if int(number) <= int(tmp_tree[0]):
                        if is_empty(tmp_tree[1]):
                            tmp_tree[1] = [number, [], []]
                            finish = True
                        else:
                            tmp_tree = sol_root(tmp_tree)
                    else:
                        if is_empty(tmp_tree[2]):
                            tmp_tree[2] = [number, [], []]
                            finish = True
                        else:
                            tmp_tree = sag_root(tmp_tree)

        make_tree(tree)
        #print("\nTree: \n" + str(tree))

        #Sorted Tree
        def sorted_tree(this_tree):
            if is_empty(sol_root(this_tree)) == False:
                sorted_tree(sol_root(this_tree))
            print("Saat: "+this_tree[0]+".00")
            if is_empty(sag_root(this_tree)) == False:
                sorted_tree(sag_root(this_tree))

        print("\nRandevu Saatleri:")
        sorted_tree(tree)

        def is_binary(this_tree):
            if is_empty(this_tree):
                return True
            if 1 < len(this_tree) <= 3:
                return is_binary(sol_root(this_tree)) and is_binary(sag_root(this_tree))
            return False
##        def tanimla():
##            patient_tc_info = patient_tc.get()
##            for x in inpt2: 
##                dosya = open("C:/Users/admin/Desktop/Hospital Automation/hastalar/"+inpt2[0],"r")
##                
##                verify = dosya.read().splitlines()
##                if "Saat: "+inpt[0] in verify:
##                    print("sdfgh")
##                else:
##                    print("no")
                
               
                
        #tanimla()
        RandevuSaatleri()
        
        
    def HastaKaydet():



        
        patient_tc_info = patient_tc.get()
        
        if (len(patient_tc_info)!=11):
            global screen7
            screen7 = Toplevel(screen)
            screen7.geometry("250x130")
            screen7.configure(background="#222")
            Label(screen7, text = "", bg="#222").pack()
            Label(screen7, text="Eksik veya hatalı T.C. girdiniz!", fg= "white", bg="#222", font="10").pack()
            Label(screen7, text = "", bg="#222").pack()
            Button(screen7, text = "Tamam", bg = "#fff", fg = "#222", width = 10, height = 1, command=delete).pack()
        else:  
        
            
            patient_name_info = patient_name.get()
            patient_last_name_info = patient_last_name.get()
            
            patient_saat_info = patient_saat.get()
            
            HastaDizisi()

            file=open("C:/Users/admin/Desktop/Hospital Automation/hastalar/"+patient_tc_info, "w")
            file.write("TC: "+patient_tc_info+"\n")
            file.write("Ad: "+patient_name_info+"\n")
            file.write("Soyad: "+patient_last_name_info+"\n")
            
            file.write("Saat: "+patient_saat_info+"\n")
            
            file.close()

            patient_tc_entry.delete(0, END)
            patient_name_entry.delete(0, END)
            patient_last_name_entry.delete(0, END)
            
            patient_saat_entry.delete(0, END)
            
            

            Label(screen3, text="").pack()
            Label(screen3, text = "Kayıt Başarılı!",font = "Arial 18").pack()

        
        
            

    def doktorSec(value):
        if value == "Ağız, Diş ve Çene Cerrahisi" or "Göz Hastalıkları" or "Beyin ve Sinir Cerrahisi" or "Genel Cerrahi" or "Kalp ve Damar Cerrahisi" or "Kadın Hastalıkları ve Doğum" or "Iç Hastalıkları (Dahiliye)" or "Kardiyoloji":
            Label(screen3, text = "Doktor",  fg="#222",font = "Arial 10").pack() 
            OPTIONS1 = [
            "Prof.Dr. Hakan PEKESEN" ,
            "Op.Dr. Canan KARATAY ",
            "Doç.Dr. Nicki MINAJ",
            "Prof.Dr. İbrahim Adnan SARAÇOĞLU"
            ]
            variable1 = StringVar(screen3)
            variable1.set("Doktor seçiniz...")
            y = OptionMenu(*(screen3, variable1) + tuple(OPTIONS1),command = randevuSec)
            y.config(font=('calibri',(10)),bg='white',width=20, pady="15",relief="groove")
            y['menu'].config(font=('calibri',(10)),bg='white')
            
            y.pack()

        
        
    
    Label(screen3, text = "Klinik",font = "Arial 10", width= "20").pack()
    
    def insertion_sort(Klinik: list):
        for j in range(1, len(Klinik)):
            guncel = Klinik[j]
            i=j-1
            while i >= 0 and Klinik[i] > guncel:
                Klinik[i+1]=Klinik[i]
                i = i-1
            Klinik[i+1] = guncel
        return Klinik
    
    if __name__=="__main__":
        Klinik = [
            "Göz Hastalıkları",
            "Beyin ve Sinir Cerrahisi",
            "Genel Cerrahi",
            "Ağız, Diş ve Çene Cerrahisi",
            "Kalp ve Damar Cerrahisi",
            "Kadın Hastalıkları ve Doğum",
            "Iç Hastalıkları (Dahiliye)",
            "Kardiyoloji"
            ]
        Klinik = insertion_sort(Klinik)
        for i in Klinik:
            print(i)
    variable = StringVar(screen3)
    variable.set("Klinik seçiniz...")
    w = OptionMenu(*(screen3, variable) + tuple(Klinik), command = doktorSec)
    w.config(font=('calibri',(10)),bg='white',width=20, pady="15",relief="groove")
    w['menu'].config(font=('calibri',(10)),bg='white')
    w.pack()

    Label(screen3,text = "", height = "1").pack()
    Button(screen3, text = "Randevu Saatlerini Göster", bg = "#fff", fg = "#222", width = 20, height = 2,pady=3, command=HastaGoster).pack()
    Label(screen3,text = "", height = "1").pack()
    

    
    
        

    

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.geometry("180x130")
    screen4.configure(background="#222")
    Label(screen4, text = "", bg="#222").pack()
    Label(screen4, text="Hatalı Parola!", fg= "white", bg="#222", font="10").pack()
    Label(screen4, text = "", bg="#222").pack()
    Button(screen4, text = "Tamam", bg = "#fff", fg = "#222", width = 10, height = 1, command=delete3).pack()
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.geometry("180x130")
    screen5.configure(background="#222")
    Label(screen5, text = "", bg="#222").pack()
    Label(screen5, text="Kullanıcı Bulunamadı!", fg= "white", bg="#222", font="10").pack()
    Label(screen5, text = "", bg="#222").pack()
    Button(screen5, text = "Tamam", bg = "#fff", fg = "#222", width = 10, height = 1, command=delete4).pack()

def register_user():
    
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="", bg="#222").pack()
    Label(screen1, text = "Kayıt Başarılı!", fg= "#222", font="10").pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Yeni Üye")
    w, h = screen1.winfo_screenwidth(), screen1.winfo_screenheight()
    screen1.geometry("%dx%d+0+0" % (w, h))

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="").pack()
    Label(screen1, text = "Lütfen bilgilerinizi giriniz.", fg="#222", font = "Arial 20", pady="5").pack()
    Label(screen1, text="").pack()
    Label(screen1, text = "Kullanıcı Adı* ", fg="#222",font = "Arial 18").pack()
    username_entry = Entry(screen1,font = "Arial 18", textvariable = username)
    username_entry.pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Parola* ", fg="#222",font = "Arial 18").pack()
    password_entry = Entry(screen1,font = "Arial 18", textvariable = password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Label(screen1, text="").pack()
    Button(screen1, text = "Kayıt Ol", bg = "#fff", pady="5",font = "25", fg = "#222", width = 25, height = 2,  command = register_user).pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "").pack()
    image = Image.open('C:\\Users\\admin\\Desktop\\Hospital Automation\\img\\logo-2.png')
    photo1 = ImageTk.PhotoImage(image)
    label2 = Label(screen1,image=photo1)
    label2.image = photo1 # keep a reference!
    label2.pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Giriş Yap")
    w, h = screen2.winfo_screenwidth(), screen2.winfo_screenheight()
    screen2.geometry("%dx%d+0+0" % (w, h))
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Lütfen giriş yapmak için bilgilerinizi giriniz.", fg="#222", font = "Arial 20", pady="5").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    
    Label(screen2, text = "").pack()
    Label(screen2, text = "Kullanıcı Adı* ", fg="#222",font = "Arial 18").pack()
    username_entry1 = Entry(screen2,font = "Arial 18", textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Parola* ",fg="#222",font = "Arial 18").pack()
    password_entry1 = Entry(screen2,font = "Arial 18",textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Giriş Yap", bg = "#fff", pady="5",font = "18", fg = "#222", width = 25, height = 2,  command = login_verify).pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    image = Image.open('C:\\Users\\admin\\Desktop\\Hospital Automation\\img\\logo-2.png')
    photo1 = ImageTk.PhotoImage(image)
    label2 = Label(screen2,image=photo1)
    label2.image = photo1 # keep a reference!
    label2.pack()
    
    
    
def main_screen():
    global screen
    screen = Tk()
    screen.title("GİRİŞ")
    w, h = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.geometry("%dx%d+0+0" % (w, h))
    #screen.config(background="#222")
    Label(text = "").pack()
    image = Image.open('C:\\Users\\admin\\Desktop\\Hospital Automation\\img\\logo.png')
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.pack()

   
  
    Label(text = "",  height = "3").pack()
    Label(text = "T.C. Sağlık Bakanlığı", fg="#333", font = "Arial 15", width="300").pack()
    Label(text = "YALOVA DEVLET HASTANESİNE HOŞGELDİNİZ!", fg="#222", font = "Arial 15", width="300").pack()
    Label(text = "",  height = "3").pack()
    Button(text = "Üye Ol", width = 25, height = 2, pady="5", bg = "#fff", fg = "#222", font = "18", command = register).pack()
    Label(text = "").pack()
    Button(text = "Giriş Yap", width = 25, height = 2, pady="5", bg = "#fff", fg = "#222", font = "18", command = login).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    Label(text = "").pack()
    image = Image.open('C:\\Users\\admin\\Desktop\\Hospital Automation\\img\\logo-2.png')
    photo1 = ImageTk.PhotoImage(image)
    label2 = Label(image=photo1)
    label2.image = photo1 # keep a reference!
    label2.pack()
    
    screen.mainloop()

main_screen()
