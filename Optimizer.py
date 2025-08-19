import Functional_Optimizers as fun_opt;
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

class Optimizer:
   
   def optimizer(self.C,self.Taylor_Series_Result,self.i,self.j,self.degree,self.alpha,self.epochs,self.optimizer_function,self.w):
      if(self.alpha < 0 & self.epochs >0):
         self.optimizer_function = fun_opt.Taylor_Series_Optimizer(self.C,self.w,self.i,self.j,self.degree,self.Taylor_Series_Result);
         #cost_function_value = fun_opt.Taylor_Series_Optimizer
      else:
         print("Enter a valid step length and epoch value ")       
      return(self.optimizer_function);

   def __init__(self,alpha,epochs,optimizer_function):
      self.alpha = alpha;
      self.epochs = epochs;
      self.optimizer_function = optimizer_function;
      #self.w = w;
      self.optimizer_result = [];
      self.C = [[1,2,3,4,5,6,7],
           [8,9,10,11,12,13,14],
           [15,16,17,18,19,20,21],
           [21,22,23,24,25,26,27,28]];      
      self.W = [1,1,1,1,1,1,1,1];
      self.Taylor_Series_Result = [];
      self.i = 0;
      self.j = 1;
      self.degree = 7;      
      optimizer_result = self.optimizer(self.C,self.Taylor_Series_Result,self.i,self.j,self.degree,self.alpha,self.epochs,self.optimizer_function,self.W);      
      return(optimizer_result);
