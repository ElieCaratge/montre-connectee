import datetime

class Sport:

    def __init__(self, id:str, name:str, MET:float) -> None:
        self.id=id
        self.name = name
        self.MET = MET
    
    def __repr__(self) -> str:
        return f"Sport({self.name})"

    def equiv_hours(self, timedelta:datetime.timedelta)->datetime.timedelta:
        return self.MET/18*timedelta
    
    def compute_intensity(self, category):
        '''Sportivity : Beginner = 600 MET.min/semaine / Intermediate = 1500 MET.min/semaine / Expert = 3000 MET.min/semaine
        On suppose en moyenne 3j sport/semaine'''
        if category == "beginner":
            sportivity = 200
        elif category == "intermediate":
            sportivity = 500
        else:
            sportivity = 1000
        delta_t = sportivity/self.MET
        return delta_t

    @classmethod
    def new_recomendation(cls, i, patient, intensity=None):
        sport = SPORTS_LIST[i]
        if intensity != None:
            advised_intensity = sport.compute_intensity(intensity)
            category = intensity
        else :
            advised_intensity = sport.compute_intensity(patient.category)
            category = patient.category
        return (sport, advised_intensity, category)


SPORTS = {
    "badminton" : Sport("badminton", "Badminton", 4.5),
    "cyclisme" : Sport("cyclisme", "Vélo", 8),
    "escalade" : Sport("escalade", "Escalade", 11),
    "randonnee" : Sport("randonnee", "Randonnée", 6),
    "pingpong" : Sport("pingpong", "Pingpong", 4),
    "courseapied" : Sport("courseapied", "Course a pied", 8),
    "ski" : Sport("ski", "Ski", 7),
    "football" : Sport("football", "Football", 7),
    "natation" : Sport("natation", "Natation", 8),
    "volleyball" : Sport("volleyball", "Volleyball", 4),
    "marche" : Sport("marche", "Marche", 3.3)
}

SPORTS_LIST = list(SPORTS.values())

N_SPORTS = len(SPORTS_LIST)