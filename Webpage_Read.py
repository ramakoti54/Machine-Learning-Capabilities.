import urllib.request as Ureq
import re;

class Webpage_Read:

   def webpage_load(self, URL,content):
      #with Ureq.urlopen(URL) as response:
      #   content = response.read();
      #   inflation_rates_file = content.decode("utf-8");
         #print(content);
         # Call Tokenizer on the instance itself
         #Html_file = self.Tokenizer(inflation_rates_file);
         #Content = "";
         #with open("/content/Scrapped_Content.txt",mode='r+',encoding='utf-8') as f:
      Scrapped_Text = open("/content/Scrapped_Content.txt",'r');
      
      #Scrapped_Text = #f.read();
      Content = self.Scrapped_Content(Scrapped_Text);
      print(Content);
         #return(inflation_rates_file);
         #self.loading_data_worddoc(Html_file);
      Scrapped_Text.close();
      return(Content);

   '''def Tokenizer(self, inflation_rates_file):
      with open("/content/inflation_rates.html",mode='r+',encoding='utf-8') as inf_file:
         # The argument to read() should be the number of characters to read, not a string.
         # Since you want to read the whole file, you can call read() without arguments.
         inf_file.write(inflation_rates_file);
         read_file = inf_file.write(inflation_rates_file);
         #print(read_file);
         # Closing the file explicitly is not necessary when using 'with open(...)'.
         # The 'with' statement ensures the file is closed automatically.
         #inf_file.close();
         inf_file.close();
      return(read_file);'''

   #def loading_data_worddoc(file_data):

      #return(stock_content_file);

   def Scrapped_Content(self, Scrapped_Text):
      with open("/content/Scrapped_Content.txt",mode='r+',encoding='utf-8') as Scrapped_file:
         # The argument to read() should be the number of characters to read, not a string.
         # Since you want to read the whole file, you can call read() without arguments.
         read_content = Scrapped_file.read()
         # = Scrapped_file.write(Scrapped_Text);
         #print(read_file);
         # Closing the file explicitly is not necessary when using 'with open(...)'.
         # The 'with' statement ensures the file is closed automatically.
         #inf_file.close();
         #Scrapped_file.close();
      return(read_content);

   def Tokenization(self,Content):
      #for con in Content:
      #   if(re.split('.',Content,re.IGNORECASE)):
      print(str(Content))
      X_Content = re.split('\.',str(Content),re.IGNORECASE);
      #X_Content = re.search(r'(?<=<p>)\w+', '');
      k = len(X_Content);
      vector_tokens = [[0,0,0],[0,0,0],[0,0,0]];
      Sentences = "";
      Words = [];
      for tokens in X_Content:
         #for tokens in X_Content:
         #token[tokens] = i;
         #i = i+1;
         #print(vector_tokens);
         #Sentences.append('tokens');
         Sentences = tokens;
         Split_Sentence = Sentences.split(" ");
         Words.append(Split_Sentence);
      return(Words);

   def __init__(self):
      URL = "https://www.jpmorganchase.com/newsroom/press-releases/2026/alabama-workforce-philanthropic-commitment";
      #"https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/annualreport-2019.pdf";
      #"https://www.msn.com/en-in/sports/cricket/from-barbados-to-ahmedabad-india-s-era-of-unparalleled-dominance/ar-AA1XPaIK?uxmode=ruby&ocid=edgntpruby&pc=U531&cvid=2440b108d3f047dfd5018884cc084654&ei=22";#"https://www.usinflationcalculator.com/inflation/current-inflation-rates/";
      content = "";
      content = self.webpage_load(URL,content);
      print(content)
      Tokens = [];
      Tokens = self.Tokenization(content);
      print(Tokens)
      return(None);

web_read = Webpage_Read();
page_read = Webpage_read();
