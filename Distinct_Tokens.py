import math;
import Distinct_Tokens;

class Probability_tokens:
   # Counting the repetitions of a specific token in the words.
   def count_tokens(self,token,tokens,i,k,freequency,Token_Probability_list):
      if(i < (len(tokens))-1):
         if((str(token).lower() != str(tokens[i+1]).lower())):
            freequency = 1;
            i=i+1;
            Token_Probability_list.append([token,freequency]);
            return(self.count_tokens(token,tokens[i:],i,k,freequency,Token_Probability_list));

         elif((str(token).lower() == str(tokens[i+1]).lower())):
            freequency = freequency+1;
            i = i+1;
            Token_Probability_list.append([token,freequency]);
            return(self.count_tokens(token,tokens[i:],i,k,freequency,Token_Probability_list));

      elif((i+1) == len(tokens) & k < int(len(tokens))):
         i = k;
         k = k+1;
         return(self.count_tokens(tokens[k],tokens[k:],i,k,freequency,Token_Probability_list));

      elif(k == int(len(tokens))):
         return(Token_Probability_list);

      return(Token_Probability_list);

   # Recursive function to identify tokens and embed them into encrypted digital format using binary format called one-hot encoding
   # to use them in N-Gram model to assign them with the probability weightage.
   def recursive_call(self,encryption,i,j,k,tokens,freequency,P_token,Token_Probability_list):
      if(i < len(encryption)):
         if(j < len(tokens)):
            Probability = self.count_tokens(tokens[j],tokens,i,k,freequency,Token_Probability_list);
            print(Probability[i]);
            count_mutualexclusive_event = Probability[i][1];
            P_token.append(int(count_mutualexclusive_event)/int(len(tokens)));
            print(P_token)
            i = i+1;
            j = j+1;
         return(self.recursive_call(encryption,i,j,k,tokens,freequency,P_token,Token_Probability_list));
      else:
         return(0);
      return(P_token);

   def Tokens_Counter(self,tokens,i,freequency):
      if(i < len(tokens) & tokens[i] not in tokens[i+1:]):
         freequency = 1;
         i = i+1;
         return(self.Tokens_Counter(tokens,i+1,freequency));

      elif(i < len(tokens) & tokens[i] in tokens[i+1:]):
         freequency = freequency+1;
         i = i+1;
         return(self.Tokens_Counter(tokens,i,freequency));
Prob_tokens = Probability_tokens();
# Defnining Tokens list and finding individual tokens from the list.
tokens =['The','mouse','ran','down','the','hill'];
# Encryption list is assigned with respective tokens from the tokens list. Here we have 6 tokens and we are going with 6x6 identity matrix to form an equivalent weight matrix to find the significance of
# each token from the matrix.
# Assigning default integer values for using as intermediate calculations in the recursive function and count functions for finding the probability of existence of each word based on the freequency of
# repetitions in the sentence/document/file/content file.
encryption = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
i = 0;
j = 0;
k = 1;
freequency = 0;
P_token = [];
Token_Probability_list = [];
print(Prob_tokens.recursive_call(encryption,i,j,k,tokens,freequency,P_token,Token_Probability_list));
