from tkinter import *
from tkinter import ttk
from datetime import *

#création de fenêtre
window=Tk()
window.title('My Sport Coach')
window.geometry('1080x720')

#Création de la frame
frame = Frame(window)

#création des frame droite et gauche dans recommandation
left_frame=Frame(frame)
right_frame = Frame(frame)

#Ajout d'un texte fixe dans l'onglet recommandation
Our_recom = Label(left_frame,text='Notre recommandation :',font=('Arial',30))
Our_recom.pack(pady=10)

#Sport et durée arbitraires
sport = ['Cyclisme','Course à pied', 'Tennis', 'Renforcement musculaire']
time = [90,40,60,30]

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
ok_button = Button(right_frame,text = "C'est très bien", font=('Arial',30),width=20, command=its_ok, activeforeground='#727CF4')
ok_button.pack(pady = 15, padx= 40)

#bouton changer
change_button = Button(right_frame,text = 'Changer de sport', font=('Arial',30),width=20,command=change_sport,activeforeground='#727CF4')
change_button.pack(pady = 15, padx= 40)

#bouton Trop long
long_button = Button(right_frame,text = "C'est trop long", font=('Arial',30),width=20,command=too_long,activeforeground='#727CF4')
long_button.pack(pady = 15, padx= 40)


#Bouton trop court 
short_button = Button(right_frame,text = "C'est trop court", font=('Arial',30),width=20,command=too_short,activeforeground='#727CF4')
short_button.pack(pady = 15, padx= 40)


#On choisit l'emplacement des frame droite et gauche
right_frame.grid(row=0, column = 1)
left_frame.grid(row=0, column = 0)

#On affiche notre frame 
frame.pack(expand=YES)

#Bouclage pour que l'interface tourne
window.mainloop()

