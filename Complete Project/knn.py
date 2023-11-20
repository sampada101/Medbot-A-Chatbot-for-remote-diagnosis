import math

#===========================Code to find eucledian distance====================
def euclidean_distance(row1, row2):
    distance=0.0
    for i in range(len(row1)-1):
        distance += math.pow(row1[i]-row2[i],2)
        
    return math.sqrt(distance)  

#===========================Code to sort Knn_list+++===========================

def sort(knn_list, index):

    knn_list.sort(key = lambda x: x[index]) 
    return knn_list     


def getKNNClusters(knn_list,k):
    knnclusters=[]
    innerlayer=[]
    outerlayer=[]
    x=1
    for row in knn_list:
        value=row[len(row)-1]
        if(x<=k):
            innerlayer.append(row)
            x=x+1
        else:
            outerlayer.append(row)
            x=x+1
    
    knnclusters.append(innerlayer)
    knnclusters.append(outerlayer)
    
    return knnclusters
    
def knnInit(dataset, userdata):
    
    knn_list=[] 
    index=0
    distance=0.0
    for row in dataset:
        distance=euclidean_distance(userdata,row)
        distance=round(distance,2)
        row.insert(len(row),distance)
        knn_list.append(row)
        index=len(row)-1
        
        
    knn_list=sort(knn_list,index)
    k=20
    knnclusters=getKNNClusters(knn_list,20)
    
    return knnclusters
    