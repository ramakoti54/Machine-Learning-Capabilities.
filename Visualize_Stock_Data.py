import plotly.graph_objects as go;
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

# Define the stock symbol and date range
#stock_symbol = "GOOGL"  # Example: Google
#start_date = "2021-01-01"
#end_date = "2021-03-30"
class Visualize_Stock_Data:
   def Visualize_Stock_Results(self,stock_data_file):
      #try:
      # Load historical data
      #
      #yf.download(stock_symbol,
      #                         start=start_date, end=end_date)

      fig = go.Figure(data=[go.Candlestick(
                      # date values
                      open = stock_data_file['Open'],
                      high = stock_data_file['High'],
                      low = stock_data_file['Low'],
                      #Mean_Price = stock_data_file['Mean_Price'],
                      #Mathematical_Price = stock_data_file['Mathematical_Price'],
                      close = stock_data_file['Close'],
                      x = stock_data_file['Date'])]);
      # Set layout size
      fig.update_layout(
      autosize=False,
      width=700,
      height=500)
      # Display the plot
      fig.update_layout(
      title=dict(text='Stock File Dataset'),
      yaxis=dict(
      title=dict(
        text='JP Morgan Stock'
        )
         ),
      shapes = [dict(
         x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
         line_width=2)],
      annotations=[dict(
         x='2016-12-09', y=0.05, xref='x', yref='paper',
         showarrow=False, xanchor='left', text='Increase Period Begins')]
            )

      fig.show();
      #except FileNotFound as fe:
      #   print("The File directory or the specified path might not be present. Look into these details for updating the file properties.Additionally, check for the File name If the error persist contact Administrator/support team for further assistence. ")
      #except SystemError as se:
      #   print("The module used in the program has internal issues and the exception is not relevent to the program. Check for sys.version to understand about the python interpreter. The System version describes if there are any issues witht python internal environment. If there needs to be a requirement of kernal restart/environment interpreter restart etc.. Check for the Python Documentation and support teams to work on it for further details. ");
      #except Exception as fe:
      #   print("All Exceptions related to System and Non system reported in here. Check with Python Documentation or support team for further details on the error.");
      return(0);

   def Statistical_Parameter_Visualization(self,Stock_data_file):
      Mean = Stock_data_file['Mean_Price'];
      #Median = Stock_data_file['Median_Price'];
      Open = Stock_data_file['Open'];
      Close = Stock_data_file['Close'];
      High = Stock_data_file['High'];
      Low = Stock_data_file['Low'];
      Volume = Stock_data_file['Volume'];
      Date = Stock_data_file['Date'];
      data = np.concatenate((Mean,Open,Close));
      data1 = np.concatenate((Open,Close,High));
      #data1 = np.concatenate((Mean,High,Low));
      #print(data)
      fig, ax = plt.subplots(3,3);
      ax[0, 0].boxplot(data);
      ax[0, 0].set_title('Base Plot');
      ax[0, 1].boxplot(data,notch='True');
      ax[0, 1].set_title('notch plot');
      ax[0, 2].boxplot(data, sym='gD');
      ax[0, 2].set_title('horizontal_plot');
      ax[1, 0].boxplot(data, sym='');
      ax[1, 0].set_title('no outlier points');
      ax[1, 1].boxplot(data1);
      ax[1, 1].set_title('Base Plot');
      ax[1, 2].boxplot(data1, notch='TRUE');
      ax[1, 2].set_title('notch plot');
      ax[2, 0].boxplot(data1, sym='gD');
      ax[2, 0].set_title('horizontal_plot');
      ax[2, 1].boxplot(data1, sym='');
      ax[2, 1].set_title("no outlier points");
      fig.subplots_adjust(left=0.18,bottom=1.59,right=1.28,top=1.78,wspace=1.07,hspace=1.25);
      plt.show();
      return(0);

stock_data_file = pd.read_csv("/content/Stock_Files/JPM.csv",delimiter=',');
Mean_Stock_Price = [];
Mean_Stock_Price = (((stock_data_file['Open']+stock_data_file['Close']+stock_data_file['High']+stock_data_file['Low'])/4));
Mathematical_Price = list(((stock_data_file['High']+stock_data_file['Low'])/2));
stock_data_file.insert(4,"Mean_Price",Mean_Stock_Price,allow_duplicates='TRUE');
stock_data_file.insert(5,"Mathematical_Price",Mathematical_Price,allow_duplicates='TRUE');
#print(type(stock_data_file),"\n",stock_data_file);
#print(stock_data_file);
Visualize_Data = Visualize_Stock_Data();
Visualize_Data.Visualize_Stock_Results(stock_data_file);
#Visualize_Data.Statistical_Parameter_Visualization(stock_data_file);
