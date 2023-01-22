import numpy as np
import datetime
from Sport import SPORTS_LIST, N_SPORTS, Sport
from CompatibilityMatrix import CompatibilityMatrix
from attribution_sport import fct_principale


class Patient:

    NOOB_THRESHOLD = 3
    EXPERT_THRESHOLD = 7

    @classmethod
    def generate_random_patient(cls, freq=3, nb_seances=8, min_min=30, min_max=60):
        """Générer un patient aléatoire.

        Paramètres
        ----------
        - freq (int) : Nombre de jours espacant chaque pratique sportive.
        - nb_sports (int) : Nombre de séances de sports pratiquées.
        - min_min (int) : Durée minimale d'une séance de sport.
        - min_max (int) : Durée maximale d'une séance de sport.
        """

        today = datetime.date.today()
        BPM = np.random.normal(70, 7, size=50)
        practice = [
            (SPORTS_LIST[np.random.randint(N_SPORTS)], today-datetime.timedelta(freq*i), datetime.timedelta(minutes=np.random.randint(min_min, min_max))) for i in range(nb_seances)
        ]

        return Patient(BPM, practice)

    def __init__(self, BPM, practice, liked_sports=dict()) -> None:
        """Initialisation d'un patient.

        Paramètres
        ----------
        - BPM (np.array) : Rythme cardiaque du patient.
        - practice (list) : Liste des séances de sport pratiquées par le patient.
        - liked_sports (dict) : Liste des sports préférés du patient.
        """

        self.BPM = BPM
        self.practice = practice
        self.main_sport = self.find_main_sport()
        self.evaluation = self.evaluate()
        self.category = "beginner" if self.evaluation < Patient.NOOB_THRESHOLD \
            else "intermediate" if self.evaluation < Patient.EXPERT_THRESHOLD else "expert"
        self.compatibility_matrix = CompatibilityMatrix()
        self.next_recommendation = self.new_recommendations()
        self.recomendation = Sport.new_recommendation(self.new_recommendations[0], self, intensity=None)
        
    def __repr__(self) -> str:
        return f"Patient({self.category})"

    def evaluate(self):
        """Évaluation de l'activité sportive du patient (note sur 10)"""

        # Paramètres à ajuster
        ALPHA, BETA = 70, 14
        # Traitement des données
        heq = self.process_activity()
        m_BPM = self.process_BPM()

        return ALPHA/m_BPM + BETA*heq

    def process_activity(self):
        """Nombre d'heures équivalentes de sport par semaine."""

        sum = datetime.timedelta()
        first_activity = self.practice[0][1]

        for sport, date, duration in self.practice:
            sum += sport.equiv_hours(duration)
            if date < first_activity:
                first_activity = date

        return (sum/(datetime.date.today()-first_activity).days*7).total_seconds()/3600

    def process_BPM(self):
        """Rythme cardiaque moyen"""

        return np.mean(self.BPM)

    def find_main_sport(self):
        """Sport principal du patient."""

        # Créer une liste de même longueur que la liste des sports
        practiced_sports = [0]*N_SPORTS
        # Pour chaque séance de sport, incrémenter le nombre de séances de ce sport
        for sport, date, duration in self.practice:
            practiced_sports[SPORTS_LIST.index(sport)] += 1
        # Trouver le sport le plus pratiqué
        return SPORTS_LIST[np.argmax(practiced_sports)]
    
    def hard_intensity_feedback(self):
        category = self.recomendation[2]
        if category == "expert":
            new_category = "intermediate"
        else:
            new_category = "beginner"
        self.recomendation = Sport.new_recommendation(self.new_recommendations[0], self, intensity=new_category)

    def easy_intensity_feedback(self):
        category = self.recomendation[2]
        if category == "beginner":
            new_category = "intermediate"
        else:
            new_category = "expert"
        self.recomendation = Sport.new_recommendation(self.new_recommendations[0], self, intensity=new_category)

    def do_sport(self):
        """Appelé quand le patient fait un sport"""
        sport, intensity, category = self.recomendation
        # Ajout de la pratique à l'historique
        self.practice.append((sport, datetime.datetime.now(), intensity))
        # Mise à jour de la condition physique du patient
        self.category = self.evaluate()
        # Mise à jour des coefficients de recommendation
        self.compatibility_matrix.positive_feedback(self.main_sport, sport)
        # Mise à jour du sport principal
        self.main_sport = self.find_main_sport()
        # Nouvelles recommendations
        self.next_recommendation = self.new_recommendations()

    def new_recommendations(self):
        """Génère une liste de recommandations pour le patient."""

        return fct_principale(self.compatibility_matrix.to_numpy(), SPORTS_LIST.index(self.main_sport))


myPatient = Patient.generate_random_patient()
print(myPatient.next_recommendation)
