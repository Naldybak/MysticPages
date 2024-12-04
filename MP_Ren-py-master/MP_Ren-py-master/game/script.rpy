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
    mc “I know, but he should know better”
    "Then, just as I was losing hope, a figure appeared in the distance, slumped against a tree. Relief hit me like a wave, but it quickly gave way to frustration."
    a @ happy "There he is!"
    mc "Orin! What in the world were you thinking?"
    s "Do you have any idea how worried we were? You’re lucky we didn’t just keep going without you."
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
        a "We’ve already come this far. If we turn back now, we’ll just be wasting time."
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

label chp3: Deciding
    “Sunlight filtered through the canopy, casting uneven patches of golden light across the forest floor. The shadows, stretched long by the fading light, seemed to shift unnaturally, their edges rippling as if stirred by some unseen hand.“
    “The air carried a mix of warmth and the faint coolness found in shaded corners, a quiet reminder of the forest's expanse. After what felt like hours of hiking, we finally stopped at a secluded clearing, nestled deep within the heart of the woods.”
    mc "Is this the place?" 
    a "Yeah, we’re here!" 
    "I paused, my eyes scanning the clearing. The afternoon sun bathed the campsite in a warm glow, but the air felt heavier, too still—as if we had stumbled into a photograph meant to remain undisturbed."
    "For a moment, I wanted to believe this was the retreat we had imagined—a quiet, untouched sanctuary far from everything. But the unease lingered, a cold thread winding through my chest, like something in the forest didn’t want us here."
    mc "It’s beautiful, but…"
    a "[mc] just wait until the sunset—it’s going to be more amazing."
    s "Honestly, after all the setbacks, I wasn’t sure we’d make it here. But I’m glad we did."
    a "Exactly! And don’t forget about the fun stuff we’ve planned for tomorrow. It’ll be worth all the trouble."
    "I envied their optimism, but something about the shadows felt unnaturally long, as if they were hiding something just out of sight—something I couldn’t explain, but felt deep in my bones.”
    mc "I hope you’re right."
    s "Don't worry, it's going to be worth it. Now let’s get these tents set up, so we can kick back and enjoy the evening!"
    o "Guys, we’ll need firewood for later, right? Mind if I go gather some? I’d also like to explore a bit."
    mc “We do need it, but after the warning, I don’t think it’s a good idea for you to wander off alone.”
    o "I think I can handle myself fine."
    a "No, warning aside, I agree with [mc]. Someone needs to keep an eye on you."
    o "I’m not a child that needs to be watched. I just want to grab a few logs and maybe go sightseeing a bit more before it gets too dark."
    mc "Oh sure, because 'sightseeing' worked out so well for us last time. What could possibly go wrong?"
    s “After what happened last time, it’s better if someone goes with you—just to make sure you don’t wander off again. Plus, an extra hand could come in handy.”
    "I glanced at Orin, who was clearly annoyed, but his eyes kept darting toward the trees, as if the forest was calling him again.”
    ”As much as I wanted to believe him, I wasn’t willing to risk another vanishing act."
Bold: mc "Any volunteers? My legs are killing me, so I prefer to stay and help set up the tents.”
    s "Then I’ll stick with Orin to make sure he doesn’t wander off again. You can help Arden with the tents."
    mc "Perfect. Now we can be reassured that we will not do another 'Find Orin' situation before dinner."
    o "Haha, very funny. Come on, Sophia. Let’s leave these two, and grab the firewood."
    s “Got it. I'll keep an eye on him. Just focus on setting the tent”
    mc “Okay”
    "As Sophia and Orin disappeared into the trees, the clearing seemed quieter, the shadows stretching longer as the sun dipped lower.”
    mc "Alright, let’s get this done."
    a "Sure thing. Let me know if you need a break."
    "I sighed, rolling my eyes, but followed Arden’s instructions as he began assembling the first tent.“
    “For once, something seemed to be going according to plan—or at least, for now. But in the back of my mind, I couldn’t shake the thought that maybe we were settling into the calm before a storm.”
    
Bold: mc "I’m exhausted, but I’ll go with Orin. Someone has to make sure he doesn’t wander off again."
    s "Are you sure? You can stay and help set up the tents if you want."
    mc "Nah, it’s fine. I’ve got this."
    s "Alright, then. I’ll help Arden with the tents, and you can make sure Orin doesn’t get any funny ideas."
    o "Haha, very funny. Come on, let’s leave these two, and grab the firewood."
    mc “Okay, leave this to me.”
    "I matched his pace as we started walking toward the trees. Occasionally I glanced over my shoulder, the others growing smaller as we moved farther from camp.”
    “My chest tightened, and despite my decision to stick with Orin, the unease gnawed at me, as if we were making the wrong choice by staying out here."
    return

label wait:
    “I shifted uneasily, my eyes darting back to the empty trail behind us. The forest felt oppressively still, broken only by the occasional snap of a twig or the faint rustle of leaves.”
    mc “Where’s Orin? Shouldn’t he be here by now?”
    s “Yeah, it’s been so long.”
    a “Maybe he’s got carried away admiring the view. Or getting cozy with some bugs.”
    mc “It’s not funny, Arden. He should’ve caught up by now. This doesn’t feel right
    “The silence around us grew heavy, pressing in like an invisible weight. I tapped my foot anxiously, a gnawing pit of unease twisting in my stomach.”
    ”The stillness of the forest was unnerving, like it was holding its breath. Every crackling branch and shifting leaf felt amplified, like they were waiting for something.”
    mc “I think It’s time to search for him. He’s been gone too long. ”
    s "That’s right. We can’t just stand here guessing. What if something happened to him? We need to split up and look."
    a “Fine, but we’re not splitting up. I know you’re worried but we should stick together."
    “Suddenly, a rustling sound broke through the thick silence, sharp and close. My heart stopped, and I stiffened, every muscle tense.”
    mc “What was that?”
    s “Is that… Orin?”
    a “Let’s hope you’re right.”
    “Then, from the shadows, a figure emerged, dragging their feet. It was Orin, his face pale and his eyes wide, as if he’d seen something he shouldn’t.”
    mc “Orin! Where in the world have you been?”
    s “Do you have any idea how worried we were? What were you doing out there?”
    o “I—”
    mc “What’s that?”
    “I noticed something in his hand, an old, tattered book. The corners had frayed, barely clinging to the fragile pages inside.”
    s “Where did you get the book?"
    o "I get this on a tree. But hear me out, this book—it warns us not to stay in this forest.“
    mc "Wait, are you saying this book is some kind of warning?"
    a "You’re not seriously believing that, are you? It’s probably some campfire story meant to scare kids."
    o "It doesn’t feel like that. I’ve been walking in circles. Then when I was about to give up suddenly I found my way here."
    mc “Orin, that sounds like you were disoriented. Are you okay?"
    o “I’m fine. But I think we should leave.”
    a “And why should we leave?”
    mc "Arden, whether he is telling the truth or not, I don’t think we should continue."
    s “Yeah, Orin isn’t in a good condition to continue”
    a “Why can’t we just rest a bit then continue. We’ve already come this far. If we turn back now, we’ll just be wasting time.”
    mc “Arden, we can still go back another day, but if something happens to Orin, surely you will regret it.
    s “Yeah, [mc] is right”
    a “Fine, let’s continue another day.”
    return

label Sleeping arrangements: 
    “As we finished the last tent, the faint sound of footsteps and muffled chatter signaled Sophia and Orin’s return. Orin carried an armful of firewood, his grin wide despite the strain, while Sophia trailed behind, a small bundle of kindling in her arms”
    mc “Welcome back”
    s "We’re back! How’s it going?"
    mc “We’re finished.”
    a "Yeah, you have perfect timing. We just wrapped up here."
    o “[mc], I hope your cautious streak carried over to setting up the tents. I’d rather not wake up buried under a pile of canvas and poles.”
    mc “Orin—it’s not going to collapse. Arden made sure of that.”
    "I watched as Orin set down the firewood he’d gathered, though his gaze kept flicking toward the tents, his expression skeptical—like he was expecting them to fold up any second."
    mc “For the record, this might be my first time setting one up, but with Arden’s instructions and help, I’m confident they’ll hold.”
    s “Wait a second. Why are there only three tents set up?”
    mc “Yeah, about that…” #kasih kecil
    a “One of the tents has a broken pole. It’s unusable.”
    s “A broken pole? Didn’t you just buy these tents?”
    mc “It’s brand new, but I must have been careless when I stored it. Maybe something hit it, or it got bent while moving stuff around.”
    "I caught the flicker of disapproval on Sophia’s face, her lips pressing into a thin line as she held back whatever remark was on the tip of her tongue”
    o “Wow, [mc] being careless? That’s a twist. First the book, now this. What’s next? Is the forest gonna whisper?”
    s “Orin, this isn’t the time for jokes. With one tent down, we’ll need to figure out our sleeping arrangements.”
    mc “The tents are big enough for three people each, so it won't be a problem.”
    a “Yeah, and it’s just for one night. We’ll manage without any issues.”
    s “Good. At least none of us will be sleeping under the stars. Now we need to figure out who’s sharing a tent”
    mc “I’ll volunteer to share if it makes things easier—It’s my fault for being careless, so I’ll take one for the team and share.”
    a “So, that just leaves us three to decide.”
    o “I don’t mind sharing if you’re okay with the risk of getting kicked in the middle of the night.”
    mc “In that case, I will sleep with Orin. I slept like a log and It’ll be simpler than drawing this out.”
    a "Well, I don’t mind sharing either—in case you want to reconsider. Just pick whoever you’re most comfortable with"
    “I knew the broken tent was my fault, but their easygoing acceptance reminded me of how much I could always count on them. Even now, they didn’t let it turn into a bigger issue. I couldn’t help but feel grateful for them.”
    mc “Don’t tell me, are you gonna say the same thing, Sophia?”
    s “Yeah, so who will you decide to sleep with?”
    a “How about me?”
    s “Nope, you get your own tent. It’s either with Orin, or with me?”
Bold: mc “I will stay with you, Sophia”
    a “What!? What’s wrong with sharing with me?”
    o “Because you’ve got an even meaner kick than I do.”
    mc “Sorry, arden. Orin’s right.”
    a “I’m not”
    s “Yes, you are.”
    “A moment of silence hung in the air before we all burst into laughter, the tension dissolving in an instant.”
    s “Perfect! It’s settled, then. Let’s go ahead and drop our stuff in the tents so we can finally relax.”
    return

label Book:
    o “Finally, the moment I’ve been waiting for—let’s light this thing up!”
    s “You seem more excited about dinner than anything else on this entire journey.”
    o “Of course! Just think about all the delicious meals we can prepare!”
    mc “You glutton, can you not think about food for a second?”
    o “Nope, can't do. Arden, could you do the honor?”
    a “Sure.”
    “I watched as Arden struck a match, and soon the flames crackled to life, casting warm, flickering light across the clearing. As we sat around the fire, the comforting glow eased the tension from earlier, but my mind still lingered on the strange feeling I had about this place.”
    o “Alright, behold! The marshmallows—just wait till I roast them.”
    mc “Eating snacks before dinner? You’ll spoil your appetite. Don’t you want to eat something else first?”
    s “Yeah, we have a few options for dinner.”
    o “Really? What’s on the menu?”
    a “Hotdogs, canned soups, instant noodles, and hotpot with ingredients of your choosing—just pick one!”
    o “Hotpot!?”
    mc “That sounds good… but wait, a hotpot with ingredients of our choosing? Are you serious? That sounds like a disaster waiting to happen!”
    “I couldn’t believe they actually thought this was a good idea. Letting everyone pick their own ingredients? That was just asking for trouble. What if someone brought something weird? I could already picture a pot full of bizarre concoctions, especially with Orin and Arden, who loved to experiment.”
    s “Yes! We asked you to bring ingredients of your choice, remember? Also Hotpot is a mix of ingredients so it shouldn’t be a problem”
    mc “Huh!? I thought it was to bring whatever snack you like to share.”
    a “No, it’s for hotpot. We already told you. It’s not our fault you didn’t listen, so you can’t protest.”
    s “But you did bring something, right?”
    mc “Yeah, I brought a few things. But honestly, I don’t think it’s a good idea to eat strange food right now.”
    a “It’ll be fine, as long as you don’t add anything weird to the hotpot!”
    mc “Says the one most likely to put something weird in there.”
    o “But think about the thrill! With the added risk… wouldn’t it be more exciting?”
    mc “Still, could we just save it for tomorrow? By then, we wouldn’t need to worry about weird food.”
    s “Either way, I don’t have a problem with it. As Orin said, it’s more interesting that way.”
    mc “I’m not sure about this…”
    a “Then it’s settled—tonight is hotpot night!”
    mc “Urgh… do whatever you want.”
    s “Let me set it up.”
    “After Sophia finished arranging the hotpot, we began taking turns tossing ingredients into the bubbling broth. The fire crackled, and a relaxed silence fell over us. But then, suddenly, Orin pulled something out of his pocket.”
    o “Guys, check this out. I found it under a bush back there.”
    s “Whoa, it looks ancient! When did you pick this up?”
    mc “Orin, you shouldn’t pick up strange things to bring along. It could be dangerous!”
    o “Yeah, but while you guys were busy arguing about whether we got lost, I spotted the book peeking out from under a bush. I was curious, so I grabbed it.”
    a “Orin, check it. If there’s some scribble on it, we might be in for an adventure.”
    o “Okay, let’s see… It’s mostly illegible… but wait, look here. ‘Turn back now. Do not enter these woods after dusk. Those who linger here are never seen again…’”
    “I felt a shiver run down my spine. The words hung heavy in the air, and the tension I felt before came back stronger than ever. I wanted to laugh it off, but the darkness surrounding us made it hard to shake the feeling that we might have stumbled into something we didn’t understand.”
    mc “Uhm, is… is that a warning of some kind?”
    a “Probably just someone’s idea of a prank. It’s not like these warnings are uncommon in places like this. After all, if you aren’t careful, you could easily get lost.”
    s “Yeah, maybe, but… it looks so old and beaten up. Why go to such lengths to scare people? There must be some truth to it.”
    o “Come on, guys—don’t tell me you’re all so chicken you can’t handle a little warning from a dusty book!”
    a “Yeah, let’s not let a spooky old book ruin our night. It’s probably nothing. Let’s just focus on the fun we’re having here.”
    o “Exactly. It’s just a story. Nothing to worry about.”
    “I wasn’t entirely convinced, but I decided to let it go for now. After all, nothing bad had happened yet, right? We were still sitting around the fire, enjoying the warmth and company. Still, as I glanced at the dark edges of the clearing, the shadows felt a little too close.”
    return
