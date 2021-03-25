class Goomba:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.speedX = 1
        self.speedY = 0

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def turn_around(self):
        self.speedX *= -1

    def to_string(self):
        return f"Goomba {self.id} located at ({self.x}, {self.y})"

g1 = Goomba(3, 4, 1)  # make a new Goomba at (3, 4) with id of 1
g2 = Goomba(2, 2, 2)  # make a new Goomba at (2, 2) with id of 2

goombas = []          # make a list of Goombas
goombas.append(g1)    # put one Goomba in a list
goombas.append(g2)    # put the other Gooma in the list

print(g1.to_string()) # print out Goomba details
print(g2.to_string()) # print out the other Goomba's details
g1.move()             # make one Goomba move
print(g1.to_string()) # print out Goomba details after it moved
g1.turn_around()      # make the Goomba turn around
g1.move()             # make the Goomba move (back to its original position)
g1.move()             # make the Goomba move again
print(g1.to_string()) # print out Goomba details
