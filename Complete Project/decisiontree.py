def decisionTreeInit(dtlist):
    
    
    rcount=0
    dbncount=len(dtlist)
 #   print('DBN probability count is ',dbncount)
    
    for row in dtlist:
        count=0
       
        trestbps=row[2]
        chol=row[3]
        thalach=row[6]
        
      #  print(trestbps)
       # print(chol)
       # print(thalach)
        
        
        if(trestbps>120):
            count=count+1
       
        if(chol>200):
            count=count+1
        
        if(thalach>120):
            count=count+1
       # print("count: ",count)
        if(count>2):
            rcount=rcount+1
      #  print("---------------------------------")
    
    
    
 #   print("Row Count: ",rcount)    
    percentage=(rcount*100)/dbncount
  #  print('Percentage of probability ',percentage)
    
    resultstr=""
    
    if(percentage>=0 and percentage<=50):
        resultstr="YOU ARE NOMRAL, NO NEED TO WORRY"
    elif(percentage>=51 and percentage<=75):
        resultstr="YOU HAVE TO CONTACT HEART SPECIALIST DOCTOR SOON"
    elif(percentage>=76 and percentage<=100):
        resultstr="YOU HAVE TO ADMIT SOON IN THE NEAREST HOSPITAL \n NEAREST HOSPITALS ARE \n 1.RUBY HALL CLINIC \n 2.OYESTER AND PEARL"
      
    
    return resultstr     

