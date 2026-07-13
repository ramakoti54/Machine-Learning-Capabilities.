''' Libraries Imported for performing Stock ticker extrapolation process includes Numpy, Pandas, Matplotlib and math'''
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import math;

# Extrapolation of Tickers using Timeseries regression method computation runs through the class Extrapolate_Ticker_Timeseries_Regression.
class Extrapolation_Ticker_Timeseries_Regression:
# Method designed to extrapolate stock ticker prices with Timeseries Regression process and it uses several arguments current value, custom timeperiod, qtr1_data,qtr2_data,qtr3_data and qtr4_data
# The results of method are going to store in lists known as Extrapolation Data for Quarter, Month and Day in three distinct objects. 
# All of the processes validate custom timeperiod value to update future cast values of the current stock ticker price depending on the coefficient check. The coefficent value
# depends on custom input value such as 2 for quarter,8 for monthly and 365/(number of days in quarter) for daywise computation.
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
   # __init__(self) method aids in the computation of average price value which is going to be called as an argument in Extrapolation of ticker price based on Timeseries Regression
   # method. There are few more arguments used to call the quarterly data existence with in the compuatational method. Init calculates the average price of stock ticker from input file
   # and it calculates the price of records from the record 10000 to the last record of the csv delimited file.
   # Lastly, the file perform extrapolation and returns in three different lists based on month, day and quarterly data of the stocks.
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
