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

    #Insert Fortune Telling Cards Here

    "A moment of collapse. Brick by brick the foundation was built, but one piece remains loose..."

    "Death shrouds your present. The grand scythe of the reaper descends upon the sands of time. Ghosts of your past scream, future road, and present tremble."

    "Love is in your future. Separated from Eros, the heartstrings yearn to fill their space, understanding they will learn."

    ft "What interesting cards!"

    y "Are they really? What does it all mean?"

    ft "That is up to your own interpretation"

    ft "However, the lines to beyond find promise, waiting to be uncovered."

    ft "I am sure that if the circumstances of your death were to be discovered…"

    ft "Then the spirits may grace you with a chance at mortal redemption."

    y "Really??"

    ft "Well, the sands are shifting. You'd best embark straight away."

    ft "Take these tarot cards with you. They will aid you on your journey. "

    y "Wait, how? Where do I start looking?"

    ft "You do not need to look. Fate will bring the answer to you (the fortune teller fades away)"

    y "Wait! I have more questions!"
    
    "What do I do here now?"

    "Do I stay here? Do I leave?"

    "They said that fate would bring the answer to me. Maybe I should stay here."

    "A peak outside wouldn't hurt though. Maybe I could get a clue."

    #insert transition here!

    sg1 " Did you see that exorcist earlier? So hot! I better marry someone like that. "
    sg2 "'Squeals' Oh my gosh, do you think they noticed us? Does my hair look okay?"

    p1 "I saw a bunch of exorcists heading towards the school last night."

    p2 "I heard it was because a spirit escaped!" 

    p1 "I heard it wass because of a tower explosion!"

    p2 "The tower? Hmm, either way we shouldn't stay out tonight."

    "Exorcists? Evil spirits? A tower?"

    "I can't believe this fortune teller stuff is just in the middle of a city. Does nobody think that's weird??"

    "{i}Suddenly there's a loud crash{/i}"

    unknown "Today is the day you disappear evil spirit!!"

    y "Wait what? Where?"

    unknown "Don't try to pretend. I can see your evil aura from a mile away!"

    unknown "It's time for you to go back to the underworld!"

    "The exorcist tries to attack you with their weapon, but you somehow evade it."

    y "Me!? But I'm not-"

    unknown "An evil spirit? Save your words, you all say the same thing."

    y "Wait!! Please hear me out!"

    unknown "Thessai...mor'en...vora'thal.."

    "The weapon in the exorcists hand starts glowing."

    "{i}I need to run! Where do I go!?{/i}"

    "Before the attack lands, you dive into an alleyway. You look around trying to figure out where you might be safe from this exorcist who seems to believe you are an evil spirit."
    "But who can help?"
    "The fortune teller!"

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
