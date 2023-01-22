from Patient import Patient
from Sport import SPORTS_LIST, SPORTS


def compute_intensity(sport, sportivity=patient.category):
    '''Sportivity : Beginner = 600 MET.min/semaine / Intermediate = 1500 MET.min/semaine / Expert = 3000 MET.min/semaine'''
    '''On suppose en moyenne 3j sport/semaine'''
    '''sport : int'''
    if Patient.category == "beginner":
        sportivity = 200
    elif Patient.category == "intermediate":
        sportivity = 500
    else:
        sportivity = 1000
    delta_t = sportivity/SPORTS_LIST[sport].MET
    return delta_t


def too_easy(sportivity=Patient.category):
    if sportivity == "beginner":
        Patient.category = "intermediate"
    if sportivity == "intermediate":
        Patient.category = "expert"


def too_hard(sportivity=Patient.category):
    if sportivity == "expert":
        Patient.category = "intermediate"
    if sportivity == "intermediate":
        Patient.category = "beginner"
