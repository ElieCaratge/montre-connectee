import pandas as pd
import numpy as np
import csv
from Sport import SPORTS_LIST, SPORTS


class CompatibilityMatrix(pd.DataFrame):

    def __init__(self) -> None:

        reponses = []

        # Read the csv file Questionnaire.csv
        with open('./Data/Questionnaire.csv', newline='') as csvfile:
            reponse = csv.reader(csvfile)
            for row in reponse:
                # row[0] is a row with the date, we don't need it
                del row[0]
                reponses.append(row)

        sports = reponses.pop(0)
        # Extract sports
        affinites = np.zeros([len(sports), len(sports)])

        # We define an affinity treshold
        palier_affinite = 1

        for j in range(len(sports)):
            for k in range(j+1):
                m = 0
                n = 0
                for i in range(len(reponses)):
                    if (int(reponses[i][j]) >= palier_affinite and int(reponses[i][k]) >= 5) or (int(reponses[i][k]) >= palier_affinite and int(reponses[i][j]) >= 5):
                        # Calculate the difference for each user between sports j and k and make a mean
                        m += abs(int(reponses[i][j])-int(reponses[i][k]))
                        n += 1
                if n != 0:
                    m_moy = m/n
                    # The greater the difference, the less affinity there is
                    m_prct = 100 - m_moy*10
                    affinites[j][k] = int(m_prct)
                    affinites[k][j] = int(m_prct)
                else:
                    affinites[j][k] = None
                    affinites[k][j] = None

        # We compile in a panda dataframe the affinity between sports
        df = pd.DataFrame(data=affinites, index=sports, columns=sports)
        A = df[[sport.name for sport in SPORTS_LIST]]
        B = A.loc[A.index.isin([sport.name for sport in SPORTS_LIST])]
        super().__init__(B)

    def positive_feedback(self, sport1, sport2):
        '''Si la recommandation est bonne : amélioration de l'affinité (+0.25 si l'affinité était nulle, +0 si elle était de 1)'''
        '''sport1 = Patient.main_sport'''
        i = SPORTS_LIST.index(sport1)
        j = SPORTS_LIST.index(sport2)
        self.iloc[i, j] += (25/10)*np.sqrt(100-self.iloc[i, j])

    def negative_feedback(self, sport1, sport2):
        '''Si la recommandation est bonne : diminution de l'affinité (-0.25 si l'affinité était de 1, -0 si elle était nulle)'''
        i = SPORTS_LIST.index(sport1)
        j = SPORTS_LIST.index(sport2)
        self.iloc[i, j] -= (25/10)*np.sqrt(self.iloc[i, j])


COMPATIBILITY_MATRIX = CompatibilityMatrix()


COMPATIBILITY_MATRIX.positive_feedback(SPORTS['escalade'], SPORTS['cyclisme'])

# Test
if __name__ == "__main__":
    print(COMPATIBILITY_MATRIX)
    # Test positive feedback
    COMPATIBILITY_MATRIX.positive_feedback(SPORTS_LIST[0], SPORTS_LIST[1])
    print(COMPATIBILITY_MATRIX)
    # Test negative feedback
    COMPATIBILITY_MATRIX.negative_feedback(SPORTS_LIST[3], SPORTS_LIST[4])
    print(COMPATIBILITY_MATRIX)