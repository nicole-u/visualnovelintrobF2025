# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
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
    "{i}{cps=*0.5}Where am I?{/i}{/cps}"
    "{i}{/cps}What's going on?{/i}{/cps}"
    "{i}Why does my head hurt?{/i}"

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "This is new dialogue."

    e "Task"

    menu first_menu:
        "Is this the right choice?":
            e "I don't know. Is this the right one?"
            e "I don't know why I chose this."
        "Or is it this one?":
            e "Yeah this is the right one."
    
    e "It's okay."
    
    # This ends the game.


    return
