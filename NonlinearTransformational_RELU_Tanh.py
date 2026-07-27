import numpy as np;
import pandas as pd;
import math;
import matplotlib.pyplot as plt;
#import API_Data_File_Loader as API_DAT_LOAD;

class NonlinearTransformational_RELU_Tanh:
   
   def model(self,Avg_Price,Weights,Result):
      '''for i in range(len(Avg_Price)):
         if(i < len(Avg_Price)):
            #Avg_Price = (Avg_Price[i]*Weights[i+1])-Prediction_Values[i];'''
      Result = Weights[0]+ np.dot(np.transpose(Avg_Price),Weights[1:]);
      print("Results of  model for dot product is: ",Result,"\n\n");
      return(Result);

   def NonlinearTransformational_Tanh(self,Avg_Price,Weights,Result):      
      Result = np.tanh(self.model(Avg_Price,Weights,Result)%360);
      print("Tanh Results are:",Result);
      return(Result);

   def NonlinearTransformational_RELU(self,Avg_Price,Weights,Result):     
      Result = (1/(1+np.exp(-1*(self.NonlinearTransformational_Tanh(Avg_Price,Weights,Result)))));
      return(Result);

   '''def Entropy_Calculation(self,RELU_Results,Original_Values,Entropy):
      for i in range(len(RELU_Results)):
         if ( i < len(RELU_Results) and i != 0):
            Entropy.append(RELU_Results[i]-Original_Values[i]);
         else:
            return(Entropy); 
      return(Entropy);   '''

   def Predict_Stock_Price(self,RELU_Results,Original_Values,Prediction_Values):
      for i in range(len(Original_Values)):
         #print(i);
         #print("\n\n --------- Originalvalues are: ",Original_Values[i]*RELU_Results);
         Prediction_Values.append((RELU_Results * Original_Values[i]));
      return(Prediction_Values);

   def Entropy_Calculation(self,Original_Values,Prediction_Values,Entropy):
      print("Lengths are: ",len(Prediction_Values),len(Original_Values));
      for i in range(len(Original_Values)):         
         Entropy.append(Original_Values[i] - Prediction_Values[i]);  
      return(Entropy);      
   
   def exponential_plot(self,Entropy,Date):
      X =  [];
      Y = [];
      X = Entropy
      Y = Date
      fig, ax = plt.subplots()

      ax.plot(Y,X);
      ax.set_xlabel('Date')
      ax.set_ylabel('RELU Activation Entropy for Nonlinear Transformations');

      #plt.xticks(np.arange(0, 98, 1), [1960, 1962, 1964, 1966, 1968, 1970, 1972,  1974, 1976, 1978, 1980]);
      fig.autofmt_xdate()
      plt.tight_layout()
      return(None);

   def __init__(self):
      #Avg_Price = [];
      #Open_Price = [];
      #Ticker_Date = []; 
      #Avg_Price = API_DAT_LOAD.API_Data_File_Loader().Avg_Price[:];
      #print(Avg_Price)
      Stock_Data = pd.read_csv('/content/sample_data/JPM.csv',delimiter=',');
      Open_Ticker_Value = [];
      Close_Ticker_Value = [];
      High_Ticker_Value = [];
      Low_Ticker_Value = [];
      Avg_Price = [];
      Open_Ticker_Value = Stock_Data['Open'];
      Close_Ticker_Value = Stock_Data['Close'];
      High_Ticker_Value = Stock_Data['High'];
      Low_Ticker_Value = Stock_Data['Low'];
      Date_Ticker_Value = Stock_Data['Date'];
      Avg_Price = (Open_Ticker_Value+Close_Ticker_Value+High_Ticker_Value+Low_Ticker_Value)/4.0;
      Avg_Price = Avg_Price[10000:]
      Original_Values = [];
      Original_Values = list(Avg_Price);#[10086:];
      Weights = [];
      Tanh_Results = [];
      
      for i in range(len(Avg_Price)):
         if(i < len(Avg_Price) and i%2 == 0):
            Weights.append(1);
         elif(i < len(Avg_Price) and i%2 != 0):
            Weights.append(0.8);  
    
      print(len(Weights),len(Avg_Price));            
      Weights.append(1);
      #Weights = np.transpose(Weights);
      print(Weights,"\n\n",Avg_Price)
      '''if(int(len(Weights)) == int(len(Avg_Price[10000:]))):
         print("Lenghts of input vector and associated weights match");
         print(Avg_Price);
         Weights.append(1);'''
      Result = [];    
      #Tanh_Results = self.NonlinearTransformational_Tanh(Avg_Price,Weights,Result);
      #print("\n\n ====================\nTanh Functional Results are:",Tanh_Results);      
      RELU_Results = 0.0;
      RELU_Results = self.NonlinearTransformational_RELU(Avg_Price,Weights,Result);
      print("\n\n ====================RELU Results are: \n",RELU_Results);
      Entropy = [];
      #Original_Values = Avg_Price[10055:];
      Prediction_Values = [];
      
      '''for i in range(len(Original_Values)):
         Prediction_Values.append(Original_Values[i]* RELU_Results);'''
      
      #print("\n\n Prediction values are: \n",Prediction_Values,Original_Values)
      Prediction_Values = self.Predict_Stock_Price(RELU_Results,Original_Values,Prediction_Values);
      print("\n\n==================Prediction values are: \n",Prediction_Values);
      Entropy = self.Entropy_Calculation(Prediction_Values,Original_Values,Entropy);
      #print("\n\n==================Entropy values are: \n",Entropy);
      maximum_Entropy = 0.0;
      maximum_Entropy = np.max(Entropy);
      print(Entropy,"\n\n Argmax value of Entropy for RELU Activation function is:\n",maximum_Entropy,"\n\n",len(Entropy));
      self.exponential_plot(Entropy,Date_Ticker_Value[10000:]);
      return(None);
Nonlinear_RELU_Tanh = NonlinearTransformational_RELU_Tanh();
