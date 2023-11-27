import pandas as pd
import numpy as np
import os
import json
os.getcwd()
os.chdir('C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\CS6603')
print(os.getcwd())
### step 1: read data
df = pd.read_csv("Application_Data.csv", sep=",")
df_Step1 = df[["Applicant_Gender", "Applicant_Age","Total_Income","Years_of_Working","Status"]]
print(df_Step1.head())
### step 2
df_Step2 = df_Step1.copy()
### step 2.1
df_Step2.loc[df['Applicant_Gender'] =='M      ', 'Applicant_Gender'] = 1
df_Step2.loc[df['Applicant_Gender'] =='F      ', 'Applicant_Gender'] = 0
df_Step2.loc[df['Applicant_Age'] >= 40, 'Applicant_Age'] = 0
df_Step2.loc[df['Applicant_Age'] < 40, 'Applicant_Age'] = 1
print(df_Step2.head())
df_Step2[df_Step2["Applicant_Gender"] == 1].count()
df_Step2[df_Step2["Applicant_Gender"] == 0].count()
df_Step2[df_Step2["Applicant_Age"] == 1].count()
df_Step2[df_Step2["Applicant_Age"] == 0].count()

### step 2.2
Threshold_1 = 10
df_Step2[df_Step2["Years_of_Working"] >= Threshold_1].count()
df_Step2[df_Step2["Years_of_Working"] < Threshold_1].count()
Threshold_2 = 300000
df_Step2[df_Step2["Total_Income"] >= Threshold_2].count()
df_Step2[df_Step2["Total_Income"] < Threshold_2].count()
Threshold_3 = 1
df_Step2[df_Step2["Status"] == Threshold_3].count()
df_Step2[df_Step2["Status"] != Threshold_3].count()

### Step 2.3 Histogram for Each Protected Class Variable
import matplotlib.pyplot as plt
df_Step2[(df_Step2["Applicant_Gender"] == 1)&(df_Step2["Years_of_Working"] >= Threshold_1)].count()
df_Step2[(df_Step2["Applicant_Gender"] == 0)&(df_Step2["Years_of_Working"] >= Threshold_1)].count()
df_Step2[(df_Step2["Applicant_Gender"] == 1)&(df_Step2["Years_of_Working"] < Threshold_1)].count()
df_Step2[(df_Step2["Applicant_Gender"] == 0)&(df_Step2["Years_of_Working"] < Threshold_1)].count()

# draw histogram for gender: male, female and years of working: >= 10, < 10



##############################################################
df_Step2[(df_Step2["Applicant_Gender"] == 1)&(df_Step2["Total_Income"] >= Threshold_2)].count()
df_Step2[(df_Step2["Applicant_Gender"] == 0)&(df_Step2["Total_Income"] >= Threshold_2)].count()
df_Step2[(df_Step2["Applicant_Gender"] == 1)&(df_Step2["Total_Income"] < Threshold_2)].count()
df_Step2[(df_Step2["Applicant_Gender"] == 0)&(df_Step2["Total_Income"] < Threshold_2)].count()
df_Step2[(df_Step2["Applicant_Gender"] == 1)&(df_Step2["Status"] == 1)].count()
df_Step2[(df_Step2["Applicant_Gender"] == 0)&(df_Step2["Status"] == 0)].count()
##############################################################
df_Step2[(df_Step2["Applicant_Age"] == 1)&(df_Step2["Years_of_Working"] >= Threshold_1)].count()
df_Step2[(df_Step2["Applicant_Age"] == 0)&(df_Step2["Years_of_Working"] >= Threshold_1)].count()
df_Step2[(df_Step2["Applicant_Age"] == 1)&(df_Step2["Years_of_Working"] < Threshold_1)].count()
df_Step2[(df_Step2["Applicant_Age"] == 0)&(df_Step2["Years_of_Working"] < Threshold_1)].count()
##############################################################
df_Step2[(df_Step2["Applicant_Age"] == 1)&(df_Step2["Total_Income"] >= Threshold_2)].count()
df_Step2[(df_Step2["Applicant_Age"] == 0)&(df_Step2["Total_Income"] >= Threshold_2)].count()
df_Step2[(df_Step2["Applicant_Age"] == 1)&(df_Step2["Total_Income"] < Threshold_2)].count()
df_Step2[(df_Step2["Applicant_Age"] == 0)&(df_Step2["Total_Income"] < Threshold_2)].count()
df_Step2[(df_Step2["Applicant_Age"] == 1)&(df_Step2["Status"] == 1)].count()
df_Step2[(df_Step2["Applicant_Age"] == 0)&(df_Step2["Status"] == 0)].count()
### step3
df_Step3 = df_Step2.copy()
# Calculate fairness metrics
# Protected class: sex
# privileged sex group (male) == 1
# unprivileged sex group (female) == 0
# Metric 1: Disparate Impact
# Metric 2: Statistical Parity Difference

# dependent variable 1: Years_of_Working
Threshold_1 = 10
Original_sex_privileged_working = df_Step3[df_Step3["Applicant_Gender"] == 1].count()
Original_sex_privileged_good_working = df_Step3[(df_Step3["Applicant_Gender"] == 1)&(df_Step3["Years_of_Working"] >= Threshold_1)].count()
Original_sex_privileged_bad_working = df_Step3[(df_Step3["Applicant_Gender"] == 1)&(df_Step3["Years_of_Working"] < Threshold_1)].count()
Original_sex_unprivileged_working = df_Step3[df_Step3["Applicant_Gender"] == 0].count()
Original_sex_unprivileged_good_working = df_Step3[(df_Step3["Applicant_Gender"] == 0)&(df_Step3["Years_of_Working"] >= Threshold_1)].count()
Original_sex_unprivileged_bad_working = df_Step3[(df_Step3["Applicant_Gender"] == 0)&(df_Step3["Years_of_Working"] < Threshold_1)].count()

Original_sex_disparate_impact_working = (Original_sex_unprivileged_good_working[0] / (Original_sex_unprivileged_working[0])) / (Original_sex_privileged_good_working[0] / (Original_sex_privileged_working[0]))
Original_sex_statistical_parity_difference_working = (Original_sex_unprivileged_good_working[0] / (Original_sex_unprivileged_working[0])) - (Original_sex_privileged_good_working[0] / (Original_sex_privileged_working[0]))
print('Original_sex_Years_of_Working - disparate_impact:',Original_sex_disparate_impact_working)
print('Original_sex_Years_of_Working - statistical_parity_difference:',Original_sex_statistical_parity_difference_working)
# dependent variable 3: Status
Original_sex_privileged_working = df_Step3[df_Step3["Applicant_Gender"] == 1].count()
Original_sex_privileged_good_working = df_Step3[(df_Step3["Applicant_Gender"] == 1)&(df_Step3["Status"] ==1)].count()
Original_sex_privileged_bad_working = df_Step3[(df_Step3["Applicant_Gender"] == 1)&(df_Step3["Status"] ==0)].count()
Original_sex_unprivileged_working = df_Step3[df_Step3["Applicant_Gender"] == 0].count()
Original_sex_unprivileged_good_working = df_Step3[(df_Step3["Applicant_Gender"] == 0)&(df_Step3["Status"] == 1)].count()
Original_sex_unprivileged_bad_working = df_Step3[(df_Step3["Applicant_Gender"] == 0)&(df_Step3["Status"] ==0)].count()

Original_sex_disparate_impact_working = (Original_sex_unprivileged_good_working[0] / (Original_sex_unprivileged_working[0])) / (Original_sex_privileged_good_working[0] / (Original_sex_privileged_working[0]))
Original_sex_statistical_parity_difference_working = (Original_sex_unprivileged_good_working[0] / (Original_sex_unprivileged_working[0])) - (Original_sex_privileged_good_working[0] / (Original_sex_privileged_working[0]))
print('Original_sex_Years_of_Working - disparate_impact:',Original_sex_disparate_impact_working)
print('Original_sex_Years_of_Working - statistical_parity_difference:',Original_sex_statistical_parity_difference_working)

# dependent variable 2: Total_Income
Threshold_2 = 300000
Original_sex_privileged_income = df_Step3[df_Step3["Applicant_Gender"] == 1].count()
Original_sex_privileged_good_income = df_Step3[(df_Step3["Applicant_Gender"] == 1)&(df_Step3["Total_Income"] >= Threshold_2)].count()
Original_sex_privileged_bad_income = df_Step3[(df_Step3["Applicant_Gender"] == 1)&(df_Step3["Total_Income"] < Threshold_2)].count()
Original_sex_unprivileged_income = df_Step3[df_Step3["Applicant_Gender"] == 0].count()
Original_sex_unprivileged_good_income = df_Step3[(df_Step3["Applicant_Gender"] == 0)&(df_Step3["Total_Income"] >= Threshold_2)].count()
Original_sex_unprivileged_bad_income = df_Step3[(df_Step3["Applicant_Gender"] == 0)&(df_Step3["Total_Income"] < Threshold_2)].count()

Original_sex_disparate_impact_income = (Original_sex_unprivileged_good_income[0] / (Original_sex_unprivileged_income[0])) / (Original_sex_privileged_good_income[0] / (Original_sex_privileged_income[0]))
Original_sex_statistical_parity_difference_income = (Original_sex_unprivileged_good_income[0] / (Original_sex_unprivileged_income[0])) - (Original_sex_privileged_good_income[0] / (Original_sex_privileged_income[0]))
print('Original_sex_Total_Income - disparate_impact:',Original_sex_disparate_impact_income)
print('Original_sex_Total_Income - statistical_parity_difference:',Original_sex_statistical_parity_difference_income)
#print(Original_sex_privileged_good[0],Original_sex_privileged_bad[0],Original_sex_unprivileged_good[0],Original_sex_unprivileged_bad[0])


# Calculate fairness metrics
# Protected class: age
# privileged age group (age >= 40) == 0
# unprivileged age group (age < 40) == 1
# Metric 1: Disparate Impact
# Metric 2: Statistical Parity Difference

# dependent variable 1: Years_of_Working
Original_age_privileged_working = df_Step3[df_Step3["Applicant_Age"] == 0].count()
Original_age_privileged_good_working = df_Step3[(df_Step3["Applicant_Age"] == 0)&(df_Step3["Years_of_Working"] >= Threshold_1)].count()
Original_age_privileged_bad_working = df_Step3[(df_Step3["Applicant_Age"] == 0)&(df_Step3["Years_of_Working"] < Threshold_1)].count()
Original_age_unprivileged_working = df_Step3[df_Step3["Applicant_Age"] == 1].count()
Original_age_unprivileged_good_working = df_Step3[(df_Step3["Applicant_Age"] == 1)&(df_Step3["Years_of_Working"] >= Threshold_1)].count()
Original_age_unprivileged_bad_working = df_Step3[(df_Step3["Applicant_Age"] == 1)&(df_Step3["Years_of_Working"] < Threshold_1)].count()

Original_age_disparate_impact_working = (Original_age_unprivileged_good_working[0] / (Original_age_unprivileged_working[0])) / (Original_age_privileged_good_working[0] / (Original_age_privileged_working[0]))
Original_age_statistical_parity_difference_working = (Original_age_unprivileged_good_working[0] / (Original_age_unprivileged_working[0])) - (Original_age_privileged_good_working[0] / (Original_age_privileged_working[0]))
print('Original_age_Years_of_Working - disparate_impact:',Original_age_disparate_impact_working)
print('Original_age_Years_of_Working - statistical_parity_difference:',Original_age_statistical_parity_difference_working)

# dependent variable 2: Total_Income
Original_age_privileged_income = df_Step3[df_Step3["Applicant_Age"] == 0].count()
Original_age_privileged_good_income = df_Step3[(df_Step3["Applicant_Age"] == 0)&(df_Step3["Total_Income"] >= Threshold_2)].count()
Original_age_privileged_bad_income = df_Step3[(df_Step3["Applicant_Age"] == 0)&(df_Step3["Total_Income"] < Threshold_2)].count()
Original_age_unprivileged_income = df_Step3[df_Step3["Applicant_Age"] == 1].count()
Original_age_unprivileged_good_income = df_Step3[(df_Step3["Applicant_Age"] == 1)&(df_Step3["Total_Income"] >= Threshold_2)].count()
Original_age_unprivileged_bad_income = df_Step3[(df_Step3["Applicant_Age"] == 1)&(df_Step3["Total_Income"] < Threshold_2)].count()

Original_age_disparate_impact_income = (Original_age_unprivileged_good_income[0] / (Original_age_unprivileged_income[0])) / (Original_age_privileged_good_income[0] / (Original_age_privileged_income[0]))
Original_age_statistical_parity_difference_income = (Original_age_unprivileged_good_income[0] / (Original_age_unprivileged_income[0])) - (Original_age_privileged_good_income[0] / (Original_age_privileged_income[0]))
print('Original_age_Total_Income - disparate_impact:',Original_age_disparate_impact_income)
print('Original_age_Total_Income - statistical_parity_difference:',Original_age_statistical_parity_difference_income)


# Resample/reweighting the dataset
df_temp = df_Step3.copy()
sample_thrshold_1 = 0.7
sample_thrshold_2 = 0.7
sample_thrshold_3 = 0.6
sample_thrshold_4 = 0.9
Flag = []
for ind, row in df_temp.iterrows():
    if row['Applicant_Gender'] == 1 and row['Total_Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_1:
            Flag.append(0)
            continue
    if row['Applicant_Gender'] == 0 and row['Years_of_Working'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_2:
            Flag.append(0)
            continue
    if row['Applicant_Age'] == 0 and row['Years_of_Working'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_3:
            Flag.append(0)
            continue
    if row['Applicant_Age'] == 0 and row['Total_Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_4:
            Flag.append(0)
            continue
    Flag.append(1)
df_temp['resample'] = Flag
df_temp = df_temp[df_temp['resample'] == 1]
df_Step3_Trans = df_temp.copy()
print(sum(Flag) / len(Flag))

# Calculate fairness metrics
# Protected class: sex
# privileged sex group (male) == 1
# unprivileged sex group (female) == 0
# Metric 1: Disparate Impact
# Metric 2: Statistical Parity Difference

# dependent variable 1: Years_of_Working
Trans_sex_privileged_working = df_Step3_Trans[df_Step3_Trans["Applicant_Gender"] == 1].count()
Trans_sex_privileged_good_working = df_Step3_Trans[(df_Step3_Trans["Applicant_Gender"] == 1)&(df_Step3_Trans["Years_of_Working"] >= Threshold_1)].count()
Trans_sex_privileged_bad_working = df_Step3_Trans[(df_Step3_Trans["Applicant_Gender"] == 1)&(df_Step3_Trans["Years_of_Working"] < Threshold_1)].count()
Trans_sex_unprivileged_working = df_Step3_Trans[df_Step3_Trans["Applicant_Gender"] == 0].count()
Trans_sex_unprivileged_good_working = df_Step3_Trans[(df_Step3_Trans["Applicant_Gender"] == 0)&(df_Step3_Trans["Years_of_Working"] >= Threshold_1)].count()
Trans_sex_unprivileged_bad_working = df_Step3_Trans[(df_Step3_Trans["Applicant_Gender"] == 0)&(df_Step3_Trans["Years_of_Working"] < Threshold_1)].count()

Trans_sex_disparate_impact_working = (Trans_sex_unprivileged_good_working[0] / (Trans_sex_unprivileged_working[0])) / (Trans_sex_privileged_good_working[0] / (Trans_sex_privileged_working[0]))
Trans_sex_statistical_parity_difference_working = (Trans_sex_unprivileged_good_working[0] / (Trans_sex_unprivileged_working[0])) - (Trans_sex_privileged_good_working[0] / (Trans_sex_privileged_working[0]))
print('Trans_sex_Years_of_Working - disparate_impact:',Trans_sex_disparate_impact_working)
print('Trans_sex_Years_of_Working - statistical_parity_difference:',Trans_sex_statistical_parity_difference_working)

# dependent variable 2: Total_Income
Trans_sex_privileged_income = df_Step3_Trans[df_Step3_Trans["Applicant_Gender"] == 1].count()
Trans_sex_privileged_good_income = df_Step3_Trans[(df_Step3_Trans["Applicant_Gender"] == 1)&(df_Step3_Trans["Total_Income"] >= Threshold_2)].count()
Trans_sex_privileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Applicant_Gender"] == 1)&(df_Step3_Trans["Total_Income"] < Threshold_2)].count()
Trans_sex_unprivileged_income = df_Step3_Trans[df_Step3_Trans["Applicant_Gender"] == 0].count()
Trans_sex_unprivileged_good_income = df_Step3_Trans[(df_Step3_Trans["Applicant_Gender"] == 0)&(df_Step3_Trans["Total_Income"] >= Threshold_2)].count()
Trans_sex_unprivileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Applicant_Gender"] == 0)&(df_Step3_Trans["Total_Income"] < Threshold_2)].count()

Trans_sex_disparate_impact_income = (Trans_sex_unprivileged_good_income[0] / (Trans_sex_unprivileged_income[0])) / (Trans_sex_privileged_good_income[0] / (Trans_sex_privileged_income[0]))
Trans_sex_statistical_parity_difference_income = (Trans_sex_unprivileged_good_income[0] / (Trans_sex_unprivileged_income[0])) - (Trans_sex_privileged_good_income[0] / (Trans_sex_privileged_income[0]))
print('Trans_sex_Total_Income - disparate_impact:',Trans_sex_disparate_impact_income)
print('Trans_sex_Total_Income - statistical_parity_difference:',Trans_sex_statistical_parity_difference_income)
#print(Trans_sex_privileged_good[0],Trans_sex_privileged_bad[0],Trans_sex_unprivileged_good[0],Trans_sex_unprivileged_bad[0])



# Calculate fairness metrics
# Protected class: age
# privileged age group (age >= 40) == 0
# unprivileged age group (age < 40) == 1
# Metric 1: Disparate Impact
# Metric 2: Statistical Parity Difference

# dependent variable 1: Years_of_Working
Trans_age_privileged_working = df_Step3_Trans[df_Step3_Trans["Applicant_Age"] == 0].count()
Trans_age_privileged_good_working = df_Step3_Trans[(df_Step3_Trans["Applicant_Age"] == 0)&(df_Step3_Trans["Years_of_Working"] >= Threshold_1)].count()
Trans_age_privileged_bad_working = df_Step3_Trans[(df_Step3_Trans["Applicant_Age"] == 0)&(df_Step3_Trans["Years_of_Working"] < Threshold_1)].count()
Trans_age_unprivileged_working = df_Step3_Trans[df_Step3_Trans["Applicant_Age"] == 1].count()
Trans_age_unprivileged_good_working = df_Step3_Trans[(df_Step3_Trans["Applicant_Age"] == 1)&(df_Step3_Trans["Years_of_Working"] >= Threshold_1)].count()
Trans_age_unprivileged_bad_working = df_Step3_Trans[(df_Step3_Trans["Applicant_Age"] == 1)&(df_Step3_Trans["Years_of_Working"] < Threshold_1)].count()

Trans_age_disparate_impact_working = (Trans_age_unprivileged_good_working[0] / (Trans_age_unprivileged_working[0])) / (Trans_age_privileged_good_working[0] / (Trans_age_privileged_working[0]))
Trans_age_statistical_parity_difference_working = (Trans_age_unprivileged_good_working[0] / (Trans_age_unprivileged_working[0])) - (Trans_age_privileged_good_working[0] / (Trans_age_privileged_working[0]))
print('Trans_age_Years_of_Working - disparate_impact:',Trans_age_disparate_impact_working)
print('Trans_age_Years_of_Working - statistical_parity_difference:',Trans_age_statistical_parity_difference_working)

# dependent variable 2: Total_Income
Trans_age_privileged_income = df_Step3_Trans[df_Step3_Trans["Applicant_Age"] == 0].count()
Trans_age_privileged_good_income = df_Step3_Trans[(df_Step3_Trans["Applicant_Age"] == 0)&(df_Step3_Trans["Total_Income"] >= Threshold_2)].count()
Trans_age_privileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Applicant_Age"] == 0)&(df_Step3_Trans["Total_Income"] < Threshold_2)].count()
Trans_age_unprivileged_income = df_Step3_Trans[df_Step3_Trans["Applicant_Age"] == 1].count()
Trans_age_unprivileged_good_income = df_Step3_Trans[(df_Step3_Trans["Applicant_Age"] == 1)&(df_Step3_Trans["Total_Income"] >= Threshold_2)].count()
Trans_age_unprivileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Applicant_Age"] == 1)&(df_Step3_Trans["Total_Income"] < Threshold_2)].count()

Trans_age_disparate_impact_income = (Trans_age_unprivileged_good_income[0] / (Trans_age_unprivileged_income[0])) / (Trans_age_privileged_good_income[0] / (Trans_age_privileged_income[0]))
Trans_age_statistical_parity_difference_income = (Trans_age_unprivileged_good_income[0] / (Trans_age_unprivileged_income[0])) - (Trans_age_privileged_good_income[0] / (Trans_age_privileged_income[0]))
print('Trans_age_Total_Income - disparate_impact:',Trans_age_disparate_impact_income)
print('Trans_age_Total_Income - statistical_parity_difference:',Trans_age_statistical_parity_difference_income)


### Step 3 Summary
protected_class_col = ['sex', 'sex', 'age', 'age', 'sex', 'sex', 'age', 'age']
dependent_varibale_col = ['years of working', 'total income', 'years of working', 'total income', 'years of working', 'total income', 'years of working', 'total income']
metrics_col = ['disparate impact', 'disparate impact', 'disparate impact', 'disparate impact', 'statistical parity', 'statistical parity', 'statistical parity', 'statistical parity']
original_metrics = [Original_sex_disparate_impact_working, Original_sex_disparate_impact_income, Original_age_disparate_impact_working, Original_age_disparate_impact_income,Original_sex_statistical_parity_difference_working, Original_sex_statistical_parity_difference_income, Original_age_statistical_parity_difference_working, Original_age_statistical_parity_difference_income]
trans_metrics = [Trans_sex_disparate_impact_working, Trans_sex_disparate_impact_income, Trans_age_disparate_impact_working, Trans_age_disparate_impact_income, Trans_sex_statistical_parity_difference_working, Trans_sex_statistical_parity_difference_income, Trans_age_statistical_parity_difference_working, Trans_age_statistical_parity_difference_income]
summary_step3 = list(zip(protected_class_col, dependent_varibale_col, metrics_col, original_metrics,trans_metrics))
pd.DataFrame(summary_step3, columns = ['Protected Class', 'Dependent Variable', 'Fairness', 'Original Metric', 'Transformed Metric'])

### Step 4
### Preprocessing and random split
df_step4_X = df[['Owned_Car','Owned_Realty', 'Total_Children', 'Income_Type', 'Education_Type', 'Family_Status', 'Housing_Type', 'Owned_Mobile_Phone', 'Owned_Work_Phone', 'Owned_Phone', 'Owned_Email', 'Job_Title', 'Total_Family_Members', 'Applicant_Age', 'Total_Bad_Debt', 'Total_Good_Debt', 'Status']]
df_step4_y = df.Total_Income


# Resample/reweighting the dataset
df_temp = df.copy()
sample_thrshold_1 = 0.7
sample_thrshold_2 = 0.7
sample_thrshold_3 = 0.6
sample_thrshold_4 = 0.9
Flag = []
for ind, row in df_temp.iterrows():
    if row['Applicant_Gender'] == 1 and row['Total_Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_1:
            Flag.append(0)
            continue
    if row['Applicant_Gender'] == 0 and row['Years_of_Working'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_2:
            Flag.append(0)
            continue
    if row['Applicant_Age'] >= 40 and row['Years_of_Working'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_3:
            Flag.append(0)
            continue
    if row['Applicant_Age'] >= 40 and row['Total_Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_4:
            Flag.append(0)
            continue
    Flag.append(1)
df_temp['resample'] = Flag
df_temp = df_temp[df_temp['resample'] == 1]

df_step4_trans_X = df_temp[['Owned_Car','Owned_Realty', 'Total_Children', 'Income_Type', 'Education_Type', 'Family_Status', 'Housing_Type', 'Owned_Mobile_Phone', 'Owned_Work_Phone', 'Owned_Phone', 'Owned_Email', 'Job_Title', 'Total_Family_Members', 'Applicant_Age', 'Total_Bad_Debt', 'Total_Good_Debt', 'Status']]
df_step4_trans_y = df_temp.Total_Income

print(sum(Flag) / len(Flag))

from sklearn.preprocessing import LabelEncoder

enc = LabelEncoder()

def encode(df):
    for col in df.columns:
        if df[col].dtype == object:  # Checks if the column is of object type
            df[col] = enc.fit_transform(df[col])
    return df

df_step4_X_enc = encode(df_step4_X.copy())
df_step4_X_trans_enc = encode(df_step4_trans_X.copy())


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_step4_X_enc, df_step4_y, test_size=0.2, random_state=42)
X_train_trans, X_test_trans, y_train_trans, y_test_trans = train_test_split(df_step4_X_trans_enc, df_step4_trans_y, test_size=0.33, random_state=42)

### train classifier
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

model_trans = DecisionTreeRegressor(random_state=1)
model_trans.fit(X_train_trans, y_train_trans)
y_pred_trans = model_trans.predict(X_test_trans)
