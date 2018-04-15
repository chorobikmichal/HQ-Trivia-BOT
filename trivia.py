import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
import image
from PIL import ImageGrab
import numpy as np
import cv2
import os
import io
from google.cloud import vision
from google.cloud.vision import types
import json
import requests
import pandas as pd
from nltk.corpus import stopwords
import nltk
import urllib.request
from http.cookiejar import CookieJar

fountq1=0
fountq2=0
fountq3=0

def searchTerms(serchTerms):
    serchTerms=serchTerms.lower()
    serchTerms = serchTerms.replace('-', ' ')
    serchTerms = serchTerms.replace(' of ', ' ')
    serchTerms = serchTerms.replace(' in ', ' ')
    serchTerms = serchTerms.replace(' a ', ' ')
    serchTerms = serchTerms.replace(' to ', ' ')
    serchTerms = serchTerms.replace('the ', '')
    serchTerms = serchTerms.replace('.', '')
    serchTerms = serchTerms.replace(',', '')
    serchTerms = serchTerms.replace('"', '')
    return(serchTerms)

def ser(bol,a1,a2,a3,question):

    serchTerms1= a1
    serchTerms2= a2
    serchTerms3= a3
    serchTerms1= searchTerms(serchTerms1)
    serchTerms2= searchTerms(serchTerms2)
    serchTerms3= searchTerms(serchTerms3)

    temp1=a1
    temp2=a2
    temp3=a3

    a1 = a1.replace(',', '')
    a1 = a1.replace('.', '')
    a1 = a1.replace('"', '')
    a2 = a2.replace(',', '')
    a2 = a2.replace('.', '')
    a2 = a2.replace('"', '')
    a3 = a3.replace(',', '')
    a3 = a3.replace('.', '')
    a3 = a3.replace('"', '')

    OGquestion = question
    question = question.replace(',', '')
    question = question.replace('.', '')
    question = question.replace('"', '')
    question = question.replace('?', '')

    if(bol==0):
        serchTerms=serchTerms1
        question = question + a1
    elif(bol==1):
        serchTerms=serchTerms2
        question = question + a2
    else:
        serchTerms=serchTerms3
        question = question + a3

    question = question.replace(' 93 ', '')


    #################################################################
    key = #your API key
    cx = #your id

    q = question

    url = "https://www.googleapis.com/customsearch/v1"
    parameters = {"q": q,
                  "cx": cx,
                  "key": key,
                  "orTerms": serchTerms,
                  #orTerms
                  #exactTerms
                  "filter": "1"
                  }

    page = requests.request("GET", url, params=parameters)
    results = json.loads(page.text)
    results.keys()

    #########################Searching the snippets and titles#############################################
    global fountq1
    global fountq2
    global fountq3

    s1=a1.lower()
    s2=a2.lower()
    s3=a3.lower()

    s1=s1.split()
    s2=s2.split()
    s3=s3.split()

    s1=[word for word in s1 if not word in stopwords.words('english')]
    s2=[word for word in s2 if not word in stopwords.words('english')]
    s3=[word for word in s3 if not word in stopwords.words('english')]

    #for item in results["items"]:
    #    print(item["snippet"])

    for item in results["items"]:
        fountq1=fountq1+(2*item["snippet"].lower().count(temp1.lower()))
        fountq1=fountq1+(2*item["title"].lower().count(temp1.lower()))
        if(a1.find('-')):
            temp1=temp1.replace('-', '')
            fountq1=fountq1+(2*item["snippet"].lower().count(temp1.lower()))
            fountq1=fountq1+(2*item["title"].lower().count(temp1.lower()))
        for x in s1:
            if(2<len(x)):
                fountq1+=item["snippet"].lower().count(x)
                fountq1+=item["title"].lower().count(x)

    for item in results["items"]:
        fountq2=fountq2+(2*item["snippet"].lower().count(temp2.lower()))
        fountq2=fountq2+(2*item["title"].lower().count(temp2.lower()))
        if(a2.find('-')):
            temp2=temp2.replace('-', '')
            fountq2=fountq2+(2*item["snippet"].lower().count(temp2.lower()))
            fountq2=fountq2+(2*item["title"].lower().count(temp2.lower()))
        for x in s2:
            if(2<len(x)):
                fountq2+=item["snippet"].lower().count(x)
                fountq2+=item["title"].lower().count(x)

    for item in results["items"]:
        fountq3=fountq3+(2*item["snippet"].lower().count(temp3.lower()))
        fountq3=fountq3+(2*item["title"].lower().count(temp3.lower()))
        if(a3.find('-')):
            temp3=temp3.replace('-', '')
            fountq3=fountq3+(2*item["snippet"].lower().count(temp3.lower()))
            fountq3=fountq3+(2*item["title"].lower().count(temp3.lower()))
        for x in s3:
            if(2<len(x)):
                fountq3+=item["snippet"].lower().count(x)
                fountq3+=item["title"].lower().count(x)

    print("**************************************************************")
    print("question: ", end='')
    print(OGquestion)

    print("")
    print(a1)
    print("snipet/title: ", end='')
    print(fountq1)
    print("")

    print("")
    print(a2)
    print("snipet/title: ", end='')
    print(fountq2)
    print("")

    print("")
    print(a3)
    print("snipet/title: ", end='')
    print(fountq3)
    print("")

    pp=0
    pp+=question.count(" NOT ")
    if(pp>0):
        print("")
        print("-------------NOT-----------")


def searchNow(alal):
    ########################Pre Processing#########################################
    list = alal.split("\n")
    length=len(list)-1

    if(length<3):
        print("string too small EXITING")
        exit()

    a1=list[length-3]
    a2=list[length-2]
    a3=list[length-1]

    question=""
    i=length-4
    while (i>=0):
        question=list[i]+" "+question
        i-=1

    print("*****************************************************************")
    print(question)

    for t in range(3):
        ser(t,a1,a2,a3,question)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save('capture.png')
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

        #cv2.imshow('Captured Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #**************************aa.py***********************************************
        print("inputting image")

        path=r"C:\Users\honol\Desktop\trivia\for-Github\capture.png"

        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
        	content = image_file.read()

        image = types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations

        count=0
        alal="empty"
        for text in texts:

        	if(count==0):
        		alal=text.description
        		count=1

        	vertices = (['({},{})'.format(vertex.x, vertex.y)
        		for vertex in text.bounding_poly.vertices])

        if(alal!="empty"):
        	searchNow(alal)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())
