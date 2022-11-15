
# might be useful to check metrics of each feature
#df.describe()


# Example to plot histograms for all features:
for i in df.columns:
    plt.figure()
    plt.title(f'{i}')
    plt.hist(df[i])
