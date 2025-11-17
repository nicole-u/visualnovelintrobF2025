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
define Priest = Character("Priest")
transform smallersize:
    zoom 0.5

init python:
    relationship = 0 

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
       
            $ relationship += 15
            "{i} A chain appears from the exorcists weapon and gets thrown at you. This time you are unable to run fast enough to evade it.{/i}"
            "How is it doing that?"
            "{i} You try to jump out of the way, but trip on an oddly placed pillow. The spell catches up to you. Brace yourself!{/i}"
        "Stand still.":
            $ relationship += 0

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
    






#screen 2
label scene2:

    scene bg_city_day
    with dissolve

    "You follow along as [exorcist] leads you through the city. His gait is steady and just slightly faster than the speed you're comfortable with. You can't help but feel it's intentional."

    y "Hey [exorcist]?"

    e "I have no desire for communication. Please refrain from breathing."

    "I can't even breathe, let alone speak?"
    "This isn't good. How am I supposed to make him love me?"
    "No, don't give up!"
    "It's time to put on the charm!"
    "Compliments charm people, right? What do I compliment?"

    menu:
        "Their clothes…they fit so well…":
            $ relationship -= 8
            jump s2_clothes

        "Their eyes…they're so dreamy…":
            $ relationship += 20
            jump s2_eyes


label s2_clothes:

    y "Y'know…those clothes…they look really good on you?"

    e "Lusting over holy vestments… how vile can you get, evil spirit?"

    y "I didn't mean it like that!"

    e "All of you evil spirits are the same—nothing but a mire of desires."

    y "I swear I didn't mean it like that!"
    y  "To begin with, I didn't mean that the clothes look good."
    y  "I meant you look good in the clothes."
    y  "You probably look hot in anything!"

    e "Is this your best attempt at flattery? Blatant sexual harassment?"

    y "…I'm sorry…"

    "Why am I so bad at this?"
    "[exorcist] shakes his head, then sighs."

    e "How dare you try and soil me with your filthy comments?"

    y "I said I'm sorry! Can I make it up to you? Please?"

    e "Hmmm. Are you willing to do anything?"

    jump s2_merge



label s2_eyes:

    y "Y'know…you have…very pretty eyes?"

    "[exorcist] stops and glances your way, just enough to reveal his left eye piercing into yours. With an exhale, he continues walking."

    e "How much do you remember, Spirit?"

    y "What do you mean?"

    e "Most of your kind—those who crawl out of the afterlife—tend to return a blank slate."
    e "Some fail to remember even the most basic of things, such as their names."
    e "This is not a coincidence, nor a byproduct of bitterly refusing to die."
    e "It is deliberate."
    e "Your kind chooses to forget because they cannot stomach the memory of who, or what, they were."
    e "All you keep are the embers of hatred, which you use to burn the world around you."
    e "You see, I am nothing like you."
    e "All I have are memories."
    e "And, of the sludge of the past that swirls in my head, day after day—"
    e "the strongest image is that of my mother."
    e "The look in her eyes as she plucked out mine with a sewing needle because “the devil was using it to watch her.”"

    y "I- I'm sorry. I was just trying to compliment you."

    e "I don't need your lies."

    y "I wasn't lying. I really do think they're pretty."

    "[exorcist] pauses for a moment, then shakes his head."

    e "…hmph, I dont need your flattery either."
    e "What I need is your assent."

    y "What do you mean?"

    e "Are you willing to do anything to solve this “issue?”"

    jump s2_merge



label s2_merge:

    "Anything? The fortune teller mentioned something about falling in love."
    "Does that mean I need to do anything to get him to love me?"
    "What does “loving me” even mean?"
    "Do we have to date?"
    "Do we need to get married?"
    "Do we have to…?"
    "Let's slow down! That's way too far into the future."
    "One step at a time."

    y "Yes, I'll do anything. I'll compliment something else about you!"

    e "That's…great, but not what I need. I have something else in mind."

    "[exorcist] stops, then turns to you."

    e "How about we take a bath together?"

    "Were jumping straight to that step!"
    "I'm not ready for this!"

    y "Wh- what?! Why all of a sudden?"

    e "You're refusing?"

    y "Well, I-I'm not saying that. I'm just confused."

    e "Well, after this mess of a day, I think I'd enjoy a nice, thorough cleaning. A cleanse, if you will."

    "That…is an interesting word of choice."

    "[exorcist] pulls you up the stairs toward a large wooden door engraved with a cross."

    scene bg_church_interior
    with fade

    "Once inside, [exorcist] speaks with one of the priests. You shyly stay behind."

    e "Might you have a bath available?"

    priest "Of course, [exorcist]. Shall I take you?"

    e "There's no need. Thank you."

    "[exorcist] brings his hands together, as if in prayer, and bows his head."

    e "Father be with you."

    priest "Father be with you."

    "[exorcist] nudges the chain and leads you deeper into the church."

    "That was quite the interaction…"

    y "Do you know him?"

    e "No, but every priest in the country knows me, for one reason or another."

    y "Are any of those reasons because of how scary you are?"

    e "Scary?"
    e "I am not the one they should fear."
    e "What they should fear are the vile, evil spirits like you."

    y "See? This is what I mean!"
    y "Every time you talk, it's like you want to murder someone."
    y "And your eyes practically yell it!"

    e "I- …no. People do not fear me."

    y "I do!"

    e "You should."

    y "See!"

    e "Never mind that!"
    e "We're here."


    "[exorcist] leads you into a wide room with a shallow pool of water."

    y "Whoa! Do all churches have these?"

    e "Yes. They are often used as 'after-work therapy' for exorcists."

    "[exorcist] steps into the pool, water reaching below his knees."

    y "What do you mean, 'grimy?'"

    e "Evil spirits are quite adept at holding grudges."
    e "And when those grudges latch onto an exorcist, it can be difficult to remove."

    y "Like a curse?"

    e "Precisely. These holy reservoirs cleanse the workings of any evil spirit."
    e "Including evil spirits themselves."

    "Wait—is he trying to kill me?"
    "If I go in, will I die for real this time?"

    y "I don't like where this is going."

    e "This is not for you to like. This is to 'solve' our issue."
    e "Now, enter."

    y "What do I do?"

    menu:
        "Resist!":
            $ relationship += 30
            jump s2_resist

        "Accept your death.":
            $ relationship += 0
            jump s2_accept



label s2_resist:

    y "No! This isn't what we agreed!"

    "[exorcist] wraps his hand around the chain and pulls."

    e "Get. In."

    "You dig your feet into the ground, trying to pull away."

    y "No! I don't wanna die!"

    e "You're already dead!"
    e "…jeez, why are you so strong?!"

    "But [exorcist] is too strong. As you near the pool, your feet slip on a puddle—you fall in headfirst."

    scene black
    with fade

    "Sloshing water echoes. You raise your head above the water, gasping."
 
    scene bg_church_interior
    with fade

    y "I'm alive! I told you I'm not an evil spirit! I'm ali-"

    "You turn to see [exorcist] had fallen in with you."

    e "Ugh, what a pain. Why are you still here?"

    "Your eyes trace over him. Wet clothes cling tightly to his body."

    y "A- are you okay?"

    "[exorcist] mutters to himself."

    e "Why did nothing happen? Could this mean…?"
    e "No, of course not. Then, is this evil spirit truly this powerful?"
    e "But then why feign fear? Are they even capable…?"

    "Ouch…"

    y "Let's do the thinking once we're dry, yeah?"

    "You stand and walk toward him—but slip, falling onto him."

    y "Ow! S-sorry!"

    "Your eyes meet, then dart away."

    e "…are you going to get off?"

    y "…do you want me to?"

    priest "Ahem. Might I bring you a towel?"

    "You both jump."

    jump s2_final



label s2_accept:

    y "Fine. I'll do it."

    "You hover one foot above the pool."

    "Please don't kill me…"

    "With all your willpower—"

    "Please!"

    "—you step in."

    scene black
    with fade

    e "This…this can't be…"

    scene bg_church_interior
    with fade
    
    "You stand knee-deep in holy water. Still alive."

    y "Does…does this mean I'm not an evil spirit?"

    e "No. It can't. This could easily be a sign of your strength!"

    y "Oh, please! Do you know how much courage that took?"

    e "Then why did you?"

    y "Because! I- I wanted to prove I'm not evil!"

    e "Hmm…"

    y "You're grasping at straws! What more do you want?"
    y "Do you want me to sink my whole body into this?"
    y "Fine!"

    "You drop backward into the water."

    y "See!"

    "You splash your own face."

    y "Totally fine!"

    e "Alright. You've proven a point. Now stop."

    "You rise—but slip. [exorcist] grabs your back, stopping you."

    y "He's so close!"

    "A warm feeling bubbles inside you."

    y "Th- thanks…"

    e "Yeah…"

    jump s2_final




label s2_final:

    e "Might I bring you some towels?"

    e "Please."

    "You exit the pool and dry off as best you can."

    y "What now?"

    e "Now, we head to the university. They should have more answers there."
    e "Maybe there I can get rid of this chain."
    e "And, if I'm lucky, get rid of you too."

    y "Alright…"

    "Answers, huh?"
    "I just hope they're the ones I need."

    "You walk out of the church, [exorcist] leading once again—though this time, the echo of squeaky shoes follows behind you."

    return

