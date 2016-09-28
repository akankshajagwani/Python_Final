class PartyAnimal:
    x = 0
    def party(self):
        print self
        self.x =self.x+1
        print 'So Far', self.x
        
an = PartyAnimal()
an.party()
an.party()
an.party()
an2 = PartyAnimal()
an2.party()
an2.party()
an2.party()