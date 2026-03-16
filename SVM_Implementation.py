import numpy as np;
import pandas as pd;
#import ndarray as nd;
#import scikit-learn as skl;
import tensorflow as tf;
import math;
import matplotlib as mtl;
import matplotlib.pyplot as plt;
#import mplfinance as mpf;
import plotly as plty;

# Support Vector Machine(SVM) Implementation process for Stock price prediction of Banking and Finance Organizations.
class SVM_Implementation:

   # Dataset Normalization procedure with Feature Engineering selection process. Using stat techniques Min, Max, Mean, Median, Std, IQR functions.
   def Dataset_Normalization(newprice):

      return(0);

   # Find Dataset median for the Normalized price calculated from the Newprice computed from source files(Stock ticker csv files)
   # The method returns median value of the datasample to compute the samples of the dataset using median value comparision.
   def median_Newprice(Newprice):
      if(int(len(Newprice))%2 == 0):
         median_Newprice = (Newprice[len(Newprice)]+Newprice[int(len(Newprice))+1])/2;
         return(median_Newprice);
      else:
         median_Newprice = math.floor(Newprice(len(Newprice[int(len(Newprice))])/2));
         return(median_Newprice);
      return(0);
   # A Sorting Algorithm for computing Sorted list of prices to compute median value of the sample.
   def sort_Newprice(Newprice,i,k,sorted_newprice):
      #print(type(Newprice))
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

   #def scatter_plots():

# Reading CSV files data for the source Stock Tickers include Banking and Finance Organizations.
# Compute the simple average of Open,Close,High and Low prices of the file to find a frame of records representing the stock prices over couple of months from the sample.
# initiate variables to calculate intermediate prices and performing required operations prior to normalization of dataset.
# Instantiation of class SVM_Implementation to call required functions from the class.
# Functional calls through required arguments.
Stock_File_Name = pd.read_csv("/content/Stock_Files/JPM.csv",delimiter=',');
Newprice = (Stock_File_Name['Open']+ Stock_File_Name['Close']+ Stock_File_Name['High']+ Stock_File_Name['Low'])/4;
volume = Stock_File_Name['Volume'];
Newprice_sample = [];
Newprice_sample = list[Newprice[10001:]];
i = 0;
k = 1;
sorted_Newprice = [];
svm_implement = SVM_Implementation();

print(" Newprice\n","========\n",sum((Newprice[9001:]))/len(Newprice[9001:]));
print("Different numbers from 9000 to 10078 records for newprice\n",Newprice[9001:],"\n10000 beyond\n",Newprice[10001:])
print("\n Minimum of Newprice\n==============\n",min(Newprice[9000:]),min(Newprice[10001:]))
print("\n Max price\n========\n",max(Newprice[9001:]),max(Newprice[10001:]))
print("\n Volume of the stock with min and max",min(Newprice[10000:]),max(Newprice[10000:]));
#print("\n Median of the Newprice\n",svm_implement.median_Newprice(Newprice_sample),svm_implement.median_Newprice(Newprice_sample));
#print(Newprice_sample)
#sorted_Newprice = svm_implement.sort_Newprice(Newprice_sample,i,k,sorted_Newprice);
#print("Sorted prices of the Newprice list",sorted_Newprice);
#median_price = svm_implement.median_Newprice(list(sorted_Newprice))
#print("\n Median value of Newprice is\n======================\n",median_price);
#Normalized_Price = svm_implement.Dataset_Normalization(list(median_price));
#print("\n Normalized prices for the Dataset is",Normalized_Price);

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

plt.style.use('_mpl-gallery');
#np.random.seed(3);
Newprice_X = Newprice[10000:];
Y = volume[10000:];
number_days = len(Newprice_X);
#size and color
sizes = np.random.uniform(0,200,len(Newprice_X));
colors = np.random.uniform(201,298,len(Newprice_X));
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
fig, ax = plt.subplots();
#ax.scatter(Newprice_X,Y,s=sizes,c=colors);
ax.scatter(Newprice_X, Y,s=sizes,c=colors);
#ax.set(xlim=(0,200),xticks=np.arange(1,200),xlabel = "Stock prices over last 98 days",
#       ylim=(0,len(Y)),yticks=np.arange(1,len(Y)),ylabel="Volume of the stock over last 98 days");
ax.set(xlim=(0,350),xticks = np.arange(1,200),xlabel="Price of stock",
       ylim=(0,max(Y)),yticks = np.arange(1,len(Y)),ylabel="Volume of the stock");
#ax.lines();
#ax.lines();
#p0,p1 = np.polyfit(Newprice_X,Y,deg=1);
#print("The value of solpe p0 is:",p0,p1)
#ax.axline(xy1=(0,Newprice_X),slope=p0,lw=2);
plt.plot(Newprice_X,Y);
plt.show();
#ax.set(xlim=(0,200), xticks=np.arange(1,200),xlabel="Stock prices over last 98 days",
#       ylim=(0,len(Y)), yticks=np.arange(1,len(Y)),ylabel="Volume of the stock over last 98 days");
#plt.show();
