import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------------
# Data wrangling
# ------------------------------------------------------------------

# Define data path
path_data = '03 Sustainable Food/01 Data/Doctoral_study_data_for_Devon_schools/Survey_data'

# Import data
school_1a = pd.read_excel(path_data + '/School_1a_2021.xlsx', skiprows=[1])
school_1b = pd.read_excel(path_data + '/School_1b_2021.xlsx', skiprows=[1])
school_2 = pd.read_excel(path_data + '/School_2_2021.xlsx', skiprows=[1])
school_3 = pd.read_excel(path_data + '/School_3_2021.xlsx', skiprows=[1])

# Add columns to 1b to make consistent with 1a and 2
school_1b['Q5_2_TEXT'], school_1b['Q6_2_TEXT'] = np.nan, np.nan

# Add school names
school_1a['School'] = "1a: St Leonard's"
school_1b['School'] = "1b: Trinity"
school_2['School'] = "2: Doddiscombsleigh"

# Append 1a, 1b and 2
df_schools = pd.concat([school_1a, school_1b, school_2], ignore_index = True)

# ------------------------------------------------------------------
# Plots for Q36: Do meat-free days sound like a good idea to you?
# ------------------------------------------------------------------

# Plot support for meat-free days by school

# Calculate counts of each response and unstack (to check sample size)
counts_school = df_schools.groupby('School')['Q36_Cleansed'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_school = df_schools.groupby('School')['Q36_Cleansed'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_school.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('School')
ax.set_ylabel('Proportion of respondents from each school')
ax.set_title('Q36: Do meat-free days sound like a good idea to you? \n Comparison by school')
ax.legend(title = None)
plt.xticks(rotation=0)

plt.show()


# Plot support for meat-free days by school, parents/carers only

# Calculate counts of each response and unstack (to check sample size)
counts_school_pc = df_schools[df_schools['Stakeholder'] == 'Parent/Carer']\
    .groupby('School')['Q36_Cleansed'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_school_pc = df_schools[df_schools['Stakeholder'] == 'Parent/Carer']\
    .groupby('School')['Q36_Cleansed'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_school_pc.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('School')
ax.set_ylabel('Proportion of respondents from each school')
ax.set_title('Q36: Do meat-free days sound like a good idea to you? \n Comparison by school, parents/carers only')
ax.legend(title = None)
plt.xticks(rotation=0)

plt.show()


# Plot support for meat-free days by school, staff only

# Calculate counts of each response and unstack (to check sample size)
counts_school_staff = df_schools[df_schools['Stakeholder'] != 'Parent/Carer']\
    .groupby('School')['Q36_Cleansed'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_school_staff = df_schools[df_schools['Stakeholder'] != 'Parent/Carer']\
    .groupby('School')['Q36_Cleansed'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_school_staff.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('School')
ax.set_ylabel('Proportion of respondents from each school')
ax.set_title('Q36: Do meat-free days sound like a good idea to you? \n Comparison by school, staff only')
ax.legend(title = None)
plt.xticks(rotation=0)

plt.show()




# Plot support for meat-free days by stakeholder

# Calculate counts of each response and unstack (to check sample size)
counts_stakeholder = df_schools.groupby('Stakeholder')['Q36_Cleansed'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_stakeholder = df_schools.groupby('Stakeholder')['Q36_Cleansed'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_stakeholder.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('Stakeholder')
ax.set_ylabel('Proportion of respondents from each stakeholder group')
ax.set_title('Q36: Do meat-free days sound like a good idea to you? \n Comparison by stakeholder')
ax.legend(title = None)
plt.xticks(rotation=0)

plt.show()




# Plot support meat-free days by ethnicity

# Calculate counts of each response and unstack (to check sample size)
counts_ethnicity = df_schools.groupby('Ethnicity')['Q36_Cleansed'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_ethnicity = df_schools.groupby('Ethnicity')['Q36_Cleansed'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_ethnicity.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('Ethnicity')
ax.set_ylabel('Proportion of respondents from each ethnic group')
ax.set_title('Q36: Do meat-free days sound like a good idea to you? \n Comparison by ethnicity')
ax.legend(title = None, loc='upper center')
plt.xticks(rotation=45)

plt.show()



# Plot support for meat-free days by ethnicity (white and minority)

# Calculate counts of each response and unstack (to check sample size)
counts_ethnicity2 = df_schools.groupby('Ethnicity_2')['Q36_Cleansed'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_ethnicity2 = df_schools.groupby('Ethnicity_2')['Q36_Cleansed'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_ethnicity2.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('Ethnicity')
ax.set_ylabel('Proportion of respondents from each ethnic group')
ax.set_title('Q36: Do meat-free days sound like a good idea to you? \n Comparison by ethnicity')
ax.legend(title = None, loc='upper center')
plt.xticks(rotation=0)

plt.show()




# Plot support for meat-free days by FSM eligibility

# Calculate counts of each response and unstack (to check sample size)
counts_fsm = df_schools.groupby('FSM_Eligibility')['Q36_Cleansed'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_fsm = df_schools.groupby('FSM_Eligibility')['Q36_Cleansed'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_fsm.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('Eligible for free school meals')
ax.set_ylabel('Proportion of respondents from each eligibility group')
ax.set_title('Q36: Do meat-free days sound like a good idea to you? \n Comparison by eligibility for free school meals')
ax.legend(title = None)
plt.xticks(rotation=0)

plt.show()



# Contingency table between ethnicity and FSM eligibility
ethnicity_fsm = pd.crosstab(index=df_schools['Ethnicity'].fillna('NA'),
                            columns=df_schools['FSM_Eligibility'].fillna('NA'),
                            margins=True)



# Plot additional amount willing to pay vs support for meat-free days

ax = sns.catplot(x='Q36_Cleansed', y='Q35_Premium', data=df_schools,
              col='School', jitter=0.2, alpha=0.8, palette='viridis',
              legend=False)
ax.set_axis_labels('Q36: Do meat-free days sound like a good idea to you?',
                   'Additional amount per meal willing to pay (£)')
sns.despine()



# ------------------------------------------------------------------
# Plots for Q37: How many meat-free days would sound reasonable to you?
# ------------------------------------------------------------------

# Plot proportion of responses to meat-free days by school

# Calculate counts of each response and unstack (to check sample size)
counts_school_days = df_schools.groupby('School')['Q37_Bins'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_school_days = df_schools.groupby('School')['Q37_Bins'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_school_days.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('School')
ax.set_ylabel('Proportion of respondents from each school')
ax.set_title('Q37: How many meat-free days would sound reasonable to you? \n Comparison by school')
ax.legend(title = None)
plt.xticks(rotation=0)

plt.show()


# Plot proportion of responses to # meat-free days by school, parents/carers only

# Calculate counts of each response and unstack (to check sample size)
counts_school_days = df_schools[df_schools['Stakeholder'] == 'Parent/Carer']\
    .groupby('School')['Q37_Bins'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_school_days = df_schools[df_schools['Stakeholder'] == 'Parent/Carer']\
    .groupby('School')['Q37_Bins'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_school_days.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('School')
ax.set_ylabel('Proportion of respondents from each school')
ax.set_title('Q37: How many meat-free days would sound reasonable to you? \n Comparison by school, parents/carers only')
ax.legend(title = None)
plt.xticks(rotation=0)

plt.show()


# Plot proportion of responses to # meat-free days by school, staff only

# Calculate counts of each response and unstack (to check sample size)
counts_school_days = df_schools[df_schools['Stakeholder'] != 'Parent/Carer']\
    .groupby('School')['Q37_Bins'].value_counts(normalize=False).unstack()

# Calculate proportion of each response and unstack
props_school_days = df_schools[df_schools['Stakeholder'] != 'Parent/Carer']\
    .groupby('School')['Q37_Bins'].value_counts(normalize=True).unstack()

# Plot bar graph
ax = props_school_days.plot(kind='bar', stacked=False, colormap='viridis')

# Customize the plot
ax.set_xlabel('School')
ax.set_ylabel('Proportion of respondents from each school')
ax.set_title('Q37: How many meat-free days would sound reasonable to you? \n Comparison by school, staff only')
ax.legend(title = None)
plt.xticks(rotation=0)

plt.show()