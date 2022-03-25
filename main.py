from __future__ import absolute_import
from __future__  import division
from __future__ import print_function
import tensorflow as tf
import numpy as np
from skimage.io import imread
from tensorflow.keras.models import load_model
from skimage.transform import resize
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from mamonfight22 import *
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import time
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
import winsound
root=Tk()
root.geometry("500x500")
duration = 3000  # milliseconds
freq = 1000


now = datetime.now()
current_time = now.strftime("%H:%M:%S")




#model = mamon_videoFightModel2(tf,wight='mamonedeffrbktoldmmon.hdf5')
model=load_model('weights.hdfs')
def send_mail():
    global otp
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    body_part = MIMEText(current_time)
    msg['Subject'] = 'VOILENCE DETECTED'
    msg['From'] = 'pythonfabhost2021@gmail.com'
    
    msg['To'] = 'pythonfabhost2021@gmail.com'
   
    msg.attach(body_part)

    SMTP_USERNAME = 'pythonfabhost2021@gmail.com'
    SMTP_PASSWORD = "skive@123"
    SMTP_PORT = 587
    SMTP_SERVER = 'smtp.gmail.com'
    FILE_1_path = './videos/output.avi'
        
    files = [FILE_1_path]   
    for file in files:
        with open(file,'rb') as file:
            msg.attach(MIMEApplication(file.read(), Name=file.name))
    server = smtplib.SMTP('smtp.gmail.com', 25)
    server.connect("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    text = msg.as_string()
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
def send_maile():
    global otp
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    #body_part = MIMEText(frametime)
    #body_part=frametime
    msg['Subject'] = 'VOILENCE DETECTED'
    msg['From'] = 'pythonfabhost2021@gmail.com'
    
    msg['To'] = 'pythonfabhost2021@gmail.com'
   
    msg.attach(MIMEText(frametime))

    SMTP_USERNAME = 'pythonfabhost2021@gmail.com'
    SMTP_PASSWORD = "skive@123"
    SMTP_PORT = 587
    SMTP_SERVER = 'smtp.gmail.com'
    FILE_1_path = './videos/output.avi'
        
    files = [FILE_1_path]   
    for file in files:
        with open(file,'rb') as file:
            msg.attach(MIMEApplication(file.read(), Name=file.name))
    server = smtplib.SMTP('smtp.gmail.com', 25)
    server.connect("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    text = msg.as_string()
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()




def vid():
    global frametime
    file = askopenfile(filetypes =[('file selector', '*')])
    cap = cv2.VideoCapture(str(file.name))
    i = 0
    frames = np.zeros((30, 160, 160, 3), dtype=np.float)
    old = []
    j = 0
    #frame_no = 0
    while(True):
        ret, frame = cap.read()
    
        # describe the type of font
        # to be used.
        font = cv2.FONT_HERSHEY_SIMPLEX
        if i > 29:
            ysdatav2 = np.zeros((1, 30, 160, 160, 3), dtype=np.float)
            ysdatav2[0][:][:] = frames
            predaction = pred_fight(model,ysdatav2,acuracy=0.96)
            print(predaction)
            if predaction[0] == True:
                cv2.imshow('video', frame)
                print('Violance detacted here ...')
                winsound.Beep(freq, duration)
                frametime1=int(cap.get(cv2.CAP_PROP_POS_MSEC))
                frametime=str(frametime1)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                vio = cv2.VideoWriter("./videos/output"+".avi", fourcc, 10.0, (fwidth,fheight))

                #vio = cv2.VideoWriter("./videos/output-"+str(j)+".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 10, (300, 400))
                for frameinss in old:
                    vio.write(frameinss)
                vio.release()
                cv2.putText(frame, 
                    'Violance', 
                    (50, 50), 
                    font, 3, 
                    (0, 255, 255), 
                    2, 
                    cv2.LINE_4)
                time.sleep(10)
            send_maile()
            #frame_no += 1   
            i = 0
            j += 1
            frames = np.zeros((30, 160, 160, 3), dtype=np.float)
            old = []
        else:
            frm = resize(frame,(160,160,3))
            old.append(frame)
            fshape = frame.shape
            fheight = fshape[0]
            fwidth = fshape[1]
            frm = np.expand_dims(frm,axis=0)
            if(np.max(frm)>1):
                frm = frm/255.0
            frames[i][:] = frm

            i+=1

        cv2.imshow('video', frame)
    

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


def live():
    
    cap = cv2.VideoCapture(0)
    i = 0
    frames = np.zeros((30, 160, 160, 3), dtype=np.float)
    old = []
    j = 0
    while(True):
        ret, frame = cap.read()
    
        # describe the type of font
        # to be used.
        font = cv2.FONT_HERSHEY_SIMPLEX
        if i > 29:
            ysdatav2 = np.zeros((1, 30, 160, 160, 3), dtype=np.float)
            ysdatav2[0][:][:] = frames
            predaction = pred_fight(model,ysdatav2,acuracy=0.96)
            print(predaction)
            if predaction[0] == True:
                cv2.putText(frame, 
                    'Violance Deacted  ... Violence .. violence', 
                    (50, 50), 
                    font, 3, 
                    (0, 255, 255), 
                    2, 
                    cv2.LINE_4)
                cv2.imshow('video', frame)
                print('Violance detacted here ...')
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                vio = cv2.VideoWriter("./videos/output"+".avi", fourcc, 10.0, (fwidth,fheight))
                #vio = cv2.VideoWriter("./videos/output-"+str(j)+".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 10, (300, 400))
                for frameinss in old:
                    vio.write(frameinss)
                vio.release()
            send_mail()
            i = 0
            j += 1
            frames = np.zeros((30, 160, 160, 3), dtype=np.float)
            old = []
        else:
            frm = resize(frame,(160,160,3))
            old.append(frame)
            fshape = frame.shape
            fheight = fshape[0]
            fwidth = fshape[1]
            frm = np.expand_dims(frm,axis=0)
            if(np.max(frm)>1):
                frm = frm/255.0
            frames[i][:] = frm

            i+=1

        cv2.imshow('video', frame)
    

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()

b1=Button(root,text="INPUT",command=vid,width=20,height=1,bg='black',fg='white',font=('times',12) )
b1.place(x=180,y=180)
b1=Button(root,text="LIVE",command=live,width=20,height=1,bg='black',fg='white',font=('times',12) )
b1.place(x=180,y=250)


root.mainloop()


