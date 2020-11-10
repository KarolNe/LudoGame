import random

import pygame
from pygame.locals import *

print(pygame.__version__)
# window 800x800 px
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Man, don't get Angry!")

# background image
background = pygame.image.load('assets/board.jpg')
window.blit(background, (0, 0))
SCREENRECT = pygame.Rect(0, 0, 640, 640)
roll_btn_image = pygame.transform.scale(pygame.image.load('assets/rollButton.png'), (150, 150))
roll_btn_image_clicked = pygame.transform.scale(pygame.image.load('assets/rollButton_clicked.png'), (150, 150))
surface = pygame.Rect((10, 100), (32, 32))
rect1 = pygame.Rect((180, 150), (32, 32))
btn_Rect = pygame.Rect((22, 100), (32, 32))
RedPlayerArrow = pygame.Rect((150, 58), (32, 32))
BluePlayerArrow = pygame.Rect((580, 58), (32, 32))

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

rolOne_image = pygame.transform.scale(pygame.image.load('assets/dice/rollOne.png'), (50, 50))
rolTwo_image = pygame.transform.scale(pygame.image.load('assets/dice/rollTwo.png'), (50, 50))
rolThree_image = pygame.transform.scale(pygame.image.load('assets/dice/rollThree.png'), (50, 50))
rolFour_image = pygame.transform.scale(pygame.image.load('assets/dice/rollFour.png'), (50, 50))
rolFive_image = pygame.transform.scale(pygame.image.load('assets/dice/rollFive.png'), (50, 50))
rolSix_image = pygame.transform.scale(pygame.image.load('assets/dice/rollSix.png'), (50, 50))
redPawnImage = pygame.transform.scale(pygame.image.load('assets/pawns/redPawn.png'), (50, 50))
bluePawnImage = pygame.transform.scale(pygame.image.load('assets/pawns/bluePawn.png'), (50, 50))
arrowImage = pygame.transform.scale(pygame.image.load('assets/pointer.png'), (50, 50))

cube = {
  1: rolOne_image,
  2: rolTwo_image,
  3: rolThree_image,
  4: rolFour_image,
  5: rolFive_image,
  6: rolSix_image,
}


def throw_a_dice():
  score = random.randint(1, 6)
  return score


FieldCoOrdinates = {
  1: [22, 300],
  2: [82, 300],
  3: [150, 300],
  4: [215, 300],
  5: [300, 300],
  6: [300, 230],
  7: [300, 160],
  8: [300, 90],
  9: [300, 23],
  10: [370, 23],
  11: [440, 23],
  12: [440, 90],
  13: [440, 160],
  14: [440, 220],
  15: [440, 300],
  16: [505, 300],
  17: [575, 300],
  18: [645, 300],
  19: [710, 300],
  20: [710, 375],
  21: [710, 445],
  22: [645, 445],
  23: [575, 445],
  24: [505, 445],
  25: [440, 445],
  26: [440, 520],
  27: [440, 580],
  28: [440, 645],
  29: [440, 720],
  30: [370, 720],
  31: [300, 720],
  32: [300, 645],
  33: [300, 580],
  34: [300, 520],
  35: [300, 445],
  36: [215, 445],
  37: [150, 445],
  38: [82, 445],
  39: [22, 445],
  40: [22, 375]

}

zmienna = 0
PawnIsOnBoard = 0


class Pawn(pygame.sprite.Sprite):
  Position = 0
  x = 0
  y = 0
  number = 0

  def __init__(self, position, number):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Create an image of the block, and fill it with a color.
    # This could also be an image loaded from the disk.
    self.image = pygame.Surface([32, 32])

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()
    self.Position = position
    self.startPosition = FieldCoOrdinates.get(position)
    self.x = self.startPosition[0]
    self.y = self.startPosition[1]
    self.rect.move_ip(self.x, self.y)
    self.number = number

  def setPosition(self, Position):
    self.Position = Position

  def getPosition(self):
    return self.Position

  def getNumber(self):
    return self.number


class Player():
  pawnInHouse = 0
  pawnOnBoard = 0
  pawnNotInGame = 4
  color = ""
  startPosition = 0
  image = 0
  Pawns = {}
  ArrowRect = 0

  def __init__(self, color, position, PawnImage, ArrowRect):
    self.color = color
    self.startPosition = position
    self.image = PawnImage
    self.Pawns = {}
    self.ArrowRect = ArrowRect

  def setPwnInHouse(self, pawnInHouse):
    self.pawnInHouse = pawnInHouse

  def getPawnInHouse(self):
    return self.pawnInHouse

  def setPawnOnBoard(self, pawnOnBoard):
    self.pawnOnBoard = pawnOnBoard

  def getPawnOnBoard(self, ):
    return self.pawnOnBoard

  def MinusPawnNotInGame(self):
    self.pawnNotInGame -=1
  def AddPawnNotInGame(self):
    self.pawnNotInGame +=1

  def getPawnNotInGame(self):
    return self.pawnNotInGame

  def getColor(self):
    return self.color

  def getStartPosition(self):
    return self.startPosition

  def getImage(self):
    return self.image

  def setPawns(self, i, Pawn):
    self.Pawns[i] = Pawn

  def getPawns(self, i):
    return self.Pawns[i]

  def DeletePawn(self,i):
    del self.Pawns[i]

  def getArrowRect(self):
    return self.ArrowRect


def wait():
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        quit()
      if event.type == KEYDOWN and event.key == K_SPACE:
        return

def isEmpty(DestinationPosition):
    for Player in Players:
      for i in range(1, 1 + len(Player.Pawns)):
        if DestinationPosition == Player.getPawns(i).getPosition():
            Player.DeletePawn(i)
            Player.AddPawnNotInGame()





def turn(Player):
  if (Player.getStartPosition() == 1):
    window.blit(pygame.transform.flip(arrowImage, 90, 0), Player.getArrowRect())
  if (Player.getStartPosition() == 11):
    window.blit(arrowImage, Player.getArrowRect())
  pygame.display.update()
  wait()
  btn_image = roll_btn_image_clicked
  score1 = throw_a_dice()
  global cube_imgae
  cube_imgae = (cube.get(score1))
  global zmienna
  zmienna = 1
  window.blit(btn_image, btn_Rect)
  window.blit(cube_imgae, rect1)
  pygame.display.update()
  pygame.time.delay(400)
  if Player.getPawnNotInGame() == 4:
    if score1 == 1 or score1 == 6:
      Player.MinusPawnNotInGame()
      Player.setPawns(1, Pawn(Player.getStartPosition(), 1))
      window.blit(Player.getImage(), Player.getPawns(1).rect)


  else:
    ActuaclPosition = FieldCoOrdinates.get(Player.getPawns(1).getPosition())
    DesitantionIndex = Player.getPawns(1).getPosition() + score1

    if DesitantionIndex > 40:
      DesitantionIndex -= 40
    isEmpty(DesitantionIndex)
    DesitantionPosition = FieldCoOrdinates.get(DesitantionIndex)
    #print(ActuaclPosition)
    #print(DesitantionPosition)
    x = DesitantionPosition[0] - ActuaclPosition[0]
    y = DesitantionPosition[1] - ActuaclPosition[1]
    Player.getPawns(1).rect.move_ip(x, y)
    Player.getPawns(1).setPosition(DesitantionIndex)
    #print(x)
    #print(y)

    window.blit(Player.getImage(), Player.getPawns(1).rect)
    window.blit(btn_image, btn_Rect)
    window.blit(cube_imgae, rect1)
    pygame.display.update()
    # pygame.time.delay(400)


redPlayer = Player('Red', 1, redPawnImage, RedPlayerArrow)
bluePlayer = Player('Blue', 11, bluePawnImage, BluePlayerArrow)
greenPlayer = Player('Green', 21, redPawnImage, RedPlayerArrow)
yellowPlayer = Player('Yellow', 31, redPawnImage, RedPlayerArrow)


Players = {redPlayer, bluePlayer}

while True:

  btn_image = roll_btn_image
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  turn(redPlayer)
  window.blit(background, (0, 0))
  window.blit(btn_image, btn_Rect)
  if zmienna == 1:
    window.blit(cube_imgae, rect1)
  for Player in Players:
    for i in range(1, 1 + len(Player.Pawns)):
      window.blit(Player.getImage(), Player.getPawns(i).rect)

  pygame.display.update()

  turn(bluePlayer)
  window.blit(background, (0, 0))
  window.blit(btn_image, btn_Rect)
  if zmienna == 1:
    window.blit(cube_imgae, rect1)
  for Player in Players:
    for i in range(1,1+len(Player.Pawns)):
        window.blit(Player.getImage(), Player.getPawns(i).rect)

pygame.display.update()
