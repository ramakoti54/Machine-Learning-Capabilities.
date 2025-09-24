import numpy as np;
import pandas as pd;
import math;


class Compute_Eigen_Parameters:
   def Compute_Eigen_Values(self,Hessian_Matrix,Identity_Matrix,i,j,lambda_h,Eigen_Values,Equation,n):
      if(i < len(Hessian_Matrix) & i != 0):
         if(j < len(Hessian_Matrix[i])):
            Eigen_Values.append(Hessian_Matrix[i][j] - np.matmul(Identity_Matrix[i][j] * lambda_h));
            j = j+1;
            self.Compute_Eigen_Values(Hessian_Matrix,Identity_Matrix,i,j,lambda_h,Eigen_Values,n);
         elif(j >= len(Hessian_Matrix[i])):
            i = i+1;
            j = 0;
            self.Compute_Eigen_Values(Hessian_Matrix,Identity_Matrix,i,j,lambda_h,Eigen_Values,n);
      elif(i >= len(Hessian_Matrix)):
         #Equation = Eigen_Values[0][0]*Eigen_Values[1][1]*Eigen_Values[2][2] + Eigen_Values[0][1]*Eigen_Values[1][2]*Eigen_Values[2][0]+Eigen_Values[0][2]*Eigen_Values[1][0]*Eigen_Values[2][1];
         while(floor(int(Equation)) != 0):
            if(Equation == 0 & n == 0):
               #lambda_h = int(Input("Enter the Lambda_h value for computation of Eigen values and enter integer to start with"))
               Equation = math.pow(lambda_h,3)-math.pow(lambda_h,2)*(Hessian_Matrix[0][0]+Hessian_Matrix[1][1]+Hessian_Matrix[2][2])+lambda_h * (Hessian_Matrix[0][0]* Hessian_Matrix[1][1]+Hessian_Matrix[0][0]*Hessian_Matrix[2][2]+Hessian_Matrix[1][1]*Hessian_Matrix[2][2])-(Hessian_Matrix[0][0]*Hessian_Matrix[1][1]*Hessian_Matrix[2][2]+Hessian_Matrix[0][1]*Hessian_Matrix[1][2]*Hessian_Matrix[2][0]+Hessian_Matrix[0][2]*Hessian_Matrix[1][0]*Hessian_Matrix[2][1]));             
               temp = Equation;
               n = n+1;
            elif(Equation != 0 & n>0 & Equation > 0):
               lambda_h = int(Input("Enter the new Lambda_h value for computation of Eigen values"));
               Equation = math.pow(lambda_h,3)-math.pow(lambda_h,2)*(Hessian_Matrix[0][0]+Hessian_Matrix[1][1]+Hessian_Matrix[2][2])+lambda_h * (Hessian_Matrix[0][0]* Hessian_Matrix[1][1]+Hessian_Matrix[0][0]*Hessian_Matrix[2][2]+Hessian_Matrix[1][1]*Hessian_Matrix[2][2])-(Hessian_Matrix[0][0]*Hessian_Matrix[1][1]*Hessian_Matrix[2][2]+Hessian_Matrix[0][1]*Hessian_Matrix[1][2]*Hessian_Matrix[2][0]+Hessian_Matrix[0][2]*Hessian_Matrix[1][0]*Hessian_Matrix[2][1]));
               n = n+1;
            elif(Equation != 0 & Equation >0 & Equation < 1):
               lambda_h = int(Input("Enter the new Lambda_h value as increments of 0.5 or less as the equation is near to find the eigen values"));
               Equation = math.pow(lambda_h,3)-math.pow(lambda_h,2)*(Hessian_Matrix[0][0]+Hessian_Matrix[1][1]+Hessian_Matrix[2][2])+lambda_h * (Hessian_Matrix[0][0]* Hessian_Matrix[1][1]+Hessian_Matrix[0][0]*Hessian_Matrix[2][2]+Hessian_Matrix[1][1]*Hessian_Matrix[2][2])-(Hessian_Matrix[0][0]*Hessian_Matrix[1][1]*Hessian_Matrix[2][2]+Hessian_Matrix[0][1]*Hessian_Matrix[1][2]*Hessian_Matrix[2][0]+Hessian_Matrix[0][2]*Hessian_Matrix[1][0]*Hessian_Matrix[2][1]));
               n = n+1;
            elif(Equation !=0 & Equation <0):
               lambda_h = int(Input("Enter the new Lambda_h value as the negative as the decremental integer/floating point could be the eigen values(roots)"));
               Equation = math.pow(lambda_h,3)-math.pow(lambda_h,2)*(Hessian_Matrix[0][0]+Hessian_Matrix[1][1]+Hessian_Matrix[2][2])+lambda_h * (Hessian_Matrix[0][0]* Hessian_Matrix[1][1]+Hessian_Matrix[0][0]*Hessian_Matrix[2][2]+Hessian_Matrix[1][1]*Hessian_Matrix[2][2])-(Hessian_Matrix[0][0]*Hessian_Matrix[1][1]*Hessian_Matrix[2][2]+Hessian_Matrix[0][1]*Hessian_Matrix[1][2]*Hessian_Matrix[2][0]+Hessian_Matrix[0][2]*Hessian_Matrix[1][0]*Hessian_Matrix[2][1]));
               n = n-1;
            elif(floor(int(Equation)) == 0 & Equation < 0.0009):
               Eigen_Values.append(Equation);                  
      root_1 = float(Eigen_Values[0]);
      D = 0.0; E = 0.0; F = 0.0; G = 0.0;
      D = Hessian_Matrix[0][0]+Hessian_Matrix[1][1]+Hessian_Matrix[2][2]-root_1;
      E = (-1*(Hessian_Matrix[0][0]*Hessian_Matrix[1][1]*Hessian_Matrix[2][2]+Hessian_Matrix[0][1]*Hessian_Matrix[1][2]*Hessian_Matrix[2][0]+Hessian_Matrix[0][2]*Hessian_Matrix[1][0]*Hessian_Matrix[2][1])/root_1);
      F = Hessian_Matrix[0][0]-Hessian_Matrix[1][1]-Hessian_Matrix[2][2]+root_1;
      G = (-1*(Hessian_Matrix[0][0]*Hessian_Matrix[1][1]*Hessian_Matrix[2][2]+Hessian_Matrix[0][1]*Hessian_Matrix[1][2]*Hessian_Matrix[2][0]+Hessian_Matrix[0][2]*Hessian_Matrix[1][0]*Hessian_Matrix[2][1])/root_1);
      Equation_1 = (lambda_h - root_1)*(math.pow(lambda_h,2)+(D-root_1)*lambda_h+E);
      Equation_2 = (lambda_h - root_1)*(math.pow(lambda_h,2)+(F+root_1)*lambda_h+E);
      Equation_3 = (lambda_h - root_1)*(math.pow(lambda_h,2)+(D-root_1)*lambda_h-G);
      Equation_4 = (lambda_h - root_1)*(math.pow(lambda_h,2)+(F+root_1)*lambda_h-G);
      if(floor(int(Equation_1)) == 0 & Equation_1 <= 0.0009):
         Eigen_Values.append(Equation_1);
      elif(floor(int(Equation_2)) == 0 & Equation_2 <= 0.0009):
         Eigen_Values.append(Equation_2);
      elif(floor(int(Equation_3)) == 0 & Equation_3 <= 0.0009):
         Eigen_Values.append(Equation_3);
      elif(floor(int(Equation_4)) == 0 & Equation_4 <= 0.0009):
         Eigen_Values.append(Equation_4);
      else:   
         return(Eigen_Values);
      return(Eigen_Values);

   def Compute_Eigen_Vectors(self,Eigen_Values,Hessian_Matrix,Eigen_Vector):
      Vector_3 = 1;
      Vector_2 = (-(Hessian_Matrix[1][2]*Hessian_Matrix[2][0]-Hessian_Matrix[2][2]*Hessian_Matrix[1][0]+Hessian_Matrix[1][0]*Eigen_Values[0])/(Hessian_Matrix[1][1]*Hessian_Matrix[2][0]-Hessian_Matrix[1][0]*Hessian_Matrix[2][1]-Hessian_Matrix[2][0]*Eigen_Values[0]));
      Vector_1 = (-((Hessian_Matrix[2][0]*Hessian_Matrix[0][1]-Hessian_Matrix[2][1]*Hessian_Matrix[0][0])*(Hessian_Matrix[1][2]*Hessian_Matrix[2][0]-Hessian_Matrix[2][2]*Hessian_Matrix[1][0]+Hessian_Matrix[1][0]*Hessian_Matrix[0][0]))-((Hessian_Matrix[2][0]*Hessian_Matrix[0][2]-Hessian_Matrix[2][2]*Hessian_Matrix[0][0]+Eigen_Values[0]*Hessian_Matrix[0][0])*(Hessian_Matrix[1][1]*Hessian_Matrix[2][0]-Hessian_Matrix[1][0]*Hessian_Matrix[2][1]-Eigen_Values[0]*Hessian_Matrix[2][0])))/(Hessian_Matrix[2][0]*Eigen_Values[0]);
      Vector_6 = 1;
      Vector_5 = (-(Hessian_Matrix[1][2]*Hessian_Matrix[2][0]-Hessian_Matrix[2][2]*Hessian_Matrix[1][0]+Hessian_Matrix[1][0]*Eigen_Values[1])/(Hessian_Matrix[1][1]*Hessian_Matrix[2][0]-Hessian_Matrix[1][0]*Hessian_Matrix[2][1]-Hessian_Matrix[2][0]*Eigen_Values[1]));
      Vector_4 = (-((Hessian_Matrix[2][0]*Hessian_Matrix[0][1]-Hessian_Matrix[2][1]*Hessian_Matrix[0][0])*(Hessian_Matrix[1][2]*Hessian_Matrix[2][0]-Hessian_Matrix[2][2]*Hessian_Matrix[1][0]+Hessian_Matrix[1][0]*Hessian_Matrix[0][0]))-((Hessian_Matrix[2][0]*Hessian_Matrix[0][2]-Hessian_Matrix[2][2]*Hessian_Matrix[0][0]+Eigen_Values[1]*Hessian_Matrix[0][0])*(Hessian_Matrix[1][1]*Hessian_Matrix[2][0]-Hessian_Matrix[1][0]*Hessian_Matrix[2][1]-Eigen_Values[1]*Hessian_Matrix[2][0])))/(Hessian_Matrix[2][0]*Eigen_Values[1]);
      Vector_9 = 1;
      Vector_8 = (-(Hessian_Matrix[1][2]*Hessian_Matrix[2][0]-Hessian_Matrix[2][2]*Hessian_Matrix[1][0]+Hessian_Matrix[1][0]*Eigen_Values[2])/(Hessian_Matrix[1][1]*Hessian_Matrix[2][0]-Hessian_Matrix[1][0]*Hessian_Matrix[2][1]-Hessian_Matrix[2][0]*Eigen_Values[2]));
      Vector_7 = (-((Hessian_Matrix[2][0]*Hessian_Matrix[0][1]-Hessian_Matrix[2][1]*Hessian_Matrix[0][0])*(Hessian_Matrix[1][2]*Hessian_Matrix[2][0]-Hessian_Matrix[2][2]*Hessian_Matrix[1][0]+Hessian_Matrix[1][0]*Hessian_Matrix[0][0]))-((Hessian_Matrix[2][0]*Hessian_Matrix[0][2]-Hessian_Matrix[2][2]*Hessian_Matrix[0][0]+Eigen_Values[2]*Hessian_Matrix[0][0])*(Hessian_Matrix[1][1]*Hessian_Matrix[2][0]-Hessian_Matrix[1][0]*Hessian_Matrix[2][1]-Eigen_Values[2]*Hessian_Matrix[2][0])))/(Hessian_Matrix[2][0]*Eigen_Values[2]);
      Eigen_Vectors.append([[Vector_1,Vector_2,Vector_3],[Vector_4,Vector_5,Vector_6],[Vector_7,Vector_8,Vector_9]]);
      return(Eigen_Vectors);

   def __initialization__(self):
      i = 0;
      j = 0;
      lambda_h = 0;
      Hessian_Matrix = [[1,2,3],[4,5,6],[7,8,9]];
      Identity_Matrix = [[1,0,0],[0,1,0],[0,0,1]];
      lambda_h = 'l';
      Equation = "";
      Hessian_Matrix = input("Enter the matrix required to perform Eigen Operations to calculate Eigen Values and Eigen Vector");
      Eigen_Values = [];
      Eigen_Vector = [];
      Eigen_Parameters = [];
      Eigen_Values = self.Compute_Eigen_Values(Hessian_Matrix,Identity_Matrix,i,j,lambda_h,Eigen_Values);
      Eigen_Vector = self.Compute_Eigen_Vector(Eigen_Values,Hessian_Matrix,Eigen_Vector);
      Eigen_Parameters=[[Eigen_Values],[Eigen_Vector]]
      return(Eigen_Parameters);

   Eigen_Parameters_Object = Compute_Eigen_Parameters();
   Eigen_Parameters = [];
   Eigen_Parameters = Eigen_Parameters_Object.__initialization__();
   print(Eigen_Parameters);