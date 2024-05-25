from tkinter import *
from experta import *

class Profil(Fact):
    pass

class SystemeExpert(KnowledgeEngine):
    questions = [
        (" \n \n \n Quel est votre niveau en langues (de 0 à 10)?\n \n", "langue"),
        (" \n \n \n Quel est votre niveau en mathématiques (de 0 à 10)?\n \n", "mathematiques"),
        (" \n \n \n Quel est votre niveau en Sciences Expérimentales (de 0 à 10)?\n \n", "scExp"),
        (" \n \n \n Quel est votre niveau en Informatique (de 0 à 10)?\n \n", "info"),
        (" \n \n \n Aimez vous le contact avec les gens ?\n \n 1.Oui \n 2.Non\n \n ","contact"),
        (" \n \n \n Acceptez-vous un salaire :\n \n 1.Moyen \n 2.Elevé \n \n","salaire"),
        (" \n \n \n Voulez-vous une profession libre?\n  \n 1.Oui \n 2.Non \n \n","libre"),
        (" \n \n \n Avez-vous un bon sens pédagogique? \n \n 1.Oui \n 2.Non\n \n ","pédagogie"),       
        (" \n \n \n Quel domaine préférez vous?\n \n 1.Informatique \n 2.Santé \n 3.Ingénierie \n 4.Enseignement \n 5.Journalisme \n 6.Droits\n \n", "domaine")]
    current_question = 0

    def ask_question(self):
        question_label.config(text=self.questions[self.current_question][0])

    def next_question(self):
        update_result()
        if self.current_question < len(self.questions):
            setattr(self, self.questions[self.current_question][1], int(reponse_entry.get()))
            self.declare(Profil(**{self.questions[self.current_question][1]: int(reponse_entry.get())}))  # Enregistrement des réponses dans les faits
            reponse_entry.delete(0, END)
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.ask_question()
            else:
                self.run()
    
    @Rule(Profil(langue=P(lambda x: x >= 5)),Profil(mathematiques=P(lambda x: x >= 7)),
          Profil(info=P(lambda x: x >= 8)),Profil(libre=1),Profil(salaire=2),OR(Profil(domaine=1),Profil(domaine=3)))
    def informatique_libre(self):
        resultat_label.config(text=" \n  ====> Profil adapté pour un poste d'ingénieur informatique freelancer .\n")
        res()

    @Rule(Profil(langue=P(lambda x: x >= 5)),Profil(mathematiques=P(lambda x: x >= 7)),
          Profil(info=P(lambda x: x >= 8)),Profil(libre=2),Profil(salaire=2),OR(Profil(domaine=1),Profil(domaine=3)))
    def informatique_nonlibre(self):
        resultat_label.config(text=" \n ====> Profil adapté pour un poste d'ingénieur informatique dans une entreprise .\n")
        res()

    @Rule(Profil(langue=P(lambda x: x >= 5)),OR(Profil(mathematiques=P(lambda x: x >= 7)),
          Profil(info=P(lambda x: x >= 7)),Profil(scExp=P(lambda x: x >= 7))),Profil(salaire=2),Profil(domaine=3))
    def ing(self):
        resultat_label.config(text=" \n ====> Profil adapté pour un poste d'ingénieur .\n")
        res()

    @Rule(AND(Profil(langue=P(lambda x: x >= 6)),Profil(pédagogie=1),Profil(salaire=1), Profil(mathematiques=P(lambda x: x >= 7)), 
              Profil(domaine=4),))
    def profMath(self):
        resultat_label.config(text=" \n ====> Profil adapté pour un poste de professeur en Mathématiques.\n")
        res()
 
    @Rule(AND(Profil(langue=P(lambda x: x >= 6)),Profil(pédagogie=1),Profil(salaire=1), Profil(scExp=P(lambda x: x >= 7)), Profil(domaine=4),))
    def profScExp(self):
        resultat_label.config(text=" \n ====> Profil adapté pour un poste de professeur en Sciences .\n")
        res()
 
    @Rule(AND(Profil(langue=P(lambda x: x >= 6)),Profil(pédagogie=1),Profil(salaire=1), Profil(info=P(lambda x: x >= 7)), Profil(domaine=4),))
    def profInfo(self):
        resultat_label.config(text=" \n ====>Profil adapté pour un poste de professeur en Informatique.\n")
        res()
 
    @Rule(AND(Profil(langue=P(lambda x: x >= 8)),Profil(pédagogie=1),Profil(salaire=1), Profil(domaine=4),))
    def profLang(self):
        resultat_label.config(text=" \n====> Profil adapté pour un poste de professeur en Langues.\n")
        res()

    @Rule(AND(Profil(langue=P(lambda x: x >= 7)), Profil(mathematiques=P(lambda x: x >= 5)), Profil(scExp=P(lambda x: x >= 8)),
               Profil(domaine=2),Profil(contact=1),Profil(salaire=2)))
    def medecine(self):
        resultat_label.config(text=" \n ====> Profil adapté pour un poste de Medecin.\n")
        res()

    @Rule(AND(Profil(langue=P(lambda x: x >= 5)), Profil(mathematiques=P(lambda x: x >= 3)), Profil(scExp=P(lambda x: x >= 6)),
               Profil(domaine=2),Profil(contact=1),Profil(salaire=1)))
    def paramedical(self):
        resultat_label.config(text=" \n====> Profil adapté pour un poste de paramédical.\n")
        res()
    
    @Rule(AND(Profil(langue=P(lambda x: x >= 7)),Profil(domaine=5),Profil(contact=1),Profil(libre=1)))
    def Journaliste(self):
        resultat_label.config(text=" \n====> Profil adapté pour un poste de journaliste.\n")
        res()

    @Rule(AND(Profil(langue=P(lambda x: x >= 7)),Profil(domaine=6),Profil(contact=1),Profil(libre=1)))
    def droits(self):
        resultat_label.config(text=" \n====> Profil adapté pour un poste de Juriste ou Avocat.\n")
        res()

    @Rule(Profil(langue=P(lambda x: x <5)))
    def non_correspondance(self):
        resultat_label.config(text=" \n => Aucune correspondance avec les professions spécifiées.\n",fg="#6d051b")
        res()


    def obtenir_profil(self):
        self.ask_question()

# Configuration de l'interface graphique avec Tkinter
root = Tk()
root.title("Système Expert - Meilleure profession")
root.configure(bg="#fbe7e7")

title_label = Label(root, text="\n \n --------------------------------------------------------- \n Système Expert - Meilleure profession\n ---------------------------------------------------------\n", font=("Arial", 18),bg="#fbe7e7", fg="#650852")
title_label.pack(pady=10)


question_title = Label(root, text="Répondez aux questions suivantes soigneusement svp ! ", font=("Arial", 12), bg="#fbe7e7",fg="#655808")
question_title.pack()


question_label = Label(root, text="",bg="#fbe7e7")
question_label.pack()

reponse_entry = Entry(root)
reponse_entry.pack()

systeme = SystemeExpert()

def update_result():
    systeme.run()

bouton_suivant = Button(root, text="Suivant", command=systeme.next_question,bg="#620543", fg="white", font=("Arial", 12))
bouton_suivant.pack(pady=10)

remerciement_affiche = False
def res():        
    global remerciement_affiche       
    question_label.pack_forget()  # Cacher les autres éléments
    reponse_entry.pack_forget()
    question_title.pack_forget()
    bouton_suivant.pack_forget()
    if not remerciement_affiche:  # Vérifier si le remerciement a déjà été affiché
        merci_title = Label(root, text="Merci pour votre réponse ! ", font=("Arial", 10), bg="#fbe7e7",fg="#655808")
        merci_title.pack()
        remerciement_affiche = True  # Mettre à jour le drapeau pour indiquer que le message a été affiché

resultat_label = Label(root, text="",fg="#1449b2",bg="#fbe7e7",font=("Arial", 12))
resultat_label.pack()

systeme.ask_question()


def quitter():
    root.quit()  # Ferme la fenêtre principale

bouton_quitter = Button(root, text="Quitter", command=quitter,bg="#866c71", fg="black", font=("Arial", 12))
bouton_quitter.pack(pady=10)

root.mainloop()