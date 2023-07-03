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

female = (gss['sex'] == 2)
print("Prob of females: " + str(prob(female)))

liberal = (gss['polviews'] <= 3)

print("Probability of being a liberal: " + str(prob(liberal)))

democrat = (gss['partyid'] <= 1)

print("Prob of being a democrat: " + str(prob(democrat)))

print("The prob of being BOTH a banker and a democrat: " + str(prob(democrat & banker)))

selected = democrat[liberal]

print("The fraction of liberals who are Democrats: " + str(prob(selected)))

selected = female[banker]

print("The probability of bankers that are female: " + str(prob(selected)))

def conditional(proposition, given):
    """Probability of A conditioned on given."""
    return prob(proposition[given])    


output = conditional(liberal, given=female)

print("The probability that a respondent is liberal given that they are female: " + str(output))

output = conditional(banker, given=female)

print("The probability that a respondent is a banker given that they are female: " + str(output))

output = conditional(female, given=liberal & democrat)

print("The probability that a respondent is a female given that they are liberal and a democrat: " + str(output))

output = conditional(liberal & female, given=banker)

print("The probability that a respondent is a liberal and a female given that they are a banker: " + str(output))

percent = female[banker].mean()

print("V1: The fraction of bankers that are female are: " + str(percent))

percent = conditional(female, given=banker)

print("V2: The fraction of bankers that are female are: " + str(percent))
