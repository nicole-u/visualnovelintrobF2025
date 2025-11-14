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

transform smallersize:
    zoom 0.5


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

    scene bg ftshop
    show ft neutral at center 

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

    scene bg city 
    hide ft

    sg1 " Did you see that exorcist earlier? So hot! I better marry someone like that. "
    sg2 "'Squeals' Oh my gosh, do you think they noticed us? Does my hair look okay?"

    p1 "I saw a bunch of exorcists heading towards the school last night."

    p2 "I heard it was because a spirit escaped!" 

    p1 "I heard it wass because of a tower explosion!"

    p2 "The tower? Hmm, either way we shouldn't stay out tonight."

    "Exorcists? Evil spirits? A tower?"

    "I can't believe this fortune teller stuff is just in the middle of a city. Does nobody think that's weird??"

    "{i}Suddenly there's a loud crash{/i}"

    show unknown mystery at center, smallersize with dissolve

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

    scene bg ftshop
    hide unknown with dissolve

    y "Help! Help!"
    y "There's an exorcist after me!"
    "{i}Where is everyone? Where did the fortune teller go? {/i}"
    "{i} You look around. There's nobody in the shop. It's silent."
    "{i}You look over to the table where you first awoke There's a piece of paper on the table. What does it say?{/i}"

    show notepaper at Position(xoffset=0, yoffset=-100) with dissolve

    "What?? What does that mean?"
    "Charm through danger your danger and through love find the answer?"
    "I can't fight when I face danger? Should I just stand there and die?"
    "The only danger here is that maniac chasing me. Is that who I need to charm?"

    hide notepaper with dissolve

    "Do I need to… make the exorcist fall in love with me?"
    "What does this mean???"

    show unknown mystery at center, smallersize with dissolve

    unknown "Alright, I'm done being merciful today."
    unknown "Any last words before I banish you?"

    y "Please, I'm not an evil spirit. I don't know how I got here and I'm confused about what's going on. Please believe me!"
    y "Also…. Uhhhh… are you dating anyone by chance?"

    unknown "My dating status is none of your concern."

    show unknown shock at center, smallersize

    unknown "Be gone now evil spirit! {i}his weapon glows, preparing to attack you.{/i}"

    "{i} You evade the attack somehow. Wow, you are lucky!{/i}"

    unknown "Stop running around! I'll try to make it quick!"

    "{i} What should I do!? {/i}"

    menu fight_choice:    
        "Keep running away.":
            "{i} A chain appears from the exorcists weapon and gets thrown at you. This time you are unable to run fast enough to evade it.{/i}"
            "How is it doing that?"
            "{i} You try to jump out of the way, but trip on an oddly placed pillow. The spell catches up to you. Brace yourself!{/i}"
        "Stand still.":
            "{i} A chain appears from the exorcists weapon and gets thrown at you.{/i}"
            "{i} The exorcist stops for a moment and the spell stops hurling towards you. {/i}"
            unknown "What games are you playing evil spirit? Why are you standing still!"
            y "You told me to stop running around! Why are you so angry!?"
            unknown "I'm really going to kill you!"
            y "Please don't!"
            unknown "Strange, will you really not run?"
            show unknown upset at center, smallersize
            "{i}The exorcist seems deep in thought, perhaps contemplating whether or not to kill you.{/i}"
            unknown "You are quite strange. I've never seen an evil spirit accept its fate like this."
            unknown "Perhaps there's something wrong..."
            unknown "Unless you are tricking me... Evil spirit, I shall chain you!"
            "{i} The exorcist raises their weapon, chaining you."

            #fade to black
    "{i} Back to consciousness. You see that you are chained to the exorcist, bound in his weapon.{/i}"
    e "What!? What dark magic is this? What have you done!? How dare you chain us together!"
    show unknown shock at center, smallersize
    "{i} Why is there a chain around the exorcist's hand? Why do I have a chain around my wrist? Why am I chained to the exorcist!?{/i}"
    e "How did you do this? Unchain me this instant!"
    y "How did {i}I{/i} do this? It was your spell! I didn't do this!"
    e "Hmm, you don't seem like the bright type."
    "{i}Same could go for you...buddy.{/i}"
    e "Very well, I'll choose to believe you."
    show unknown upset at center, smallersize
    e "Korran veilith suun da'rethal!"
    "{i} Sparks fly off of his hand, but the chain does not come off {/i}"
    e "Why is this thing so strong? How did this happen?"
    e "Come on, we need to get to the university."
    e "Why aren't you moving?"
    y "Wait, why are we going to the university?"
    show unknown mystery at center, smallersize
    e "Cause I feel like it. Come on, let's go."
    menu refuse_exorcist:
        "No, tell me why, or I won't go.":
            e "Why are you so annoying!?"
   
    show unknown upset at center, smallersize
    e "It's because I want to show my colleagues this magical chain. I've never seen anything like it before."
    y "What's in it for me?"
    e "What do you mean?"
    y "If I go with you, and you get someone to take the chain off, you'll just kill me!"
    show unknown flirty at center, smallersize
    e "Awwh, you think this chain is protecting you? How cute."
    y "Then, why aren't you trying to kill me anymore?"
    show unknown mystery at center, smallersize
    e "Because I don't want to."
    y "You seem like you wanted to a few minutes ago."
    e "Come on, let's go."
    y "No."
    e "Ugh...Fine.."
    show unknown shock at center, smallersize
    e "What do you want from me? Let's make a deal."
    y "If you let me live after we become unchained, {i}and{/i} none of your exorcist friends kill me either, without loopholes, I'll go."
    e "Sorry, can't do that."
    y "Why not?"
    e "You're an evil spirit. I can't just let you live!"
    y "Fine, then I'm not going. And for the last time, I'M NOT AN EVIL SPIRIT!"
    show unknown tease at center, smallersize
    e "Y'know, you seem to be overlooking the fact that I am the best exorcist in this country."
    show unknown upset at center, smallersize
    e "At some point I will figure out how to unchain us, and then, you'll be dead, evil spirit."
    y "Okay, but what if I come with you, if you help me find out how I died?"
    show unknown shock at center, smallersize
    e "And why do you want to find out how you died?"
    y "None of your business."

    "{i} The exorcist contemplates your proposal."

    e "Fine. We have a deal."
    y "Yesss..."
    e "Now I don't want to hear a single peep out of you."
    show unknown mystery at center, smallersize
    e "Stay out of my business."
    y "Okay!"
    "{i} Well, that might be a little hard."
    y "But first, what's your name?"
    show unknown upset at center, smallersize
    "{i} The exorcist glares at you.{/i}"
    e "i literally just told you to stay out of my business."
    y "I didn't think a name would be 'part of your business'"
    e "It's ____. Now let's get going."
    e "Actually, wait. What's your name?"
    y "[player_name]"
    



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
