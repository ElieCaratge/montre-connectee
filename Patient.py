import numpy as np
import datetime
from Sport import SPORTS_LIST, N_SPORTS

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

    def __init__(self, BPM, practice) -> None:
        self.BPM = BPM
        self.practice = practice
        self.evaluation = self.evaluate()
        self.category = "beginner" if self.evaluation < Patient.NOOB_THRESHOLD \
            else "intermediate" if self.evaluation < Patient.EXPERT_THRESHOLD else "expert"

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

        sum=datetime.timedelta()
        first_activity = self.practice[0][1]

        for sport, date, duration in self.practice:
            sum += sport.equiv_hours(duration)
            if date < first_activity:
                first_activity = date

        return (sum/(datetime.date.today()-first_activity).days*7).total_seconds()/3600

    def process_BPM(self):
        """Rythme cardiaque moyen"""

        return np.mean(self.BPM)

myPatient = Patient.generate_random_patient()