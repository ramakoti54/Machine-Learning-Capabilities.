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
from statsmodels.stats.diagnostic import acorr_ljungbox;

class ARIMA_Stock_Price_Prediction:
   #def ARIMA_Stock_Price_Computation(self,endog: Union[pd.Series, list], order_list: list, d: int)-> pd.DataFrame:
   def ARIMA_Stock_Price_Computation(self,endog,order_list,d):
      results = [];
      #order = [];
      #i = 0;
      print("Order list values are: ",order_list[:]);
      for order in range(len(order_list)):#tqdm_notebook(order_list):
         #order.append(order);
         #print("\n\n Order value is:\n",type(order));
         #if(i==0):
         #   order_previous = order;
         #   i = i+1;
         #   break;
         #elif(i == 1 or i ==2):
         #order_previous = order;
         #print("Result DF is: ",endog[1]);
         try:
            #model = self.Differencing(endog,order,order_previous,order_list);
            #model = SARIMAX(endog, order=(list(endog[1]),d,list(order_list)),simple_differencing=False).fit(disp=False);
            model = SARIMAX(endog,order=(3,d,3),simple_difference=False,enforce_stationarity=False,enforce_invertibility=False).fit(disp=False);
            #print("Model values are: ",model.summary());
         except:
            continue;
            #results.append();
            #aic = model.aic;
            #results.append([order, aic]);
      #result_df = pd.DataFrame(results)
      #print("\n\n Results list: \n",result_df);
      #result_df.columns = ['(p,q)', 'AIC'];
      #Sort in ascending order, lower AIC is better
      #result_df = result_df.sort_values(by='AIC',ascending=True).reset_index(drop=True);
      #print("\n\n Result Data Frame is: \n\n====================\n",result_df)
      print(model.summary());
      model.plot_diagnostics(lags=10,figsize=(10,8));
      residuals = model.resid;
      #lbvalue, pvalue =
      print(acorr_ljungbox(residuals, np.arange(1, 11, 1)));
      #print(pvalue,lbvalue);
      return (None);
      #return();

   def exponential_plot(self,Avg_Price,Date):
      X =  [];
      Y = [];
      X = Avg_Price;
      Y = Date;
      fig, ax = plt.subplots()
      #print("Length of X and Y are",len(X),len(Y));
      ax.plot(Y,X);
      ax.set_xlabel('Date Ranges from 2019-11-07 to 2020-04-01')
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

   def standard_Normalizer(self,x):
      #for i in range(np.len)
      x_standard_normalizer = [];
      x_mean = self.Mean(x);
      x_std = self.Standard_Deviation(x);
      for i in range(len(x)):
         x_standard_normalizer.append(x[i]- (x[i]-x_mean)/x_std);
      return(x_standard_normalizer);

   def Standard_Deviation(self,x):
      sum_std = 0.0;
      mean_x = self.Mean(x);
      for i in range(len(x)):
         sum_std = sum_std + math.pow((x[i]- mean_x),2);
      std_x = math.sqrt(sum_std/(len(x)-1));
      print("Standard Deviation value is:\n",std_x);
      return(std_x);

   def Mean(self,x):
      sum = 0.0;
      for i in range(len(x)):
         sum = sum + x[i];
      mean = sum/len(x);
      print("Mean value is: \n",mean);
      return(mean);

   def sort_Newprice(self,Newprice,i,k,sorted_newprice):
      #print(type(Newprice))
      #sorted_newprice = [];
      if(i < len(Newprice)-1):
         if(Newprice[i] <= Newprice[i+1]):
            sorted_newprice.append(Newprice[i]);
            i = i+1;
            self.sort_Newprice(Newprice[i:],i,k,sorted_newprice);
         elif(Newprice[i] > Newprice[i+1] and i < int(len(Newprice))):
            temp = Newprice[i];
            Newprice[i] = Newprice[i+1];
            Newprice[i+1] = temp;
            sorted_newprice.append(Newprice[i]);
            i = i+1;
            self.sort_Newprice(Newprice[i:],i,k,sorted_newprice);
      elif(k < len(Newprice)):
         i = k;
         k = k+1;
         return(self.sort_Newprice(Newprice[k:],i,k,sorted_newprice));
      elif(k == len(Newprice)):
         return(sorted_newprice);
      return(sorted_newprice);

   def Median_Newprice(self,Newprice):
      median_Newprice = 0.0;
      if(int(len(Newprice))%2 == 0):
         median_Newprice = (Newprice[len(Newprice)/2] + Newprice[int(len(Newprice))/2+1])/2;
         return(median_Newprice);
      else:
         median_Newprice = Newprice[math.floor(int(len(Newprice))/2)];
         return(median_Newprice);
      return(median_Newprice);

   def Gaussian_Mean(self,x):
      mean_x = self.Mean(x);
      std_x = self.Standard_Deviation(x);
      sum_std = 0.0;
      Gaussian_Mean = [];
      for i in range(len(x)):
         sum_std = sum_std + math.pow((x[i]- mean_x),2);
         Gaussian_Mean.append((1/math.sqrt(2*math.pi)*std_x)*(math.exp((sum_std*-1)/(2*math.pow(std_x,2)))));
      
      return(Gaussian_Mean);

   def Gaussian_Median(self,x):
      median_x = self.Median_Newprice(x);
      std_x = self.Standard_Deviation(x);
      sum_std = 0.0;
      Gaussian_Median = [];
      for i in range(len(x)):
         sum_std = sum_std + math.pow((x[i]-median_x),2);
         Gaussian_Median.append((1/math.sqrt(2*math.pi)*std_x)*(math.exp((sum_std*-1)/(2*math.pow(std_x,2)))));
      return(Gaussian_Median);

   def Statistical_Methods(self,x,i,k,calling,sorted_newprice):
      #plot_scatter = self.Plot_Scatter(Newprice_Sample,Volume_Sample);
      x_mean =[];
      x_median = [];
      x_std_norm = [];
      x_gaussian_mean = [];
      x_gaussian_median = [];

      if(calling == 'Mean'):
         x_mean = self.Mean(x);
         return(x_mean);
      elif(calling == 'Median'):
         x = self.sort_Newprice(x,i,k,sorted_newprice);
         x_median = self.Median_Newprice(x);
         return(x_median);
      elif(calling == 'Standard_Normalizer'):
         x_std_norm = self.standard_Normalizer(x);
         return(x_std_norm);
      elif(calling == 'Gaussian_Mean'):
         x_gaussian_mean = self.Gaussian_Mean(x);
         return(x_gaussian_mean);
      elif(calling == 'Gaussian_Median'):
         sorted_newprice = self.sort_Newprice(x,i,k,sorted_newprice);
         x_gaussian_median = self.Gaussian_Median(sorted_newprice);
         return(x_gaussian_median);
      else:
         print("Enter the calling method for expected statistical method");
         return(0);
      return(0);

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
      #print("Exponential plots Avg price is: ",Avg_Price[10000:]);
      #self.exponential_plot(Avg_Price[10000:],Date_Ticker_Value[10000:]);
      print("\n\n\n ================================================")
      Stationary_factor = 0;
      Stationary_factor = int(input("Enter an integer value to represent Order of Differenciation process"));

      '''if(Stationary_factor == 0):
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
         self.exponential_plot(Avg_Price[10000:],Date_Ticker_Value[10002:]);
      else:
         return(None);'''
      #Avg_Price = Avg_Price[10000:];
      #Training_Sample = pd.Series(Avg_Price[10000:]); #[pd.Series(Date_Ticker_Value[10000:]),list(Avg_Price[10000:])];
      #Test_Sample = Avg_Price[10000:];
      d = 1;
      Order_list = (1,d,1)
      #self.ARIMA_Stock_Price_Computation(Training_Sample, Order_list, d);
      median_price = [];
      calling = str(input("Enter a Statistical method as one of the selections. 1. Mean 2. Median 3. Standard_Normalizer 4. Gaussian_Mean 5. Gaussian_Median"));
      Sorted_Newprice = [];
      i = 0; k = 0;
      statistical_method_result = [];
      statistical_method_result = self.Statistical_Methods(list(Avg_Price[10000:]),i,k,calling,Sorted_Newprice);
      Avg_Price = list(Avg_Price[10000:]);
      print("Avg_Price list is:\n",Avg_Price,len(statistical_method_result));
      #j = 10000;
      Gaussian_Measure = [];
      for i in range(len(statistical_method_result)):
         Gaussian_Measure.insert(i,np.abs(statistical_method_result[i]-Avg_Price[i]));
         #j = j+1;
      #Avg_Price = statistical_method_result;
      print("Avg_Price list is:\n",Gaussian_Measure,"Length of Avg price is: \n",len(Gaussian_Measure));
      Avg_Price = [];
      Avg_Price = Gaussian_Measure;
      if(Stationary_factor == 0):
         self.ADF_Test(Avg_Price);
         self.exponential_plot(Avg_Price,Date_Ticker_Value[10000:]);
      elif(Stationary_factor == 1):
         Avg_Price = np.diff(Avg_Price,n=1);
         #print("Avg Stationary Price values are: ",Avg_Price,len(Date_Ticker_Value[10000:]),"\n\n Length of Avg price Data smaple is:",len(Avg_Price));
         self.ADF_Test(Avg_Price);
         self.exponential_plot(Avg_Price,Date_Ticker_Value[10001:]);
      elif(Stationary_factor == 2):
         Avg_Price = np.diff(Avg_Price,n=2);
         self.ADF_Test(Avg_Price);
         print("Avg price list length: \n",len(Avg_Price));
         self.exponential_plot(Avg_Price,Date_Ticker_Value[10002:]);
      else:
         return(None);
      statistical_method_result = Avg_Price;
      self.ARIMA_Stock_Price_Computation(pd.Series(statistical_method_result),Order_list,d);
      return(None);

ARIMA_Stock_Price_Predict = ARIMA_Stock_Price_Prediction();
