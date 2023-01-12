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