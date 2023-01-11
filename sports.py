class Sport:

    def __init__(self, id:str, name:str, MET:float) -> None:
        self.id=id
        self.name = name
        self.MET = MET

SPORTS = {
    "badminton" : Sport("badminton", "Badminton", 4.5),
    "cyclisme" : Sport("cyclisme", "Cyclisme", 8),
    "escalade" : Sport("escalade", "Escalade", 11),
    "randonnee" : Sport("randonnee", "Randonnée", 6),
    "pingpong" : Sport("pingpong", "Ping-Pong", 4),
    "courseapied" : Sport("courseapied", "Course à pied", 8),
    "ski" : Sport("ski", "Ski", 7),
    "football" : Sport("football", "Football", 7),
    "natation" : Sport("natation", "Natation", 8),
    "volleyball" : Sport("volleyball", "Volley-ball", 4),
    "marche" : Sport("marche", "Marche", 3.3)
}