from math import sqrt
from typing import List
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
from random import sample
import array as arr

from pandas.core.indexes.base import Index;
Data=pd.read_csv("pokemon_data.csv")

def Draw (Chart,Att):
    plt.figure()
    if(Chart=="X"):
        if(Att=="A"):
            Data["Attack"].plot(kind="box")
        elif(Att=="D"):
            Data["Defense"].plot(kind="box")
        elif(Att=="S"):   
            Data["Speed"].plot(kind="box")
    elif(Chart=="H"):
        if(Att=="A"):
            Data["Attack"].plot(kind="hist")
            plt.axvline(Data["Attack"].mean(), color='k', linestyle='dashed', linewidth=1)
        elif(Att=="D"):
            Data["Defense"].plot(kind="hist")
            plt.axvline(Data["Defense"].mean(), color='k', linestyle='dashed', linewidth=1)
        elif(Att=="S"):   
            Data["Speed"].plot(kind="hist")
            plt.axvline(Data["Speed"].mean(), color='k', linestyle='dashed', linewidth=1)

    else:
        print("Enter a Valid Character: ")  
       

def ShowTypeDiff():
    Data.groupby("Type 1")["HP","Attack","Defense","Speed"].mean().plot(kind="bar")
    plt.title("Mean for Every Atribute in Every Type")

def ShowGenDiff():
    Data.groupby("Generation")["HP","Attack","Defense","Speed"].mean().plot(kind="bar")
    plt.title("Mean For Every Generation")


def ShowPieChart():
    plt.figure()
    plt.pie(no_of_Type,labels=("Water","Normal","Bug","Grass","Other"),autopct='%1.1f%%')

def ShowScatter(Att,Val):
    #x=Data["HP"].sample(99)
    #y=Data["HP"].sample(99)
    x=Data["Attack"].loc[0:98]
    y=Data["HP"].loc[0:98]
    R=np.corrcoef(x,y)
    print(R)
    B1=R[0,1]*(x.std()/y.std())
    B2=y.median()-B1*x.median()
    B1="%.3f" % B1
    B2="%.3f" % B2
    if(Att.upper()=="HP"):
        y1=float(Val)
        BC1=float(B1)
        BC2=float(B2)
        x1=(y1-BC2)/BC1
        print("Monster's Attack = ")
        print(x1)
    elif (Att.upper()=="Atk"):
        BC1=float(B1)
        BC2=float(B2)
        x1=Val
        y1=B1*x1+B2
        print("Monster's HP= ")
        print("y1")

    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
    plt.title("Y="+str(B1)+"X"+"+"+str(B2)+"------ Scatter Between HP & Atk")
    plt.scatter(x,y)

def App():
    C=input("Do you Wanna Make An Estimation? Y:Yes , N:No : ")
    est_Att="X"
    est_Val="Y"
    if(C.upper()=="Y"):
        est_Att=input("Enter the known Attribute (HP , Atk): ")
        est_Val=input("Enter the Value: ")
        (ShowScatter(est_Att,est_Val))
    else:
        ShowScatter(est_Att,est_Val)
    B=input("Draw One Dimensional Chart? Y:Yes N:No : ")
    if(B.upper()=="Y"):
        In=input("Please Enter Chart Type (X:Box,H:Hist): ")
        N=input("Please Enter Attribute (A:ATk,D:Def,S:Speed): ")
        Draw(In,N)
    Pie=input("Show Pie Chart? Y:Yes N:No : ")
    type_mean=input("Show Mean For Every Type? Y:Yes N:NO : ")
    gen_mean=input("Show Mean For Every Generation? Y:Yes N:No : ")
    if(Pie.upper()=="Y"):
        ShowPieChart()
    if(type_mean.upper()=="Y"):
        ShowTypeDiff()
    if(gen_mean.upper()=="Y"):
        ShowGenDiff()

def hist_of_means():
    Listp=[]
    Sum=0
    for x in range(1000):
        Sample=Data["Attack"].sample(50)
        Listp.append(Sample.mean())
    plt.hist(Listp,density=1, bins=20)
    plt.axvline(np.mean(Listp), color='k', linestyle='dashed', linewidth=1)

    plt.axis([50,120,0,0.2])

def MeanOfSamples():
    
    Sample=Data["Attack"].sample(50)
    SE=np.std(Sample)/sqrt(50)
    PopMeanMin=Sample.mean()-SE*2.12
    PopMeanMax=Sample.mean()+SE*2.12
    print("Population Mean is Between : "+ str(PopMeanMin)+" , "+str(PopMeanMax))
    
def outliers_detect():
    Z_Threshold=3
    Outliers=Data.loc[113]
    for i in range (len(Data)):
        ZScore=(Data["Attack"].loc[i]-Data["Attack"].mean())/Data["Attack"].std()
        if (abs(ZScore)>Z_Threshold):
            Outliers=Outliers.append(Data.loc[i])
    print(Outliers["Name"]+":")

def Numeric(Att):
    Data["Attack"].describe()
    Data["Defense"].describe()
    Data["Speed"].describe()



    




WaterD=Data.loc[Data['Type 1']=="Water"]
NormalD=Data.loc[Data['Type 1']=="Normal"]
GrassD=Data.loc[Data['Type 1']=="Grass"]
BugD=Data.loc[Data["Type 1"]=="Bug"]
Other=len(Data)-(len(NormalD)+len(WaterD)+len(GrassD)+len(BugD))
no_of_Type=[len(WaterD),len(NormalD),len(BugD),len(GrassD),Other]
#print(Data.groupby("Type 1")["HP","Attack","Defense","Speed"].mean())
#print(Data.groupby("Type 1")["HP","Attack","Defense","Speed"].var())

#ShowPieChart()
#ShowTypeDiff()
#Att1=input("Type X Axis ")
#Att2=input("Type Y Axis")
#MeanOfSamples()
#Att_s=input("Enter the Attribute You Want to describe: ")
#Numeric(Att_s)
#ShowScatter("X","Y")
outliers_detect()
plt.show()