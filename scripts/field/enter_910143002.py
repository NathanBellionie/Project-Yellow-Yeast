# id 910143002 (null), field 910143002
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.zoomCamera(0, 1000, 0, 127, 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(3)
sm.sendNext("There must be a way out of here!")
sm.sendSay("I am #eso#n over this place.")
sm.sendDelay(2000)
sm.spawnNpc(1501012, 480, 133)
sm.showNpcSpecialActionByTemplateId(1501012, "summon", 0)
sm.sendDelay(1000)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 0, 0, 0)
sm.sendDelay(1500)
sm.flipNpcByTemplateId(1501012, False)
sm.sendDelay(500)
sm.moveNpcByTemplateId(1501012, False, 200, 150)
sm.sendDelay(2000)
sm.sendDelay(1500)
sm.sendDelay(1000)
sm.sendNext("What the...?")
sm.sendSay("Is that the witch?")
sm.sendDelay(1000)
sm.sendDelay(1000)
sm.sendDelay(1000)
sm.avatarOriented("Effect/OnUserEff.img/emotion/ddam")
sm.sendNext("Uhh...")
sm.sendSay("She didn't turn me into a newt or anything. Hm... Maybe she's a nice witch.")
sm.sendDelay(1000)
sm.forcedMove(False, 800)
sm.sendDelay(3000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.warp(101081300)
