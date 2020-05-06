# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()
print(loan_status)
data['Loan_Status'].value_counts().plot.bar()

property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot.bar(stacked=False)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
#Code starts here
education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
property_and_loan.plot.bar()
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)

#Code starts here
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

#fig ,(ax_1,ax_2,ax_3)= plt.subplots(nrows = 3 , ncols = 1, figsize=(20,10))
#plt.plot(data['ApplicantIncome'],data['LoanAmount'],kind='bar', stacked=True, ax=ax_1)

#Code starts here
#Code starts here
fig ,(ax_1,ax_2,ax_3)= plt.subplots(nrows = 3 , ncols = 1, figsize=(20,10))
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Applicant Income')
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')
#ax_2.scatter(data['CoapplicantIncome'],data['CoacantIncomeppli'])#
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
#print(data['TotalIncome'][1] == 6091)
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_3.set_title('Total Income')
plt.show()


