from tkinter import *
from functions import *
from tkinter import ttk

#création de fenêtre
window=Tk()
window.title('My Sport Coach')
window.geometry('1080x720')

#Création du widget à onglets
tabControl = ttk.Notebook(window)

#Création des frame qui vont servir d'onglets
Recom = Frame(tabControl)
Histo = Frame(tabControl)

#Ajout du nom de ces onglets
tabControl.add(Recom, text ='Recommandation')
tabControl.add(Histo, text ='Historique')
tabControl.pack(expand = 1, fill ="both")

#Sous-frame des onglets (pour pouvoir mieux les gérer)
sub_recom = Frame(Recom)
sub_histo = Frame(Histo)

#création des frame droite et gauche dans recommandation

left_frame=Frame(sub_recom)
right_frame = Frame(sub_recom)

#Ajout d'un texte fixe dans l'onglet recommandation
Our_recom = Label(left_frame,text='Notre recommandation :',font=('Arial',30))
Our_recom.pack(pady=10)

#Sport et durée arbitraires
sport = ['Cyclisme','Tennis','Danse']
time = [30,50,20]

#commande pour vider la frame de gauche
def clear_frame():
   for widgets in left_frame.winfo_children():
      widgets.destroy()

#Commande pour changer sport
def change_sport():
    del sport[0]
    del time[0]
    clear_frame()
    Our_recom = Label(left_frame,text='Notre recommandation :',font=('Arial',30))
    Our_recom.pack(pady=10)
    sport_recom = Label(left_frame,text=sport[0],font=('Arial',30), fg='green')
    sport_recom.pack(pady=10)
    time_recom = Label(left_frame,text='Durée : '+str(time[0])+' min', font=('Arial',30),fg='red')
    time_recom.pack(pady=10)
    left_frame.grid(row=0, column = 0)

#commande pour raccourcir de 5min
def too_long():
    time[0]-=5
    clear_frame()
    Our_recom = Label(left_frame,text='Notre recommandation :',font=('Arial',30))
    Our_recom.pack(pady=10)
    sport_recom = Label(left_frame,text=sport[0],font=('Arial',30), fg='green')
    sport_recom.pack(pady=10)
    time_recom = Label(left_frame,text='Durée : '+str(time[0])+' min', font=('Arial',30),fg='red')
    time_recom.pack(pady=10)
    left_frame.grid(row=0, column = 0)

#commande pour rallonger de 5 min
def too_short():
    time[0]+=5
    clear_frame()
    Our_recom = Label(left_frame,text='Notre recommandation :',font=('Arial',30))
    Our_recom.pack(pady=10)
    sport_recom = Label(left_frame,text=sport[0],font=('Arial',30), fg='green')
    sport_recom.pack(pady=10)
    time_recom = Label(left_frame,text='Durée : '+str(time[0])+' min', font=('Arial',30),fg='red')
    time_recom.pack(pady=10)
    left_frame.grid(row=0, column = 0)

#commande pour dire que ça nous convient
def its_ok():
    clear_frame()
    noted = Label(left_frame,text='Bien noté ! Rappel :',font=('Arial',30))
    noted.pack(pady=10)
    sport_recom = Label(left_frame,text=sport[0],font=('Arial',30), fg='green')
    sport_recom.pack(pady=10)
    time_recom = Label(left_frame,text='Durée : '+str(time[0])+' min', font=('Arial',30),fg='red')
    time_recom.pack(pady=10)
    left_frame.grid(row=0, column = 0)
   


#Ajout du sport et durée recommandés
sport_recom = Label(left_frame,text=sport[0],font=('Arial',30), fg='green')
sport_recom.pack(pady=10)
time_recom = Label(left_frame,text='Durée : '+str(time[0])+' min', font=('Arial',30),fg='red')
time_recom.pack(pady=10)


#Bouton c'est très bien
ok_button = Button(right_frame,text = "C'est très bien", font=('Arial',30),width=20, command=its_ok)
ok_button.pack(pady = 15, padx= 40)

#bouton changer
change_button = Button(right_frame,text = 'Changer de sport', font=('Arial',30),width=20,command=change_sport)
change_button.pack(pady = 15, padx= 40)

#bouton Trop long
long_button = Button(right_frame,text = "C'est trop long", font=('Arial',30),width=20,command=too_long)
long_button.pack(pady = 15, padx= 40)


#Bouton trop court 
short_button = Button(right_frame,text = "C'est trop court", font=('Arial',30),width=20,command=too_short)
short_button.pack(pady = 15, padx= 40)


#Ajout d'un texte dans l'onglet Historique
Your_Histo = Label(sub_histo,text='Votre Historique',font=('Arial',30))
Your_Histo.pack()

#On choisit l'emplacement des frame droite et gauche
right_frame.grid(row=0, column = 1)
left_frame.grid(row=0, column = 0)

# On affiche ces sous-frame
sub_histo.pack(expand=YES)
sub_recom.pack(expand=YES)



#Bouclage pour que l'interface tourne
window.mainloop()

