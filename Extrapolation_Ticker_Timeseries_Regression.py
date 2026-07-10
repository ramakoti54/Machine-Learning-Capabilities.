import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import math;


class Extrapolation_Ticker_Timeseries_Regression:
   def Extrapolate_Ticker_Timeseries_Regression(self,current_value,custom_timeperiod,qtr1_data,qtr2_data,qtr3_data,qtr4_data,Extrapolation_Qtr_Data,Extrapolation_Mon_Data,Extrapolation_Daily_Data):
      for i in range(len(current_value)):
         if(i < len(current_value)  and custom_timeperiod == 2):
            Extrapolation_Qtr_Data.append(float(current_value[i]-(1.132*(2*custom_timeperiod))-(27.268*qtr2_data)-(16.336*qtr3_data)+(92.882*qtr4_data)));
         elif(i < len(current_value)  and custom_timeperiod == 8):
            Extrapolation_Mon_Data.append(float(current_value[i]-(1.132*(2*custom_timeperiod))-(27.268*qtr2_data)-(16.336*qtr3_data)+(92.882*qtr4_data)));
         elif(i < len(current_value)  and custom_timeperiod == 0):
            Extrapolation_Daily_Data.append(float(current_value[i]-(1.132*(365/(31+30+31))-(27.268*qtr2_data)-(16.336*qtr3_data)+(92.882*qtr4_data))));   
         elif(i == int(len(current_value))):
            return([Extrapolation_Qtr_Data,Extrapolation_Mon_Data,Extrapolation_Daily_Data]); 
      return([Extrapolation_Qtr_Data,Extrapolation_Mon_Data,Extrapolation_Daily_Data]);
   
   def __init__(self):
      custom_timeperiod = int(input("Enter the numeric value of timeperiod to compute Trend based evenly quantified constant"));
      qtr1_data = int(input("Enter binary input value as either 0 or 1 for qtr1 to represent the ticker price existence over the given time range"));
      qtr2_data = int(input("Enter binary input value as either 0 or 1 for qtr2 to represent the ticker price existence over the given time range"));
      qtr3_data = int(input("Enter binary input value as either 0 or 1 for qtr3 to represent the ticker price existence over the given time range"));
      qtr4_data = int(input("Enter binary input value as either 0 or 1 for qtr4 to represent the ticker price existence over the given time range"));
      Extrapolation_Data = [];
      Price = [];
      Data_file = pd.read_csv("/content/Stocks_File/JPM.csv",delimiter=',');
      Price = Data_file['Open']+Data_file['High']+Data_file['Low']+Data_file['Close']/4;
      print(Price[10000:]);
      current_value = [];
      current_value = list(Price[10000:]);
      Extrapolation_Qtr_Data = [];
      Extrapolation_Mon_Data = [];
      Extrapolation_Daily_Data = [];

      Extrapolation_Qtr_Data = self.Extrapolate_Ticker_Timeseries_Regression(list(current_value),custom_timeperiod,qtr1_data,qtr2_data,qtr3_data,qtr4_data,Extrapolation_Qtr_Data,Extrapolation_Mon_Data,Extrapolation_Daily_Data)[0];
      Extrapolation_Mon_Data = self.Extrapolate_Ticker_Timeseries_Regression(list(current_value),custom_timeperiod,qtr1_data,qtr2_data,qtr3_data,qtr4_data,Extrapolation_Qtr_Data,Extrapolation_Mon_Data,Extrapolation_Daily_Data)[1];
      Extrapolation_Daily_Data = self.Extrapolate_Ticker_Timeseries_Regression(list(current_value),custom_timeperiod,qtr1_data,qtr2_data,qtr3_data,qtr4_data,Extrapolation_Qtr_Data,Extrapolation_Mon_Data,Extrapolation_Daily_Data)[2];
      print(Extrapolation_Qtr_Data);
      print("\n\n",Extrapolation_Mon_Data);
      print("\n\n",Extrapolation_Daily_Data);
      return(None);

extrapolate_ticker_price = Extrapolation_Ticker_Timeseries_Regression();
