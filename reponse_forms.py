import csv
import sklearn.cluster
import pandas as pd
import numpy as np
from Affinity import feedback
from Affinity import affinity_zero

reponses = []
# Read the csv file, mine is called reponses.csv
with open('montre-connectee/Data/reponses.csv', newline='') as csvfile:
    reponse = csv.reader(csvfile)
    for row in reponse:
        # row[0] is a row with the date, we don't need it
        del row[0]
        reponses.append(row)

sports = reponses.pop(0)

affinités = affinity_zero

# We compile in a panda dataframe the affinity between sports
affinity_dataframe = pd.DataFrame(data=affinités, index=sports, columns=sports)
print(affinity_dataframe)

# We don't need to recommandate sports to everyone who answer to the google forms,
# so we need a list with only the sports that users practise and like
# Here, to make it easier, I took every answer of the forms I made

users_sports = reponses

# Usefull to know which number correspond to which sport
numéro_sport = {i: sports[i] for i in range(len(sports))}
sport_numéro = {sports[i]: i for i in range(len(sports))}

fb = []

with open('montre-connectee/Data/feedback.csv', newline='') as csvfile:
    feedback_csv = csv.reader(csvfile)
    for row in feedback_csv:
        # row[0] is a row with the date, we don't need it
        del row[0]
        fb.append(row)
fb.pop(0)
# Each line k is a recommandation rate of the sport k for the sport j (column)
feedback_users = np.zeros([len(sports), len(sports)]).tolist()
for i in range(len(feedback_users)):
    for j in range(len(feedback_users[i])):
        feedback_users[i][j] = [None]
for feed in fb:
    if feedback_users[sport_numéro[feed[0]]][sport_numéro[feed[1]]] != [None]:
        feedback_users[sport_numéro[feed[0]]
                       ][sport_numéro[feed[1]]].append(int(feed[2]))
    else:
        feedback_users[sport_numéro[feed[0]]
                       ][sport_numéro[feed[1]]] = [int(feed[2])]
for i in range(len(feedback_users)):
    for j in range(len(feedback_users[i])):
        if feedback_users[i][j] != None:
            feedback_users[i][j] = sum(
                feedback_users[i][j])/len(feedback_users[i][j])


# Define a recommandation treshold ∈ [0,10] (here I took 5)
palier_recom = 5
# Weight of the affinity between sports over the feedback
w = 0.5
# We will eliminate sports that are not below that treshold
user_recom = []
taux_recom = []
for i in range(len(users_sports)):
    empty = True
    niv_recom = []*len(users_sports)
    for j in range(len(sports)):
        m = 0
        for k in range(len(sports)):
            # For each user i and for each sport j, we determine if there is a product (among all sports k)
            # affinity between j and k (∈[0,1]) * how much the user i likes the sport k that is greater than the treshold
            # That product will be the recommendation rate

            m = max(int(users_sports[i][j])*(w*affinités[j]
                    [k]/100 + (1-w)*feedback_users[k][j]), m)

        if m >= palier_recom:
            if empty:
                user_recom.append([numéro_sport[j]])
                niv_recom.append(m)
                empty = False
            elif numéro_sport[j] not in user_recom[i]:
                user_recom[i].append(numéro_sport[j])
                niv_recom.append(m)
    # We compile all recommendation rate and convert it into a percentage
    taux_recom.append([str(niv*10) + ' %' for niv in niv_recom])
    # We class all sports according to recommandation rate (the first sport will be the most recommended)
    if empty:
        user_recom.append([])
    else:
        maxi = 5
        niv_recom = np.array(niv_recom)
        indice_recom = []
        while maxi >= 5:
            maxi = niv_recom.max()
            if maxi != 0:
                indice = np.where(niv_recom == maxi)
                indice_recom = indice_recom + list(indice[0])
                for j in list(indice[0]):
                    niv_recom[j] = 0
        l = [user_recom[i][j] for j in indice_recom]
        tx = [taux_recom[i][j] for j in indice_recom]
        user_recom[i] = l
        taux_recom[i] = tx

# We take a list of which sport each user can practise
list_sports_users = [['Badminton', 'Tennis', 'Natation', 'Basketball', 'Football'],
                     ['Escalade', 'Natation', 'Basketball', 'Football'], ['Escalade', 'Badminton', 'Natation', 'Basketball', 'Football'], ['Tennis', 'Escalade', 'Natation', 'Basketball', 'Football'], ['Badminton', 'Escalade', 'Natation', 'Basketball', 'Football'], ['Tennis', 'Natation', 'Basketball', 'Football'], ['Escalade', 'Basketball', 'Football'], ['Badminton', 'Tennis', 'Natation', 'Basketball', 'Football'], ['Badminton', 'Tennis', 'Escalade', 'Natation', 'Basketball', 'Football'], ['Tennis', 'Escalade', 'Natation', 'Basketball', 'Football'], ['Escalade', 'Natation', 'Basketball', 'Football'], ['Badminton', 'Escalade', 'Natation', 'Basketball', 'Football'], ['Badminton', 'Tennis', 'Natation', 'Basketball', 'Football'], ['Tennis', 'Escalade', 'Natation', 'Basketball', 'Football'], ['Badminton', 'Natation', 'Basketball', 'Football']]
# We eliminate of the recommendation list all the sports that each user can't practise
for i in range(len(users_sports)):
    l = []
    tx = []
    for j in range(len(user_recom[i])):
        if user_recom[i][j] in list_sports_users[i]:
            l.append(user_recom[i][j])
            tx.append(taux_recom[i][j])
    user_recom[i] = [[l[j], tx[j]] for j in range(len(l))]

# We compile on a panda dataframe the recommendation list
users = ['user ' + str(i + 1) for i in range(len(users_sports))]
nb_recomm_max = 0
for j in range(len(users_sports)):
    if len(user_recom[j]) > nb_recomm_max:
        nb_recomm_max = len(user_recom[j])
    recommandations = ['recommandation ' +
                       str(i+1) for i in range(nb_recomm_max)]
affinity_dataframe = pd.DataFrame(
    data=user_recom, index=users, columns=recommandations)
print(affinity_dataframe)

# clusters = sklearn.cluster.k_means(users_sports, n_clusters=4)
# print(clusters)

# KMeans = sklearn.cluster.KMeans(n_clusters=4)
# kmean = KMeans.fit(users_sports)
# print(kmean.cluster_centers_)
# print(kmean.labels_)
# print(KMeans.predict(np.array([[0, 6, 8, 9, 5, 4, 2, 3, 1, 5, 2, 3, 6, 4, 5, 7, 2, 1, 0, 0, 0, 0, 3, 2, 0, 1, 0, 2, 0, 1, 0], [
#      0, 1, 0, 2, 0, 6, 0, 5, 0, 0, 0, 0, 8, 0, 9, 0, 0, 0, 0, 4, 0, 6, 5, 4, 2, 1, 0, 1, 2, 0, 3], [1, 1, 1, 2, 4, 5, 1, 2, 3, 5, 4, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 2, 5, 9, 8, 9, 8, 9, 6, 5, 4]])))


# test prediction : [1.87500000e+00, 2.50000000e-01,  5.00000000e-01,  3.50000000e+00,
#                               2.50000000e-01,  2.50000000e-01,  1.50000000e+00,  1.00000000e+00,
#                               -6.93889390e-18,  1.12500000e+00,  7.50000000e-01,  3.75000000e-01,
#                               4.37500000e+00,  2.50000000e-01,  6.25000000e-01,  0.00000000e+00,
#                               1.25000000e-01,  1.37500000e+00,  1.25000000e+00,  5.50000000e+00,
#                               3.75000000e-01,  7.50000000e-01,  1.50000000e+00,  2.37500000e+00,
#                               7.50000000e-01,  3.75000000e-01,  1.12500000e+00,  4.25000000e+00,
#                               1.25000000e+00,  8.75000000e-01,  0.00000000e+00], [1.87500000e+00, 2.50000000e-01,  5.00000000e-01,  3.50000000e+00,
#                               2.50000000e-01,  2.50000000e-01,  1.50000000e+00,  1.00000000e+00,
#                               -6.93889390e-18,  1.12500000e+00,  7.50000000e-01,  3.75000000e-01,
#                               4.37500000e+00,  2.50000000e-01,  6.25000000e-01,  0.00000000e+00,
#                               1.25000000e-01,  1.37500000e+00,  1.25000000e+00,  5.50000000e+00,
#                               3.75000000e-01,  7.50000000e-01,  1.50000000e+00,  2.37500000e+00,
#                               7.50000000e-01,  3.75000000e-01,  1.12500000e+00,  4.25000000e+00,
#                               1.25000000e+00,  8.75000000e-01,  0.00000000e+00]


mets = []
with open('montre-connectee/Data/METS.csv', newline='') as csvfile:
    mets_ = csv.reader(csvfile)
    for row in mets_:
        mets.append(row)
mets.pop(0)
METS = {mets[i][0]: float(mets[i][1]) for i in range(len(mets))}
print(METS)
