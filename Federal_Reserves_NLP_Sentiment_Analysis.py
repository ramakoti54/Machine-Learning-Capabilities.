import urllib.request as Ureq


class Webpage_read:

   def webpage_load(self, URL,content):
      with Ureq.urlopen(URL) as response:
         content = response.read();
         inflation_rates_file = content.decode("utf-8");
         #print(content)
         # Call Tokenizer on the instance itself
         self.Tokenizer(inflation_rates_file);
         #return(inflation_rates_file);

   def Tokenizer(self, inflation_rates_file):
      with open("/content/inflation_rates_file.html",mode='r+',encoding='utf-8') as inf_file:
         # The argument to read() should be the number of characters to read, not a string.
         # Since you want to read the whole file, you can call read() without arguments.
         read_file = inf_file.write(inflation_rates_file);
         #print(read_file);
         # Closing the file explicitly is not necessary when using 'with open(...)'.
         # The 'with' statement ensures the file is closed automatically.
         #inf_file.close();

page_read = Webpage_read();
URL = "https://www.usinflationcalculator.com/inflation/current-inflation-rates/";
content = "";
page_read.webpage_load(URL,content);
