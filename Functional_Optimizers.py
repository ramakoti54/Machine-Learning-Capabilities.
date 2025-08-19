import numpy as np;
import pandas as pd;
import tensorflow as tf;
import matplotlib.pyplot as plt;
import math;
#import mlrefinedlibraries
# *********. Taylor Series First Order Optimizer ********** #
# *********. The Optimizer works to identify the number of degrees from the polynomial equation and sends it an input to the Taylor Series First Order Optimizer *********#
# *********. The Optimizer looks for the feature vector(C), Weights(W) and degree of the polynomial to compute Taylor_Series_Result vector with result *********#
# *********.  (W[0]-(W_i /(n*C_i))) ************# 
class Functional_Optimizers:
      
   def Taylor_Series_Optimizer(self,C,W,i,j,n,Taylor_Series_Result):
      #for i in range(C.size[0]):
      #print("Degree:",n);
      if(i < len(C) & len(C) != 0):
         print("Degree of the feature vector is:",n);
         if(j < len(C[i])):
            #print("Degree is:",n)
            #print((W[0])- (W[j]) / (n * (C[i][j])));
            #Taylor_Series_Result.append((W[0])-(W[j] / (n * (C[i][j]))));
            magnitude = math.sqrt(C[i][j]**2+C[i][j+1]**2+C[i][j+2]**2+C[i][j+3]**2+C[i][j+4]**2+C[i][j+5]**2+C[i][j+6]**2);
            Taylor_Series_Result.append(np.sum(np.cos(C[i][j]/magnitude)));
            j = j+1;
            self.Taylor_Series_Optimizer(C[i][j:],W,i,j,n,Taylor_Series_Result);         
      #else:
      #   return(Taylor_Series_Result);      
      return(Taylor_Series_Result);

   def Taylor_First_Order_Optimizer(self,W,C,i,j,n,Taylor_First_Order_Optimizer_Result,Taylor_Series_Result):                
      if(i < int(len(C)) & j < int(len(C[i]))):
         #print("Degree is:",n);
         #if(C.len[i][j] == 2):                     
         Taylor_First_Order_Optimizer_Result.append(self.Taylor_Series_Optimizer(C[i][j:],W,i,j,n,Taylor_Series_Result));
         i = i+1;
         self.Taylor_First_Order_Optimizer(W,C[i][j:],i,j,n,Taylor_First_Order_Optimizer_Result,Taylor_Series_Result);
      elif(i == (len(C)-1)):
         if(j == len(C[i])):
            self.Taylor_First_Order_Optimizer_Result.append(self.Taylor_Series_Optimizer(C[i][j:],W,i,j,n,Taylor_Series_Result));
         else:
            return(0); 
      else:
         return(Taylor_First_Order_Optimizer_Result); 

Function_Optimizers = Functional_Optimizers();
C = [[1,2,3,4,5,6,7],
     [8,9,10,11,12,13,14],
     [15,16,17,18,19,20,21],
     [21,22,23,24,25,26,27,28]];     
W = [1,1,1,1,1,1,1,1];
Taylor_Series_Result = [];
i = 0;
j = 1;
degree = 7;
Taylor_First_Order_Optimizer_Result = [];
Taylor_First_Order_Optimizer = Function_Optimizers.Taylor_First_Order_Optimizer(W,C,i,j,degree,Taylor_First_Order_Optimizer_Result,Taylor_Series_Result);
print(Taylor_First_Order_Optimizer);
#print();
