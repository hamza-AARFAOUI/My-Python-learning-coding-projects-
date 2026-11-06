class eleves :
    nom=""
    prenom=""
    numero=0
    age=0
    def afficher(self):
        print( " le nom est:"   +self.nom )
        print(" le  prenom est :" + self.prenom )
        print(" le numero est :" + str(self.numero))
        print(" le age est :" + str(self.age))
elv1= eleves()
elv1.nom="aarfaoui "
elv1.prenom=("hamza")
elv1. numero=2
elv1.age=22
elv2= eleves()
elv2.nom="aarfaoui "
elv2.prenom=("soufiane ")
elv2.numero=1
elv2.age=23
elv1.afficher()
elv2.afficher()



