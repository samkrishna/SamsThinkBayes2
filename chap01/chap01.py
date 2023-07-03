import pandas as pd

gss = pd.read_csv('gss_bayes.csv', index_col=0)
gss.head()

banker = (gss['indus10'] == 6870)
print(banker.head())

print("\nHow many bankers are there? " + str(banker.sum()))

def prob(A):
    """Computes the probability of a proposition, A."""    
    return A.mean()

percent = prob(banker * 100.0)
print("About to calculate the percentage of bankers: " + str(percent) + "%")
