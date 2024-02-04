# id 64025 ([MONAD: The First Omen] Evacuation Prep), field 867200400
sm.lockInGameUI(True, False)
sm.sendDelay(2500)
sm.speechBalloon(True, 0, 0, "...Of course I want to save everyone. \r\nBut if the risk is that great...", 2000, 1, 0, 0, 0, 4, 9400587, 4878499)
sm.sendDelay(2500)
sm.speechBalloon(True, 0, 0, "We have to find a way! \r\nHow can a chief say such things?!", 2000, 1, 0, 0, 0, 4, 9400589, 4878499)
sm.sendDelay(3000)
sm.speechBalloon(True, 0, 0, "...", 2000, 1, 0, 0, 0, 4, 9400587, 4878499)
sm.sendDelay(5000)
sm.speechBalloon(True, 0, 0, "Don't bring this up in front of the others. Ever.", 2000, 1, 0, 0, 0, 4, 9400589, 4878499)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendNext("#face0#Ah, #h0#. ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#... ")
sm.setParam(57)
sm.sendSay("#bWhat is it? Is something wrong? ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#Ah... No, we were just... discussing how to carry the injured. ")
sm.sendSay("#face0#I'm sure you've seen, but all of our wagons in town were destroyed in the attack. ")
sm.setParam(57)
sm.sendSay("#bHmm... ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#What about the wagon outside of town? It was probably missed in the attack and shouldn't be hard to patch up. ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#The wagon Aruhi used to move leather with? It's too small, even for our belongings. ")
sm.setParam(57)
sm.sendSay("#bCould we modify it while making repairs? You know, add some parts for the injured to ride on. ")
sm.setParam(37)
sm.sendSay("#face0#As long as we can get the wood, it should be doable. Seems like our best plan at the moment. ")
sm.setParam(57)
sm.sendSay("#bI'll take care of the wood. ")
sm.setParam(37)
sm.sendSay("#face0#Oh! That would be terrific. ")
sm.setParam(57)
sm.sendSay("#bOf course. ")
sm.setParam(37)
sm.sendSay("#face0#Do you remember the mountain that we just came back from? ")
sm.sendSay("#face0#I think 50 more pieces should be enough. I'm sorry to work you so hard, #h0#. ")
sm.setParam(57)
sm.sendSay("#bThink nothing of it. I'll be back in a jiffy.")
sm.sendDelay(1000)
sm.forcedFlip(True)
sm.sendDelay(500)
sm.forcedMove(True, 100)
sm.sendDelay(1000)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendNext("#face0##h0#!")
sm.sendDelay(500)
sm.sendNext("#face0#Thank you.")
sm.setParam(57)
sm.sendSay("#bYou're welcome.")
sm.sendDelay(1000)
sm.forcedFlip(True)
sm.sendDelay(500)
sm.forcedMove(True, 300)
sm.sendDelay(2000)
sm.lockInGameUI(False, True)
sm.startQuest(parentID)
sm.warp(867200440)
