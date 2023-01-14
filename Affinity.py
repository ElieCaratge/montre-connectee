import csv
import sklearn.cluster
import pandas as pd
import numpy as np

reponses = []
# Read the csv file, mine is called reponses.csv
with open('montre-connectee/Data/reponses.csv', newline='') as csvfile:
    reponse = csv.reader(csvfile)
    for row in reponse:
        # row[0] is a row with the date, we don't need it
        del row[0]
        reponses.append(row)

sports = reponses.pop(0)
# Extract sports
affinités = np.zeros([len(sports), len(sports)])

# We define an affinity treshold
palier_affinité = 1

for j in range(len(sports)):
    for k in range(j+1):
        m = 0
        n = 0
        for i in range(len(reponses)):
            if (int(reponses[i][j]) >= palier_affinité and int(reponses[i][k]) >= 5) or (int(reponses[i][k]) >= palier_affinité and int(reponses[i][j]) >= 5):
                # Calculate the difference for each user between sports j and k and make a mean
                m += abs(int(reponses[i][j])-int(reponses[i][k]))
                n += 1
        if n != 0:
            m_moy = m/n
            # The greater the difference, the less affinity there is
            m_prct = 100 - m_moy*10
            affinités[j][k] = int(m_prct)
            affinités[k][j] = int(m_prct)
        else:
            affinités[j][k] = None
            affinités[k][j] = None
affinity_zero = affinités


def feedback(pos, i, j, mat=affinity_zero):
    """Is the feedback from sport i to sport j posiive (pos = True) or negative (pos = False)"""
    if pos:
        mat[i][j] += (25/10)*np.sqrt(100-mat[i][j])
    else:
        mat[i][j] += (25/10)*np.sqrt(mat[i][j])
    return mat
