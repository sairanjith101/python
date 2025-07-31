#Initialize matrix a  
a = [    
        [1, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ];  
   
#Calculates number of rows and columns present in given matrix  
cols = len(a[0]);  
 
   
#Calculates sum of each column of given matrix  
for i in range(0, cols):  
    sumCol = 0;  
    for j in range(0, cols):  
        sumCol = sumCol + a[j][i];  
    print("Sum of " + str(i+1) + " column: " + str(sumCol));

##########################################################################

#Initialize matrix a  
a = [    
        [1, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ];  
   
#Calculates number of rows and columns present in given matrix  
cols = len(a[0]);  
 
   
#Calculates sum of each column of given matrix  
for i in range(0, cols):  
    sumCol = 0;  
    for j in range(0, cols):  
        sumCol = sumCol * a[j][i];  
    print("Sum of " + str(i+1) + " column: " + str(sumCol));