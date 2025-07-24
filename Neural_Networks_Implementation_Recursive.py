# Implementation without Bias
import numpy as np;
import pandas as pd;
#import ndarray as nd;
import matplotlib.pyplot as plt;
# Single Layer Convolutionary Neural Networks Solution and the Model Impact
# The Linear Nature of the NN can be observed through plots using matplotlib
class Neural_Network_Implementation:
   def NN_Implementation(self, X,W,A,i,j,k):
      if(i < len(X)):
         if(j < len(X[i]) & i == 0 & X[i][j] == 1):
            A.append(X[i][j]* W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k);
         elif(j < len(X[i]) & i == 1 & X[i][j] == 1):
            A.append(X[i][j] * W[k+1]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k);
            
         elif(j < len(X[i]) & i == 2 & X[i][j] == 1):         
            A.append(X[i][j]*W[k+2]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k);
         elif(j < len(X[i]) & i == 3 & X[i][j]==1): 
            A.append(X[i][j]*W[k+2]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k); 
         elif(j < len(X[i]) & i == 4 & X[i][j] == 1):
            A.append(X[i][j]*W[k+2]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k);               
         elif(j < len(X[i]) & i == 5 & X[i][j] == 1):
            A.append(X[i][j]*W[k+3]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k);
         elif(j < len(X[i]) & i == 6 & X[i][j]==1):
            A.append(X[i][j]*W[k+3]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k);
         elif(j < len(X[i]) & i == 7 & X[i][j]==1):
            A.append(X[i][j]*W[k+3]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k); 
         elif(j < len(X[i]) & i == 8 & X[i][j]==1):
            A.append(X[i][j]*W[k+3]);
            i = i+1;
            j = j+1;
            NN_Implementation(X[i:],W,i,j,k);         
      else:
         return(A);
      return(A);
   
   # Plotting the Neural Network output from the Input features vector X and Weights associated to each of the input features.
   def Plot_NN_Output(self,X):
      np.random.seed(len(X));
      l = len(X); 
      X = X[:];
      Y = np.random.rand(len(X));
      
      area = (len(X)*len(X))**2;
      colors = np.random.rand(l);

      plt.scatter(X,Y,s=area,c=colors,alpha=0.5);
      plt.show();
      return(0);

   # Introducing Fully Convolutional Network solution using Hidden Layer concepts.(Non-linearity check for using Non-linear functions in the Activation functions of Hidden layers.)
'''   def MultiLayer_NN_Implementation(self, A,W,A,i,j,k):
      return(0);
   def NN_Implementation_Hidden_Layer(self, A,W,i,j,k):
      if(i < len(A)):
         if(j < len(A[i]) & i == 0 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);  
         elif(j < len(A[i]) & i == 1 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         elif(j < len(A[i]) & i == 2 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         elif(j < len(A[i]) & i == 3 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         elif(j < len(A[i]) & i == 4 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         elif(j < len(A[i]) & i == 5 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         elif(j < len(A[i]) & i == 6 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         elif(j < len(A[i]) & i == 7 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         elif(j < len(A[i]) & i == 8 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         elif(j < len(A[i]) & i == 9 & A[i][j] == 1):
            H.append(A[i][j]*W[k]);
            i = i+1;
            j = j+1;
            NN_Implementation_Hidden_Layer(A[i:],W,i,j,k);
         esle:
            return(H);
      else:
         return(H);
      return(H);
'''
X1_18_29 = [0,1,0];
X1_30_50 = [0,0,1];
X1_AB_50 = [1,0,0];
X2_income_lessthan_100k = [0,1,0];
X2_income_100k_300k = [1,0,0];
X2_income_AB_300k = [0,0,1];
X3_Male = [1,0,0];
X3_Female = [0,1,1];
X4_Married = [1,0,1];
Input_Features = [X1_18_29,X1_30_50, X1_AB_50,X2_income_lessthan_100k,X2_income_100k_300k, X2_income_AB_300k,X3_Male,X3_Female, X4_Married];
#W = [0.6,0.7,0.75,0.8,0.99,0.1];
W = [1,2,2,1];
i = 0;
j = 0;
k = 0;
A = [];
NN_Imp = Neural_Network_Implementation();
results = NN_Imp.NN_Implementation(Input_Features,W,A,i,j,k);
print(results)
NN_Imp.Plot_NN_Output(results);
