import json
from tkinter import *
from PIL import Image,  ImageTk
from difflib import get_close_matches
import time
from medbot import *

usermessage=[]
userinfo=[]
age=0
cp=0
trestbps=0
chol=0
fbs=0
restecg=0
thalach=0     

class Medbot:
       
    def __init__(self,root):
        # code to give medbot window title
        root.title("Med Bot")

        # code to give medbot window dimension
        root.geometry('350x500')

        # #code to change titlebar icon
        # photo = PhotoImage(file = "doctor.png")
        # root.iconphoto(False, photo)
        image1 = Image.open("doctor.png")
        test = ImageTk.PhotoImage(image1)
        root.iconphoto(False, test)

        #code to create chat area
        # bd==Border
        # bg==Backgroubd colour
        self.chatWindow=Text(root,bd=1,bg='black',fg='white',width=50, height=8,relief="flat", font=("Times New Roman", 10), undo=True, wrap="word")
        self.chatWindow.place(x=6,y=6,height=420,width=338)
        self.message_position = 1.5

        #code to create message window
        self.Message_Entry = Entry(root, width=40, font=('Times', 12))
        self.Message_Entry.bind('<Return>', self.reply_to_you)
        self.Message_Entry.place(x=6,y=435,height=40,width=235)

        #code to create button to send the message
        self.Button=Button(root,text='Send',bg='purple',fg='white',activebackground='light blue',width=30,height=4,font=('Times New Roman',14),relief ='flat', command = self.reply_to_you)
        self.Button.place(x=242,y=435,height=40,width=100)

        #code to add scrollbar
        self.scrollbar=Scrollbar(root,command=self.chatWindow.yview())
        self.scrollbar.place(x=325,y=6,height=420)
        self.add_chat("Medbot: Hi this is automated Medboat \nPlease Answer these Questions\n\n")
        self.add_chat("Medbot: Please enter your age")
        usermessage.append("Please enter your age: ")
       # self.Brain = json.load(open('knowledge.json'))

    def add_chat(self,message):
        self.message_position+=1.5
        #print(self.message_position)
        self.Message_Entry.delete(0, 'end')
        self.chatWindow.config(state='normal')
        self.chatWindow.insert(self.message_position, message)
        self.chatWindow.see('end')
        self.chatWindow.config(state='disabled')
    
   
    
    def reply_to_you(self,event=None):
       
        
        
        message=self.Message_Entry.get().lower()
        print("User Enterred Message is: ",message)
        string=message
        dispmessage = '\nyou: '+ string+'\n'
        print("dispmessage ",dispmessage)
        print("usermessage ",usermessage)
        self.add_chat(dispmessage)
         
        #time.sleep(5)
        if(string.isdigit()):
            
           # usermessage.append(string)
            #self.add_chat(dispmessage)
            print("Reached ---------------")
            print("usermessage  List is:",usermessage)
            if(usermessage[len(usermessage)-1]=="Please enter your age: "):
                age=int(string)
                userinfo.append(age)
                print("User Entered Age: ",age)
                reply = '\nMedbot: '+ 'Please enter your chest pain level: '
                usermessage.append("Please enter your chest pain level: ")
                self.add_chat(reply)
                                
                                              
            elif(usermessage[len(usermessage)-1]=="Please enter your chest pain level: "):
                cp=int(string)
                userinfo.append(cp)
                print("User Entered cp : ",cp)
                #self.add_chat(message)
                reply = '\nMedbot: '+ 'Please enter your trestbps: '
                usermessage.append("Please enter your trestbps: ")
                self.add_chat(reply) 
                
            elif(usermessage[len(usermessage)-1]=="Please enter your trestbps: "):
                trestbps=int(string)
                userinfo.append(trestbps)
                print("User Entered trestbps : ",trestbps)
                #self.add_chat(message)
                reply = '\nMedbot: '+ 'Please enter your cholestrol: '
                usermessage.append("Please enter your cholestrol: ")
                self.add_chat(reply) 
                
            elif(usermessage[len(usermessage)-1]=="Please enter your cholestrol: "):
                chol=int(string)
                userinfo.append(chol)
                print("User Entered cholestrol : ",chol)
                #self.add_chat(message)
                reply = '\nMedbot: '+ 'Please enter your fasting blood sugar: '
                usermessage.append("Please enter your fasting blood sugar: ")
                self.add_chat(reply)
                
            elif(usermessage[len(usermessage)-1]=="Please enter your fasting blood sugar: "):
                fbs=int(string)
                userinfo.append(fbs)
                print("User Entered fasting blood sugar : ",fbs)
                #self.add_chat(message)
                reply = '\nMedbot: '+ 'Please enter your restecg: '
                usermessage.append("Please enter your restecg: ")
                self.add_chat(reply)   
            
            elif(usermessage[len(usermessage)-1]=="Please enter your restecg: "):
                restecg=int(string)
                userinfo.append(restecg)
                print("User Entered restecg : ",restecg)
                #self.add_chat(message)
                reply = '\nMedbot: '+ 'Please enter your maximum heart rate: '
                usermessage.append("Please enter your maximum heart rate: ")
                self.add_chat(reply)   
                
            elif(usermessage[len(usermessage)-1]=="Please enter your maximum heart rate: "):
                thalach=int(string)
                userinfo.append(thalach)
                print("User Entered maximum heart rate : ",thalach)
                #print(userinfo)
                reply1=getheartDiseaseResult(userinfo)
                #self.add_chat(message)
                
                reply1 = '\nMedbot: '+ reply1
               # usermessage.append("Please enter your maximum heart rate: ")
                self.add_chat(reply1)    
           
           
                
        else:
                reply = 'Medbot: '+ 'Value is not in Integer Format,Please Re-enter again\n'
                self.add_chat(reply)
        
            
        
    
    
        
#code to create tkinter object
root=Tk()
Medbot(root)
root.mainloop()



