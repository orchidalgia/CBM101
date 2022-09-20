
g = sns.pairplot(df.loc[:, ['thal', 'oldpeak', 'maximum_heart_rate_achieved', 'number_of_major_vessels', 'Disease']], 
                 diag_kind='kde', 
                 hue='Disease', 
                 markers=["o", "s"])

# None of the pairwise comparisons can separate the classes 
# but there seems to be some correlation between these variables and disease.
# Correlation is easier to see in continuous variables (max heart rate & oldpeak separates the groups pretty well)
# In descrete variables it's harder to see but seems that number of major vessels correlates with disease
# 
