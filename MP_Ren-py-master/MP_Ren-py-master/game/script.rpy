#Deklarasi gambar
image bg_blck = "#000"
image bg_wht = "#fff"
image splash = "splash.png"
image jlnHutan = im.Scale("bg/1.webp", 1920, 1080)
image jlnHutanb = im.Scale("bg/2.png", 1920, 1080)
image lapangan = im.Scale("bg/lapangan.png", 1920, 1080)
image tenda = im.Scale("bg/tenda.png", 1920, 1080)

image arden marah = "images/arden/arden angry.png"


# Deklarasikan karakter yang digunakan di game.
define mc= Character("[name]", color="#efc8ff", image="mc")
define a = Character("Arden", color="#e96666", image="arden")
define o = Character("Orin", color="#66c0e9", image ="orin")
define s = Character("Sophia", color="#e9b066", image = "sophia")

#Deklarasi posisi
define right2 = Position(xalign=0.9, yalign=0.5)
define right3 = Position(xalign=0.7, yalign=0.5)
define left2 = Position(xalign=0.1, yalign=0.5)
define left3 = Position(xalign=0.3, yalign=0.5)
define center2 = Position(xalign=0.5, yalign=0.5)

#Tampilan logo team
label splashscreen:
    scene bg_blck
    with Pause(1)

    #Pemanggilan gambar logo
    #play sound "audio/z.wav"
    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
                
# Game dimulai disini.
label start:
    scene bg_blck
    $ name = renpy.input("What's your name?", length=10, allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    $ name = name.strip()
    if not name:
        $ name = "Arisha"
    jump prolog
    return

label prolog:
    scene bg_blck
    show jlnHutan
    with fade
    play music "audio/forest.mp3"
    show mc at left2
    show arden at right3
    show sophia at center2
    mc "I want to go home"
    "I missed the comfort of my bed, where I could lie down and scroll through social media without a care in the world"
    "My legs protested with every step, each movement heavier than the last. Sweat clung to my skin, and the suffocating heat made it hard to breathe."
    mc "Arden, are we getting close?"
    show arden confused at right2
    a "Yeah, it’s just ten more minutes."
    mc "Are you sure? Because I swear we passed that tree half an hour ago."
    show arden at right2
    a "We’re in a forest, [mc]. Of course they will look the same"
    mc  "But we haven't seen a single soul in the last 10 minutes. Could you at least check the map?"    
    a "I don’t think it’s necessary. Besides, this isn’t exactly a popular trail, so it’s no surprise we haven’t seen anyone."
    s "Still [mc] has a point. It doesn’t hurt to take a quick look, right? Just to be sure?"
    mc "Yeah, it's not like the map gonna bite"
    a "Alright, alright."
    "Arden unfolded the map, his eyes narrowing as he traced the faded lines and markings."
    "I glanced past him, taking in the endless expanse of forest—a sprawling sea of green that seemed to swallow the horizon. A knot of worry tightened in my chest. What if we were lost?."
    mc "So, are we good?"
    a "Ye—"
    s @ confused "Wait… Where’s Orin?"
    a  "Orin? What do you mean?"
    mc "Shouldn’t he be right behind us?"
    "I turned, my eyes scanned the path. My breath hitched. The familiar figure wasn’t there. How did I miss it? My chest tightened as the weight of the silence pressed in, louder than any sound."
    s "I… I haven’t heard him in the past few minutes."
    a "He’s probably just taking a break. Let’s give it a few minutes. He’ll catch up."
    s "Does he even know the way? What if he gets lost?"
    a "He’ll be fine. As long as he follows the trail, he’ll catch up."
    mc "But what if he didn't follow the trail? Or worse…?"
    "A cold shiver ran down my spine. My stomach tightened, and the air around us seemed to thicken, each rustle in the leaves louder, like they were whispering doubts."
    s "We should search for him… at least check the trail!"
    a "Relax. Orin knows to stay on the trail. He’ll be fine."
    mc "I know, but like you said this isn’t exactly a popular spot. There’s no one around to help him find his way if he wanders around"
    a "Let’s not jump to conclusions. There’s no reason to think the worst just yet."
    "I took a deep breath to calm my nerves, processing the word Arden said. Arden had a point—it hadn’t been that long. Maybe I was overreacting. But something doesn't feel right as every instinct I had told me that we needed to find him."

    menu :
        "What would you do?"
        "Follow your instinct":
            mc "We need to check the trail. It’s better to look now than to just stand here guessing."
            $ search = True
        "Trust Arden":
            mc "Maybe you’re right... Maybe I’m overreacting. But I just... I can’t shake the feeling something’s wrong."
            $ search = False
            
    if search== True:
        s "Yeah, it's better to be safe than sorry. Let's check the trail while he's still nearby"
        a "Fine, fine. Let’s go look, but I’m telling you, he’s probably just sitting somewhere, enjoying the peace while we freak out."
        mc "If he’s lazing around, then good. At least we’ll know he’s safe."
        "The three of us turned back, retracing our steps along the worn trail. The forest, once a comforting escape, now loomed ominously around us."
        jump found
    else :
        s "It’s okay. I know what you mean."
        a "Alright, alright. I know we’re all a little on edge but let’s give Orin a chance to catch up"
        mc "Okay, we’ll wait... but if he’s not back soon, we’re going to have to look for him."
        jump wait

label found:
    scene bg_blck
    show jlnHutanb
    show sophia at center2
    s "ORIN!!!" 
    show sophia at right2 
    with move
    show mc at center2
    mc "Orin… Are you there?"
    "The familiar trail now felt strange, almost hostile. Each step deepened the unease, the silence pressing in on us, broken only by the crunch of our footsteps."
    s "Where is he? I don’t see signs of Orin."
    show mc at left2
    with move
    show arden at center2
    with dissolve
    a "He’s probably just sitting somewhere, watching bugs. You know how he is."
    mc "Yeah, but he shouldn't just vanish without saying something."
    "Then, just as I was losing hope, a figure appeared in the distance, slumped against a tree. Relief hit me like a wave, but it quickly gave way to frustration."
    s @ happy "There he is!"
    mc "Orin! What in the world were you thinking?"
    a "Do you have any idea how worried we were? You’re lucky we didn’t just keep going without you."
    show arden at right3
    show orin at center2
    o "Sorry… I didn’t mean to scare you. I got… distracted."
    mc "Seriously? That’s your excuse?"
    o "I also found this book."
    "He held up an old, tattered book. The leather was soft, but worn with age, the cover cracked and stained. The corners had frayed, barely clinging to the fragile pages inside."
    s "That’s it? A book? Are you kidding me?!"
    mc "Where did you even find that?"
    o "It was just... there. Sitting on the roots of a tree. Like it was waiting for someone."
    a "Orin, that’s creepy. Why would you even pick it?"
    o "It felt… familiar. And listen to this"
    "He flipped open the book, the brittle pages crinkling under his touch. The ink was dark and uneven, scrawled in hurried strokes across the yellowed paper"
    o "Beware to those who wander these woods. The forest keeps what it desires, and those who linger will never leave."
    mc "Is that supposed to be a warning?"
    s "Could be just someone’s idea of a prank."
    a "It must be an old campfire story. Nothing to freak out over."
    o "It doesn’t feel like that. The writing… there’s something off about it."
    s "Something off? Like what?"
    o "Disappearing. Hearing voices. Seeing things that aren’t there."
    "His voice was calm, almost detached, but the forest suddenly felt more alive—as if the trees themselves were listening."
    "My pulse quickened, and I found myself glancing over my shoulder, straining to catch glimpses of things that weren’t there—or maybe things I wished weren’t."
    mc "I don’t feel safe here. Should we just turn back?"
    a "Are you seriously believing the old book?"
    mc "I’m not but this place just feels... odd. What are the chances we’d find something like this out here?"
    s "[mc], I don’t think it’s real—the warning sounds fishy. If something was truly wrong with this forest, wouldn’t we have noticed it by now?."
    o "I’m not so sure. Maybe we haven’t noticed, but something about this doesn’t sit right. It’s Like it was meant to be found, and now we’re paying the price."
    "The more I thought about it, the more uneasy I became. Something wasn’t right—something I couldn’t put into words, but the feeling was there, heavy in the air."
    mc "Let’s just get back. I don’t think it’s worth the risk"
    a  "Come on, it’s just a book. We’ve come this far; we’re not turning back now."
    s "He’s right. Let’s just keep moving. If something feels off, we’ll deal with it then."
    mc "That’s easy for you to say. What if we’re making a mistake?"
    s "Let’s vote, then. Do we keep going, or turn back"
    a "We keep going. The book’s just some old nonsense. There’s no point in overthinking it."
    mc "But what if it’s not? What if we’re walking into something we can’t handle?"
    s "[mc], I understand. But we’ve been fine up until now. Let’s not let fear stop us."
    "I hesitated, but they’re right, nothing has happened so far. Maybe I was overreacting. Maybe it was nothing."

    menu :
        "Risk it":
            mc "…Alright. Let’s just finish the hike. But I’m not ignoring this. We need to stay alert."
            $ Camp = True
        "Not take chances":
            mc "You're right. But I’m not taking chances, I say we turn back."
            $ Camp = False

    if Camp==True:
        s "Great, then it’s settled. We push forward."
        o "But what about the warning?"
        a "Forget it, Orin. The trail’s waiting, and we're not going to let some creepy story derail us."
        "As we started walking again, I couldn’t shake the feeling that the forest was watching us. And the words from the book echoed in my mind: ‘The forest keeps what it desires.’"
        jump arrive
    else :
        s "We’ve already come this far. If we turn back now, we’ll just be wasting time."
        mc "Better wasting time than ending up lost out here, or worse."
        o "I’m with [mc] on this one."
        a "You can’t be serious."
        s "Then it’s decided. Arden, I know you’re disappointed, but we can still come another day"
        scene bg_blck with dissolve
        centered "Two weeks after there's news of missing people found on the forest"
        return

label arrive:
    scene bg_blck
    show lapangan
    show mc happy at center2
    with dissolve
    mc "Finally, we made it!"
    show arden at right2
    a "Told you we’d get here eventually."
    show mc at left2
    with move
    show orin at center2
    o "About time! I was starting to think we were doomed to wander the forest forever."
    # show orin at 
    s "Orin, let’s try to keep the peace, okay?"
    o "You’re no fun, Sophia."
    "As I stepped into the clearing, I felt some tension slip away, but a lingering unease stayed with me. The campsite was stunning, bathed in the fading daylight, yet something about the forest still felt watchful."
    mc "This place is incredible!"
    a "Just wait until sunset; the view is going to blow you away."
    mc "I can’t wait! The views along the way have been absolutely stunning. But I can’t help wondering… are those scenic detours why we’ve taken longer to get here?"
    s "Well… when Arden and I planned this trip, we wanted it to be special so we might’ve taken a more scenic route."
    mc "Oh, so it was part of the plan?"
    "A small sense of relief washed over me, knowing our delay wasn’t entirely accidental. A sense of unease prickled at the back of my mind as I caught her glance toward the darkening trees, her eyes shifting away as if she hoped I wouldn’t catch it."
    s "Sorry, I thought the path would be easy to follow, but I didn’t expect it to take quite that long either."
    mc "Wait, so why didn’t either of you mention this ‘scenic route’ when I asked Arden to double-check the map?"
    a "I didn’t think it was a big deal. Figured we’d make it eventually—and look, here we are. No harm done, right?"
    o "Hold on—you’re saying we were actually lost? I thought you two had it all planned out!"
    "The realization hit hard. It wasn’t just about getting lost—it was that they’d chosen this detour without telling us. I’d trusted them to keep us on track, and now… doubt crept in. If they’d been willing to lead us off course without a word, how could I rely on their judgment out here?"
    mc "Look, I get wanting to enjoy the view, but what if we hadn’t made it before dark? We could’ve ended up in serious trouble."
    a "Alright, maybe I underestimated how long this would take. But we’re here now, and the view was worth it, wasn’t it?"
    "I glanced at Arden, noticing how his nonchalant tone didn’t quite mask the flicker of unease on his face. Arden wasn’t usually this casual about details—something wasn’t adding up. They’d never been this careless before."
    mc "It’s a nice view, sure, but a heads-up would’ve been good. I don’t exactly enjoy surprises."
    a "We just wanted to do something different this time, you know? The best memories come from a bit of spontaneity."
    o "Spontaneity is fine, but wandering a forest without signal isn’t exactly my idea of fun."
    mc "Exactly. If you’re planning something adventurous, let us decide if we’re up for it."
    a "Well, we’re here now, and everything turned out fine. It was just a small detour."
    s "Exactly! Now we’re at the campsite, we should focus on setting up before it gets too dark."
    o "But what if we get lost on the way back? Or worse, what if we’re stuck wandering around all night looking for the exit? Anyone want to hear a spooky camping story to pass the time?"
    a "We’re already here, so what’s the big deal?"
    "I bit my tongue, fighting the urge to snap back at Arden. He knew I didn’t like surprises, especially after what happened last time. A simple warning could have avoided all this frustration"
    mc "Just… next time, clue us in before going ‘scenic.’ I’ve had enough close calls lately."
    a "If you’re that worried, maybe pitch in with planning next time."
    o "Oh, we definitely will—though fair warning, I’ll probably suggest another grand food tour. Assuming we survive this one, of course."
    s "Orin, we’re not doing another food tour and of course we’re making it back."
    a "Exactly! Besides, I’ve planned some great activities for tomorrow. You’ll love it."
    "Despite Arden’s reassuring words, I couldn’t shake the feeling we were tempting fate. My gaze drifted back to the trees, half-expecting something to emerge from the shadows."
    mc "Hopefully ones that lead us out of here."
    a "Aw, don’t be a downer. You’ll enjoy it, trust me."
    o "If we get any surprises, let’s just make sure it’s the fun kind. Don’t need any more /‘unplanned detours./’"
    s "There shouldn’t be any more surprises—unless the weather decides otherwise. Let’s just get these tents set up so we can finally relax."
    o "Actually, could I go gather firewood? While it’s still light, I also want to look around a bit."
    mc "My legs feel like they might give out, so I’ll stay here and help set up the tents."
    s "Good idea. I’ll join Orin to make sure he doesn’t wander too far. Arden, you can help [mc] with the tents."
    mc "Why can't Arden help Orin?"
    s "Because Arden’s the only one who knows how to set these up."
    o "Oh, so another one of Arden’s hidden talents?"
    a "No, it’s not. I asked my uncle to teach me since it’s our first camping trip."
    "I glanced at Arden skeptically. He’d put thought into the trip, yet somehow neglected to mention the scenic route. What else was he keeping to himself? Arden wasn’t usually secretive, but today, it was like he had his own agenda."
    mc "Great, just one more thing to wonder about."
    s "[mc], we may be new to this, but as long as we’re together, we’ll get through anything."
    o "Alright, you two try not to kill each other. Sophie and I will get the firewood—and then, dinner."
    mc "Fine, I’ll follow Arden’s instructions."
    a "You can sit this one out if you don’t want to. I don’t mind handling this."
    mc "No, I’ll help. Setting up four tents by yourself might take a while."
    "I could handle a little teamwork if it gave me something to do—away from the ever-present feeling of being watched."
    s "Good, Orin and I will gather the firewoods then"
    return

label chp3:
    return

label wait:

    return