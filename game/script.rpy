# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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
