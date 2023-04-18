
# Variable importance tells how well that feature can separate different classes. 
# In other words, the higher the score, the more predictive feature

# pairplot of maximum_heart_rate_achieved, chest_pain_type, oldpeak and Disease
g = sns.pairplot(df.loc[:, ['maximum_heart_rate_achieved', 'chest_pain_type', 'oldpeak', 'Disease']], 
                 diag_kind='kde', 
                 hue='Disease', 
                 markers=["o", "s"])

# None of the features can separate the classes efficiently
# but some correlation can be seen between these variables and disease.
# E.g high max heart rate together with low oldpeak indicates no disease, 
# but there's no clear line between the groups

# Also chest pain type 4 correlates with disease (see distribution plot), 
# but there's also many patients with thesame measure but no disease 
