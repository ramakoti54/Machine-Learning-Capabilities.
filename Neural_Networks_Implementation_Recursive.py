# Implementation without Bias
import numpy as np;
import pandas as pd;
import ndarray as nd;
import pyplot as plt;

class Neural_Network_Implementation:
   def NN_Implementation(X,W,i,j,k):
      if(X[0][j] == 1 & i < len(X) & j < len(X[i])):
         if(i == 0 & X[i][j] == 1 & X[4][j]==1):
            Probability = Probability.append(X[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k);
         elif(i == 0 & X[i][j] == 1 & X[5][j]==1):
            Probability = Probability.append(X[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:]W,i,j,k);
      elif((X[1][j] == 1 | X[2][j] == 1) & i < len(X) & j < len(X[i])):         
         if(X[5][j] == 1):
            Probability = Probability.append(X[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:]W,i,j,k);
         elif(X[6][j]==1 & (X[4][j] == 1 | X[5][j])): 
            Probability = Probability.append(X[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:]W,i,j,k); 
         elif(X[7][j]==1 & (X[5][j] == 1) & X[8][j] == 0):
            Probability = Probability.append(X[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:]W,i,j,k);               
         elif(X[8][j] == 1 & X[5][j]==1):
            Probability = Probability.append(X[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:]W,i,j,k);
         else:
            return(Probability); 
      else:
         if(X[2][j]==1):
            Probability = Probability.append(X[2][j]*W[k]);
            j = j+1;
            k = k+1;
            NN_Implementation(X[i:],W,i,j,k);
         elif(X[5][j] == 1):
            Probability = Probability.append(X[2][j]*W[k]);
            j = j+1;
            k = k+1;
            NN_Implementation(X[i:],W,i,j,k);      
         else:
            return(Probability);
      return(Probability);


X1_18_29 = [0,1,0];
X1_30_50 = [0,0,1];
X1_AB_50 = [0,0,1];

X2_income_lessthan_100k = [0,1,0];
X2_income_100k_300k = [1,0,0];
X2_income_AB_300k = [0,0,1];
X3_Male = [1,0,0];
X3_Female = [0,1,1];
X4_Married = [1,0,1];
Input_Features = [X1_18_29,X1_30_50, X1_AB_50,X2_income_lessthan_100k,X2_income_100k_300k, X2_income_AB_100k,X3_Male,X3_Female, X4_Married];
W_1 = [2,2,2]; W_2 = [2,2];
W = W_1 + W_2;
i = 0;
j = 0;
k = 0;

results = NN_Implementation(Input_Features,W,i,j,k);
