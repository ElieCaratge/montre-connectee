import numpy as np
import datetime
from Sport import SPORTS_LIST, N_SPORTS

class Patient:

    NOOB_THRESHOLD = 3
    EXPERT_THRESHOLD = 7

    @classmethod
    def generate_random_patient(cls):
        today = datetime.date.today()
        BPM = np.random.normal(70, 7, size=50)
        practice = [
            (SPORTS_LIST[np.random.randint(N_SPORTS)], today-datetime.timedelta(3*i), datetime.timedelta(minutes=np.random.randint(20, 40))) for i in range(8)
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
        # Paramters to adjust
        ALPHA, BETA = 70, 0.1
        min_eq = self.process_activity().total_seconds()//60
        m_BPM = self.process_BPM()
        return ALPHA/m_BPM + BETA*min_eq # Sould be between 0 and 10

    def process_activity(self):
        """Return the number of equivalent hours of sport"""
        sum=datetime.timedelta()
        for sport, date, duration in self.practice:
            sum += sport.equiv_hours(duration)
        return sum

    def process_BPM(self):
        """Return the mean of the BPM"""
        return np.mean(self.BPM)

myPatient = Patient.generate_random_patient()
print(myPatient.evaluation)