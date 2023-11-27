import os
import json
import pandas as pd
os.getcwd()
os.chdir('C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\CS6603')
print(os.getcwd())

#step 1: read in the data
df = pd.read_csv("adult.csv", sep=",")
df.head()
df_Step1 = df[["Gender", "Age","Income","EducationNum"]]
df_Step1.head()

#step 2: convert the data into json format
df_Step2 = df_Step1.copy()
#step 2.1
df_Step2.loc[df['Gender'] ==' Male', 'Gender'] = 1
df_Step2.loc[df['Gender'] ==' Female', 'Gender'] = 0
df_Step2.loc[df['Age'] >= 40, 'Age'] = 0
df_Step2.loc[df['Age'] < 40, 'Age'] = 1
df_Step2.head()

df_Step2[df_Step2["Gender"] == 1].count()
df_Step2[df_Step2["Gender"] == 0].count()
df_Step2[df_Step2["Age"] == 1].count()
df_Step2[df_Step2["Age"] == 0].count()

#step 2.2
Threshold_1 = 13
df_Step2[df_Step2["EducationNum"] >= Threshold_1].count()
df_Step2[df_Step2["EducationNum"] < Threshold_1].count()
Threshold_2 = " <=50K"
df_Step2[df_Step2["Income"] == Threshold_2].count()
Threshold_2 = " >50K"
df_Step2[df_Step2["Income"] == Threshold_2].count()
# Step 2.3 Histogram for Each Protected Class Variable
df_Step2[(df_Step2["Gender"] == 1)&(df_Step2["EducationNum"] >= Threshold_1)].count()
df_Step2[(df_Step2["Gender"] == 0)&(df_Step2["EducationNum"] >= Threshold_1)].count()
df_Step2[(df_Step2["Gender"] == 1)&(df_Step2["EducationNum"] < Threshold_1)].count()
df_Step2[(df_Step2["Gender"] == 0)&(df_Step2["EducationNum"] < Threshold_1)].count()
df_Step2[(df_Step2["Gender"] == 1)&(df_Step2["Income"] >= Threshold_2)].count()
df_Step2[(df_Step2["Gender"] == 0)&(df_Step2["Income"] >= Threshold_2)].count()
df_Step2[(df_Step2["Gender"] == 1)&(df_Step2["Income"] < Threshold_2)].count()
df_Step2[(df_Step2["Gender"] == 0)&(df_Step2["Income"] < Threshold_2)].count()
df_Step2[(df_Step2["Age"] == 1)&(df_Step2["EducationNum"] >= Threshold_1)].count()
df_Step2[(df_Step2["Age"] == 0)&(df_Step2["EducationNum"] >= Threshold_1)].count()
df_Step2[(df_Step2["Age"] == 1)&(df_Step2["EducationNum"] < Threshold_1)].count()
df_Step2[(df_Step2["Age"] == 0)&(df_Step2["EducationNum"] < Threshold_1)].count()
df_Step2[(df_Step2["Age"] == 1)&(df_Step2["Income"] >= Threshold_2)].count()
df_Step2[(df_Step2["Age"] == 0)&(df_Step2["Income"] >= Threshold_2)].count()
df_Step2[(df_Step2["Age"] == 1)&(df_Step2["Income"] < Threshold_2)].count()
df_Step2[(df_Step2["Age"] == 0)&(df_Step2["Income"] < Threshold_2)].count()

import matplotlib.pyplot as plt

# Thresholds
Threshold_1 = 13  # Threshold for EducationNum
Threshold_2 = " >50K"  # Assuming " >50K" indicates higher income category

# Create a figure with subplots
plt.figure(figsize=(12, 8))

# Histogram for EducationNum by Gender
plt.subplot(2, 2, 1)
df_Step2[df_Step2["Gender"] == 1]['EducationNum'].plot(kind='hist', alpha=0.5, bins=10, label='Male')
df_Step2[df_Step2["Gender"] == 0]['EducationNum'].plot(kind='hist', alpha=0.5, bins=10, label='Female')
plt.axvline(Threshold_1, color='red', linestyle='dashed', linewidth=1)
plt.title("EducationNum by Gender")
plt.xlabel("EducationNum (Years of Education)")
plt.ylabel("Count")
plt.legend()

# Histogram for EducationNum by Age
plt.subplot(2, 2, 2)
df_Step2[df_Step2["Age"] == 1]['EducationNum'].plot(kind='hist', alpha=0.5, bins=10, label='<40')
df_Step2[df_Step2["Age"] == 0]['EducationNum'].plot(kind='hist', alpha=0.5, bins=10, label='>=40')
plt.axvline(Threshold_1, color='red', linestyle='dashed', linewidth=1)
plt.title("EducationNum by Age")
plt.xlabel("EducationNum (Years of Education)")
plt.ylabel("Count")
plt.legend()

# Histogram for Income by Gender
plt.subplot(2, 2, 3)
df_Step2[df_Step2["Gender"] == 1]['Income'].value_counts().plot(kind='bar', label='Male', alpha=0.5)
df_Step2[df_Step2["Gender"] == 0]['Income'].value_counts().plot(kind='bar', label='Female', color='orange', alpha=0.5)
plt.title("Income by Gender")
plt.xlabel("Income")
plt.ylabel("Count")
plt.legend()

# Histogram for Income by Age
plt.subplot(2, 2, 4)
df_Step2[df_Step2["Age"] == 1]['Income'].value_counts().plot(kind='bar', label='<40', alpha=0.5)
df_Step2[df_Step2["Age"] == 0]['Income'].value_counts().plot(kind='bar', label='>=40', color='green', alpha=0.5)
plt.title("Income by Age")
plt.xlabel("Income")
plt.ylabel("Count")
plt.legend()

# Adjust the layout
plt.tight_layout()

# Display the plots
plt.show()
# step 3
df_Step3 = df_Step2.copy()
# Calculate fairness metrics
# Protected class: sex
# privileged sex group (male) == 1
# unprivileged sex group (female) == 0
# Metric 1: Disparate Impact
# Metric 2: Statistical Parity Difference

# dependent variable 1: EducaationNum
Threshold_1 = 13
Original_sex_privileged_working = df_Step3[df_Step3["Gender"] == 1].count()
Original_sex_privileged_good_working = df_Step3[(df_Step3["Gender"] == 1)&(df_Step3["EducationNum"] >= Threshold_1)].count()
Original_sex_privileged_bad_working = df_Step3[(df_Step3["Gender"] == 1)&(df_Step3["EducationNum"] < Threshold_1)].count()
Original_sex_unprivileged_working = df_Step3[df_Step3["Gender"] == 0].count()
Original_sex_unprivileged_good_working = df_Step3[(df_Step3["Gender"] == 0)&(df_Step3["EducationNum"] >= Threshold_1)].count()
Original_sex_unprivileged_bad_working = df_Step3[(df_Step3["Gender"] == 0)&(df_Step3["EducationNum"] < Threshold_1)].count()

Original_sex_disparate_impact_working = (Original_sex_unprivileged_good_working[0] / (Original_sex_unprivileged_working[0])) / (Original_sex_privileged_good_working[0] / (Original_sex_privileged_working[0]))
Original_sex_statistical_parity_difference_working = (Original_sex_unprivileged_good_working[0] / (Original_sex_unprivileged_working[0])) - (Original_sex_privileged_good_working[0] / (Original_sex_privileged_working[0]))
print('Original_sex_Years_of_Working - disparate_impact:',Original_sex_disparate_impact_working)
print('Original_sex_Years_of_Working - statistical_parity_difference:',Original_sex_statistical_parity_difference_working)

# dependent variable 2: Total_Income
Threshold_2 = " >50K"
Threshold_3 = " <=50K"

Original_sex_privileged_income = df_Step3[df_Step3["Gender"] == 1].count()
Original_sex_privileged_good_income = df_Step3[(df_Step3["Gender"] == 1)&(df_Step3["Income"] == Threshold_2)].count()
Original_sex_privileged_bad_income = df_Step3[(df_Step3["Gender"] == 1)&(df_Step3["Income"] == Threshold_3)].count()
Original_sex_unprivileged_income = df_Step3[df_Step3["Gender"] == 0].count()
Original_sex_unprivileged_good_income = df_Step3[(df_Step3["Gender"] == 0)&(df_Step3["Income"] == Threshold_2)].count()
Original_sex_unprivileged_bad_income = df_Step3[(df_Step3["Gender"] == 0)&(df_Step3["Income"] == Threshold_3)].count()

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

# dependent variable 1: EducationNum
Original_age_privileged_working = df_Step3[df_Step3["Age"] == 0].count()
Original_age_privileged_good_working = df_Step3[(df_Step3["Age"] == 0)&(df_Step3["EducationNum"] >= Threshold_1)].count()
Original_age_privileged_bad_working = df_Step3[(df_Step3["Age"] == 0)&(df_Step3["EducationNum"] < Threshold_1)].count()
Original_age_unprivileged_working = df_Step3[df_Step3["Age"] == 1].count()
Original_age_unprivileged_good_working = df_Step3[(df_Step3["Age"] == 1)&(df_Step3["EducationNum"] >= Threshold_1)].count()
Original_age_unprivileged_bad_working = df_Step3[(df_Step3["Age"] == 1)&(df_Step3["EducationNum"] < Threshold_1)].count()

Original_age_disparate_impact_working = (Original_age_unprivileged_good_working[0] / (Original_age_unprivileged_working[0])) / (Original_age_privileged_good_working[0] / (Original_age_privileged_working[0]))
Original_age_statistical_parity_difference_working = (Original_age_unprivileged_good_working[0] / (Original_age_unprivileged_working[0])) - (Original_age_privileged_good_working[0] / (Original_age_privileged_working[0]))
print('Original_age_Years_of_Working - disparate_impact:',Original_age_disparate_impact_working)
print('Original_age_Years_of_Working - statistical_parity_difference:',Original_age_statistical_parity_difference_working)

# dependent variable 2: Total_Income
Original_age_privileged_income = df_Step3[df_Step3["Age"] == 0].count()
Original_age_privileged_good_income = df_Step3[(df_Step3["Age"] == 0)&(df_Step3["Income"] == Threshold_2)].count()
Original_age_privileged_bad_income = df_Step3[(df_Step3["Age"] == 0)&(df_Step3["Income"] == Threshold_3)].count()
Original_age_unprivileged_income = df_Step3[df_Step3["Age"] == 1].count()
Original_age_unprivileged_good_income = df_Step3[(df_Step3["Age"] == 1)&(df_Step3["Income"] == Threshold_2)].count()
Original_age_unprivileged_bad_income = df_Step3[(df_Step3["Age"] == 1)&(df_Step3["Income"] == Threshold_3)].count()

Original_age_disparate_impact_income = (Original_age_unprivileged_good_income[0] / (Original_age_unprivileged_income[0])) / (Original_age_privileged_good_income[0] / (Original_age_privileged_income[0]))
Original_age_statistical_parity_difference_income = (Original_age_unprivileged_good_income[0] / (Original_age_unprivileged_income[0])) - (Original_age_privileged_good_income[0] / (Original_age_privileged_income[0]))
print('Original_age_Total_Income - disparate_impact:',Original_age_disparate_impact_income)
print('Original_age_Total_Income - statistical_parity_difference:',Original_age_statistical_parity_difference_income)

# Resample/reweighting the dataset
import numpy as np
df_temp = df_Step3.copy()
sample_thrshold_1 = 0.7
sample_thrshold_2 = 0.7
sample_thrshold_3 = 0.6
sample_thrshold_4 = 0.9
Flag = []
for ind, row in df_temp.iterrows():
    if row['Gender'] == 1 and row['Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_1:
            Flag.append(0)
            continue
    if row['Gender'] == 0 and row['EducationNum'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_2:
            Flag.append(0)
            continue
    if row['Age'] == 0 and row['EducationNum'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_3:
            Flag.append(0)
            continue
    if row['Age'] == 0 and row['Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_4:
            Flag.append(0)
            continue
    Flag.append(1)
df_temp['resample'] = Flag
df_temp = df_temp[df_temp['resample'] == 1]
df_Step3_Trans = df_temp.copy()

sum(Flag) / len(Flag)

# Calculate fairness metrics
# Protected class: sex
# privileged sex group (male) == 1
# unprivileged sex group (female) == 0
# Metric 1: Disparate Impact
# Metric 2: Statistical Parity Difference

# dependent variable 1: EducationNum
Trans_sex_privileged_working = df_Step3_Trans[df_Step3_Trans["Gender"] == 1].count()
Trans_sex_privileged_good_working = df_Step3_Trans[(df_Step3_Trans["Gender"] == 1)&(df_Step3_Trans["EducationNum"] >= Threshold_1)].count()
Trans_sex_privileged_bad_working = df_Step3_Trans[(df_Step3_Trans["Gender"] == 1)&(df_Step3_Trans["EducationNum"] < Threshold_1)].count()
Trans_sex_unprivileged_working = df_Step3_Trans[df_Step3_Trans["Gender"] == 0].count()
Trans_sex_unprivileged_good_working = df_Step3_Trans[(df_Step3_Trans["Gender"] == 0)&(df_Step3_Trans["EducationNum"] >= Threshold_1)].count()
Trans_sex_unprivileged_bad_working = df_Step3_Trans[(df_Step3_Trans["Gender"] == 0)&(df_Step3_Trans["EducationNum"] < Threshold_1)].count()

Trans_sex_disparate_impact_working = (Trans_sex_unprivileged_good_working[0] / (Trans_sex_unprivileged_working[0])) / (Trans_sex_privileged_good_working[0] / (Trans_sex_privileged_working[0]))
Trans_sex_statistical_parity_difference_working = (Trans_sex_unprivileged_good_working[0] / (Trans_sex_unprivileged_working[0])) - (Trans_sex_privileged_good_working[0] / (Trans_sex_privileged_working[0]))
print('Trans_sex_Years_of_Working - disparate_impact:',Trans_sex_disparate_impact_working)
print('Trans_sex_Years_of_Working - statistical_parity_difference:',Trans_sex_statistical_parity_difference_working)

# dependent variable 2: Total_Income
Trans_sex_privileged_income = df_Step3_Trans[df_Step3_Trans["Gender"] == 1].count()
Trans_sex_privileged_good_income = df_Step3_Trans[(df_Step3_Trans["Gender"] == 1)&(df_Step3_Trans["Income"] >= Threshold_2)].count()
Trans_sex_privileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Gender"] == 1)&(df_Step3_Trans["Income"] < Threshold_2)].count()
Trans_sex_unprivileged_income = df_Step3_Trans[df_Step3_Trans["Gender"] == 0].count()
Trans_sex_unprivileged_good_income = df_Step3_Trans[(df_Step3_Trans["Gender"] == 0)&(df_Step3_Trans["Income"] >= Threshold_2)].count()
Trans_sex_unprivileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Gender"] == 0)&(df_Step3_Trans["Income"] < Threshold_2)].count()

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

# dependent variable 1: EducatonNum
Trans_age_privileged_working = df_Step3_Trans[df_Step3_Trans["Age"] == 0].count()
Trans_age_privileged_good_working = df_Step3_Trans[(df_Step3_Trans["Age"] == 0)&(df_Step3_Trans["EducationNum"] >= Threshold_1)].count()
Trans_age_privileged_bad_working = df_Step3_Trans[(df_Step3_Trans["Age"] == 0)&(df_Step3_Trans["EducationNum"] < Threshold_1)].count()
Trans_age_unprivileged_working = df_Step3_Trans[df_Step3_Trans["Age"] == 1].count()
Trans_age_unprivileged_good_working = df_Step3_Trans[(df_Step3_Trans["Age"] == 1)&(df_Step3_Trans["EducationNum"] >= Threshold_1)].count()
Trans_age_unprivileged_bad_working = df_Step3_Trans[(df_Step3_Trans["Age"] == 1)&(df_Step3_Trans["EducationNum"] < Threshold_1)].count()

Trans_age_disparate_impact_working = (Trans_age_unprivileged_good_working[0] / (Trans_age_unprivileged_working[0])) / (Trans_age_privileged_good_working[0] / (Trans_age_privileged_working[0]))
Trans_age_statistical_parity_difference_working = (Trans_age_unprivileged_good_working[0] / (Trans_age_unprivileged_working[0])) - (Trans_age_privileged_good_working[0] / (Trans_age_privileged_working[0]))
print('Trans_age_Years_of_Working - disparate_impact:',Trans_age_disparate_impact_working)
print('Trans_age_Years_of_Working - statistical_parity_difference:',Trans_age_statistical_parity_difference_working)

# dependent variable 2: Total_Income
Trans_age_privileged_income = df_Step3_Trans[df_Step3_Trans["Age"] == 0].count()
Trans_age_privileged_good_income = df_Step3_Trans[(df_Step3_Trans["Age"] == 0)&(df_Step3_Trans["Income"] == Threshold_2)].count()
Trans_age_privileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Age"] == 0)&(df_Step3_Trans["Income"] == Threshold_3)].count()
Trans_age_unprivileged_income = df_Step3_Trans[df_Step3_Trans["Age"] == 1].count()
Trans_age_unprivileged_good_income = df_Step3_Trans[(df_Step3_Trans["Age"] == 1)&(df_Step3_Trans["Income"] == Threshold_2)].count()
Trans_age_unprivileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Age"] == 1)&(df_Step3_Trans["Income"] == Threshold_3)].count()

Trans_age_disparate_impact_income = (Trans_age_unprivileged_good_income[0] / (Trans_age_unprivileged_income[0])) / (Trans_age_privileged_good_income[0] / (Trans_age_privileged_income[0]))
Trans_age_statistical_parity_difference_income = (Trans_age_unprivileged_good_income[0] / (Trans_age_unprivileged_income[0])) - (Trans_age_privileged_good_income[0] / (Trans_age_privileged_income[0]))
print('Trans_age_Total_Income - disparate_impact:',Trans_age_disparate_impact_income)
print('Trans_age_Total_Income - statistical_parity_difference:',Trans_age_statistical_parity_difference_income)


# step3 Summary
protected_class_col = ['sex', 'sex', 'age', 'age', 'sex', 'sex', 'age', 'age']
dependent_varibale_col = ['EducationNum', 'total income', 'EducationNum', 'total income', 'EducationNum', 'total income', 'EducationNum', 'total income']
metrics_col = ['disparate impact', 'disparate impact', 'disparate impact', 'disparate impact', 'statistical parity', 'statistical parity', 'statistical parity', 'statistical parity']
original_metrics = [Original_sex_disparate_impact_working, Original_sex_disparate_impact_income, Original_age_disparate_impact_working, Original_age_disparate_impact_income,Original_sex_statistical_parity_difference_working, Original_sex_statistical_parity_difference_income, Original_age_statistical_parity_difference_working, Original_age_statistical_parity_difference_income]
trans_metrics = [Trans_sex_disparate_impact_working, Trans_sex_disparate_impact_income, Trans_age_disparate_impact_working, Trans_age_disparate_impact_income, Trans_sex_statistical_parity_difference_working, Trans_sex_statistical_parity_difference_income, Trans_age_statistical_parity_difference_working, Trans_age_statistical_parity_difference_income]
summary_step3 = list(zip(protected_class_col, dependent_varibale_col, metrics_col, original_metrics,trans_metrics))
pd.DataFrame(summary_step3, columns = ['Protected Class', 'Dependent Variable', 'Fairness', 'Original Metric', 'Transformed Metric'])

# step 4
# Preprocessing and random split
df_step4_X = df[['Age','Workclass','Final Weight','Education','EducationNum','Marital Status','Occupation','Relationship','Race','Gender','Capital Gain','capital loss','Hours per Week','Native Country']]
df_step4_y = df.Income

# Resample/reweighting the dataset
df_temp = df.copy()
sample_thrshold_1 = 0.7
sample_thrshold_2 = 0.7
sample_thrshold_3 = 0.6
sample_thrshold_4 = 0.9
Flag = []
for ind, row in df_temp.iterrows():
    if row['Gender'] == 1 and row['Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_1:
            Flag.append(0)
            continue
    if row['Gender'] == 0 and row['EducationNum'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_2:
            Flag.append(0)
            continue
    if row['Age'] >= 40 and row['EducationNum'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_3:
            Flag.append(0)
            continue
    if row['Age'] >= 40 and row['Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_4:
            Flag.append(0)
            continue
    Flag.append(1)
df_temp['resample'] = Flag
df_temp = df_temp[df_temp['resample'] == 1]

df_step4_trans_X = df_temp[['Age','Workclass','Final Weight','Education','EducationNum','Marital Status','Occupation','Relationship','Race','Gender','Capital Gain','capital loss','Hours per Week','Native Country']]
df_step4_trans_y = df_temp.Income
sum(Flag) / len(Flag)

from sklearn.preprocessing import LabelEncoder

enc = LabelEncoder()

def encode(df):
    for col in df.columns:
        if df[col].dtype in ['string', 'object']:
            print(col)
        df[col] = enc.fit_transform(df[col])
    return df

df_test = pd.read_csv("adult.test.csv", sep=",", names=['Age', 'Workclass', 'Final Weight', 'Education', 'EducationNum',
                                                        'Marital Status', 'Occupation', 'Relationship', 'Race', 'Gender',
                                                        'Capital Gain', 'capital loss', 'Hours per Week', 'Native Country', 'Income'])
df_test
# Resample/reweighting the dataset
df_temp = df_test.copy()
sample_thrshold_1 = 0.7
sample_thrshold_2 = 0.7
sample_thrshold_3 = 0.6
sample_thrshold_4 = 0.9
Flag = []
for ind, row in df_temp.iterrows():
    if row['Gender'] == 1 and row['Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_1:
            Flag.append(0)
            continue
    if row['Gender'] == 0 and row['EducationNum'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_2:
            Flag.append(0)
            continue
    if row['Age'] >= 40 and row['EducationNum'] >= Threshold_1:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_3:
            Flag.append(0)
            continue
    if row['Age'] >= 40 and row['Income'] >= Threshold_2:
        rand_threshold = np.random.random_sample()
        if rand_threshold > sample_thrshold_4:
            Flag.append(0)
            continue
    Flag.append(1)
df_temp['resample'] = Flag
df_temp = df_temp[df_temp['resample'] == 1]

df_test_step4_trans_X = df_temp[['Age','Workclass','Final Weight','Education','EducationNum','Marital Status','Occupation','Relationship','Race','Gender','Capital Gain','capital loss','Hours per Week','Native Country']]
df_test_step4_trans_y = df_temp.Income



df_step4_X_enc = encode(df_step4_X)
df_step4_X_trans_enc = encode(df_step4_trans_X)


df_test_step4_X = df_test[['Age','Workclass','Final Weight','Education','EducationNum','Marital Status','Occupation','Relationship','Race','Gender','Capital Gain','capital loss','Hours per Week','Native Country']]
df_test_step4_y = df_test.Income

enc = LabelEncoder()

def encode(df_test):
    for col in df_test.columns:
        if df_test[col].dtype in ['string', 'object']:
            print(col)
        df_test[col] = enc.fit_transform(df_test[col])
    return df_test

df_test_step4_X_enc = encode(df_test_step4_X)
df_test_step4_X_trans_enc = encode(df_test_step4_trans_X)

X_train=df_step4_X_enc
y_train=df_step4_y
X_test= df_test_step4_X_enc
y_test = df_step4_y

df_step4_X_enc = encode(df_step4_X)
df_step4_X_trans_enc = encode(df_step4_trans_X)

### train classifier
from sklearn.preprocessing import LabelEncoder

# Assuming `y_train` and `y_test` are your target variables containing '<=50K' and '>50K'.
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)
y_test_encoded = le.transform(y_test)

# After encoding, you can fit a classifier (not regressor for categorical targets):
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train_encoded)
y_pred = model.predict(X_test)

df_pred = X_test.copy()
df_pred['pred'] = y_pred
df_pred["Age"] = df_pred["Age"] < 40

df_pred_trans = X_test.copy()
df_pred_trans['pred'] = y_pred
df_pred_trans["Age"] = df_pred_trans["Age"] < 40

#Compare Fairness metrics with Step3a
# dependent variable 2: Total_Income
Original_age_privileged_income = df_Step3[df_Step3["Age"] == 0].count()
Original_age_privileged_good_income = df_Step3[(df_Step3["Age"] == 0)&(df_Step3["Income"] == Threshold_2)].count()
Original_age_privileged_bad_income = df_Step3[(df_Step3["Age"] == 0)&(df_Step3["Income"] == Threshold_3)].count()
Original_age_unprivileged_income = df_Step3[df_Step3["Age"] == 1].count()
Original_age_unprivileged_good_income = df_Step3[(df_Step3["Age"] == 1)&(df_Step3["Income"] == Threshold_2)].count()
Original_age_unprivileged_bad_income = df_Step3[(df_Step3["Age"] == 1)&(df_Step3["Income"] == Threshold_3)].count()

Original_age_disparate_impact_income_step3 = (Original_age_unprivileged_good_income[0] / (Original_age_unprivileged_income[0])) / (Original_age_privileged_good_income[0] / (Original_age_privileged_income[0]))
Original_age_statistical_parity_difference_income_step3 = (Original_age_unprivileged_good_income[0] / (Original_age_unprivileged_income[0])) - (Original_age_privileged_good_income[0] / (Original_age_privileged_income[0]))
print('Step3 --- Original_age_Total_Income - disparate_impact:',Original_age_disparate_impact_income_step3)
print('Step3 --- Original_age_Total_Income - statistical_parity_difference:',Original_age_statistical_parity_difference_income_step3)

# dependent variable 2: Total_Income
Original_age_privileged_income = df_pred[df_pred["Age"] == 0].count()
Original_age_privileged_good_income = df_pred[(df_pred["Age"] == 0)&(df_pred["pred"] == Threshold_2)].count()
Original_age_privileged_bad_income = df_pred[(df_pred["Age"] == 0)&(df_pred["pred"] == Threshold_3)].count()
Original_age_unprivileged_income = df_pred[df_pred["Age"] == 1].count()
Original_age_unprivileged_good_income = df_pred[(df_pred["Age"] == 1)&(df_pred["pred"] == Threshold_2)].count()
Original_age_unprivileged_bad_income = df_pred[(df_pred["Age"] == 1)&(df_pred["pred"] == Threshold_3)].count()

Original_age_disparate_impact_income_step4 = (Original_age_unprivileged_good_income[0] / (Original_age_unprivileged_income[0])) / (Original_age_privileged_good_income[0] / (Original_age_privileged_income[0]))
Original_age_statistical_parity_difference_income_step4 = (Original_age_unprivileged_good_income[0] / (Original_age_unprivileged_income[0])) - (Original_age_privileged_good_income[0] / (Original_age_privileged_income[0]))
print('Step4 --- Original_age_Total_Income - disparate_impact:',Original_age_disparate_impact_income_step4)
print('Step4 --- Original_age_Total_Income - statistical_parity_difference:',Original_age_statistical_parity_difference_income_step4)

# dependent variable 2: Total_Income
Trans_age_privileged_income = df_Step3_Trans[df_Step3_Trans["Age"] == 0].count()
Trans_age_privileged_good_income = df_Step3_Trans[(df_Step3_Trans["Age"] == 0)&(df_Step3_Trans["Income"] == Threshold_2)].count()
Trans_age_privileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Age"] == 0)&(df_Step3_Trans["Income"] == Threshold_3)].count()
Trans_age_unprivileged_income = df_Step3_Trans[df_Step3_Trans["Age"] == 1].count()
Trans_age_unprivileged_good_income = df_Step3_Trans[(df_Step3_Trans["Age"] == 1)&(df_Step3_Trans["Income"] == Threshold_2)].count()
Trans_age_unprivileged_bad_income = df_Step3_Trans[(df_Step3_Trans["Age"] == 1)&(df_Step3_Trans["Income"] == Threshold_3)].count()

Trans_age_disparate_impact_income_step3 = (Trans_age_unprivileged_good_income[0] / (Trans_age_unprivileged_income[0])) / (Trans_age_privileged_good_income[0] / (Trans_age_privileged_income[0]))
Trans_age_statistical_parity_difference_income_step3 = (Trans_age_unprivileged_good_income[0] / (Trans_age_unprivileged_income[0])) - (Trans_age_privileged_good_income[0] / (Trans_age_privileged_income[0]))
print(f'Step3 --- Trans_age_Total_Income - disparate_impact: {Trans_age_disparate_impact_income_step3:.5f}')
print(f'Step3 --- Trans_age_Total_Income - statistical_parity_difference: {Trans_age_statistical_parity_difference_income_step3:.5f}')


# dependent variable 2: Total_Income
Trans_age_privileged_income = df_pred_trans[df_pred_trans["Age"] == 0].count()
Trans_age_privileged_good_income = df_pred_trans[(df_pred_trans["Age"] == 0)&(df_pred_trans["pred"] == Threshold_2)].count()
Trans_age_privileged_bad_income = df_pred_trans[(df_pred_trans["Age"] == 0)&(df_pred_trans["pred"] == Threshold_3)].count()
Trans_age_unprivileged_income = df_pred_trans[df_pred_trans["Age"] == 1].count()
Trans_age_unprivileged_good_income = df_pred_trans[(df_pred_trans["Age"] == 1)&(df_pred_trans["pred"] == Threshold_2)].count()
Trans_age_unprivileged_bad_income = df_pred_trans[(df_pred_trans["Age"] == 1)&(df_pred_trans["pred"] == Threshold_3)].count()

Trans_age_disparate_impact_income_step4 = (Trans_age_unprivileged_good_income[0] / (Trans_age_unprivileged_income[0])) / (Trans_age_privileged_good_income[0] / (Trans_age_privileged_income[0]))
Trans_age_statistical_parity_difference_income_step4 = (Trans_age_unprivileged_good_income[0] / (Trans_age_unprivileged_income[0])) - (Trans_age_privileged_good_income[0] / (Trans_age_privileged_income[0]))
print('Step4 --- Trans_age_Total_Income - disparate_impact:',Trans_age_disparate_impact_income_step4)
print('Step4 --- Trans_age_Total_Income - statistical_parity_difference:',Trans_age_statistical_parity_difference_income_step4)


protected_class_col = ['Age', 'Age']
dependent_varibale_col = ['Income', 'Income']
metrics_col = ['disparate impact', 'statistical parity']
step = [ 'step 4',  'step 4']
original_metrics = [Original_age_disparate_impact_income_step4, Original_age_statistical_parity_difference_income_step4]
trans_metrics = [Trans_age_disparate_impact_income_step4,  Trans_age_statistical_parity_difference_income_step4]
summary_step4 = list(zip(protected_class_col, dependent_varibale_col, metrics_col, step, original_metrics,trans_metrics))
pd.DataFrame(summary_step4, columns = ['Protected Class', 'Dependent Variable', 'Fairness', 'step', 'Original Metric', 'Transformed Metric'])

protected_class_col = ['Age', 'Age', 'Age', 'Age']
dependent_varibale_col = ['Income', 'Income', 'Income', 'Income']
metrics_col = ['disparate impact', 'disparate impact', 'statistical parity', 'statistical parity']
step = ['step 3', 'step 4', 'step 3', 'step 4']
original_metrics = [Original_age_disparate_impact_income_step3, Original_age_disparate_impact_income_step4, Original_age_statistical_parity_difference_income_step3, Original_age_statistical_parity_difference_income_step4]
trans_metrics = [Trans_age_disparate_impact_income_step3, Trans_age_disparate_impact_income_step4, Trans_age_statistical_parity_difference_income_step3, Trans_age_statistical_parity_difference_income_step4]
summary_step4 = list(zip(protected_class_col, dependent_varibale_col, metrics_col, step, original_metrics,trans_metrics))
pd.DataFrame(summary_step4, columns = ['Protected Class', 'Dependent Variable', 'Fairness', 'step', 'Original Metric', 'Transformed Metric'])


metrics = ['disparate_impact', 'statistical_parity_difference']
after_transforming = ['positive', 'positive']
after_training_original = ['positive', 'positive']
after_training_tranformed = ['positive', 'positive']
table_step4 = list(zip(metrics, after_transforming, after_training_original, after_training_tranformed))
pd.DataFrame(table_step4, columns = ['Metrics', 'after_transforming', 'after_training_original', 'after_training_tranformed'])

# step 5
import matplotlib.pyplot as plt
import numpy as np

#sex EducationNum disparate impact
fig = plt.figure(figsize = (9,6))

data = [1.2728,1.0184]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 1.0, '0.8~1.25, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.axhline(y=0.8,color = "black",linestyle = "-")
plt.axhline(y=1.25,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Disparate Impact")
plt.show()

# sex, total income, disparate impact

fig = plt.figure(figsize = (9,6))

data = [0.6351,0.7434]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 1.0, '0.8~1.25, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.axhline(y=0.8,color = "black",linestyle = "-")
plt.axhline(y=1.25,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Disparate Impact")
plt.show()

#age, EducationNum, disparate impact
fig = plt.figure(figsize = (9,6))

data = [0.5870,0.7846]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 1.0, '0.8~1.25, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.axhline(y=0.8,color = "black",linestyle = "-")
plt.axhline(y=1.25,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Disparate Impact")
plt.show()

# age, total income, disparate impact
fig = plt.figure(figsize = (9,6))

data = [0.8941,0.9329]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 1.0, '0.8~1.25, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.axhline(y=0.8,color = "black",linestyle = "-")
plt.axhline(y=1.25,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Disparate Impact")
plt.show()


# sex, EducationNum, statistical parity
fig = plt.figure(figsize = (9,6))

data = [0.0906,0.0049]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 0.02, '-0.1~0.1, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
plt.axhline(y=-0.1,color = "black",linestyle = "-")
plt.axhline(y=0.1,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Statistical Parity")
plt.show()

# sex, EducationNum, total income
fig = plt.figure(figsize = (9,6))

data = [-0.1906,-0.1067]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 0.02, '-0.1~0.1, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
plt.axhline(y=-0.1,color = "black",linestyle = "-")
plt.axhline(y=0.1,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Statistical Parity")
plt.show()

# age, EducationNum, statistical parity
fig = plt.figure(figsize = (9,6))

data = [-0.1991,-0.0656]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 0.02, '-0.1~0.1, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
plt.axhline(y=-0.1,color = "black",linestyle = "-")
plt.axhline(y=0.1,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Statistical Parity")
plt.show()


# age, total income,statistical parity
fig = plt.figure(figsize = (9,6))

data = [-0.0450,-0.0243]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 0.02, '-0.1~0.1, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
plt.axhline(y=-0.1,color = "black",linestyle = "-")
plt.axhline(y=0.1,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Statistical Parity")
plt.show()

# age, total income, disparate impact
fig = plt.figure(figsize = (9,6))

data = [1.0574,0.9864]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 1.0, '0.8~1.25, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.axhline(y=0.8,color = "black",linestyle = "-")
plt.axhline(y=1.25,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Disparate Impact")
plt.show()

# age, total income,statistical parity
fig = plt.figure(figsize = (9,6))

data = [0.0220,-0.0053]
x_labels = ["Before Transformed", "After Transformed"]

plt.bar(x_labels, data, width = 0.5,color = ['grey','pink'])
plt.text(0.4, 0.02, '-0.1~0.1, Fair', fontsize = 10)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
plt.axhline(y=-0.1,color = "black",linestyle = "-")
plt.axhline(y=0.1,color = "black",linestyle = "-")
ax.set_xticklabels(x_labels)
plt.title("Statistical Parity")
plt.show()