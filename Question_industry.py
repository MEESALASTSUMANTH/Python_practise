# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:08:36 2022

@author: suman
"""
#this code is about how to use inheritance 
#And how to create object array 
#while using the switch case and through switches we can perform some actions
#And also we read and write input and outputs in files

#In this question industry is a parent and company is child
class industry():
    def __init__(self,name,company_count_under_industry,countryoforigin):
        self.name = name
        self.company_count_under_industry = company_count_under_industry
        self.countryoforigin = countryoforigin
    
    def display(self):
        print("name of the industry:",self.name)
        print("company count under industry :",self.company_count_under_industry)
        print("country of origin :",self.countryoforigin)
        
class company(industry):
    def __init__(self,Cname,noofemp,baselocation,parentindustry,name, company_count_under_industry, countryoforigin):
        industry.__init__(self, name, company_count_under_industry, countryoforigin)
        self.Cname = Cname
        self.noofemp = noofemp
        self.baselocation = baselocation
        self.parentindustry = parentindustry
    def display1(self):
        print("company name :",self.Cname)
        print("no of employees",self.noofemp)
        print("base location :",self.baselocation)
        print("parent industry :",self.name)
        

A=[]
B=[]
def addition_of_industry():
    ind_name = str(input("name of the industry :"))
    com_count = int(input("count of company under industry :"))
    cou_origin = str(input("country of origin :"))
    A.append(industry(ind_name,com_count,cou_origin))

def addition_of_company():
    
    cname = str(input("name of the company :"))
    noe   = int(input("no of employees:"))
    bloca = str(input(" base location of company :"))
    parent = str(input("parent industry :"))
    if(checking_industry_name(parent)!= None):
        obj =checking_industry_name(parent)
        obj.company_count_under_industry = obj.company_count_under_industry +1
        B.append(company(cname,noe,bloca,parent,obj.name,obj.company_count_under_industry,obj.countryoforigin))
        return True
    else:
        print("invalid company ,invalid industry")
        return False

    
        
def checking_industry_name(parent):
    
    for i in range(0,len(A)):
        # A[i].company_count_under_industry = A[i].company_count_under_industry + 1
        
        if(parent==A[i].name):
            return A[i]
    
    return None

def display_industry():
    for i in range(0,len(A)):
            print(A[i].name,A[i].company_count_under_industry,A[i].countryoforigin)
  

def display_company():
    for j in range(0,len(B)):
        print(B[j].Cname,B[j].noofemp,B[j].baselocation,B[j].name,B[j].company_count_under_industry,B[j].countryoforigin)
    
def Industry_read():
    file1 = open("Industry.txt","r")
    print(file1.read())
    file1.close()
def Company_read():
    file2 = open("company.txt","r")
    print(file2.read())
    file2.close()
def Industry_write(A):
    with open("Industry.txt","w") as file1:
        file1.writelines(A)
        file1.close()
def company_write(A):
    with open("company.txt","w") as file2:
        file2.writelines(B)
        file2.close()
while(True):
    print("choose one option below and press number")
    print("1.Add Industry \n","2.Add company \n","3.display industry\n","4.display company\n","5.reading industry  from file\n","6.reading companies  from file\n","7.writing in industry file\n","8.writing the company file\n","9.exit")
    i = int(input("enter your choice :"))
    if(i==0):
        print("thank you")
        break
    elif(i==1):
        addition_of_industry()
        print("industry added succesfully")
    elif(i==2):
        if(addition_of_company()):
            print("company added succesfully")
        else:
            print("company addition unsuccesfull")
    elif(i==3):
        display_industry()
        
    elif(i==4):
        display_company()
    elif(i==5):
        Industry_read() 
    elif(i==6):
        Company_read()
       
    elif(i==7):
        Industry_write(str(A))
        
    elif(i==8):
        company_write(str(B))
        
    else:
        break

