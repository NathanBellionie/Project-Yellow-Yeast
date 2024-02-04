# id 17651 ([Commerci Republic] A Funny Kind of Peace), field 865000002
sm.setSpeakerID(9390207) # Zion
sm.setParam(32)
sm.setColor(1)
sm.sendNext("What would your lord emperor have of you, you mean?")
sm.sendSay("First, you will only trade with the allies of the Heaven Empire, and all trade items will come from a list of approved materials. Every transaction will have a 1% tariff levied upon it as tribute to the glory of the empire.")
sm.setParam(56)
sm.sendSay("That's crazy!")
sm.setParam(36)
sm.setInnerOverrideSpeakerTemplateID(9390203) # Gilberto Daniella
sm.sendSay("Hear him out.")
sm.setParam(32)
sm.sendSay("Second, the Heaven Empire will require a standing order of goods, and citizens, to be delivered at such times as his grace see fit.")
sm.sendSay("Third, the sea lanes used by Commerci for trade will be considered the domain of the Heaven Empire. Therefore, the emperor will have free use of these routes, and ships sailing within them will be subject to random inspections.")
sm.sendSay("Fourth, as a show of our favor, we will take one child from each trade family to reside in the empire for a period of 10 years. They will be raised as one of ours, and to learn of our advanced technology. Kept close, and safe, so long as our peace remains. It is a most gracious offering.")
sm.sendSay("I will have your signature.")
sm.setParam(36)
sm.sendSay("Hm...")
sm.showNpcSpecialActionByTemplateId(9390236, "summon", 0)
sm.setInnerOverrideSpeakerTemplateID(9390202) # Leon Daniella
sm.sendSay("This is not happening!")
sm.setParam(32)
sm.sendSay("This is your son, yes?")
sm.setParam(36)
sm.sendSay("I'm Leon Daniella, the second son of the Prime Minister, and pride of the Commerci Republic!")
sm.setParam(32)
sm.sendSay("I know who you are, young man. I've heard tale of your adventures. You are said to be an excellent ship captain...")
sm.setParam(36)
sm.sendSay("Oh, really? Thanks-- HEY! Don't kiss up to me!")
sm.setParam(32)
sm.sendSay("I am not kissing up, I am here to carry out a mission of peace that concerns both of our countries.")
sm.setParam(36)
sm.sendSay("You call that peace? Ha! You walk in here with a deal that would make us your slaves, and you call it peace? You'd better get outta here now, before I stick the rest of you in that top hat!")
sm.setParam(32)
sm.sendSay("Prime Minister Gilberto, this hostility in your care is less than flattering. I will return tomorrow for your response. I hope that it will be the right one.")
sm.setParam(36)
sm.sendSay("That guy was making me MAD! Sorry, dad, but I have to go take care of some stuff and punch walls.")
sm.completeQuestNoCheck(parentID)
sm.createQuestWithQRValue(18418, "B=33281")
