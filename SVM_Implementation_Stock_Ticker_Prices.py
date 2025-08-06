import numpy as np;
import pandas as pd;
#import ndarray as nd;
#import scikit-learn as skl;
import tensorflow as tf;
import math;
import matplotlib as mtl;
import matplotlib.pyplot as plt;
import plotly.graph_objects as go;
import Visualize_Stock_Data as vsd;

# Support Vector Machine(SVM) Implementation process for Stock price prediction of Banking and Finance Organizations.
class SVM_Implementation:

   # Dataset Normalization procedure with Feature Engineering selection process. Using stat techniques Min, Max, Mean, Median, Std, IQR functions.
   def Dataset_Normalization(newprice):

      return(0);

   def Mean(self,x):
      sum = 0.0;
      for i in range(len(x)):
         sum = sum + x[i];
      mean = sum/len(x);
      return(mean);

   def Standard_Deviation(self,x):
      sum_std = 0.0;
      mean_x = self.Mean(x);
      for i in range(len(x)):
         sum_std = sum_std + sum(pow((x[i]- mean_x),2));

      std_x = math.sqrt(sum_std/(len(x)-1));
      return(std_x);

   def Minimum(self,x):
      min_x = [];
      for i in range(len(x)):
         if(x[i] <= x[i+1]):
            min_x = x[i];
         else:
            min_x = x[i+1];
      return(min_x);

   def Maximum(self,x):
      max_x = [];
      for i in range(len(x)):
         if(x[i] >= x[i+1]):
            max_x = x[i];
         else:
            max_x = x[i+1];
      return(max_x);

   def Optimal_Range(self,x,range1,range2):
      for i in range(len(x)):
         range1 = range1 + x['Close']- x['Open'];
         range2 = range2 + x['High'] - x['Low'];
      return([range1,range2]);

   def Gaussian_Mean(self,x):
      mean_x = self.Mean(x);
      std_x = Standard_Deviation(x);
      sum_std = 0.0;
      for i in range(len(x)):
         sum_std = sum_std + sum(pow((x[i]- mean_x),2));

      Gaussian_Mean = (1/sqrt(2*math.pi)*std_x)*(exp((sum_std*-1)/(2*pow(std_x,2))));
      return(Gaussian_Mean);

   def Gaussian_Median(self,x):
      median_x = self.Median(x);
      std_x = Standard_Deviation(x);
      sum_std = 0.0;
      for i in range(len(x)):
         sum_std = sum_std + sum(pow((x[i]-median_x),2));
      
      Gaussian_Median = (1/sqrt(2*math.pi)*std_x)*(exp((sum_std*-1)/(2*pow(std_x,2))));

      return(Gaussian_Median);

   def Gaussian_Standard_Deviation(self,x):
      median_x = self.Median(x);
      std_x = Standard_Deviation(x);
      sum_std = 0.0;
      for i in range(len(x)):
         sum_std = sum_std + sum(pow((x[i]-std_x),2));
      
      Gaussian_Std = (1/sqrt(2*math.pi)*std_x)*(exp((sum_std*-1)/(2*pow(std_x,2))));

      return(Gaussian_Std);

   def Gaussian_Minimum(self,x):
      Min_x = self.Minimum(x);
      std_x = Standard_Deviation(x);
      sum_std = 0.0;
      for i in range(len(x)):
         sum_std = sum_std + sum(pow((x[i]-Min_x),2));
      
      Gaussian_Minimum = (1/sqrt(2*math.pi)*std_x)*(exp((sum_std*-1)/(2*pow(std_x,2))));

      return(Gaussian_Minimum);

   def Gaussian_Maximum(self,x):
      Max_x = self.Maximum(x);
      std_x = Standard_Deviation(x);
      sum_std = 0.0;
      for i in range(len(x)):
         sum_std = sum_std + sum(pow((x[i]-Max_x),2));
      
      Gaussian_Maximum = (1/sqrt(2*math.pi)*std_x)*(exp((sum_std*-1)/(2*pow(std_x,2))));

      return(Gaussian_Maximum);

   # Find Dataset median for the Normalized price calculated from the Newprice computed from source files(Stock ticker csv files)
   # The method returns median value of the datasample to compute the samples of the dataset using median value comparision.
   def Median_Newprice(self,Newprice):
      median_Newprice = 0.0;
      if(int(len(Newprice))%2 == 0):
         median_Newprice = (Newprice[len(Newprice)] + Newprice[int(len(Newprice))+1])/2;
         return(median_Newprice);
      else:
         median_Newprice = math.floor(Newprice(len(Newprice[int(len(Newprice))])/2));
         return(median_Newprice);
      return(0);

   # A Sorting Algorithm for computing Sorted list of prices to compute median value of the sample.
   def sort_Newprice(self,Newprice,i,k,sorted_newprice):
      #print(type(Newprice))
      #sorted_newprice = [];
      if(i < len(Newprice)-1):
         if(Newprice[i] <= Newprice[i+1]):
            sorted_newprice.append(Newprice[i]);
            i = i+1;
            sorted_Newprice(Newprice[i:],i,k,sorted_newprice);
         elif(Newprice[i] > Newprice[i+1] & i < int(len(Newprice))):
            temp = Newprice[i];
            Newprice[i] = Newprice[i+1];
            Newprice[i+1] = temp;
            sorted_newprice.append(Newprice[i]);
            i = i+1;
            sorted_Newprice(Newprice[i:],i,k,sorted_newprice);
      elif(k < len(Newprice)):
         i = k;
         k = k+1;
         return(sorted_Newprice(Newprice[k:],i,k,sorted_newprice));
      elif(k == len(Newprice)):
         return(sorted_newprice);
      return(sorted_newprice);

   def standard_Normalizer(self,x):
      #for i in range(np.len)
      x_mean = self.Mean(x);
      x_std = self.Standard_Deviation(x);
      for i in len(range(x)):
         x_standard_normalizer = (x[i]-x_mean)/x_std;
      return(x_standard_normalizer);

   def Plot_Scatter(self,X,Y):
      plt.style.use('_mpl-gallery');
      #np.random.seed(3);
      number_days = len(X);
      #size and color
      sizes = np.random.uniform(0,200,len(X));
      colors = np.random.uniform(201,298,len(X));
      plt.plot(X,Y);
      fig, ax = plt.subplots();
      ax.scatter(X,Y,s=sizes,c=colors);
      ax.set(xlim=(0,200), xticks=np.arange(1,200),xlabel="Stock prices over last 98 days",
      ylim=(0,len(Y)), yticks=np.arange(1,len(Y)),ylabel="Volume of the stock over last 98 days");
      plt.show();

   def Candlestick_Graph(Stock_File):
      fig = go.Figure(data = [go.Candlestick(
                    x = Stock_File['Date'],
                    Open = Stock_File['Open'],
                    Close = Stock_File['Close'],
                    Low = Stock_File['Low'],
                    High = Stock_File['High'],
                    Volume = Stock_File['Volume'],
                    Date = Stock_File['Date']
                        )]);
      fig.update_layout(xaxis_rangeslider_visible=False);
      # Set layout size
      fig.update_layout(autosize=False,width=700,height=500);
      fig.show();
      fig.write_html("/content/Stock_Files/candlestick-plotly-basic.html");
      return(0);

   def Statistical_Methods(self,x,volume,median_price,Stock_Files,i,k,sorted_newprice,range1,range2,calling):
      plot_scatter = self.Plot_Scatter(Newprice_Sample,Volume_Sample);
      if(calling == 'Mean'):
         x_mean = self.Mean(x);
         return(x_mean);
      elif(calling == 'Std'):
         x_std = self.Standard_Deviation(x);
         return(x_std);
      elif(calling == 'Min'):
         x_min = self.Minimum(x);
         return(x_min);
      elif(calling == 'Max'):
         x_max = self.Maximum(x);
         return(x_max);
      elif(calling == 'Median'):
         x_median = self.Median_Newprice(median_price);
         return(x_median);
      elif(calling == 'Optimal_Range'):
         x_optimal_range = self.Optimal_Range(x,range1,range2);
         return(x_optimal_range);
      elif(calling == 'Standard_Normalizer'):
         x_std_norm = self.standard_Normalizer(x);
         return(x_std_norm);
      elif(calling == 'Gaussian_Mean'):
         x_gaussian_mean = self.Gaussian_Mean(x);
         return(x_gaussian_mean);
      elif(calling == 'Gaussian_Median'):
         x_gaussian_median = self.Gaussian_Median(x);
         return(x_gaussian_median);
      elif(calling == 'Gaussian_Standard_Deviation'):
         x_gaussian_std = self.Gaussian_Standard_Deviation(x);
         return(x_gaussian_std);
      elif(calling == 'Gaussian_Minimum'):
         x_gaussian_min = self.Gaussian_Minimum(x);
         return(x_gaussian_min);
      elif(calling == 'Gaussian_Maximum'):
         x_gaussian_max = self.Gaussian_Maximum(x);
         return(x_gaussian_max);
      elif(calling == 'Plot_Scatter'):
         plots = self.Plot_Scatter(x,volume);
         return(0);
      elif(calling == 'Candlestick_Graph'):
         Candlestick = self.Candlestick_Graph(Stock_File);
         return(0);
      else:
         print("Enter the calling method for expected statistical method");
         return(0);
      return(0);

#def scatter_plots():
# Reading CSV files data for the source Stock Tickers include Banking and Finance Organizations.
# Compute the simple average of Open,Close,High and Low prices of the file to find a frame of records representing the stock prices over couple of months from the sample.
# initiate variables to calculate intermediate prices and performing required operations prior to normalization of dataset.
# Instantiation of class SVM_Implementation to call required functions from the class.
# Functional calls through required arguments.
Stock_File_Name = pd.read_csv("/JPM.csv",delimiter=',');
Newprice = (Stock_File_Name['Open']+ Stock_File_Name['Close']+ Stock_File_Name['High']+ Stock_File_Name['Low'])/4;
volume = Stock_File_Name['Volume'];
Newprice_sample = [];
Newprice_Sample = list[Newprice[10001:]];
Volume_Sample = list(volume[10001:]);
i = 0;
k = 1;
sorted_Newprice = [];
svm_implement = SVM_Implementation();
range1 = [];
range2 = [];
calling = str(input("Enter one of the calling method as in ['Mean','Std','Min','Max','Median','Optimal_Range','Gaussian_Mean','Gaussian_Median','Gaussian_Standard_Deviation','Gaussian_Minimum','Gaussian_Maximum','Plot_Scatter','Candlestick_Graph'] for Statistical Method"));
Standard_Normal_Price = svm_implement.standard_Normalizer(Newprice);
#print("Input x_p after applying standard normalization function",x_p);

#print(" Newprice\n","========\n",sum((Newprice[9001:]))/len(Newprice[9001:]));
#print("Different numbers from 9000 to 10078 records for newprice\n",Newprice[9001:],"\n10000 beyond\n",Newprice[10001:])
#print("\n Minimum of Newprice\n==============\n",min(Newprice[9000:]),min(Newprice[10001:]))
#print("\n Max price\n========\n",max(Newprice[9001:]),max(Newprice[10001:]))
#print("\n Volume of the stock with min and max",min(Newprice[10000:]),max(Newprice[10000:]));
#Optimum_Range = Optimal_Range(Stock_File_Name,range1,range2);
#print("\n Optimal Range of the price values over the intraday looks like\n",Optimum_Range[0],Optimum_Range[1]);
#print("\n Median of the Newprice\n",svm_implement.median_Newprice(Newprice_sample),svm_implement.median_Newprice(Newprice_sample));
#print(Newprice_sample)
Sorted_Newprice = svm_implement.sort_Newprice(Newprice_Sample,i,k,sorted_Newprice);
#print("Sorted prices of the Newprice list",sorted_Newprice);
median_price = svm_implement.median_Newprice([Sorted_Newprice]);
#print("\n Median value of Newprice is\n======================\n",median_price);
#Normalized_Price = svm_implement.Dataset_Normalization(list(median_price));
#print("\n Normalized prices for the Dataset is",Normalized_Price);
statistical_method_result = svm_implement.Statistical_Methods(Newprice,volume,median_price,Stock_File_Name,i,k,Sorted_Newprice,range1,range2,calling);


visualize_Data.Visualize_Stock_Results();

'''plt.style.use('_mpl-gallery')
# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
print(x,y);
# size and color:

sizes = np.random.uniform(15, 80, 7)
colors = np.random.uniform(15, 80, 7)
print("sizes are ",sizes);

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 15), xticks=np.arange(1, 15),xlabel='random_generated_with_dynamic_width',
       ylim=(0, 15), yticks=np.arange(1, 15),ylabel='random_generated_with_dynamic_width based on x label');

plt.show()'''

'''['#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728',
'#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728','#d62728'];#np.random.uniform(0,200,len(sizes));'''
#print(colors);
#sizes = np.random.uniform(0,200,1100);
#colors = np.random.uniform(0,200,1100);
#sizes =
#ploting prices and volumes of stock
