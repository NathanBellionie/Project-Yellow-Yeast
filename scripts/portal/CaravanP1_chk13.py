# id 13 (CaravanP1_chk13), field 867200500
sm.createQuestWithQRValue(64006, "WC=6;k1=0;k2=0;speed=20;man=200;prog=0;Pt=Caravan_chk13;Ec=13;weather=2;max=16;food=240")
sm.createQuestWithQRValue(64006, "WC=6;k1=0;k2=0;speed=20;man=200;prog=0;Pt=CaravanP1_chk13;Ec=13;weather=2;max=16;food=240")
sm.createQuestWithQRValue(64006, "WC=6;k1=0;k2=0;k3=1;speed=20;man=200;prog=0;Pt=CaravanP1_chk13;Ec=13;weather=2;max=16;food=240")
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendNext("#face1#You're going hunting again? Splendid, I'll join you! My noble soul aches for the thrill of combat! ")
sm.sendSay("#face0#Gillie, I leave Alika in your capable hands. Protect her with your life! ")
sm.sendSay("#face0#I can't be away from Alika for too long, #h0#, so let's make quick work of these brutes! ")
sm.setParam(35)
sm.sendSay("Go to #m867200650#.")
sm.createQuestWithQRValue(64006, "WC=6;k1=0;k2=0;k3=0;speed=20;man=200;prog=0;Pt=CaravanP1_chk13;Ec=13;weather=2;max=16;food=240")
sm.createQuestWithQRValue(64007, "happy0=100;happy1=100;happy2=100;happy3=100;man0=56;man1=33;man2=38;man3=73")
sm.warp(867200650)
