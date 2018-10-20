import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.to_csv('../../data/processed/tiantic.csv', index=False)