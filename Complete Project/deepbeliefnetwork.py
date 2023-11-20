import numpy as np
import math
import random
from sklearn.preprocessing import MinMaxScaler


weights = np.random.rand(40) 
#print(weights)


w1=random.choice(weights)
w2=random.choice(weights)
w3=random.choice(weights)
w4=random.choice(weights)
w5=random.choice(weights)
w6=random.choice(weights)
w7=random.choice(weights)
w8=random.choice(weights)
w9=random.choice(weights)
w10=random.choice(weights)
w11=random.choice(weights)
w12=random.choice(weights)
w13=random.choice(weights)
w14=random.choice(weights)
w15=random.choice(weights)
w16=random.choice(weights)
w17=random.choice(weights)
w18=random.choice(weights)
w19=random.choice(weights)
w20=random.choice(weights)
w21=random.choice(weights)
w22=random.choice(weights)
w23=random.choice(weights)
w24=random.choice(weights)
w25=random.choice(weights)
w26=random.choice(weights)
w27=random.choice(weights)
w28=random.choice(weights)
w29=random.choice(weights)
w30=random.choice(weights)
w31=random.choice(weights)
w32=random.choice(weights)
w33=random.choice(weights)
w34=random.choice(weights)
w35=random.choice(weights)
w36=random.choice(weights)
w37=random.choice(weights)
w38=random.choice(weights)
w39=random.choice(weights)
w40=random.choice(weights)
w41=random.choice(weights)
w42=random.choice(weights)
w43=random.choice(weights)
w44=random.choice(weights)
w45=random.choice(weights)
w46=random.choice(weights)
w47=random.choice(weights)
w48=random.choice(weights)
w49=random.choice(weights)
w50=random.choice(weights)
w51=random.choice(weights)
w52=random.choice(weights)
w53=random.choice(weights)
w54=random.choice(weights)
w55=random.choice(weights)
w56=random.choice(weights)


bias = 1



def sigmoid_derivative(x):
    sigmoid= 1 / (1 + math.exp(-x)) 
    return sigmoid
    
   
    
def getContrastiveDivergence(hiddenoutput1,hiddenoutput2,hiddenoutput3,hiddenoutput4,hiddenoutput5,hiddenoutput6,hiddenoutput7):
    
    outputlayer1=hiddenoutput1*w50+hiddenoutput2*w51 +hiddenoutput3*w52+hiddenoutput4*w53+hiddenoutput5*w54 +hiddenoutput6*w55+hiddenoutput7*w56 
    
    dbnprobability=sigmoid_derivative(outputlayer1)
    #print(dbnprobability)
    
    return dbnprobability
    
    
def getRBN(input1,input2,input3,input4,input5,input6,input7):
    
    ############# Linear Summation of Input#################################
    hiddenlayer1=input1*w1+input2*w2 +input3*w3+input4*w4+input5*w5 +input6*w6+input7*w7+bias  
    hiddenlayer2=input1*w8+input2*w9 +input3*w10+input4*w11+input5*w12 +input6*w13+input7*w14+bias  
    hiddenlayer3=input1*w15+input2*w16 +input3*w17+input4*w18+input5*w19 +input6*w20+input7*w21+bias
    hiddenlayer4=input1*w22+input2*w23 +input3*w24+input4*w25+input5*w26 +input6*w27+input7*w28+bias  
    hiddenlayer5=input1*w29+input2*w30 +input3*w31+input4*w32+input5*w33 +input6*w34+input7*w35+bias  
    hiddenlayer6=input1*w36+input2*w37 +input3*w38+input4*w39+input5*w40 +input6*w41+input7*w42+bias  
    hiddenlayer7=input1*w43+input2*w44 +input3*w45+input4*w46+input5*w47 +input6*w48+input7*w49+bias  
    
    #print("Hidden Layer 1: ",hiddenlayer1)
    
    ###########Activation Function introduce non linearity into the output#####   
    hiddenoutput1=sigmoid_derivative(hiddenlayer1)
    hiddenoutput2=sigmoid_derivative(hiddenlayer2)
    hiddenoutput3=sigmoid_derivative(hiddenlayer3)
    hiddenoutput4=sigmoid_derivative(hiddenlayer4)
    hiddenoutput5=sigmoid_derivative(hiddenlayer4)
    hiddenoutput6=sigmoid_derivative(hiddenlayer6)
    hiddenoutput7=sigmoid_derivative(hiddenlayer7)
   
    
    # print("Hidden 1: ",hiddenoutput1)
    # print("Hidden 2: ",hiddenoutput2)
    # print("Hidden 3: ",hiddenoutput3)
    dbnprobability=getContrastiveDivergence(hiddenoutput1,hiddenoutput2,hiddenoutput3,hiddenoutput4,hiddenoutput5,hiddenoutput6,hiddenoutput7)
    
    return dbnprobability

def sort(dbnprobabilitylist,index):
    dbnprobabilitylist.sort(key = lambda x: x[index],reverse=True) 
    return dbnprobabilitylist 

def DBNInit(dbninputlist):
    
    dbnprobabilityvalues=[]
    for row in dbninputlist:
        input1=row[0]
        input2=row[1]
        input3=row[2]
        input4=row[3]
        input5=row[4]
        input6=row[5]
        input7=row[6]
       
        dbnprobability=getRBN(input1,input2,input3,input4,input5, input6, input7) 
        dbnprobability=round(dbnprobability,5)
        dbnprobabilityvalues.append(dbnprobability)
               
    return dbnprobabilityvalues
        
        
        
        
