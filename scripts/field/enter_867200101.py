# id 867200101 (Abrup Basin : Hunters's Temporary Base Camp), field 867200101
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.setMapTaggedObjectVisible("fire1", False, 0, 0)
sm.setMapTaggedObjectVisible("snow1", False, 0, 0)
sm.setMapTaggedObjectVisible("snow2", False, 0, 0)
sm.setMapTaggedObjectVisible("snow3", False, 0, 0)
sm.sendDelay(500)
sm.forcedMove(False, 100)
sm.sendDelay(500)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#b(Could this be a temporary base camp for hunters?)")
sm.sendDelay(1000)
sm.sendDelay(2000)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT1/wind", 128)
sm.sendNext("#b(It'll be dark soon, and that much colder. This might be a good spot to stop for the night.)")
sm.sendDelay(1000)
sm.sendNext("#b(I should start by clearing the snow and starting a fire.)")
sm.createQuestWithQRValue(64010, "enter=1")
sm.completeQuestNoCheck(64010)
sm.startQuest(64011)
sm.setMapTaggedObjectVisible("fire1", True, 0, 0)
sm.setMapTaggedObjectVisible("snow1", True, 0, 0)
sm.setMapTaggedObjectVisible("snow2", True, 0, 0)
sm.setMapTaggedObjectVisible("snow3", True, 0, 0)
sm.lockInGameUI(False, True)
sm.setMapTaggedObjectVisible("snow1", False, 0, 0)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT1/sonw2", 128)
sm.createQuestWithQRValue(64011, "clean=1")
sm.setMapTaggedObjectVisible("snow2", False, 0, 0)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT1/sonw2", 128)
sm.createQuestWithQRValue(64011, "clean=2")
sm.setMapTaggedObjectVisible("snow3", False, 0, 0)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT1/sonw1", 128)
sm.createQuestWithQRValue(64011, "clean=3")
sm.setMapTaggedObjectVisible("fire1", False, 0, 0)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT1/sonw1", 128)
sm.createQuestWithQRValue(64011, "clean=4")
sm.warp(867200102)