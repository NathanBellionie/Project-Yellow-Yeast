# id 450003770 (Lachelein : Nightmare Clocktower), field 450003770
sm.lockInGameUI(True, False)
sm.spawnNpc(3003250, 170, -50)
sm.showNpcSpecialActionByTemplateId(3003250, "summon", 0)
sm.showNpcSpecialActionByTemplateId(3003250, "stand2", -1)
sm.zoomCamera(0, 2000, 0, 80, 50)
sm.startQuest(34331)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003250) # Lucid
sm.sendNext("#face6#So, you've finally made it here. ")
sm.playExclSoundWithDownBGM("Voice3.img/Lucid/Q4/0", 128)
sm.setParam(57)
sm.sendSay("It's time to set everyone free! No one is happy in this world you've created! ")
sm.sendSay("Did you really think that just going through the motions, day after day would make them happy? Eating, drinking, and dancing, every single day. They're not content, they're puppets in your sick show!")
sm.setParam(37)
sm.sendSay("#face6#I don't care if they're happy. The act will be enough, if I can change my master's mind.")
sm.playExclSoundWithDownBGM("Voice3.img/Lucid/Q4/2", 128)
sm.setParam(57)
sm.sendSay("What do you mean? Aren't you working for the Black Mage? ")
sm.sendSay("What is the Black Mage scheming?!  ")
sm.setParam(37)
sm.sendSay("#face5#Could you even comprehend #ehis#n true goal? No, I don't think so. I won't waste my time explaining.")
sm.playExclSoundWithDownBGM("Voice3.img/Lucid/Q4/4", 128)
sm.sendSay("#face5#Hehe. You look tired.")
sm.playExclSoundWithDownBGM("Voice3.img/Lucid/Q4/6", 128)
sm.sendSay("#face5#Why don't you rest? Forever...")
sm.playExclSoundWithDownBGM("Voice3.img/Lucid/Q4/7", 128)
sm.spawnNpc(3003251, -107, -5)
sm.showNpcSpecialActionByTemplateId(3003251, "summon", 0)
sm.setInnerOverrideSpeakerTemplateID(3003251) # Protective Mask
sm.sendSay("#face0#Be careful!")
sm.setParam(57)
sm.sendSay("Protective Mask?!")
sm.setParam(37)
sm.sendSay("#face0#The dream's magic is carried on the wings of her butterflies!\r\nIf you breathe in that dust...!")
sm.setInnerOverrideSpeakerTemplateID(3003250) # Lucid
sm.sendSay("#face5#Sorry. You're too late.")
sm.showNpcSpecialActionByTemplateId(3003250, "special", 1)
sm.sendDelay(3000)
sm.spineScreen(True, False, True, 0, "Map/Effect3.img/BossLucid/fog2/mist_003","animation","")
sm.playSound("Sound/SoundEff.img/ArcaneRiver/butterfly1", 200)
sm.sendDelay(2000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(1000)
sm.setParam(57)
sm.sendNext("What do I do now?!  ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(3003251) # Protective Mask
sm.sendSay("#face0#Listen to me carefully, #h0#. \r\nI'm not blinded by her magic, because my mask is a gas mask. ")
sm.sendSay("#face0#I am her nightmare. I was created to stop her. ")
sm.sendSay("#face0#You're #ealready inside the dream#n but you can break free with my help. Now, follow my instructions carefully. ")
sm.setParam(57)
sm.sendSay("(Speak with Protective Mask to begin the fight with #rLucid (Story)#k. ) ")
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.lockInGameUI(False, True)
sm.warp(450004000)