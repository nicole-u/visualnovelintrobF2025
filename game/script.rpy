# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ft = Character("Fortune Teller")
define sg1 = Character("School Girl 1")
define sg2 = Character("School Girl 2")
define p1 = Character("Passerby 1")
define p2 = Character("Passerby 2")
define unknown = Character("???")
define e = Character("Exorcist")
define a = Character("Archivist")
define p = Character("Professor")


# The game starts here.

label start:
    scene black

    $ player_name = renpy.input(prompt = "Please enter a name.")
    if player_name == "":
        $ player_name = "Y/N"

    $ y = Character(player_name)

    "{i}{cps=*0.5}Where am I?{/i}{/cps}"
    "{i}{cps=*0.5}What's going on?{/i}{/cps}"
    "{i}{cps=*0.5}Why does my head hurt?{/i}{/cps}"

    y "What the- where is this place?"

    ft "So you've awakened..."

    ft "Welcome to my emporium. I am a fortune teller."

    ft "You may rest here as long as it takes to restore your vitality."

    ft "The journey through death can be very taxing."

    y "Death?What are you talking about???"

    ft "Oh, silly me!"

    ft "It seems in my excitement at meeting a new face, I had forgotten you are clueless about what has transpired!"

    ft "You died!"

    y "Huh-!?"

    ft "Don't fret about it. Happens to the best of us. And all of us."

    y "Wait what?"

    y "I died?"

    y "How?"

    y "Where?"

    y "When?"

    y "Why??"

    ft "Hmm, that I could not tell you."

    ft "But perhaps my tarot cards could.."

    menu first_menu:
        "Is this the right choice?":
            e "I don't know. Is this the right one?"
            e "I don't know why I chose this."
        "Or is it this one?":
            e "Yeah this is the right one."
    
    e "It's okay."
    
    # This ends the game.

    e "I have no idea what i am doing/"


    return
