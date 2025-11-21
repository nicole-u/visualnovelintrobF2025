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
define priest = Character("Priest")
transform smallersize:
    zoom 0.5
transform normalsize:
    zoom 1.6
transform minisize: 
    zoom 0.45
transform lowered:
    ypos 1.5
transform side:
    xpos -0.1
transform side2:
    xpos 1.15
transform evensmallersize:
    zoom 0.8

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
    with fade

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
       
            $ relationship += 20
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
    show exorcist shock at center, smallersize
    e "I literally just told you to stay out of my business."
    y "I didn't think a name would be 'part of your business'"
    e "Well, surely you know of me? I am quite well renowned in the exorcism industry."
    $ exorcist = renpy.input(prompt = "What do you think is the Exorcist's name?")
    e "You got it, now tell me yours, so we can get moving."
    y "[player_name]"
    

# $ exorcist = "timothy the placeholder"




#screen 2
label scene2:

    scene bg city
    with dissolve

    show exorcist neutral at center, smallersize
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

    show exorcist upset at center, smallersize
    e "Lusting over holy vestments… how vile can you get, evil spirit?"

    y "I didn't mean it like that!"

    e "All of you evil spirits are the same—nothing but a mire of desires."

    y "I swear I didn't mean it like that!"
    y  "To begin with, I didn't mean that the clothes look good."
    y  "I meant you look good in the clothes."
    y  "You probably look hot in anything!"

    show exorcist neutral at center, smallersize
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

    show exorcist neutral at center, smallersize
    e "How much do you remember, Spirit?"

    y "What do you mean?"

    e "Most of your kind—those who crawl out of the afterlife—tend to return a blank slate."
    e "Some fail to remember even the most basic of things, such as their names."
    e "This is not a coincidence, nor a byproduct of bitterly refusing to die."
    e "It is deliberate."
    show exorcist upset at center, smallersize
    e "Your kind chooses to forget because they cannot stomach the memory of who, or what, they were."
    show exorcist shock at center, smallersize
    e "All you keep are the embers of hatred, which you use to burn the world around you."
    show exorcist mystery at center, smallersize
    e "You see, I am nothing like you."
    e "All I have are memories."
    e "And, of the sludge of the past that swirls in my head, day after day—"
    e "the strongest image is that of my mother."
    e "The look in her eyes as she plucked out mine with a sewing needle because “the devil was using it to watch her.”"

    y "I- I'm sorry. I was just trying to compliment you."

    
    e "I don't need your lies."

    y "I wasn't lying. I really do think they're pretty."
    show exorcist upset at center, smallersize
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
    show exorcist neutral at center, smallersize
    e "That's…great, but not what I need. I have something else in mind."

    "[exorcist] stops, then turns to you."

    show exorcist flirty at center, smallersize
    e "How about we take a bath together?"

    "Were jumping straight to that step!"
    "I'm not ready for this!"

    y "Wh- what?! Why all of a sudden?"

    show exorcist upset at center, smallersize
    e "You're refusing?"

    y "Well, I-I'm not saying that. I'm just confused."

    show exorcist flirty at center, smallersize
    e "Well, after this mess of a day, I think I'd enjoy a nice, thorough cleaning. A cleanse, if you will."

    "That…is an interesting choice of words.."

    "[exorcist] pulls you up the stairs toward a large wooden door engraved with a cross."

    scene church hall
    with fade

    
    show exorcist neutral at center, smallersize
    show priest neutral at left, smallersize
    
    "Once inside, [exorcist] speaks with one of the priests. You shyly stay behind."

    e "Might you have a bath available?"

   
    priest "Of course, [exorcist]. Shall I take you?"

    e "There's no need. Thank you."

    "[exorcist] brings his hands together, as if in prayer, and bows his head."

    e "Father be with you."

    priest "Father be with you."
    hide priest neutral with dissolve
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

    show exorcist upset at center, smallersize
    e "I- …no. People do not fear me."

    y "I do!"

    e "You should."

    y "See!"

    e "Never mind that!"
    e "We're here."


    "[exorcist] leads you into a wide room with a shallow pool of water."

    y "Whoa! Do all churches have these?"

    show exorcist neutral at center, smallersize
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
 
    scene church hall
    with fade

    y "I'm alive! I told you I'm not an evil spirit! I'm ali-"

    "You turn to see [exorcist] had fallen in with you."
    show exorcist mystery at center, smallersize, with dissolve 
    e "Ugh, what a pain. Why are you still here?"

    "Your eyes trace over him. Wet clothes cling tightly to his body."

    y "A- are you okay?"

    "[exorcist] mutters to himself."

    show exorcist upset at center, smallersize
    e "Why did nothing happen? Could this mean…?"
    e "No, of course not. Then, is this evil spirit truly this powerful?"
    e "But then why feign fear? Are they even capable…?"

    "Ouch…"

    y "Let's do the thinking once we're dry, yeah?"

    "You stand and walk toward him—but slip, falling onto him."

    y "Ow! S-sorry!"

    "Your eyes meet, then dart away."

    show exorcist neutral at center, smallersize
    e "…are you going to get off?"

    y "…do you want me to?"
    show exorcist shock at center, smallersize, with dissolve 
    show priest neutral at left, smallersize 
    priest "Ahem. Might I bring you a towel?"

    "You both jump."

    e "Huh-!?"
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

    scene church hall
    with fade
    
    "You stand knee-deep in holy water. Still alive."

    y "Does…does this mean I'm not an evil spirit?"
    show exorcist shock at center, smallersize, with dissolve
    e "No. It can't. This could easily be a sign of your strength!"

    y "Oh, please! Do you know how much courage that took?"

    e "Then why did you?"

    y "Because! I- I wanted to prove I'm not evil!"

    show exorcist upset at center, smallersize
    e "Hmm…"

    y "You're grasping at straws! What more do you want?"
    y "Do you want me to sink my whole body into this?"
    y "Fine!"

    "You drop backward into the water."

    y "See!"

    "You splash your own face."

    y "Totally fine!"

    show exorcist shock at center, smallersize
    e "Alright. You've proven a point. Now stop."

    "You rise—but slip. [exorcist] grabs your back, stopping you."

    y "He's so close!"

    "A warm feeling bubbles inside you."

    y "Th- thanks…"

    e "Yeah…"

    jump s2_final




label s2_final:

    priest "Might I bring you some towels?"

    show exorcist neutral at center, smallersize
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

    jump unihall

label unihall:
    scene bg schoolhall
    with fade

    show exorcist neutral at center, smallersize 

    
    e "Finally, we’re here."
    e "Let’s get this over with."
    y "Now wait a minute, we still haven’t made any progress towards finding out how, you know…"
    y "I died?"
    show exorcist shock at center, smallersize
    e "That isn’t of my concern right now-"
    y "But we had a deal." 

    "The exorcist is visibly annoyed."

    e "Fine."
    show exorcist neutral at center, smallersize
    e "Do you have any information at all about what may have caused your death?"
    y "Well, earlier today I woke up in the fortune teller tent you found me near. The fortune teller there told me that I had died, and gave me a tarot card reading when I asked why."

    "You show the exorcist your tarot cards."

    y "Tower, death, and love. Don’t know what they mean though."

    e "Hmm…anything else?"

    "I probably shouldn’t tell them about the note."

    y "That’s all I’ve got…"
    show exorcist neutral at center, smallersize
    e "Seriously? Really not much to go off of."
    y "Not my fault."
    e "Evil spirits really are useless…"
    y "How many times do I have to tell you, I am not an evil spirit."
    e "Sighs. Regardless, there’s an archivist here in the university that may be able to help us decipher whatever this means."
    e "They’re the most knowledgeable on this sort of topic…although a bit unique. I suggest we visit them."
    y "I guess if that’s our best option then let’s go."
    y "Also, no more tricks, right?"
    show exorcist upset at center, smallersize
    e "…"
    show exorcist neutral at center, smallersize
    e "Right."

    "You and the exorcist are now in the hallway on the way to the archivist."

    "The walk has been quiet, maybe I can take this opportunity?"

    y "So, how is it like at the university?"
    show exorcist mystery at center, smallersize
    e "And why is this of importance?"
    y "Seems like an interesting place, and I’d like to get to know more about you."
    e "Quit trying to pry…however, I do quite enjoy it here."
    show exorcist upset at center, smallersize
    e "The academics are thorough, and I’ve found great success because of some of the people here."
    y "What should I say?"

    menu universitychoice:
        "Do you have a lot of friends? You seem like the popular type.":
            $ relationship -= 5
            jump university1
        "You’re always so well spoken, do you study hard?":
            $ relationship += 10
            jump university2
    return
    $ professorchoice = "none"
    label university1:
        e "I generally don't concern myself with social interaction. I'd rather not distract myself from my studies."
        show exorcist shock at center, smallersize
        e "Honestly, I'm offended that that is your takeaway of me."
        y "I didn't mean to hit a nerve, take it as a compliment rather."
        y "I would be happy to know that I strike someone as popular."
        show exorcist upset at center, smallersize
        e "Again, it is not of my concern [player_name]."
        e "I spend all my time studying and improving my work as an exorcist and to be dumbed down to merely my physical attractiveness is an insult."
        y "Well, it's not like I mentioned physical attractiveness in the first place!" 
        "I definitely meant it though."

        e "Just keep your antics to yourself. We're almost to the archivist’s room."
    jump unicontinue

    label university2:
        show exorcist neutral at center, smallersize
        e "Yes, it is my main focus here at the university."
        e "I pride myself on my academics and work as an exorcist. It’s hard work, but I manage. I’m… glad that you recognized this."
        y "Knowledge is important, keep doing what you’re doing."
        y "Just know that I appreciate you helping me figure out what caused my death."
        show exorcist tease at center, smallersize
        "The exorcist blushes a little."

        jump unicontinue

    label unicontinue:
        show exorcist shock at center, smallersize
        e "Hey! I require your assistance."

        "You spot someone hunched over their desk in the corner of the room. They jump up after hearing the exorcist’s shouting."

        show arch nerv at right, minisize
        show exorcist neutral at left, normalsize, lowered, side


        a "Oh my days…how many times have I told you NOT to barge in here yelling like that!"
        a "You know how I get with loud noise…"
        e "Sorry, but I really don’t have the time today."
        e "I need you to figure out how this evil spirit-"
        show arch scared at right, minisize
        a "Evil spirit????? WHERE?????"

        "The archivist frantically looks around and backs away from you two."
        e "Oh get a grip, they’re literally chained to me." 
        e "And aren’t you being quite loud for someone so concerned about loud noises?"
        show arch dis at right, minisize
        a "Sorry…I…sorry, I’m just…you know how I get with ghosts…"
        e "Same thing every time. Just get your glasses on so you can see the evil spirit."
        a "Right, sorry again…"
        "The archivist takes a pair of glasses out of their back pocket and puts them on. They seem to be tinted with a special green hue."

        show exorcist upset at left, normalsize, lowered, side
        e "Back to what I was saying, I need you to figure out how this…living soul…died."
        a "Um…nobody else showed up when I put on my glasses. Still just you two."
        e "Well, there are only two of us so it’s working."
        show arch scared at right, minisize
        a "Sorry, must not have noticed your…friend…earlier."
        show arch think at right, minisize
        a "You said they needed to find out how they died?"
        y "Correct. Also, contrary to popular belief, I am in fact not an evil spirit."
        show arch scared at right, minisize
        a "Eeek! It’s talking to me!"
        y "Calm down! I didn’t mean to scare you, but it really is true…"
        show arch norm at right, minisize
        show exorcist shock at left, normalsize, lowered, side
        e "You both are really testing my patience right now. Just show the tarot cards, [player_name]."
        y "Right, here we are."

        "You show the archivist the tarot cards and explain how you got them, and what the fortune teller said to you regarding your death. They seem hesitant to help you but eventually settle down."

        show arch think at right, minisize
        show exorcist neutral at left, normalsize, lowered, side
        a "So tower, death and love hm? An…interesting selection.."
        y "Do you have any idea what these could mean?"
        a "Well, I could make a few guesses, but let's ask the cards first."
        y "Wait sorry, ask the cards-?"
        show arch shock at right, minisize
        a "Can you tell me more information about the death of this evil spirit, specifically how it happened?"

        "The cards suddenly realign in the order of lovers, tower and death."

        "Lovers: Those who have felt affection for another take unnecessary risks."
        "Tower: Those who take unnecessary risks will seek an untimely end."
        "Death: Those who will seek an untimely end find themselves back where it all started."

        y "…"
        y "So…you can just do that?"
        e "…"
        show arch nerv at right, minisize
        a "Well yes, you didn’t know?"
        show exorcist mystery at left, normalsize, lowered, side
        e "HOW are you this foolish, [player_name]??"
        e "We spent all this time trying to decipher these stupid cards and you didn’t even bother to ask?"
        y "Well to be fair you didn’t ask either-"
        show exorcist upset at left, normalsize, lowered, side
        e "What a waste of time! We could have been unchained by now, how truly despicable."
        y "Hey, at least we can focus on the good now. The cards gave us more info…although still cryptic unfortunately."

        "Affection? Unnecessary risks? That could have something to do with the fortune teller’s note."

        show arch norm at right, minisize
        a "Hmm, how odd. The lovers card may represent a past romance you may have had, though I am unsure how that would relate to your death. The death card is too obvious, which makes me think there is some deeper meaning."
        y "And what about the tower?"
        a "I was saving this for last, because coincidentally one of our towers exploded not too long ago, yesterday in fact."
        y "Seriously?? There could be some actual correlation here."

        "One of the cards mentioned an untimely end and going back to where it all started…is this where we have to go?"

        y "[exorcist], we have to go to that tower."
        e "Slow down, we got a lot of information on your death. Now, it's time to get back to breaking this wretched chain."
        y "But we’re getting close to the answer, I can feel it!"
        e "I won’t be making exceptions this time. We’re going to the professor."
        y "…"
        y "Fine. But do you promise to follow me to the tower afterwards?"
        e "…"
        e "Yes."

        "You and the exorcist leave the archivist's room, going to the professor's door."

        y "Do we knock first?"

        "[exorcist] ignores you."

        "You stare in shock as [exorcist] suddenly kicks in the door!"

        scene black
        with fade

        "You hear a thump in the classroom and after regaining your senses, peer inside to see a shocked professor holding their knee in pain after hitting it against the desk"

        scene bg classroom:
            zoom 1.2
        with fade

        show exorcist neutral at right, lowered, evensmallersize, side2    
        show p surpr at left, smallersize

        y "What the?"

        p "Goodness!"
        p "Oh! [exorcist], it’s you! Haven’t I taught you how to knock?"

        y "(whispering) I told you."

        "[exorcist] blinks without giving it a second thought."

        p "What a surprise! It’s great to see you! Come in! Come in!"

        "The professor quickly closes the book on his table and slides it behind his back, but you catch a glimpse of the title. It seems like Ride and Prejudice by Ane Austen."

        e "(sighs) Forgive the intrusion… I hope you have a moment, professor?"
        p "Of course!"
        p "Oh, and you brought a companion. How nice."
        p "Wait, [player_name]! Is that you? I haven’t seen you in so long! How have you been?"

        y "Oh uhhh… good?"

        e "Wait! You know each other??!"

        p "Why of course! [player_name] was in my Enchantments 102 class. I remember you staring out the window every time your—" 
        "—the professor points at [exorcist]—"
        "—fighting class was taking place in the quad."

        "[exorcist] stares at you."

        e "You went to school here? (side-eye)"
        y "I did?"

        e "I’ve never seen you before, you were really in school with me?"

        "The exorcist stands in surprise, seemingly re-evaluating everything they had previously assumed about you. Of course… because why would a student of a school for exorcists… become an evil spirit."

        y "I don’t know? I don’t remember."

        p "I see things worked out for you ;)"

        "The professor winks at you and glances at the chain between the two of you."

        e "Professor, was this person really a student? At the same time as me?"

        "[exorcist] called me a person… well that’s… quite a development, who would’ve known."

        p "(Smiling) Of course!"
        p "[player_name] was quite a talented student... even if you didn’t say much."
        p "I remember you had quite a good summoning spell."

        "Really??? I was a great student? That’s amazing!"
        "I really wish I could remember now."
        "Maybeee, I should take this opportunity…"
        "I could flirt a little more now, what should I do:"
        
        menu flirtingexorcist:
            "Flirt with the exorcist.":
                $ relationship += 10
                $ professorchoice = "none"
                jump flirt_exorcist
            "Flirt with the professor":
                $ relationship += 5
                $ professorchoice = "professor"
                jump flirt_professor
            
    label flirt_exorcist:

        y "Do you hear that, [exorcist]? I was such a great summoner. Not some evil spirit, the only thing dropping to the floor around me is your heart. (wink)"

        "There's an awkward silence. The professor and the exorcist both stare at you, cringing at the fact that you were able to come up with such a cheesy line. You remain smiling until the professor clears his throat."

        p "Anyways, what brings the two of you here?"
        e "Unfortunately, it's not good news, professor."
        e "As you can see we've found ourselves in quite the predicament."

        "The exorcist raises your wrist and the professor takes a good long look at it, holding his hand over his mouth. You swear you could see a smirk flash on his face for a second."

        e "I tried to capture this evil spirit, but it seems that my spell backfired."
        p "Evil spirit? Are you sure? [player_name] doesn't look like an evil spirit."
        y "See? I told you, I'm really not!"

        "[exorcist] ignores you."

        e "They're just really good at hiding it, but don't you see the dark death miasma? It's faint but it's definitely there."
        p "Hmm… I don't know, but if YOU say so, it must be true. You're one of the best exorcists out there now. (smiling) I'm very proud of you, by the way."
        e "Thank you, professor."
        p "Maybe I'm just getting old."

    label flirt_professor:
        p "What brings the two of you here anyway?"

        e "Unfortunately, it’s not good news, professor."
        e "As you can see we’ve found ourselves in quite the predicament."

        "The exorcist raises your wrist and the professor takes a good long look at it, holding his hand over his mouth. You swear you could see a smirk flash on his face for a second."

        y "It seems that [exorcist]’s spell backfired. Maybe if you cast it, professor, it would have worked. (wink)"
        y "Do you think you could help us out?"

        p "Oh! Aren’t you quite the flirt! Not that I mind the flattery. (wink)"
        p "You’ve definitely gotten more bold since you were here."

        e "Professor, please. Can you do anything about this spell?"

        p "Well, aren’t you impatient, [exorcist]. Maybe if you fed me a few compliments like [player_name], I’d work faster."

        p "(sigh) But of course I’ll help you out. First, I’d love to hear about how this came about."

        "[exorcist] begins talking about how you met, and you notice that the professor is glancing back at his book on the table. You decide to interject."

        y "Of course, I’ve spent the last few hours with [exorcist] and it’s been quite the… adventure."
        y "[exorcist] is quite a stickler, but I think we’re starting to warm up to each other. (wink)"
        y "We had quite the moment at the church earlier, when [exorcist] took my hand and led me into the pool."

        "This seems to intrigue the professor, who gasps and leans in closer with wide eyes."

        p "And then? (nodding)"

        e "(blushes) *clears throat*"

        y "(sigh) And then nothing! I lived."

        p "?"

        y "I mean, if YOU were the one who pulled me into a pool of holy water, professor, I’m sure I would’ve died on the spot at the sight of your dashing looks."

        p "(blushing) Ohhh, haha, you’re quite good at this aren’t you?"

        y "Thank you, but you see, I went in and I lived!"
        y "I’ve been trying to tell [exorcist] this entire time that I’m not an evil spirit but— (sigh) unfortunately I don’t seem to be believed."
        y "Maybe you could shed some light on this, professor. Am I an evil spirit?"

        p "(gasps) Evil spirit?? Of course not!"
        p "The way you are right now is definitely not representative of an evil spirit. You do look quite ill, but not to THAT extent."

        "[exorcist] looks at the professor, surprised."

        e "Are you sure, professor? You… don’t think [player_name] is an evil spirit?"

        p "Of course not! What makes you think so?"

        e "Do you not see the clear dark death miasma surrounding [player_name]?"

        p "Hmm… I don’t."

        e "That’s quite strange, professor. Is there no other reason you’re not able to see it?"

        y "*gasp* What are you saying? Of course our intelligent and kind professor isn’t getting it wrong!"

        p "Right, right. What [player_name] said."

        jump professorcontinue

    label professorcontinue:
        p "This is quite strange… For now, I’ll help you two remove those chains."

        y "WAIT! If you remove these chains right now, are you still gonna kill me?" 
        " You turn to [exorcist]."

        "[exorcist] remains silent in thought. A few seconds pass before they speak up."

        e "... I won’t."

        y "Really?"

        e "I promised… that we would find out how you died, so we’ll do that first… I keep my word."

        y "(scoffing) That wasn’t so clear earlier at the church."

        e "I’m going to keep you chained to me until we figure it out, in case you decide to run."

        y "(gasp) Are you sure you’re not just doing this because you want to be chained to me longer?"
        y "Ahaha… I’m just kidding, but you know I’d never run from you, you’re too beautiful to not be the last thing I see before I leave this mortal plane. (sigh)"

        "The exorcist looks away."

        e "Well, professor, we’ll return later. We’re heading up to the tower."

        p "Oh! But it’s been destroyed!"

        e "We know… but we spoke to the archivist and it seems that’s where [player_name]’s death likely took place."

        p "Oh! Oh… I see."
        p "Yes, it blew up the other day. If that’s really where you died, [player_name], something must have gone seriously wrong."

        p "Here!"

        "The professor takes out a piece of paper and begins writing something on it. He folds it up and hands it to [exorcist]."

        p "For later! To break the spell. I’m not sure if I’ll still be here when you two get back."

        "You all turn your heads to the window. It’s already dark; so much time has passed."

        p "Good luck."

        if professorchoice == "professor":
            jump professor_flirt_continued
        elif professorchoice == "none":
            jump professor_normal_continued


    label professor_flirt_continued:
        e "Well, you’re quite the big flirt."

        y "Are you jealous that I flirted with the professor?"

        e "(looks to the side) Of course not!"

        y "Don’t worry, I only did it so he would help! And didn’t you see that book he was reading? It seems like our old professor’s quite the romance enjoyer!"

        "The Exorcist looks at you in surprise, with maybe a hint of being impressed?"

        e "You’re quite perceptive, I… didn’t expect that."

        y "Well, didn’t you hear? It seems like I was quite the bright student!"
        y "Don’t you think that there’s at least a liiiitttle chance that I’m NOT an evil spirit now?"

        e "… No… you’re definitely an evil spirit… just not like any other evil spirit that I’ve killed."

        "WHYYY?? I mean this is much better than before, but still! I suppose it is a bit hard to believe, especially if I have this weird death aura stuff around me."
        "What is it anyway? What does it look like? No one else sees it… I’m not actually an evil spirit am I?"
        "Of course not! There’s no way!"

        "Either way, it doesn’t seem like [exorcist] really sees me as a bad person anymore. I should take this opportunity."

        y "Wait!"
        jump lorecontinues

    label professor_normal_continued:
        e "All right, let’s go."

        y "…Don’t you think that there’s at least a liiiitttle chance that I’m NOT an evil spirit?"

        e "No, you’re definitely an evil spirit, just… not like any other evil spirit that I’ve killed before." 
        "Exorcist looks at you suspiciously."

        y "Wait!"

        "If we go to the tower, and figure out how I died, there’s no way [exorcist] will let me live! I have to do something about it."
        jump lorecontinues

label lorecontinues:
    "What should I do?"

    menu flirtingagain:
        "Try to prove you're not an evil spirit.":
            $ relationship += 10
        "Flirt more with the exorcist.":
            $ relationship += 5
            
label flirtingmore:
    y "I- I know that you think I’m an evil spirit, but-"
    y "But like you said, I’m not like any other evil spirit you’ve seen, what if I’m a nice evil spirit?"

    e "Mmm… I think that kind of defeats the purpose of me saying you’re an evil spirit."

    y "Right… Dumb question, okay."
    y "Okay, well, what if you’re not like any other exorcist too?"

    e "What?"

    y "I mean, from what I heard, you’re one of the best, and I bet that means that with you around, I wouldn’t be able to do any “evil spirit” stuff either way, right?"

    e "What are you getting at?"

    y "What if you let me live?"

    e "That’s not how it works."

    y "Ever heard of enemies to lovers?"

    e "What?"

    y "You know… like that book! About the exorcist and the evil spirit?"
    y "Born to kill each other, destined to be with one another. I’m sure the professor knows the one. He’d make some good recommendations."

    e "(skeptical) I’ve… never heard of that before."

    y "In the story the kind, good looking, charming, and powerful exorcist with a tragic past meets a kind, good looking, charming, and powerful evil spirit with a possibly also tragic past."

    e "Uh huh…."

    y "You see, they meet each other and the exorcist needs to kill the evil spirit."
    y "BUT the evil spirit is immediately captivated by the exorcist and falls in love at first sight,"

    e "Really?"

    y "Yes! And the evil spirit promises to do no wrong to any human and instead help the exorcist catch other evil spirits."

    e "(breathes out) I see. And then…?"

    y "The exorcist also falls in love with the evil spirit… and they become a dynamic duo, fighting evil for the rest of their lives."
    y "What do you think? Doesn’t that sound like a great story?"
    y "Don’t you think that could be us?"

    "You bat your eyelashes while looking at [exorcist]."

    e "(sighs) Okay, let’s say hypothetically this book is real, which I know it's not, because you don’t remember anything—"
    e "I don’t think you know how this works."

    y "What do you mean?"

    e "Evil spirits feed on the living to stay on this mortal plane."

    y "I’m not gonna eat people, who do you think I am?"

    e "I know you might not feel it right now and I know you don’t “think” you’re an evil spirit, but eventually you will, and it’ll be unbearable to not feed."

    y "Well, what happens if I don’t?"

    e "Then you’ll fade away… painfully, as if you’re starving."

    y "Damn, well that was intense."

    "[exorcist] doesn’t know that I can come back to life after we figure out how I died… Maybe I should just follow along for now."

    e "So you see, even if I wanted to keep you alive, I can’t."

    y "But you want to?"

    e "… No." 
    "The exorcist turns away."

    y "Sureee…"
    y "(sigh) And there’s so much I’ve yet to experience."

    e "How would you know? You don’t remember."

    y "Even worse! I only have a day’s worth of memories, I haven’t hurt anyone, and I’ll die soon." 
    y "*bigger sigh*"
    y "What awful luck. Of course I got to meet someone so attractive, but I couldn’t even experience romance."

    e "Okay, okay, I get it. You can stop."

    y "If only someone kind, powerful, intelligent, and good-looking would grant my dying wish to fall in love."

    e "…"
    e "Okay, I’ll make you a deal. If we figure out how you died, and you didn’t do anything bad… I’ll take you on one date before I have to kill you."

    y "Really?"

    e "I… suppose it’s true that you haven’t… technically done anything wrong."

    "I didn’t expect that to actually work, maybe [exorcist] is a really good person."
    "Maybe, this could actually work out."

    e "Don’t make me regret this. Let’s go."

    "The two of you move out of the hallway towards the tower; the mood is much less dreary."




