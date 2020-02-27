from Animals import Cow

class Vocalizer:
    def speak(self):
        print("Vocalizing cow sound here")
		
class VocalCow(Vocalizer, Cow):
    pass

c = VocalCow('Bessie')
print(c.speak())    # speak is in both classes!
c.speak()           

