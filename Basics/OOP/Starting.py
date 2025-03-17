class Animal:
  x = 0

  def party(self):
    self.x = self.x + 1
    print('So far', self.x)

an = Animal()
print("dir", dir(an))
an.party()
an.party()
an.party()
an.party()
Animal.party(an)