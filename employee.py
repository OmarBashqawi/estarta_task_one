import pandas as pd
import numpy as np


df = pd.read_excel("Employee Sample Data - A.xlsx")

#check duplicates
print(df.duplicated().sum())
# There is no Duplicates

# Replace null values with values
#For FullName Column
df["Full Name"].fillna("unkown", inplace= True)

#For Job Title
Job = df["Job Title"].mode()[0]
df["Job Title"].fillna(Job, inplace= True)

#For Department 
Department = df["Department"].mode()[0]
df["Department"].fillna(Department, inplace= True)

#For Gendar
Gender = df["Gender"].mode()[0]
df["Gender"].fillna(Gender,inplace = True)

#For Ethnicity
for x in df.index:
    if pd.isna(df.loc[x, "Ethnicity"]) or df.loc[x, "Ethnicity"].strip() == "":
        if df.loc[x, "Country"] == "China":
            df.loc[x, "Ethnicity"] = "Asian"
        elif df.loc[x, "Country"] =="Brazil":
            df.loc[x, "Ethnicity"] = "Latino"
        else:
            df.loc[x, "Ethnicity"] = "Not Provided"
            
#For Age 
age = df["Age"].mean()
df["Age"].fillna(age, inplace = True)

#For Hiredate
df["Hire Date"].fillna("Not Provided", inplace = True)

#for Annual Salary
annual = df["Annual Salary"].median()
df["Annual Salary"].fillna(annual, inplace = True)

# For Bouns%
bonus = df["Bonus %"].mean()
df["Bonus %"].fillna(bonus, inplace = True)

# For Country
df["Country"].fillna("United States", inplace = True)

#For City
for x in df.index:
    if pd.isna(df.loc[x, "City"]) or df.loc[x, "City"].strip() == "":
        if df.loc[x, "Country"] == "United States" and df.loc[x, "Ethnicity"] == "Caucasian":
            city = df["City"].mode()[0]
            df["City"].fillna(city, inplace = True)
        
#For Exit Date
df["Exit Date"].fillna("Still working", inplace = True)
print("\nTable Info: ")
print(df.info())

#Row with the largest salary
largest_salary = df.loc[df["Annual Salary"].idxmax()]
print("\nLargest_Salary: ")
print(largest_salary)

#Groupby Department to find Avg age and salary
print("\nAvrage age and Salary for Department: ")
avg_age_salary = df.groupby("Department")[["Age","Annual Salary"]].mean()
print(avg_age_salary)

#Groupby Department and Ethnicity to find max_age, min_Age and median_salary
print("\nMaximum age,Minimum age and Median salary: ")
agg = df.groupby(["Department", "Ethnicity"])[["Age", "Annual Salary"]].agg(
    max_age =("Age", "max"),
    min_age =("Age", "min"),
    avg_salary =("Annual Salary", "median"))
print(agg)

# Save the cleaned data to a new Excel file
df.to_excel("Cleaned_Employee_Data.xlsx", index=False)


