**Algorithm to Build an ML Model for Sentiment Analysis:**
	
Step 1: Gather data from various news paper articles and social media websites to form text files about a specific stock on Banking and Finance sectors. Collect inputs and transfer the information as input to form a specific Machine Learning Model with two major approaches

1. N- Gram and 2. SepCNN

** N-Gram:
	    N-Gram is a sequence of word representations to form tokens from the given textual information documents. Building tokens using single word of a sentence called 1-Gram,  the same applies for 2-Gram if there are two words used to form a token and tri-Gram or 3-Gram represents three word tokens from a sentence. The same holds true for all distinct Grams for a maximum token length of N in case of N-Gram.

The collected input data must be segregated to multiple samples to form a ratio of number of samples in the dataset to the number of words in each individual sample. The ratio is used as a condition to identify the Machine Learning model to be used for predicting the sentiment impact on the stock price as either positive, negative or neutral. 

An N-Gram model is a statistical method to find the probabilities of mass of words in a given sentence to assign it as a weight to understand significance of the word in the context of the text. The method uses the following statistical formulas to represent them through equations.

The total document/website page/file with content converted to form a token list with multiple words in the list of tokenizers. It could be an easier approach to form a tokenizer with distinct keywords from the page/document/file content.
Finding words to represent Unigram, Bi-Gram and Trigram model

	pi (Total Probability of sentence.) = i=1..m sigma(Pi)  
where  P1 P2 P3 …Pm  represents Probabilities of individual tokens in a given sentence.
	Pi  = (number of times Pi  repeated in the document/sentence)/Total number of words(count of
 words in the document/sentence).
	pi (Probability of a query/Token in a sentence)= i=1..m II (Pi) 
where P1 P2 P3 …Pm  represents Probabilities of individual tokens in a query.

Sentence:   ‘The mouse ran down the hill and choose the fatty mouse to burn some fat’
    	
UniGram: 
          Tokens = [‘The’,’mouse’,’ran’,’down’,’the’,’hill’,’and’,’choose’,’the’,’fatty’,’mouse’,’to’,’burn’,’some’,’fat’]
          Number of tokens = 15
          i = P1+P2+P3+....P15=1 
          p((‘The’,’mouse’,’ran’,’down’,’the’,’hill’),6) = PThe Pmouse Pran Pdown Pthe Phill 
          Total probability = 1  
          P1 = ⅙ =0.16  P2=⅙=0.16 …. P6=⅙=0.16 mutually exclusive pair of items with equal
          probability.
P The P mouse P ran P down Pthe Phill  = ⅙ *⅕ *¼ *⅓ *½ *1 = 1/720 =0.000103
Token Weightage for P1 = P1/(i=1m Pi)  = (⅙)/1/720 =120
for P2 = P2/(i=1m Pi) = 120.
Based on the probabilities we can identify the probability of occurrence of a specific word in the given sentence of a document. We can find the complete probability by assigning the statistical model rules to the entire document to find the likelihood of occurrence of a specific word in the given document.

