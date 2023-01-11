class Patient:

    NOOB_THRESHOLD = 3
    EXPERT_THRESHOLD = 7

    def __init__(self, BPM, practice) -> None:
        self.BPM = BPM
        self.practice = practice
        self.evaluation = self.evaluate()
        self.category = "beginner" if self.evaluation < Patient.NOOB_THRESHOLD \
            else "intermediate" if self.evaluation < Patient.EXPERT_THRESHOLD else "expert"
    
    def evaluate(self):
        # Paramters to adjust
        ALPHA, BETA = 0, 0
        h_eq = self.process_activity()
        m_BPM = self.process_BPM()
        return ALPHA*m_BPM + BETA*h_eq # Sould be between 0 and 10

    def process_activity(self):
        """Return the number of equivalent hours of sport"""
        pass

    def process_BPM(self):
        """Return the mean of the BPM"""
        pass