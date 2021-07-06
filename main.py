# text based game
# define character name
# this game will lead to actual other minigames
# gameloops will be needed for all of them
# when certain commands are typed ie secret passwords other games will open, and on getting a certain score within these games you can continue the main text based story
# there shall be many ways to die in this game, wrong decisions will cause death
# however the correct decision may not always be the most obvious
# and of course there will be easter eggs (grue)
# have card elements inside this so that you can collect and use spells at certain times, cards do specific things and the command to us them will only be available if you have been given the card, unless you want to have a skill based game and therefore if you can remeber the names of the spells and how to use them they may actually be useful in other places
# ensure the game has a save function
# maybe have the start to the real game hidden within the card game menu somewhere
# i want the to be a whole inventory system, which will only allow you to use the items if you have them
# I want to game to be text based but with graphics to go along with it, to keep track of inventory etc.
# I want to ability to customise character and background, with an image of that character that will be different depending on the options/ class /background you choose
# TODO: Create the Story
# Todo: Create the main menu, will likely just use the one from card_game
# todo: mini game loops
# todo: further definitions
# todo: create places with images
# todo: have interactive towns
# todo: make the game able to restart on death
# todo: create a nice looking UI
# todo: make the inputs simple so that you dont have to type absolutely everything

import pygame, sys, time, math, random, pip, PIL
from time import sleep
from pygame import mixer
from pygame.locals import *
from PIL import Image
from pprint import pprint

pygame.init()
import pygame.freetype

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.mixer.init()

# definitions

# colours
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
dark_red = 110, 0, 0
slighty_lighter_red = 150, 0, 0
yellow = 255, 255, 0
cyan = 0, 255, 255
magenta = 255, 0, 255
purple = 110, 0, 255
fuschia = 255, 0, 110
sky_blue = 0, 120, 255
turquoise_green = 0, 255, 115
grey = 110, 110, 110
orange = 225, 120, 0
dark_green = 0, 100, 0
dark_blue = 0, 0, 120
# colours

# screen settings 2560 x 1440 for big monitor, 1920 x 1080 fits my small screen, 1280 x 720 will have the same aspect ratio but be smaller


screen_width = 1920
screen_height = 1080

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# fonts

big_font = pygame.font.Font('freesansbold.ttf', int(screen_width / 24))
base_font = pygame.font.Font(None, int(screen_width/60))
small_font = pygame.font.Font(None, int(screen_width / 44))
font = pygame.font.Font(None, int(screen_width / 38.4))
game_font = pygame.font.Font('freesansbold.ttf', int(screen_width / 96))
user_text = ''

input_rect = pygame.Rect(round(screen_width/(1920/100)), round(screen_height/(1080/200)), round(screen_width/(1920/140)), round(screen_height/(1080/32)))
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
class Character:
    def __init__(self, MChealth, MCattack, MCdefence, MCluck, MCrace, MCmagic, MCname):
        self.health = MChealth
        self.attack = MCattack
        self.defence = MCdefence
        self.luck = MCluck
        self.race = MCrace
        self.magic = MCmagic
        self.name = MCname

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getDefence(self):
        return self.defence

    def getLuck(self):
        return self.luck

    def getRace(self):
        return self.race

    def getMagic(self):
        return self.magic

    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setDefence(self, newDefence):
        self.defence = newDefence

    def setLuck(self, newLuck):
        self.luck = newLuck

    def setRace(self, newRace):
        self.race = newRace

    def setMagic(self, newMagic):
        self.magic = newMagic

    def setName(self, newName):
        self.name = newName


# Base images------------------------------------------------------------------------------------------------------------------------------------------
orc_image = pygame.image.load('Base_orc.png')
orc_imageX = screen_width/(1920/1200)
orc_imageY = screen_height/(1080/149)

human_image = pygame.image.load('Base_human.png')
human_imageX = screen_width/(1920/1201)
human_imageY = screen_height/(1080/154)

elf_image = pygame.image.load('Base_elf.png')
elf_imageX = screen_width/(1920/1190)
elf_imageY = screen_height/(1080/150)

# mage images
orc_mage_image = pygame.image.load('orc_mage.png')
orc_mage_imageX = screen_width/(1920/1200)
orc_mage_imageY = screen_height/(1080/100)

human_mage_image = pygame.image.load('human_mage.png')
human_mage_imageX = screen_width/(1920/1200)
human_mage_imageY = screen_height/(1080/120)

elf_mage_image = pygame.image.load('elf_mage.png')
elf_mage_imageX = screen_width/(1920/1200)
elf_mage_imageY = screen_height/(1080/100)

# fighter images
orc_fighter_image = pygame.image.load('orc_fighter.png')
orc_fighter_imageX = screen_width/(1920/1200)
orc_fighter_imageY = screen_height/(1080/150)

human_fighter_image = pygame.image.load('human_fighter.png')
human_fighter_imageX = screen_width/(1920/1202)
human_fighter_imageY = screen_height/(1080/154)

elf_fighter_image = pygame.image.load('elf_fighter.png')
elf_fighter_imageX = screen_width/(1920/1200)
elf_fighter_imageY = screen_height/(1080/150)

# noble images
orc_noble_image = pygame.image.load('orc_noble.png')
orc_noble_imageX = screen_width/(1920/1200)
orc_noble_imageY = screen_height/(1080/100)

human_noble_image = pygame.image.load('human_noble.png')
human_noble_imageX = screen_width/(1920/1200)
human_noble_imageY = screen_height/(1080/100)

elf_noble_image = pygame.image.load('elf_noble.png')
elf_noble_imageX = screen_width/(1920/1200)
elf_noble_imageY = screen_height/(1080/100)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# sound


pygame.mixer.music.load('beautiful_village.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.queue('elven_forest.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.queue('forest_ventures.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.load('beautiful_village.mp3')
pygame.mixer.music.play(-1)

Volume = pygame.mixer.music.set_volume(0.1)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# initialise game everything after this is game

pygame.display.set_caption("Untitled Game, test area")
screen = pygame.display.set_mode((screen_width, screen_height))
icon = pygame.image.load('DM_char_whitebackground.png')
pygame.display.set_icon(icon)

# Dungeon Master
DM_tutorial = pygame.image.load('resized_DM_char.png')
DMX = int(screen_width / 2.4)
DMY = int(screen_height / 10.8)
DMX_change = 0
DMY_change = 0

# coin
coin = pygame.image.load('resized_coin_blackbg.png')
coinX = int(screen_width / 2.4)
coinY = int(screen_height / 7.2)

bg = pygame.image.load("resizedfantasybackground1.png")
bgf1 = pygame.image.load("resizedfantasybackground1f.png")
bgf2 = pygame.image.load("resizedfantasybackground2f.png")
bgf3 = pygame.image.load("resizedfantasybackground3f.png")
bgf4 = pygame.image.load("resizedfantasybackground4f.png")


# Main Character - have this relate to the hero class, and have the code select the correct file from the list depending on which

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# todo: create character classes copy everything in here from scratch_9
# todo: create character attributes
# todo: create character artwork


# todo: find fantasy background for the character creation screen/ tutorial
# background section

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (int(x), int(y))
    surface.blit(textobj, textrect)


def update():
    pygame.display.update()


# images
def coin_image(x, y):
    screen.blit(coin, (round(x), round(y)))


def DM(x, y):
    screen.blit(DM_tutorial, (round(x), round(y)))


def Raceimage():
    if hRace == 'Orc':
        Orcimage(orc_imageX, orc_imageY)


    elif hRace == 'Human':
        Humanimage(human_imageX, human_imageY)

    elif hRace == 'Elf':
        Elfimage(elf_imageX, elf_imageY)


def Mageimage():
    if hRace == 'Orc':
        orcmageimage(orc_mage_imageX, orc_mage_imageY)

    elif hRace == 'Elf':
        elfmageimage(elf_mage_imageX, elf_mage_imageY)

    elif hRace == 'Human':
        humanmageimage(human_mage_imageX, human_mage_imageY)


def Fighterimage():
    if hRace == 'Orc':
        orcfighterimage(orc_fighter_imageX, orc_fighter_imageY)

    elif hRace == 'Elf':
        elffighterimage(elf_fighter_imageX, elf_fighter_imageY)

    elif hRace == 'Human':
        humanfighterimage(human_fighter_imageX, human_fighter_imageY)


def Nobleimage():
    if hRace == 'Orc':
        orcnobleimage(orc_noble_imageX, orc_noble_imageY)

    elif hRace == 'Elf':
        elfnobleimage(elf_noble_imageX, elf_noble_imageY)

    elif hRace == 'Human':
        humannobleimage(human_noble_imageX, human_noble_imageY)


def orcmageimage(x, y):
    screen.blit(orc_mage_image, (x, y))


def humanmageimage(x, y):
    screen.blit(human_mage_image, (x, y))


def elfmageimage(x, y):
    screen.blit(elf_mage_image, (x, y))


def orcfighterimage(x, y):
    screen.blit(orc_fighter_image, (x, y))


def humanfighterimage(x, y):
    screen.blit(human_fighter_image, (x, y))


def elffighterimage(x, y):
    screen.blit(elf_fighter_image, (x, y))


def orcnobleimage(x, y):
    screen.blit(orc_noble_image, (x, y))


def humannobleimage(x, y):
    screen.blit(human_noble_image, (x, y))


def elfnobleimage(x, y):
    screen.blit(elf_noble_image, (x, y))


def Orcimage(x, y):
    screen.blit(orc_image, (x, y))


def Humanimage(x, y):
    screen.blit(human_image, (x, y))


def Elfimage(x, y):
    screen.blit(elf_image, (x, y))


def story_text(text, y):
    draw_text(text, font, white, screen, screen_width/(1920/100), screen_height/(1080/(y * 100)))


def story_text_dark(text, y):
    draw_text(text, font, black, screen, screen_width/(1920/100), screen_height/(1080/(y * 100)))


def eyes_close():
    screen.fill(black)
    screen.blit(bgf4, (0, 0))
    update()
    time.sleep(0.05)
    screen.fill(black)
    screen.blit(bgf3, (0, 0))
    update()
    time.sleep(0.05)
    screen.fill(black)
    screen.blit(bgf2, (0, 0))
    update()
    time.sleep(0.05)
    screen.fill(black)
    screen.blit(bgf1, (0, 0))
    update()
    time.sleep(0.05)
    screen.fill(black)
    update()
    time.sleep(0.5)


def eyes_open():
    screen.fill(black)
    time.sleep(0.2)
    screen.blit(bgf1, (0, 0))
    update()
    time.sleep(0.05)
    screen.blit(bgf2, (0, 0))
    update()
    time.sleep(0.05)
    screen.blit(bgf3, (0, 0))
    update()
    time.sleep(0.05)
    screen.blit(bgf4, (0, 0))
    update()
    time.sleep(0.05)
    screen.blit(bg, (0, 0))
    update()
    time.sleep(2)


def eyes_open_fast():
    screen.blit(bgf1, (0, 0))
    update()
    time.sleep(0.01)
    screen.blit(bgf2, (0, 0))
    update()
    time.sleep(0.01)
    screen.blit(bgf3, (0, 0))
    update()
    time.sleep(0.01)
    screen.blit(bgf4, (0, 0))
    update()
    time.sleep(0.01)
    screen.blit(bg, (0, 0))
    update()
    time.sleep(2)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def stats_race_text():
    draw_text("Attack: " + str(hAttack), font, white, screen, screen_width/(1920/100), screen_height/(1080/200))
    draw_text("Defence: " + str(hDefence), font, white, screen, screen_width/(1920/100), screen_height/(1080/250))
    draw_text("Magic: " + str(hMagic), font, white, screen, screen_width/(1920/100), screen_height/(1080/300))


def character_background_text():
    draw_text('Mage', font, white, screen, screen_width/(1920/175), screen_height/(1080/415))
    draw_text('Fighter', font, white, screen, screen_width/(1920/460), screen_height/(1080/415))
    draw_text('Noble', font, white, screen, screen_width/(1920/770), screen_height/(1080/415))


def choice_1_text():
    draw_text('Knife', font, white, screen, screen_width/(1920/110), screen_height/(1080/710))
    draw_text('Run', font, white, screen, screen_width/(1920/410), screen_height/(1080/710))


def find_character_race():
    global contents
    f = open("Characterrace.txt", 'r')
    if f.mode == 'r':
        Race = f.read(10)
        print(Race)


def find_character_name():
    global contents
    f = open("Charactername.txt", 'r')
    if f.mode == 'r':
        contents = f.read(10)
        f.close()


def setBackground():
    global hbackground
    f = open("Characterbackground.txt", "w+")
    f.write(str(hbackground))
    f.close()


def getBackground():
    global hbackground
    f = open("Characterbackground.txt", "r")
    if f.mode == 'r':
        hbackground = f.read(7)
        f.close()


def character_creation_text():
    draw_text('Elf', font, white, screen, screen_width/(1920/180), screen_height/(1080/415))
    draw_text('Orc', font, white, screen, screen_width/(1920/480), screen_height/(1080/415))
    draw_text('Human', font, white, screen, screen_width/(1920/760), screen_height/(1080/415))


def StoryPart_1():
    screen.fill(black)
    story = True
    while story:
        f = open("Charactername.txt", "r")
        Heroname = f.read(10)
        f.close()
        f = open("C:/Users\me\PycharmProjects\TextBasedGame\Characterbackground.txt", "r")
        Herobackground = f.read(7)
        f.close()

        story_text("Hello " + Heroname + " !", 1)
        update()
        time.sleep(1)
        story_text("You are now part of our world, and have embarked on the path of a " + Herobackground, 2)
        update()
        time.sleep(1)
        story_text("It's time to wake up.", 3)
        update()
        time.sleep(2)
        eyes_open()
        # -----------------------------------------------
        eyes_close()
        # ---------------------------------------------
        eyes_open_fast()

        story_text_dark('You have awoken in the forest, you recall that you were travelling back from', 1)
        story_text_dark('the neighbouring city after a trade mission.', 1.5)
        update()
        time.sleep(2)
        story_text_dark('You look down and realise you hands are bound, clearly the mission was a failure.', 2.5)
        update()
        time.sleep(1)
        story_text_dark('As you start to regain some sense,', 3.5)
        story_text_dark('you begin to look around to try and get out of the situation you find yourself in.', 4)
        update()
        time.sleep(1)

        eyes_close()
        story_text('You cannot see anyone nearby, nor can you hear anyone.', 1)
        update()
        time.sleep(1)
        story_text('Near to you, on a table you can see a small knife', 2)
        story_text('You also realise that your legs are not bound and you are able to move', 2.5)
        update()
        time.sleep(1)
        story_text('Would you like to attempt to use the knife to escape,', 3.5)
        story_text('or try to make a run for it without untying your hands?', 4)
        update()
        choice_1()


def choice_1():
    running = True
    while running:

        mx, my = pygame.mouse.get_pos()

        button_knife = pygame.Rect(screen_width/(1920/100), screen_height/(1080/700), screen_width/(1920/200), screen_height/(1080/50))
        button_run = pygame.Rect(screen_width/(1920/400), screen_height/(1080/700), screen_width/(1920/200), screen_height/(1080/50))

        pygame.draw.rect(screen, (dark_red), button_knife)
        pygame.draw.rect(screen, (dark_red), button_run)
        choice_1_text()

        click_select_choice_1 = False

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_select_choice_1 = True

        if button_knife.collidepoint((mx, my)):
            pygame.draw.rect(screen, (slighty_lighter_red), button_knife)
            pygame.draw.rect(screen, (dark_red), button_run)
            choice_1_text()
            update()
            if click_select_choice_1:
                knife_choice_1()
        # this is where links to the decisions will go, this is the nobles path so far however as this is the only story that has anything in it all paths lead to this, later on down the line, this will be one of multiple beginnings for the noble path.

        elif button_run.collidepoint((mx, my)):
            pygame.draw.rect(screen, (dark_red), button_knife)
            pygame.draw.rect(screen, (slighty_lighter_red), button_run)
            choice_1_text()
            update()
            if click_select_choice_1:
                run_choice_1()
        update()


def knife_choice_1():
    screen.fill(black)
    update()
    if hRace == "Elf":
        story_text("As an Elf you are more dexterous than most and you are able to quietly move to the knife", 1)
        update()


    elif hRace == "Orc":
        story_text("As an Orc you are less dexterous than most and you make a large amount of noise", 1)
        update()


    elif hRace == "Human":
        story_text("As a Human you are fairly dexterous and quietly manage to get to teh knife", 1)
        update()


    elif hRace == "Dark Elf":
        story_text(
            "Oh Nix of course you manage to get the knife, in fact you deftly take the knife and cut your bindings", 1)
        update()

    pass


def run_choice_1():
    screen.fill(black)
    update()
    if hRace == "Elf":
        story_text("As an Elf", 1)
        update()


    elif hRace == "Orc":
        story_text("As an Orc", 1)
        update()


    elif hRace == "Human":
        story_text("As a Human", 1)
        update()


    elif hRace == "Dark Elf":
        story_text(
            "Nix nix nix", 1)
        update()

    pass



# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# restart loop
def play_again():
    # this will need to contain all of the variables to be reset when the game needs restarted, ie gold, hp, class, everything.
    pass


def character_background():
    global click_select_background, hbackground
    raceselect = True
    while raceselect:

        screen.fill(black)
        if hRace == "Human":
            draw_text("You are a " + str(hRace), big_font, white, screen, screen_width/(1920/100), screen_height/(1080/100))

        else:
            draw_text("You are an " + str(hRace), big_font, white, screen, screen_width/(1920/100), screen_height/(1080/100))

        stats_race_text()

        mx, my = pygame.mouse.get_pos()

        button_mage = pygame.Rect(screen_width/(1920/100), screen_height/(1080/400), screen_width/(1920/200), screen_height/(1080/50))
        button_fighter = pygame.Rect(screen_width/(1920/400), screen_height/(1080/400), screen_width/(1920/200), screen_height/(1080/50))
        button_noble = pygame.Rect(screen_width/(1920/700), screen_height/(1080/400), screen_width/(1920/200), screen_height/(1080/50))

        pygame.draw.rect(screen, (dark_red), button_mage)
        pygame.draw.rect(screen, (dark_red), button_fighter)
        pygame.draw.rect(screen, (dark_red), button_noble)
        Raceimage()
        character_background_text()

        # this is the code for making buttons work, this section needs to go above the button collision code
        click_select_background = False

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_select_background = True

        if button_mage.collidepoint((mx, my)):
            pygame.draw.rect(screen, (slighty_lighter_red), button_mage)
            pygame.draw.rect(screen, (dark_red), button_fighter)
            pygame.draw.rect(screen, (dark_red), button_noble)
            character_background_text()
            Mageimage()
            update()
            if click_select_background:
                hbackground = "mage"
                setBackground()
                StoryPart_1()

        if button_fighter.collidepoint((mx, my)):
            pygame.draw.rect(screen, (dark_red), button_mage)
            pygame.draw.rect(screen, (slighty_lighter_red), button_fighter)
            pygame.draw.rect(screen, (dark_red), button_noble)
            character_background_text()
            Fighterimage()
            update()
            if click_select_background:
                hbackground = "fighter"
                setBackground()
                StoryPart_1()

        if button_noble.collidepoint((mx, my)):
            pygame.draw.rect(screen, (dark_red), button_mage)
            pygame.draw.rect(screen, (dark_red), button_fighter)
            pygame.draw.rect(screen, (slighty_lighter_red), button_noble)
            character_background_text()
            Nobleimage()
            pygame.display.update()
            if click_select_background:
                hbackground = "noble"
                setBackground()
                StoryPart_1()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def character_race():
    global hRace, hAttack, hDefence, hMagic
    f = open("C:/Users/me/PycharmProjects/TextBasedGame/venv/Charactername.txt", 'a')
    f.write(" " + str(hRace))
    f.close()
    screen.fill(black)
    if hRace == "Human":
        draw_text("You are a " + str(hRace), big_font, white, screen, screen_width/(1920/100), screen_height/(1080/100))
        f = open("C:/Users/me/PycharmProjects/TextBasedGame/venv/Characterrace.txt", "w+")
        f.write(str(hRace))
        f.close()
        pygame.display.update()
    else:
        draw_text("You are an " + str(hRace), big_font, white, screen, screen_width/(1920/100), screen_height/(1080/100))
        f = open("C:/Users/me/PycharmProjects/TextBasedGame/venv/Characterrace.txt", "w+")
        f.write(str(hRace))
        f.close()
        pygame.display.update()

    if hRace == "Orc":
        Raceimage()
        hAttack = 75
        hMagic = 0
        hDefence = 50
        stats_race_text()
        pygame.display.update()
        character_background()
        time.sleep(3)

    elif hRace == "Human":
        Raceimage()
        hAttack = 70
        hMagic = 25
        hDefence = 30
        stats_race_text()
        pygame.display.update()
        character_background()
        time.sleep(3)

    elif hRace == "Elf":
        Raceimage()
        hAttack = 15
        hMagic = 100
        hDefence = 10
        stats_race_text()
        pygame.display.update()
        character_background()
        time.sleep(3)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


def character_creation():
    global hRace, hName, contents
    time.sleep(0.2)
    screen.fill(black)
    find_character_name()
    draw_text("Welcome " + (str(contents)) + "!", font, white, screen, screen_width/(1920/100), screen_height/(1080/100))
    pygame.display.update()
    time.sleep(1)
    draw_text("This is a fantasy world,", font, white, screen, screen_width/(1920/100), screen_height/(1080/200))
    pygame.display.update()
    time.sleep(1)
    draw_text("Here, there are several races of sentient beings, ", font, white, screen, screen_width/(1920/100), screen_height/(1080/300))
    draw_text("From which of the races are you descended?", font, white, screen, screen_width/(1920/100), screen_height/(1080/350))
    pygame.display.update()
    time.sleep(2)
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()

        button_elf = pygame.Rect(screen_width/(1920/100), screen_height/(1080/400), screen_width/(1920/200), screen_height/(1080/50))
        button_orc = pygame.Rect(screen_width/(1920/400), screen_height/(1080/400), screen_width/(1920/200), screen_height/(1080/50))
        button_human = pygame.Rect(screen_width/(1920/700), screen_height/(1080/400), screen_width/(1920/200), screen_height/(1080/50))

        pygame.draw.rect(screen, (dark_red), button_elf)
        pygame.draw.rect(screen, (dark_red), button_orc)
        pygame.draw.rect(screen, (dark_red), button_human)
        character_creation_text()

        if button_elf.collidepoint((mx, my)):
            pygame.draw.rect(screen, (slighty_lighter_red), button_elf)
            pygame.draw.rect(screen, (dark_red), button_orc)
            pygame.draw.rect(screen, (dark_red), button_human)
            character_creation_text()
            Elfimage(elf_imageX, elf_imageY)
            pygame.display.update()
            if click_char_creation:
                hRace = "Elf"
                character_race()

        if button_orc.collidepoint((mx, my)):
            pygame.draw.rect(screen, (dark_red), button_elf)
            pygame.draw.rect(screen, (slighty_lighter_red), button_orc)
            pygame.draw.rect(screen, (dark_red), button_human)
            character_creation_text()
            Orcimage(orc_imageX, orc_imageY)
            pygame.display.update()
            if click_char_creation:
                hRace = "Orc"
                character_race()

        if button_human.collidepoint((mx, my)):
            pygame.draw.rect(screen, (dark_red), button_elf)
            pygame.draw.rect(screen, (dark_red), button_orc)
            pygame.draw.rect(screen, (slighty_lighter_red), button_human)
            character_creation_text()
            Humanimage(human_imageX, human_imageY)
            pygame.display.update()
            if click_char_creation:
                hRace = "Human"
                character_race()

        click_char_creation = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_char_creation = True

        pygame.display.update()


active = False


def text_input_screen():
    global active, user_text, color
    running = True
    while running:

        screen.fill(black)

        if active:
            color = color_active
        else:
            color = color_passive

        draw_text("What is your Name?", font, white, screen, screen_width/(1920/100), screen_height/(1080/100))

        pygame.draw.rect(screen, color, input_rect, 2)

        text_surface = base_font.render(user_text, True, white)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    hName = user_text
                    f = open("Charactername.txt", "w")
                    f.write(str(hName))
                    f.close()
                    character_creation()
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not input_rect.collidepoint(event.pos):
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]

                    else:
                        user_text += event.unicode


# Main Menu loop
def main_game_loop():
    time.sleep(0.2)
    click = False
    running = True
    while running:
        screen.fill(black)
        # Fill in the positional data for this section when we manage to get onto that
        draw_text(" ", font, white, screen, screen_width/(1920/100), screen_height/(1080/100))
        pygame.display.update()


# text shorten
def text_mainmenu():
    draw_text("Begin adventure", font, white, screen, screen_width/(1920/460), screen_height/(1080/635))
    draw_text("Options", font, white, screen, screen_width/(1920/1210), screen_height/(1080/635))
    draw_text("Quit Game", font, white, screen, screen_width/(1920/855), screen_height/(1080/885))
    draw_text("Untitled RPG", big_font, white, screen, screen_width/(1920/680), screen_height/(1080/450))


def text_options():
    draw_text("Audio", font, white, screen, screen_width/(1920/550), screen_height/(1080/635))
    draw_text("Video", font, white, screen, screen_width/(1920/1230), screen_height/(1080/635))
    draw_text("Credits", font, white, screen, screen_width/(1920/535), screen_height/(1080/885))
    draw_text("Options", big_font, white, screen, screen_width/(1920/780), screen_height/(1080/50))
    draw_text("Main Menu", font, white, screen, screen_width/(1920/1190), screen_height/(1080/885))
    coin_image(coinX, coinY)


def video_text():
    draw_text("Large", font, white, screen, screen_width/(1920/400), screen_height/(1080/635))
    draw_text("Normal", font, white, screen, screen_width/(1920/890), screen_height/(1080/635))
    draw_text("Small", font, white, screen, screen_width/(1920/1400), screen_height/(1080/635))
    draw_text("Video Settings", big_font, white, screen, screen_width/(1920/660), screen_height/(1080/50))


def video():
    time.sleep(0.2)
    global screen, screen_width, screen_height
    click_video = False
    running = True
    while running:
        screen.fill(black)

        button_large = pygame.Rect(screen_width/(1920/300), screen_height/(1080/600), screen_width/(1920/300), screen_height/(1080/100))
        button_normal = pygame.Rect(screen_width/(1920/800), screen_height/(1080/600), screen_width/(1920/300), screen_height/(1080/100))
        button_small = pygame.Rect(screen_width/(1920/1300), screen_height/(1080/600), screen_width/(1920/300), screen_height/(1080/100))

        pygame.draw.rect(screen, (dark_red), button_large)
        pygame.draw.rect(screen, (dark_red), button_normal)
        pygame.draw.rect(screen, (dark_red), button_small)
        video_text()

        mx, my = pygame.mouse.get_pos()

        # button collides
        if button_large.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (slighty_lighter_red), button_large)
            pygame.draw.rect(screen, (dark_red), button_normal)
            pygame.draw.rect(screen, (dark_red), button_small)
            video_text()
            pygame.display.update()
            if click_video:
                screen = pygame.display.set_mode((2560, 1440))
                screen_width = 2560
                screen_height = 1440
                pygame.display.update()

        if button_normal.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (dark_red), button_large)
            pygame.draw.rect(screen, (slighty_lighter_red), button_normal)
            pygame.draw.rect(screen, (dark_red), button_small)
            video_text()
            pygame.display.update()
            if click_video:
                screen = pygame.display.set_mode((1920, 1080))
                screen_height = 1080
                screen_width = 1920
                pygame.display.update()

        if button_small.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (dark_red), button_large)
            pygame.draw.rect(screen, (dark_red), button_normal)
            pygame.draw.rect(screen, (slighty_lighter_red), button_small)
            video_text()
            pygame.display.update()
            if click_video:
                screen = pygame.display.set_mode((1280, 720))
                screen_height = 720
                screen_width = 1280
                pygame.display.update()

        # keybinds
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    options()
                if event.key == K_RETURN:
                    pass
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_video = True

        pygame.display.update()


def audio():
    time.sleep(0.2)
    global Volume
    running = True
    while running:
        screen.fill(black)

        draw_text("Audio Settings", big_font, white, screen, screen_width/(1920/650), screen_height/(1080/100))

        button_mute = pygame.Rect(screen_width/(1920/800), screen_height/(1080/700), screen_width/(1920/300), screen_height/(1080/100))
        button_unmute = pygame.Rect(screen_width/(1920/800), screen_height/(1080/500), screen_width/(1920/300), screen_height/(1080/100))
        pygame.draw.rect(screen, dark_red, button_mute)
        pygame.draw.rect(screen, dark_red, button_unmute)
        draw_text("Mute", font, white, screen, screen_width/(1920/910), screen_height/(1080/730))
        draw_text("Unmute", font, white, screen, screen_width/(1920/890), screen_height/(1080/530))
        mx, my = pygame.mouse.get_pos()

        click_mute = False

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_mute = True

        if button_mute.collidepoint(mx, my):
            screen.fill(black)
            draw_text("Audio Settings", big_font, white, screen, screen_width/(1920/650), screen_height/(1080/100))
            pygame.draw.rect(screen, (slighty_lighter_red), button_mute)
            pygame.draw.rect(screen, (dark_red), button_unmute)
            draw_text("Mute", font, white, screen, screen_width/(1920/910), screen_height/(1080/730))
            draw_text("Unmute", font, white, screen, screen_width/(1920/890), screen_height/(1080/530))
            pygame.display.update()
            if click_mute:
                Volume = pygame.mixer.music.set_volume(0)

        if button_unmute.collidepoint(mx, my):
            screen.fill(black)
            draw_text("Audio Settings", big_font, white, screen, screen_width/(1920/650), screen_height/(1080/100))
            pygame.draw.rect(screen, (dark_red), button_mute)
            pygame.draw.rect(screen, (slighty_lighter_red), button_unmute)
            draw_text("Mute", font, white, screen, screen_width/(1920/910), screen_height/(1080/730))
            draw_text("Unmute", font, white, screen, screen_width/(1920/890), screen_height/(1080/530))
            pygame.display.update()
            if click_mute:
                Volume = pygame.mixer.music.set_volume(0.1)

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                main_menu()

        pygame.display.update()


def credits():
    time.sleep(0.2)
    running = True
    while running:
        screen.fill(black)

        draw_text("Made by Dan White", font, white, screen, screen_width/2.4, screen_height/5.4)

        button_secret = pygame.Rect(screen_width/6.4, screen_height/1.8, screen_width/6.4, screen_height/10.8)
        pygame.draw.rect(screen, (dark_red), button_secret)

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_secret = True

        if button_secret.collidepoint(mx, my):
            screen.fill((black))
            draw_text("Made by Dan White", font, white, screen, screen_width/2.4, screen_height/5.4)
            pygame.draw.rect(screen, (slighty_lighter_red), button_secret)
            pygame.display.update()
            if click_secret:
                secretrace()

        click_secret = False

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        pygame.display.update()


def secretrace():
    running = True
    global hRace, hName, hBackground
    while running:
        screen.fill(black)

        f = open('Charactername.txt', 'w')
        f.write('Nix')
        hName = 'Nix'
        f.close()

        g = open('Characterrace.txt', 'w')
        g.write('Dark Elf')
        hRace = 'Dark Elf'
        g.close()

        h = open('Characterbackground.txt', 'w')
        h.write('Outcast')
        hBackground = 'Outcast'
        h.close()

        hAttack = 75
        hDefence = 75
        hMagic = 75

        draw_text('Nix you really are a Filthy Outcast', base_font, white, screen, screen_width/(1920/100), screen_height/(1080/50))

        draw_text('Attack: ' + str(hAttack), game_font, white, screen, screen_width/(1920/100), screen_height/(1080/200))
        draw_text('Defence: ' + str(hDefence), game_font, white, screen, screen_width/(1920/100), screen_height/(1080/250))
        draw_text('Magic: ' + str(hMagic), game_font, white, screen, screen_width/(1920/100), screen_height/(1080/300))
        pygame.display.update()
        time.sleep(2)

        StoryPart_1()


def options():
    time.sleep(0.2)
    click_options = False
    running = True
    while running:
        screen.fill(black)

        # buttons
        button_audio = pygame.Rect(round(screen_width/(1920/450)), round(screen_height/(1080/600)), screen_width/(1920/300), screen_height/(1080/100))
        button_video = pygame.Rect(screen_width/(1920/1130), screen_height/(1080/600), screen_width/(1920/300), screen_height/(1080/100))
        button_credits = pygame.Rect(screen_width/(1920/450), screen_height/(1080/850), screen_width/(1920/300), screen_height/(1080/100))
        button_main_menu = pygame.Rect(screen_width/(1920/1130), screen_height/(1080/850), screen_width/(1920/300), screen_height/(1080/100))

        pygame.draw.rect(screen, (dark_red), button_audio)
        pygame.draw.rect(screen, (dark_red), button_video)
        pygame.draw.rect(screen, (dark_red), button_credits)
        pygame.draw.rect(screen, dark_red, button_main_menu)
        text_options()

        mx, my = pygame.mouse.get_pos()
        # button collides
        if button_audio.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (slighty_lighter_red), button_audio)
            pygame.draw.rect(screen, (dark_red), button_video)
            pygame.draw.rect(screen, (dark_red), button_credits)
            pygame.draw.rect(screen, dark_red, button_main_menu)
            text_options()
            pygame.display.update()
            if click_options:
                audio()

        if button_video.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (dark_red), button_audio)
            pygame.draw.rect(screen, (slighty_lighter_red), button_video)
            pygame.draw.rect(screen, (dark_red), button_credits)
            pygame.draw.rect(screen, dark_red, button_main_menu)
            text_options()
            pygame.display.update()
            if click_options:
                video()

        if button_credits.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (dark_red), button_audio)
            pygame.draw.rect(screen, (dark_red), button_video)
            pygame.draw.rect(screen, (slighty_lighter_red), button_credits)
            pygame.draw.rect(screen, dark_red, button_main_menu)
            text_options()
            pygame.display.update()
            if click_options:
                credits()

        if button_main_menu.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (dark_red), button_audio)
            pygame.draw.rect(screen, (dark_red), button_video)
            pygame.draw.rect(screen, (dark_red), button_credits)
            pygame.draw.rect(screen, slighty_lighter_red, button_main_menu)
            text_options()
            pygame.display.update()
            if click_options:
                main_menu()

        # keybinds
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
                if event.key == K_RETURN:
                    pass
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_options = True

        coin_image(coinX, coinY)
        pygame.display.update()


# text based loop
def main_menu():
    time.sleep(0.2)
    click_choose = False
    running = True
    screen_width = 1920
    screen_height = 1080
    while running:
        screen.fill(black)
        # buttons
        button_begin = pygame.Rect(round(screen_width/(1920/450)), round(screen_height/(1080/600)), round(screen_width/(1920/300)), round(screen_height/(1080/100)))
        button_options = pygame.Rect(round(screen_width/(1920/1130)), round(screen_height/(1080/600)), round(screen_width/(1920/300)), round(screen_height/(1080/100)))
        button_quit = pygame.Rect(round(screen_width/(1920/790)), round(screen_height/(1080/850)), round(screen_width/(1920/300)), round(screen_height/(1080/100)))

        pygame.draw.rect(screen, (dark_red), button_begin)
        pygame.draw.rect(screen, (dark_red), button_options)
        pygame.draw.rect(screen, (dark_red), button_quit)
        text_mainmenu()

        mx, my = pygame.mouse.get_pos()

        if button_begin.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (slighty_lighter_red), button_begin)
            pygame.draw.rect(screen, (dark_red), button_options)
            pygame.draw.rect(screen, (dark_red), button_quit)
            text_mainmenu()
            DM(DMX, DMY)
            pygame.display.update()
            if click_choose:
                text_input_screen()

        if button_options.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (dark_red), button_begin)
            pygame.draw.rect(screen, (slighty_lighter_red), button_options)
            pygame.draw.rect(screen, (dark_red), button_quit)
            text_mainmenu()
            DM(DMX, DMY)
            pygame.display.update()
            if click_choose:
                options()
                click_choose = False

        if button_quit.collidepoint(mx, my):
            screen.fill((black))
            pygame.draw.rect(screen, (dark_red), button_begin)
            pygame.draw.rect(screen, (dark_red), button_options)
            pygame.draw.rect(screen, (slighty_lighter_red), button_quit)
            text_mainmenu()
            DM(DMX, DMY)
            pygame.display.update()
            if click_choose:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RETURN:
                    pass
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_choose = True

        DM(DMX, DMY)
        pygame.display.update()


main_menu()
