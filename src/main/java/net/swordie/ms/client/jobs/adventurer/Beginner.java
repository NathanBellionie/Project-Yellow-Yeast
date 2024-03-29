package net.swordie.ms.client.jobs.adventurer;

import net.swordie.ms.client.Client;
import net.swordie.ms.client.character.Char;
import net.swordie.ms.client.character.CharacterStat;
import net.swordie.ms.client.character.info.HitInfo;
import net.swordie.ms.client.character.items.Item;
import net.swordie.ms.client.character.skills.Option;
import net.swordie.ms.client.character.skills.Skill;
import net.swordie.ms.client.character.skills.info.AttackInfo;
import net.swordie.ms.client.character.skills.info.SkillInfo;
import net.swordie.ms.client.character.skills.info.SkillUseInfo;
import net.swordie.ms.client.character.skills.temp.CharacterTemporaryStat;
import net.swordie.ms.client.character.skills.temp.TemporaryStatManager;
import net.swordie.ms.client.jobs.Job;
import net.swordie.ms.connection.InPacket;
import net.swordie.ms.constants.JobConstants;
import net.swordie.ms.enums.Stat;
import net.swordie.ms.loaders.ItemData;
import net.swordie.ms.loaders.SkillData;
import net.swordie.ms.scripts.ScriptType;

/**
 * Created on 12/14/2017.
 */
public class Beginner extends Job {
    public static final int THREE_SNAILS = 1000;
    public static final int RECOVERY = 1001;
    public static final int NIMBLE_FEET = 1002;

    public static final int MAPLE_RETURN = 1281;

    private static final int[] addedSkills = new int[]{
            RECOVERY,
            NIMBLE_FEET,
            THREE_SNAILS
    };

    public Beginner(Char chr) {
        super(chr);

        if (chr != null && chr.getId() != 0 && isHandlerOfJob(chr.getJob())) {
            for (int id : addedSkills) {
                if (!chr.hasSkill(id)) {
                    Skill skill = SkillData.getSkillDeepCopyById(id);
                    skill.setRootId(0);
                    skill.setMasterLevel(3);
                    skill.setMaxLevel(3);
                    chr.addSkill(skill);
                }
            }
            if (!JobConstants.isPathFinder(chr.getJob()) && !JobConstants.isDualBlade(chr.getJob())) {
                Skill skill = SkillData.getSkillDeepCopyById(MAPLE_RETURN);
                skill.setCurrentLevel(skill.getMasterLevel());
                chr.addSkill(skill);
            }
        }
    }

    @Override
    public void handleAttack(Client c, AttackInfo attackInfo) {
        super.handleAttack(c, attackInfo);
    }

    @Override
    public void handleSkill(Char chr, TemporaryStatManager tsm, int skillID, int slv, InPacket inPacket, SkillUseInfo skillUseInfo) {
        super.handleSkill(chr, tsm, skillID, slv, inPacket, skillUseInfo);

        final int NIMBLE_FEET = 1002; // Skill ID for Nimble Feet

        if (skillID == NIMBLE_FEET) {
            if (chr.hasSkillOnCooldown(NIMBLE_FEET)) {
                // Skill is on cooldown. Inform the player as needed.
                return;
            }

            if (!chr.applyMpCon(NIMBLE_FEET, slv)) {
                // Not enough MP or applyMpCon failed. Inform the player as needed.
                return;
            }

            // Set the cooldown for "Nimble Feet" to 1 minute (60000 milliseconds)
            chr.addSkillCoolTime(NIMBLE_FEET, 60000);

            // Apply the effects of Nimble Feet based on skill level (slv)
            Option o1 = new Option();
            switch (slv) {
                case 1:
                    o1.nValue = 10; // Movement Speed for Level 1
                    o1.tTerm = 4;   // Duration for Level 1
                    break;
                case 2:
                    o1.nValue = 15; // Movement Speed for Level 2
                    o1.tTerm = 8;   // Duration for Level 2
                    break;
                case 3:
                    o1.nValue = 20; // Movement Speed for Level 3
                    o1.tTerm = 12;  // Duration for Level 3
                    break;
                // Add more cases if there are more levels
            }
            o1.nReason = NIMBLE_FEET;
            tsm.putCharacterStatValue(CharacterTemporaryStat.IndieSpeed, o1);

            tsm.sendSetStatPacket();
        }


           // case RECOVERY:

             //   break;
        }



    @Override
    public void handleHit(Client c, InPacket inPacket, HitInfo hitInfo) {
        super.handleHit(c, inPacket, hitInfo);
    }

    @Override
    public boolean isHandlerOfJob(short id) {
        JobConstants.JobEnum job = JobConstants.JobEnum.getJobById(id);
        return job == JobConstants.JobEnum.BEGINNER;
    }

    @Override
    public int getFinalAttackSkill() {
        return 0;
    }

    @Override
    public void setCharCreationStats(Char chr) {
        super.setCharCreationStats(chr);
        CharacterStat cs = chr.getAvatarData().getCharacterStat();
        switch (chr.getSubJob()) {
            case 1 -> {
                Item dagger = ItemData.getItemDeepCopy(1332000);
                chr.addItemToInventory(dagger);
                Item katara = ItemData.getItemDeepCopy(1342000);
                chr.addItemToInventory(katara);
            }
        }
    }

    @Override
    public void handleLevelUp() {
        super.handleLevelUp();
//        short level = chr.getLevel();
//        switch (level) {
//            case 60:
//                break;
//            case 100:
//                break;
//        }
    }

    @Override
    public void handleJobStart() {
        super.handleJobStart();
        if (!JobConstants.isPathFinder(chr.getJob()) && chr.getSubJob() != 1 && chr.getSubJob() != 2) { //subjob 1 = dual blade // subjob 2 = Cannoneer
            chr.getScriptManager().startScript(0, "job_explorer", ScriptType.Npc);
        }
        if (chr.getSubJob() == 1) {
            chr.setJob(JobConstants.JobEnum.THIEF.getJobId());
            chr.setStatAndSendPacket(Stat.job, chr.getJob());
            chr.addSpToJobByCurrentJob(5);
        }
        if (chr.getSubJob() == 2) {
            chr.setJob(JobConstants.JobEnum.PIRATE_CANNONEER.getJobId());
            chr.setStatAndSendPacket(Stat.job, chr.getJob());
            chr.addSpToJobByCurrentJob(3);
        }
    }

    @Override
    public void handleJobEnd() {
        super.handleJobEnd();
        Item theRelaxer = ItemData.getItemDeepCopy(3010000);
        chr.addItemToInventory(theRelaxer);
    }
}
