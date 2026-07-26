import numpy as np;
import pandas as pd;
import stat;
import statistics;
import math;
import matplotlib.pyplot as plt;
#import SVM_Implementation;
from statsmodels.tsa.stattools import adfuller;
from typing import Union;
from tqdm import tqdm_notebook;
from statsmodels.tsa.statespace.sarimax import SARIMAX;
from statsmodels.tsa.arima_model import ARIMA;
from itertools import product;

class ARIMA_Stock_Price_Prediction:
   
   #def ARIMA_Stock_Price_Computation(self,endog: Union[pd.Series, list], order_list: list, d: int)-> pd.DataFrame:    
   def ARIMA_Stock_Price_Computation(self,endog,order_list,d):
      results = []; 
      #endog = pd.DataFrame(endog[:]);
      #order = [];                 
      #i = 0;
      #y_series = pd.Series(np.sin(np.linspace(0, 20, 36)) + np.random.normal(0, 0.2, 36), index=dates)
      #endog = y_series[:-6]
      #print("Order list values are: ",order_list[:]);                  
      for order in range(len(order_list)):#tqdm_notebook(order_list):
         #order.append(order);        
         #print("\n\n Order value is:\n",type(order));
         #if(i==0):
         #   order_previous = order;
         #   i = i+1;
         #   break;
         #elif(i == 1 or i ==2):
         order_previous = order;
         #print("Result DF is: ",endog[1]);
         try: 
            #model = self.Differencing(endog,order,order_previous,order_list);
            #model = SARIMAX(endog, order=(list(endog[1]),d,list(order_list)),simple_differencing=False).fit(disp=False);
            #model = optimize_ARIMA(endog, order_list, d);
            model = SARIMAX(endog,order=(1,d,1),simple_difference=False)
            model.fit(disp=False);
            print("Model values are: ",model);
         except:
            continue;            
            #results.append();
            aic = model.aic;
            print(aic);                             
            results.append([order, aic]);        
      result_df = pd.DataFrame(results)
      print("\n\n Results list: \n",result_df);               
      result_df.columns = ['(p,q)', 'AIC'];                
      #Sort in ascending order, lower AIC is better
      result_df = result_df.sort_values(by='AIC',ascending=True).reset_index(drop=True);    
      return result_df;
      #return();

   def exponential_plot(self,Avg_Price,Date):
      X =  [];
      Y = [];
      X = Avg_Price
      Y = Date
      fig, ax = plt.subplots()

      ax.plot(Y,X);
      ax.set_xlabel('Date')
      ax.set_ylabel('Stock Ticker value');

      #plt.xticks(np.arange(0, 98, 1), [1960, 1962, 1964, 1966, 1968, 1970, 1972,  1974, 1976, 1978, 1980]);
      fig.autofmt_xdate()
      plt.tight_layout()
      return(None);

   def ADF_Test(self,Avg_Price):
      ad_fuller_result = adfuller(Avg_Price);
      print(f'ADF Statistic: {ad_fuller_result[0]}')
      print(f'p-value: {ad_fuller_result[1]}')
      return(None);

   def __init__(self):
      Stock_Data = pd.read_csv('/content/Stock_Files/JPM.csv',delimiter=',');
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

      Median_Price = [];
      #Median_Price = SVM_Implementation.Median_Price(Avg_Price);
      print("Exponential plots Avg price is: ",Avg_Price[10000:]);
      #self.exponential_plot(Avg_Price[10000:],Date_Ticker_Value[10000:]);
      print("\n\n\n ================================================")
      Stationary_factor = 0;
      Stationary_factor = int(input("Enter an integer value to represent Order of Differenciation process"));

      if(Stationary_factor == 0):
         self.ADF_Test(Avg_Price);
         self.exponential_plot(Avg_Price[10000:],Date_Ticker_Value[10000:]);
      elif(Stationary_factor == 1):
         Avg_Price = np.diff(Avg_Price,n=1);
         #print("Avg Stationary Price values are: ",Avg_Price,len(Date_Ticker_Value[10000:]),"\n\n Length of Avg price Data smaple is:",len(Avg_Price));
         self.ADF_Test(Avg_Price);
         self.exponential_plot(Avg_Price[10000:],Date_Ticker_Value[10001:]);
      elif(Stationary_factor == 2):
         Avg_Price = np.diff(Avg_Price,n=2);
         self.ADF_Test(Avg_Price);
         self.exponential_plot(Avg_Price[10000:],Date_Ticker_Value[10001:]);
      else:
         return(None);
      #Avg_Price = Avg_Price[10000:];   
      Training_Sample = Avg_Price[10000:];
      #dates = Date_Ticker_Value[10000:];
      #y_series = pd.Series(np.sin(np.linspace(0, 20, 36)) + np.random.normal(0, 0.2, 36), index=dates)
      #Training_Sample = y_series[:-6];
      #Test_Sample = Avg_Price[10000:];
      ps = range(0, 1, 1);                
      qs = range(0, 1, 1);   
      Order_List = list(product((ps,qs)));  
      d = 1;
      endog = pd.DataFrame(Training_Sample[:]);
      self.ARIMA_Stock_Price_Computation(Training_Sample, Order_List,d);
      return(None);

ARIMA_Stock_Price_Predict = ARIMA_Stock_Price_Prediction();
