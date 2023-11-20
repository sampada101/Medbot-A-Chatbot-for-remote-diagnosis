import pandas as pd
import math
import warnings
from IPython import get_ipython
import matplotlib.pyplot as plt
from knn import *
from linearregression import *
from deepbeliefnetwork import *
from sklearn.preprocessing import MinMaxScaler
from decisiontree import *
warnings.filterwarnings('ignore')


def getheartDiseaseResult(userinfo):
    #=======================Code To Clear Console===================================
    get_ipython().magic('clear')

# User Attributes Input Value

# chest pain as cp
# resting blood pressure trestbps
# serum cholestoral as chol
# fasting blood sugar as fbs
# resting electrocardiographic as restecg
# maximum heart rate as thalach


    age=int(userinfo[0])
    cp=int(userinfo[1])
    trestbps=int(userinfo[2])
    chol=int(userinfo[3])
    fbs=int(userinfo[4])
    restecg=int(userinfo[5])
    thalach=int(userinfo[6])

    #=======================Code To Read Dataset====================================
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 700)

    dataset = pd.read_csv("heart.csv")
    # dataset.hist(figsize=(10,10))
    # fig = plt.figure(1)
    # fig.canvas.set_window_title('Original Dataset')
    # plt.show()

    print("\n")
    print("************************Dataset Description***************************")
    print("\n")
    print(dataset.describe())



    print("\n")
    print("****************************Raw Dataset*******************************")
    print("\n")
    database_list = []
    database_list=dataset.values.tolist()
    print(database_list)


    #=======================Code To Preprocess Dataset====================================
    prepro_list=[]

    for record in database_list: 
        val1=record[0]
        val2=record[2]
        val3=record[3]
        val4=record[4]
        val5=record[5]
        val6=record[6]
        val7=record[7]
        temp=[val1,val2,val3,val4,val5,val6,val7]
        prepro_list.append(temp)
    

    print("\n")
    print("****************************Preprocess Dataset************************")
    print("\n")
    print(prepro_list )
    

    #=======================Code For KNN Clustering============================

    userdata=[age,cp,trestbps,chol,fbs,restecg,thalach]
    knnclusters= knnInit(prepro_list,userdata)
   

    print("\n")
    print("****************************Print KNN Clusters are**************************")
    print("\n")
    i=1     
    for row in knnclusters:   
        print("\n")
        print("KNN Cluster No:",i)
        print("\n")
    
        for record in row:
            print(record)
            i+=1
 

    #####################Code for Linear Regression##############################

    y=[age,cp,trestbps,chol,fbs,restecg,thalach]
    innerlayer=knnclusters[0]  
    linearcluster=[]

    for i in range(len(innerlayer)):
        x=innerlayer[i]
        del x[len(x)-1]
        interceptval=initRegression(x, y)
        #print("interceptvalue: ",interceptval)
        x.insert(len(x),interceptval)
        linearcluster.append(x)
    
    def sort(datalist, index):
        datalist.sort(key = lambda x: x[index],reverse=True) 
        return datalist 

    linearcluster=sort(linearcluster,7)    
    print("\n")
    print("****************************Linear Regression Values**************************")
    print("\n")
    
    for row in linearcluster:
        print(row)
        
    #####################Code for DBN ###############################################
    
    dbninputlist=[]    
    
    size=len(linearcluster)
    index=int (size*80/100)
    
    for i in range(index):
        row=linearcluster[i]
        del row[len(row)-1]
        dbninputlist.append(row)
        
    print("\n")
    print("****************************DBN Input List**************************")
    print("\n")
    
    for row in dbninputlist:
        print(row)   
        
    length=len(dbninputlist)
    #print(length)
    
    scaler = MinMaxScaler()
    scalerdbninputlist=scaler.fit_transform(dbninputlist)
    
    # for row in scalerdbninputlist:
    #     print(row)    
    
    dbnprobabilityvalues=DBNInit(scalerdbninputlist)    
    
    dbnprobabilitylist=[]  
    i=0
    for row in dbninputlist:
        value=dbnprobabilityvalues[i]
        row.insert(len(row),value)
        dbnprobabilitylist.append(row)
        i+=1  
    
    print("\n")
    print("**************************DBN Probability List*****************************")
    print("\n")  
    
    dbnprobabilitylist=sort(dbnprobabilitylist,7)
    for row in dbnprobabilitylist:
          print(row)
          
    ######################Code for Decision Tree###################################  
    dtlist=[]
    size1=len(dbnprobabilitylist)
    index1=int (size1*50/100)
    
    for i in range(index1):
        row=dbnprobabilitylist[i]
        del row[len(row)-1]
        dtlist.append(row)  
    
    print("\n")
    print("********************Decision Tree Result***********************")
    print("\n") 
    
    
    # for row in dtlist:
    #     print(row)    
        
    
    dtresult=decisionTreeInit(dtlist)
    print(dtresult)
    return dtresult.title()