# id 17640 ([Commerci Republic] Pack Up, and Set Sail 3), field 865000000
sm.setSpeakerID(9390204) # Robed Lady
sm.setParam(56)
sm.setColor(1)
sm.sendNext("All right, off to the dock.")
sm.setParam(32)
sm.sendSay("Oh my, we meet again.")
sm.setParam(56)
sm.sendSay("Ahh! Geez... What are you doing behind me?")
sm.setParam(32)
sm.sendSay("You were just in my way.")
sm.setParam(56)
sm.sendSay("I see. Well then, let me get OUT of your way. I'm sorta busy so...")
sm.setParam(32)
sm.sendSay("You're heading out to deal with the pirates?")
sm.setParam(56)
sm.sendSay("Yes. Why? Interested?")
sm.setParam(32)
sm.sendSay("Deary me, no. Why would I be interested in such a crude, barbaric voyage? You enjoy yourselves.")
sm.setParam(56)
sm.sendSay("...Crude? Barbaric? Whatever. I really should head to the dock.")
sm.completeQuestNoCheck(parentID)
sm.completeQuestNoCheck(17730)
sm.createQuestWithQRValue(18418, "B=33265")
sm.createQuestWithQRValue(18418, "B=33266")
