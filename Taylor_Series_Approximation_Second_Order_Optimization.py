import tensorflow as tf;
#import tensorflow.keras as ks;
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import autograd as ad;
import tensorflow as tf;
from tensorflow import linalg as linalg;
import re;
#*********** Taylor Series Approximation with Single Variable Quadratic form *********
#*********** The form of the equation is g(v) = a+bv+cv^2 **********
#*********** The optimization method would help in optimizing the curvature behaviour *******
#*********** following minimum number of operations to be required for the model.    ********

class Taylor_Series_Approximation_Second_Order_Optimization:
   def Taylor_Series_Second_Order(self,C):
      #for i in range(len(C)):
      #   for j in range(len(C[i])):
      #      if(i < len(C[i]) & C[i] != 0):
      #         C[i][j].append(np.sub(C[i][j],np.dot(I[i][j]*l)));
      Eigen_Values = (linalg.eigh(C));
      return(Eigen_Values);

   def Optimization_Method(self,Eigen_Values,i):
      if(i < len(Eigen_Values) and Eigen_Values[i] != np.nan):
         if(Eigen_Values[i] > 0):
            print("The nature of the curve points at",{Eigen_Values[i]} , "towards upperside of the axis. The convex curve has a minimum value for the function at below mentioned point");
            i = i+1;
            self.Optimization_Method(self,Eigen_Values,i);
         elif(Eigen_Values[i] < 0):
            print("The nature of the curve points at",{Eigen_Values[i]},"towards downside of the axis. The concave curve has a minimum value for the function at below mentioned point");
            i = i+1;
            self.Optimization_Method(self,Eigen_Values,i);
         elif(Eigen_Values[i] == 0):
            print("The function is in neither convex nor concave It is at Inflection point");
            i = i+1;
            self.Optimization_Method(self,Eigen_Values,i);
         else:
            print("The function is both convex and concave");
            i = i+1;
            self.Optimization_Method(self,Eigen_Values,i);
      else:
         return(0);
      return(0);

   def Taylor_Series_Grad_Function(self,C,b,w,i,j,k):
      with tf.GradientTape() as g:
         g.watch(w)
         with tf.GradientTape() as g:
            g.watch(w)
            y = 5 + b*w + C * pow(w,2);
            dy_dw = g.gradient(y,w);
            d2y_dw2 = g.gradient(dy_dw,w);
      return(d2y_dw2);

   def Taylor_Series_Second_Order_Cost(self,C,b,w,i,j,k):
      '''for i in range(len(C)):
         for j in range(len(C[i])):
            if(i < len(C[i]) & C[i] != ''):
               Cost_Function = b[i]+tf.matmul(2*C[i][j]);'''
      Cost_Function = self.Taylor_Series_Grad_Function(C,b,w,i,j,k);
      return(Cost_Function);

#def Convergence_Criteria(self,)
C = tf.constant([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]]);
w = [1,1,2,1,1];
b = [1,2,3];
i = 0;
j = 0;
k = 0;
I = [[1,0,0],[0,1,0],[0,0,1]];
Eigen_Values = tf.constant([]);
Eigen_Vector = tf.constant([]);
Taylor_Series_Approx = Taylor_Series_Approximation_Second_Order_Optimization();
Eigen_Values = Taylor_Series_Approx.Taylor_Series_Second_Order(C)[0];
str_removed_values = str(Eigen_Values).lstrip("tf.Tensor([");
Eigen_Values = str_removed_values.rstrip("  ], shape=(3,), dtype=float32)");
Eigen_Values = [float(Eigen_Values[0:10]),float(Eigen_Values[11:20]),float(Eigen_Values[21:29])];
Eigen_Vector = Taylor_Series_Approx.Taylor_Series_Second_Order(C)[1];
string_replaced = str(Eigen_Vector).lstrip("tf.Tensor(");
Eigen_Vector = string_replaced.rstrip(", shape=(3, 3), dtype=float32)")
EigenVector = [];
EigenVector.append(float(Eigen_Vector[3:12]));
EigenVector = [[float(Eigen_Vector[3:14]),float(Eigen_Vector[15:26]),float(Eigen_Vector[26:38])],[float(Eigen_Vector[42:54]),float(Eigen_Vector[54:67]),float(Eigen_Vector[67:77])],[float(Eigen_Vector[81:92]),float(Eigen_Vector[93:103]),float(Eigen_Vector[104:116])]];
#print(Eigen_Values,EigenVector)
Taylor_Series_Approx.Optimization_Method(Eigen_Values,i);
Taylor_Series_Approx.Taylor_Series_Second_Order_Cost(EigenVector,w,i,j,k);
