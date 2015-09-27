#coding=utf8
from ID_items import *
from ID_quests import *
from ID_factions import *
##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  ITEM SLOTS             #############################��Ʒslot
########################################################

slot_item_is_checked               = 0  ###��Ʒ�Ѿ����slot�����ڼ����Ʒ��
slot_item_food_bonus               = 1  ###ʳ��ʿ����
slot_item_book_reading_progress    = 2  ###�鼮�Ķ����
slot_item_book_read                = 3  ###�鼮�Ķ�
slot_item_intelligence_requirement = 4  ###��Ʒ�鱨����

slot_item_amount_available         = 7  ###��Ʒ��Ӧ��

###�����������һ���õ������ڳ���Ĳ�����λ����Ϊ��Ҫ����Ŀ�����������۸�ϸ�
slot_item_urban_demand             = 11 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
###��ũ�����������ڳ���Ĳ�����λ
slot_item_rural_demand             = 12 #consumer demand in villages, measured in abstract units
###��ũ�����������ڳ���Ĳ�����λ
slot_item_desert_demand            = 13 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 14   ###��Ʒ���slot
slot_item_production_string        = 15   ###��Ʒ����ַ�

###��Ʒ��õļ۸� ���磬�����ͽ���װ�׹��ߣ��ĵ沼��Ƥ�Ƥ����Ʒ����
slot_item_tied_to_good_price       = 20 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

###��Ʒ�������
slot_item_num_positions            = 22
###��Ʒ��꿪ʼ
slot_item_positions_begin          = 23 #reserve around 5 slots after this ###�������Լ5 slot֮��


slot_item_multiplayer_faction_price_multipliers_begin = 30 #reserve around 10 slots after this ###�������Լ10 slot֮��

slot_item_primary_raw_material    		= 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items of inputs consumed per run
###��Ʒ��۸�
slot_item_base_price                    = 53 #taken from module_items
#slot_item_production_site			    = 54 #a string replaced with function - Armagan
slot_item_output_per_run                = 55 #number of items produced per run
slot_item_overhead_per_run              = 56 #labor and overhead per run
slot_item_secondary_raw_material        = 57 #in this case, the amount used is only one
slot_item_enterprise_building_cost      = 58 #enterprise building cost


slot_item_multiplayer_item_class   = 60 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 61 #temporary, can be moved to higher values


########################################################
##  AGENT SLOTS            #############################agent slot
########################################################

slot_agent_target_entry_point     = 0   ###��ڵ㴥������������ظ�����
slot_agent_target_x_pos           = 1   ###x��괥��
slot_agent_target_y_pos           = 2   ###y��괥��
slot_agent_is_alive_before_retreat= 3   ###����֮ǰ����
slot_agent_is_in_scripted_mode    = 4   ###�籾ģʽ
slot_agent_is_not_reinforcement   = 5   ###agent����Ԯ��
slot_agent_tournament_point       = 6   ###��������
slot_agent_arena_team_set         = 7   ###����agent���������
slot_agent_spawn_entry_point      = 8   ###agentˢ���
slot_agent_target_prop_instance   = 9   ###����ʵ��
slot_agent_map_overlay_id         = 10  ###agent��ͼ��ͼid
slot_agent_target_entry_point     = 11  ###��ڵ㴥������������ظ�����
slot_agent_initial_ally_power     = 12  ###����Ѿ�����
slot_agent_initial_enemy_power    = 13  ###�����������
slot_agent_enemy_threat           = 14  ###���˵���в
slot_agent_is_running_away        = 15  ###agent������
slot_agent_courage_score          = 16  ###agent��������
slot_agent_is_respawn_as_bot      = 17  ###agent����ΪBOT
slot_agent_cur_animation          = 18  ###agent��ǰ����
slot_agent_next_action_time       = 19  ###agent�´��¼�ʱ��
slot_agent_state                  = 20  ###agent״̬
slot_agent_in_duel_with           = 21  ###agent������
slot_agent_duel_start_time        = 22  ###agent������ʼʱ��

slot_agent_walker_occupation      = 25  ###ɢ�����˵�ְҵ
#Equipment cost fix
slot_agent_bought_horse           = 26
###

########################################################
##  FACTION SLOTS          #############################���slot
########################################################
###���ai״̬
slot_faction_ai_state                   = 4
###���ai����
slot_faction_ai_object                  = 5
###���ai��ݣ�Ŀǰδʹ�õģ��������ӵ��Ӿ��߱���ɵ��ַ�
slot_faction_ai_rationale               = 6 #Currently unused, can be linked to strings generated from decision checklists


###���Ԫ˧
slot_faction_marshall                   = 8
###���ai������׷����
slot_faction_ai_offensive_max_followers = 9

###����Ļ�
slot_faction_culture                    = 10
###��ҹ���
slot_faction_leader                     = 11

###�����ʱslot
slot_faction_temp_slot                  = 12

##slot_faction_vassal_of            = 11
###�������
slot_faction_banner                     = 15

###��Ҿ����Ŀ
slot_faction_number_of_parties    = 20
###���״̬
slot_faction_state                = 21

###�����Ѿ�
slot_faction_adjective            = 22


###�����Ҿ���
slot_faction_player_alarm         		= 30
###����ϴι�Ӷ����ʱ��
slot_faction_last_mercenary_offer_time 	= 31
###��ҳ������
slot_faction_recognized_player    		= 32

#overriding troop info for factions in quick start mode.###ѹ��һ�еĶ�����Ϣ�ڿ�������ģʽ�Ĺ�ҡ�
slot_faction_quick_battle_tier_1_infantry      = 41 ###��ҿ���ս�����������1
slot_faction_quick_battle_tier_2_infantry      = 42 ###��ҿ���ս�����������2
slot_faction_quick_battle_tier_1_archer        = 43 ###��ҿ���ս�������ֱ�����1
slot_faction_quick_battle_tier_2_archer        = 44 ###��ҿ���ս�������ֱ�����2
slot_faction_quick_battle_tier_1_cavalry       = 45 ###��ҿ���ս����������1
slot_faction_quick_battle_tier_2_cavalry       = 46 ###��ҿ���ս����������2

slot_faction_tier_1_troop         = 41 ###��ұ�����1
slot_faction_tier_2_troop         = 42 ###��ұ�����2
slot_faction_tier_3_troop         = 43 ###��ұ�����3
slot_faction_tier_4_troop         = 44 ###��ұ�����4
slot_faction_tier_5_troop         = 45 ###��ұ�����5

###��Ӫ�ӱ�
slot_faction_deserter_troop       = 48
###��Ӫ����
slot_faction_guard_troop          = 49
###��Ӫ�����
slot_faction_messenger_troop      = 50
###��Ӫ��������
slot_faction_prison_guard_troop   = 51
###��Ӫ�Ǳ�����
slot_faction_castle_guard_troop   = 52

###����ɢ������
slot_faction_town_walker_male_troop      = 53
###����ɢ��Ů��
slot_faction_town_walker_female_troop    = 54
###��ׯɢ������
slot_faction_village_walker_male_troop   = 55
###��ׯɢ��Ů��
slot_faction_village_walker_female_troop = 56
###�������Լ��
slot_faction_town_spy_male_troop         = 57
###����Ů�Լ��
slot_faction_town_spy_female_troop       = 58

###����췴����
slot_faction_has_rebellion_chance = 60

###��Ҳ��ȶ������һ�β���
slot_faction_instability          = 61 #last time measured


#UNIMPLEMENTED FEATURE ISSUES
slot_faction_war_damage_inflicted_when_marshal_appointed = 62 #Probably deprecate###���ܷ���
slot_faction_war_damage_suffered_when_marshal_appointed  = 63 #Probably deprecate###���ܷ���

###�����������
slot_faction_political_issue 							 = 64 #Center or marshal appointment
###�����������ʱ��
slot_faction_political_issue_time 						 = 65 #Now is used


#Rebellion changes
#slot_faction_rebellion_target                     = 65
#slot_faction_inactive_leader_location         = 66
#slot_faction_support_base                     = 67
#Rebellion changes



#slot_faction_deserter_party_template       = 62

slot_faction_reinforcements_a        = 77 ###���ˢ��ģ��a
slot_faction_reinforcements_b        = 78 ###���ˢ��ģ��b
slot_faction_reinforcements_c        = 79 ###���ˢ��ģ��c

slot_faction_num_armies              = 80 ###��Ҿ����
slot_faction_num_castles             = 81 ###��ҳǱ�����
slot_faction_num_towns               = 82 ###��ҳ�������

slot_faction_last_attacked_center    = 85 ###������������
slot_faction_last_attacked_hours     = 86 ###��������ʱ��
slot_faction_last_safe_hours         = 87 ###������ȫ��ʱ��

slot_faction_num_routed_agents       = 90 ###���agent·������

#useful for competitive consumption ####���ھ��������
slot_faction_biggest_feast_score      = 91
slot_faction_biggest_feast_time       = 92
slot_faction_biggest_feast_host       = 93


#Faction AI states ###���AI״̬
###�������������Ὺʼ��������Ҫ������
slot_faction_last_feast_concluded       = 94 #Set when a feast starts -- this needs to be deprecated
###��������Ὺʼʱ�䡣
slot_faction_last_feast_start_time      = 94 #this is a bit confusing

###���AI����ʱ��
slot_faction_ai_last_offensive_time 	= 95 #Set when an offensive concludes
###���AI������
slot_faction_last_offensive_concluded 	= 95 #Set when an offensive concludes

###���AI�������ʱ�䡣���һ�Σ�����ΥԼ��ʢ�硪�����������������˶�����faction_ai�ű�
slot_faction_ai_last_rest_time      	= 96 #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
###���AI��ǰ״̬���
slot_faction_ai_current_state_started   = 97 #

###���AI�������Ե��¼������Եķ��ء����Ի�ս��
slot_faction_ai_last_decisive_event     = 98 #capture a fortress or declaration of war

###��ҹ��troop��ʿ��
slot_faction_morale_of_player_troops    = 99

#diplomacy
slot_faction_truce_days_with_factions_begin 			= 120
slot_faction_provocation_days_with_factions_begin 		= 130
slot_faction_war_damage_inflicted_on_factions_begin 	= 140
slot_faction_sum_advice_about_factions_begin 			= 150

#revolts -- notes for self
#type 1 -- minor revolt, aimed at negotiating change without changing the ruler
#type 2 -- alternate ruler revolt (ie, pretender, chinese dynastic revolt -- keep the same polity but switch the ruler)
	#subtype -- pretender (keeps the same dynasty)
	#"mandate of heaven" -- same basic rules, but a different dynasty
	#alternate/religious
	#alternate/political
#type 3 -- separatist revolt
	# reGonalist/dynastic (based around an alternate ruling house
	# regionalist/republican
	# messianic (ie, Canudos)

########################################################
##  PARTY SLOTS            #############################����slot
########################################################
###��������
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle

###���鳷�˱�ǩ
slot_party_retreat_flag        = 2
###����������
slot_party_ignore_player_until = 3
###����ai״̬
slot_party_ai_state            = 4
###����ai����
slot_party_ai_object           = 5
###����ai��ݣ���ǰδʹ�ã����������ڱ���һ���ַ����������˼��
slot_party_ai_rationale        = 6 #Currently unused, but can be used to save a string explaining the lord's thinking

#slot_town_belongs_to_kingdom   = 6
###��������
slot_town_lord                 = 7
###����ai
slot_party_ai_substate         = 8
###��Ҷ��߳���
slot_town_claimed_by_player    = 9

###��Ҹ�ţ
slot_cattle_driven_by_player = slot_town_lord #hack

###������
slot_town_center        = 10
###����Ǳ�
slot_town_castle        = 11
###�������
slot_town_prison        = 12
###����ƹ�
slot_town_tavern        = 13
###�����̵�
slot_town_store         = 14
###���򾺼���
slot_town_arena         = 16
###����С��
slot_town_alley         = 17
###�����ǽ
slot_town_walls         = 18
###�����Ļ�
slot_center_culture     = 19

###����ƹ��ϰ�
slot_town_tavernkeeper  = 20
###���������ϰ�
slot_town_weaponsmith   = 21
###��������ϰ�
slot_town_armorer       = 22
###�����ӻ��ϰ�
slot_town_merchant      = 23
###������ƥ�ϰ�
slot_town_horse_merchant= 24
###�����򳤡���ׯ�峤
slot_town_elder         = 25
###������ҹ�ϵ
slot_center_player_relation = 26

###Χ�����ĵĹ�����
slot_center_siege_with_belfry = 27
###������һ�ν��ܵ�troop
slot_center_last_taken_by_troop = 28

# party will follow this party if set:
slot_party_commander_party = 30 #default -1   #Deprecate###����
###����������
slot_party_following_player    = 31
###����������ʱ������
slot_party_follow_player_until_time = 32
###���鲻Ҫ�������ʱ������
slot_party_dont_follow_player_until_time = 33

###��ׯ�Ѳ�
slot_village_raided_by        = 34
###��ׯ״̬ svs_normal�� svs_being_raided��ʼ�Ѳ� svs_looted�Ӷ� svs_recovering�ָ� svs_deserted���˾�ס
slot_village_state            = 35 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
###����ǰ��
slot_village_raid_progress    = 36
###�ָ�ǰ��
slot_village_recover_progress = 37
###��ׯ����ð��
slot_village_smoke_added      = 38

###��ׯ����ǿ��
slot_village_infested_by_bandits   = 39

###�����ϴη��ʵ�����
slot_center_last_visited_by_lord   = 41

###�����ϴ���Ҿ���Сʱ
slot_center_last_player_alarm_hour = 42

###��ׯ��Ҳ���͵ţ
slot_village_player_can_not_steal_cattle = 46

###�����ۻ�˰��
slot_center_accumulated_rents      = 47 #collected automatically by NPC lords NPC�������Զ��ռ�
###�����ۻ��˰
slot_center_accumulated_tariffs    = 48 #collected automatically by NPC lords NPC�������Զ��ռ�
###����Ǳ��Ƹ�
slot_town_wealth        = 49 #total amount of accumulated wealth in the center, pays for the garrison
###�����ٶ�
slot_town_prosperity    = 50 #affects the amount of wealth generated
###������Ҽ��ʡ�ʤ��
slot_town_player_odds   = 51


###�����ϴ�֧���շ�ʱ��
slot_party_last_toll_paid_hours = 52
###����Ǳ�ʳ�ﴢ����
slot_party_food_store           = 53 #used for sieges
###��ׯ��Χ
slot_center_is_besieged_by      = 54 #used for sieges
###�ϴη��ֵĵ���
slot_center_last_spotted_enemy  = 55

slot_party_cached_strength        = 56  ###���黺��ǿ��
slot_party_nearby_friend_strength = 57  ###���鸽������ǿ��
slot_party_nearby_enemy_strength  = 58  ###���鸽��о�ǿ��
slot_party_follower_strength      = 59  ###�������ǿ��

slot_town_reinforcement_party_template = 60 ###����Ԯ�����ģ��
slot_center_original_faction           = 61 ###����ԭʼ���
slot_center_ex_faction                 = 62 ###����֮����

###���������
slot_party_follow_me                   = 63
###����Χ����ʼʱ��
slot_center_siege_begin_hours          = 64 #used for sieges
###����Χ���Ѷ�
slot_center_siege_hardness             = 65

slot_center_sortie_strength            = 66 ###����ͻΧǿ��
slot_center_sortie_enemy_strength      = 67 ###����ͻΧ�о�ǿ��

slot_party_last_in_combat              = 68 #used for AI ###�����ϴ�ս����ʱ��
slot_party_last_in_home_center         = 69 #used for AI ###�����ϴ��ڳ�������ʱ��
slot_party_leader_last_courted         = 70 #used for AI ###���������ϴ�׷���ʱ��
slot_party_last_in_any_center          = 71 #used for AI ###�����ϴ����κγ����ʱ��



slot_castle_exterior    = slot_town_center ###�Ǳ��ⲿ=��������

#slot_town_rebellion_contact   = 76
#trs_not_yet_approached  = 0
#trs_approached_before   = 1
#trs_approached_recently = 2


########################## slot_troop_kingsupport_argument ###npc֧�ֹ�����۵Ĳ���
argument_none         = 0
###����
argument_claim        = 1 #deprecate for legal      ###���ӷ���
###����
argument_legal        = 1

###�߶�
argument_ruler        = 2 #deprecate for commons    ###����Ϊ����Ժ
###����Ժ
argument_commons      = 2

###Ч��
argument_benefit      = 3 #deprecate for reward     ###���Խ���
###����
argument_reward       = 3

###ʤ��
argument_victory      = 4
###����Ժ
argument_lords        = 5
###�Կ�
argument_rivalries    = 6 #new - needs to be added  ###��Ҫ����

slot_town_village_product = 76

slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_town_arena_melee_mission_tpl = 78
slot_town_arena_torny_mission_tpl = 79
slot_town_arena_melee_1_num_teams = 80
slot_town_arena_melee_1_team_size = 81
slot_town_arena_melee_2_num_teams = 82
slot_town_arena_melee_2_team_size = 83
slot_town_arena_melee_3_num_teams = 84
slot_town_arena_melee_3_team_size = 85
slot_town_arena_melee_cur_tier    = 86
##slot_town_arena_template	  = 87

slot_center_npc_volunteer_troop_type   = 90
slot_center_npc_volunteer_troop_amount = 91
slot_center_mercenary_troop_type  = 90
slot_center_mercenary_troop_amount= 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93

#slot_center_companion_candidate   = 94
slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99

###�����Ӷ�����slot
num_party_loot_slots    = 5
###�����´��Ӷ���Ʒslot
slot_party_next_looted_item_slot  = 109
slot_party_looted_item_1          = 110
slot_party_looted_item_2          = 111
slot_party_looted_item_3          = 112
slot_party_looted_item_4          = 113
slot_party_looted_item_5          = 114
slot_party_looted_item_1_modifier = 115
slot_party_looted_item_2_modifier = 116
slot_party_looted_item_3_modifier = 117
slot_party_looted_item_4_modifier = 118
slot_party_looted_item_5_modifier = 119

slot_village_bound_center         = 120   ###��ׯ�������Ǹ�����Ǳ�
slot_village_market_town          = 121   ###��ׯ�����г�
slot_village_farmer_party         = 122   ###��ׯ������
slot_party_home_center            = 123   ###����ļ�����������   #Only use with caravans and villagers ###ֻ���̶Ӻʹ���ʹ��

###���ĵ�ǰ����
slot_center_current_improvement   = 124
###���Ľ������ʱ��
slot_center_improvement_end_hour  = 125

###�����ϴκ�����ó��
slot_party_last_traded_center     = 126



slot_center_has_manor            = 130 #village###ׯ԰
slot_center_has_fish_pond        = 131 #village###������ĥ��
slot_center_has_watch_tower      = 132 #village###������
slot_center_has_school           = 133 #village###ѧУ
slot_center_has_messenger_post   = 134 #town, castle, village###��վ
slot_center_has_prisoner_tower   = 135 #town, castle###����

village_improvements_begin = slot_center_has_manor
village_improvements_end          = 135

walled_center_improvements_begin = slot_center_has_messenger_post
walled_center_improvements_end               = 136

###������ҹ���
slot_center_player_enterprise     				  = 137 #noted with the item produced
slot_center_player_enterprise_production_order    = 138
slot_center_player_enterprise_consumption_order   = 139 #not used
###������ҹ�������ʱ��
slot_center_player_enterprise_days_until_complete = 139 #Used instead

slot_center_player_enterprise_balance             = 140 #not used
slot_center_player_enterprise_input_price         = 141 #not used
slot_center_player_enterprise_output_price        = 142 #not used



slot_center_has_bandits                        = 155  ###����������
slot_town_has_tournament                       = 156  ###�����н�����
slot_town_tournament_max_teams                 = 157  ###��������������
slot_town_tournament_max_team_size             = 158  ###���������������С

slot_center_faction_when_oath_renounced        = 159


###########################����ɢ��������
slot_center_walker_0_troop                   = 160
slot_center_walker_1_troop                   = 161
slot_center_walker_2_troop                   = 162
slot_center_walker_3_troop                   = 163
slot_center_walker_4_troop                   = 164
slot_center_walker_5_troop                   = 165
slot_center_walker_6_troop                   = 166
slot_center_walker_7_troop                   = 167
slot_center_walker_8_troop                   = 168
slot_center_walker_9_troop                   = 169

slot_center_walker_0_dna                     = 170
slot_center_walker_1_dna                     = 171
slot_center_walker_2_dna                     = 172
slot_center_walker_3_dna                     = 173
slot_center_walker_4_dna                     = 174
slot_center_walker_5_dna                     = 175
slot_center_walker_6_dna                     = 176
slot_center_walker_7_dna                     = 177
slot_center_walker_8_dna                     = 178
slot_center_walker_9_dna                     = 179

slot_center_walker_0_type                    = 180
slot_center_walker_1_type                    = 181
slot_center_walker_2_type                    = 182
slot_center_walker_3_type                    = 183
slot_center_walker_4_type                    = 184
slot_center_walker_5_type                    = 185
slot_center_walker_6_type                    = 186
slot_center_walker_7_type                    = 187
slot_center_walker_8_type                    = 188
slot_center_walker_9_type                    = 189

###################����ó��·��
slot_town_trade_route_1           = 190
slot_town_trade_route_2           = 191
slot_town_trade_route_3           = 192
slot_town_trade_route_4           = 193
slot_town_trade_route_5           = 194
slot_town_trade_route_6           = 195
slot_town_trade_route_7           = 196
slot_town_trade_route_8           = 197
slot_town_trade_route_9           = 198
slot_town_trade_route_10          = 199
slot_town_trade_route_11          = 200
slot_town_trade_route_12          = 201
slot_town_trade_route_13          = 202
slot_town_trade_route_14          = 203
slot_town_trade_route_15          = 204

slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_15 + 1

###������Ʒ�� = ����Ʒ - ����
num_trade_goods = itm_siege_supply - itm_spice
slot_town_trade_good_productions_begin       = 500 #a harmless number, until it can be deprecated

#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate

###��ׯţ����
slot_village_number_of_cattle   = 205
###����⣬���ң����أ����ͣ�
slot_center_head_cattle         = 205 #dried meat, cheese, hides, butter
###�������������㳦����ë
slot_center_head_sheep			= 206 #sausages, wool
###��������������������ڸ���ó����Ŀ��������
slot_center_head_horses		 	= 207 #horses can be a trade item used in tracking but which are never offered for sale

###��������Ķ�����ţ��������������ֵΪţ����������ߣ��������
slot_center_acres_pasture       = 208 #pasture area for grazing of cattles and sheeps, if this value is high then number of cattles and sheeps increase faster


###�����Դ��ʼ
slot_production_sources_begin = 209

slot_center_acres_grain			= 209 #grain            ###ũ������ʳ��
slot_center_acres_olives        = 210 #olives       ###���԰����魣�
slot_center_acres_vineyard		= 211 #fruit          ###����԰�����ѣ�
slot_center_acres_flax          = 212 #flax         ###����԰�����飩
slot_center_acres_dates			= 213 #dates

slot_center_fishing_fleet		= 214 #smoked fish      ###���㴬�ӣ�Ѭ�㣩
slot_center_salt_pans		    = 215 #salt             ###����Σ�

slot_center_apiaries       		= 216 #honey          ###��䳡�����ۣ�
slot_center_silk_farms			= 217 #silk             ###˿�񳡣�˿��
slot_center_kirmiz_farms		= 218 #dyes             ###Ⱦ�ϳ���Ⱦ�ϣ�

slot_center_iron_deposits       = 219 #iron         ###��󴲣�������
slot_center_fur_traps			= 220 #furs               ###ëƤ���壨ëƤ��

slot_center_mills				= 221 #bread                ###ĥ�������
slot_center_breweries			= 222 #ale                ###ơ�Ƴ���ơ�ƣ�
slot_center_wine_presses		= 223 #wine             ###��Ƴ������Ѿƣ�
slot_center_olive_presses		= 224 #oil              ###��魻�����ͣ�

slot_center_linen_looms			= 225 #linen            ###����֯�����飩
slot_center_silk_looms          = 226 #velvet       ###˿֯������ޣ�
slot_center_wool_looms          = 227 #wool cloth   ###ë֯��

slot_center_pottery_kilns		= 228 #pottery          ###��Ҥ��������
slot_center_smithies			= 229 #tools              ###���̣����ߣ�
slot_center_tanneries			= 230 #leatherwork        ###�Ƹﳧ��Ƥ�
#naval stores - uses timber, pitch, and linen###�����̵�-ʹ��ľ�ģ����࣬�����鲼
slot_center_shipyards			= 231                     ###����

slot_center_household_gardens   = 232 #cabbages     ###��ͥ��԰(���Ĳ�)

###�����Դ����
slot_production_sources_end = 233

#all spice comes overland to Tulga ###���е�������½·Tulga ͼ³��
#all dyes come by sea to Jelkala  ###���е�Ⱦ�����ɺ�����jelkala �ܿ���

#chicken and pork are perishable and non-tradeable, and based on grain production
###����������������ԺͲ��ɽ��׵ģ�������ʳ���
#timber and pitch if we ever have a shipbuilding industry ###ľ�ĺ����������������촬ҵ
#limestone and timber for mortar, if we allow building ###ʯ��ʯ��ľ��ɰ��������������?��

slot_town_last_nearby_fire_time                         = 240 ###����Ǳ��ϴθ����ׯ�Ż�ʱ��

#slot_town_trade_good_prices_begin            = slot_town_trade_good_productions_begin + num_trade_goods + 1
###�����������troop
slot_party_following_orders_of_troop        = 244
###������������
slot_party_orders_type				        = 245
###��������Ŀ��
slot_party_orders_object				    = 246
###��������ʱ��
slot_party_orders_time				    	= 247

slot_party_temp_slot_1			            = 248 #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts
slot_party_under_player_suggestion			= 249 #move this up a bit
slot_town_trade_good_prices_begin 			= 250

slot_center_last_reconnoitered_by_faction_time 				= 350
#slot_center_last_reconnoitered_by_faction_cached_strength 	= 360
#slot_center_last_reconnoitered_by_faction_friend_strength 	= 370




#slot_party_type values
##spt_caravan            = 1  ###�̶�
spt_castle             = 2    ###�Ǳ�
spt_town               = 3    ###����
spt_village            = 4    ###��ׯ
##spt_forager            = 5  ###������
##spt_war_party          = 6  ###
##spt_patrol             = 7  ###Ѳ�߶ӡ�����
##spt_messenger          = 8  ###��ʹ
##spt_raider             = 9  ###Ϯ���ߡ�������
##spt_scout              = 10 ###���
spt_kingdom_caravan    = 11   ###�����̶�
##spt_prisoner_train     = 12 ###������
spt_kingdom_hero_party = 13   ###�����������
##spt_merchant_caravan   = 14 ###�����̶�
spt_village_farmer     = 15   ###��ׯũ��ũ����
spt_ship               = 16   ###��
spt_cattle_herd        = 17   ###ţȺ
spt_bandit_lair       = 18    ###ǿ����Ѩ
#spt_deserter           = 20  ###�ӱ�

kingdom_party_types_begin = spt_kingdom_caravan
kingdom_party_types_end = spt_kingdom_hero_party + 1


#slot_faction_state values ###slot_faction_state ��Ӫ���״̬��ֵ

sfs_active                     = 0 ###��Ծ��
sfs_defeated                   = 1 ###��ܵ�
sfs_inactive                   = 2 ###����Ծ��
sfs_inactive_rebellion         = 3 ###����Ծ������
sfs_beginning_rebellion        = 4 ###��ʼ����


#slot_faction_ai_state values ###slot_faction_ai_state��Ӫ���ai״̬��ֵ
###Ĭ��
sfai_default                   		 = 0 #also defending
###�ۻ���
sfai_gathering_army            		 = 1
###��������
sfai_attacking_center          		 = 2
###Ϯ����ׯ
sfai_raiding_village           		 = 3
###�������˾��
sfai_attacking_enemy_army      		 = 4
###��������������Χ
sfai_attacking_enemies_around_center = 5
###��ᣬ���磬���񣬻��ش�����
sfai_feast             		 		 = 6 #can be feast, wedding, or major tournament

#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
###����¼���һ��ͨ�õĹ���ۻᡣ�����������������һ��С���ҳ��������������һ���Ǳ���

#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present
###�����ڶ��������¼�������Ƕ����Ѿ�����һ���£����Ůʿ�ļ໤���Ǹ������������������ﶼ�Ǵ��ڵ�



#Rebellion system changes begin ###�ƶȱ�Ǩ��ʼ����
sfai_nascent_rebellion          = 7
#Rebellion system changes end


#slot_party_ai_state values ###slot_party_ai_state����AI״̬��ֵ
###δ�����
spai_undefined                  = -1
###Χ������
spai_besieging_center           = 1
###���ĸ���Ѳ��
spai_patrolling_around_center   = 4
###Ϯ��������Χ���Ӷ��ׯ
spai_raiding_around_center      = 5
##spai_raiding_village            = 6
###��������
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
###Ϯ�����
spai_engaging_army              = 10
###������
spai_accompanying_army          = 11
###�������
spai_screening_army             = 12
###����ó��
spai_trading_with_town          = 13
###�����ĳ�������
spai_retreating_to_center       = 14
##spai_trading_within_kingdom     = 15
###���ʴ�ׯ
spai_visiting_village           = 16 #same thing, I think. Recruiting differs from holding because NPC parties don't actually enter villages ###ͬ������飬���롣��Ƹ��ع���ΪNPC������û����������ׯ


#slot_village_state values ###slot_village_state��ׯ״̬��ֵ
###���
svs_normal                      = 0
###���Ѳ�
svs_being_raided                = 1
###�Ӷ�
svs_looted                      = 2
###����
svs_recovering                  = 3
###�����
svs_deserted                    = 4
###Χ��
svs_under_siege                 = 5

#$g_player_icon_state values ���icon״̬
pis_normal                      = 0   ###��
pis_camping                     = 1   ###��Ӫ
pis_ship                        = 2   ###��


########################################################
##  SCENE SLOTS            #############################����slot
########################################################

slot_scene_visited              = 0   ###��������
slot_scene_belfry_props_begin   = 10  ###�������������߿�ʼ



########################################################
##  TROOP SLOTS            #############################troop slot
########################################################
#slot_troop_role         = 0  # 10=Kingdom Lord ###troop��λ

###troopְҵ 0���� 1����
slot_troop_occupation          = 2  # 0 = free, 1 = merchant
#slot_troop_duty               = 3  # Kingdom duty, 0 = free ###troopְ��
#slot_troop_homage_type         = 45  ###troopЧ��˳������
#homage_mercenary =             = 1 #Player is on a temporary contract ###�����һ����ʱ��ͬ
#homage_official =              = 2 #Player has a royal appointment ###�����һ���ʼ�����
#homage_feudal   =              = 3 #


###troop״̬
slot_troop_state               = 3
###���̸ʱ��
slot_troop_last_talk_time      = 4
###��Ҳ������󰮵�״̬�������ܳ�Ϊ��׸
slot_troop_met                 = 5 #i also use this for the courtship state -- may become cumbersome
###troop�󰮽�չ 2��ʾ���� 3ͬ����� 4�����ϵ
slot_troop_courtship_state     = 5 #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship

###troop����ģ��
slot_troop_party_template      = 6
###troop����ײ�
#slot_troop_kingdom_rank        = 7

###troop����
slot_troop_renown              = 7

###troop������
##slot_troop_is_prisoner         = 8  # important for heroes only ֻ������Ҫ��Ӣ��
###����troop����
slot_troop_prisoner_of_party   = 8  # important for heroes only ֻ������Ҫ��Ӣ��
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

###troopĿǰ�¼�
slot_troop_present_at_event    = 9

###troop�쵼�Ķ��飬ֻ����������������������²�����slot��ֵΪ-1����ʾ���ܴ��κα�
slot_troop_leaded_party         = 10 # important for kingdom heroes only
###troop�Ʋ�ֻ����������
slot_troop_wealth               = 11 # important for kingdom heroes only
###troop��ǰ���ڳ������� npc�ھƹ�ˢ���ã�������Ӣ�ۣ�
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)

###troop�����������ģ�ֻ�������������
slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only

###troopԭʼ��Ӫ
slot_troop_original_faction     = 14 # for pretenders
#slot_troop_loyalty              = 15 #deprecated - this is now derived from other figures###����
slot_troop_player_order_state   = 16 #Deprecated###����
slot_troop_player_order_object  = 17 #Deprecated###����

#troop_player order state are all deprecated in favor of party_order_state. This has two reasons -- 1) to reset AI if the party is eliminated, and 2) to allow the player at a later date to give orders to leaderless parties, if we want that


#Post 0907 changes begin
###troop����
slot_troop_age                 =  18
###troop������ò
slot_troop_age_appearance      =  19

#Post 0907 changes end

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
###troop����Һø�
slot_troop_player_relation     = 22
#slot_troop_player_favor        = 23
slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26 ###troop�ϴ�˵��ʱ��
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28

#Post 0907 changes begin
slot_troop_last_comment_slot   = 29
#Post 0907 changes end

###��ż
slot_troop_spouse              = 30
###����
slot_troop_father              = 31
###ĸ��
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
###δ���δ����
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents
#slot_troop_daughter            = 33
#slot_troop_son                 = 34
#slot_troop_sibling             = 35
###troop׷���Ůʿ��1Ŀ��
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
###troop׷���Ůʿ��2Ŀ��
slot_troop_love_interest_2     = 36
###troop׷���Ůʿ��3Ŀ��
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38
#ways to court -- discuss a book, commission/compose a poem, present a gift, recount your exploits, fulfil a specific quest, appear at a tournament
#preferences for women - (conventional - father's friends)
slot_lady_no_messages          				= 37
slot_lady_last_suitor          				= 38
slot_lord_granted_courtship_permission      = 38

slot_troop_betrothal_time                   = 39 #used in scheduling the wedding

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
slot_troop_trainer_training_fight_won        = 37


slot_lady_used_tournament					= 40


slot_troop_current_rumor       = 45
slot_troop_temp_slot           = 46
slot_troop_promised_fief       = 47   ###troop��ŵ���

slot_troop_set_decision_seed       = 48 #Does not change
slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue
###������һ����������ı�г���ͬ�ĵط����˷��м���ϰ�����Ȼû�����յļ��㣬����ȡ����һЩ���ȫ�־��ߵ�����
###�������ӿ���ʹһЩ����Կ��Ա���ӵ�ȫ���˴�ľ�������������������ʼ��˴���
###��ʱ�������������ϴθ���Ա��NPC��λ��24��48Сʱ�����趨����ֻ�������ⳡ�ϵı仯
###�����Ӿ��в�ͬ��ģ��ʹ�ò�ͬ�����⣬���/�͵Ľ�������ʹ�õ����Ĳ�ۣ�ÿ������


###troop��ı����
slot_troop_intrigue_impatience = 51
#recruitment changes end

#slot_troop_honorable          = 50
#slot_troop_merciful          = 51
###�Ը�����
###lrep_quarrelsome�ñ�� lrep_debauched�ŵ��� lrep_goodnatured������ lrep_martial��ս��
###lrep_upstanding��ֱ�� lrep_selfrighteous������ֱ lrep_cunning�ƻ��� lrep_roguish������

###lrep_adventurousð�յ� lrep_otherworldly����� lrep_conventional��ͳ�� lrep_moralist���µ� lrep_ambitiousҰ�Ĳ�����
slot_lord_reputation_type     		  = 52
slot_lord_recruitment_argument        = 53 #the last argument proposed by the player to the lord
###������ļ�����ĺ�ѡ��
slot_lord_recruitment_candidate       = 54 #the last candidate proposed by the player to the lord

###troop�����Ӫ
slot_troop_change_to_faction          = 55

#slot_troop_readiness_to_join_army     = 57 #possibly deprecate
#slot_troop_readiness_to_follow_orders = 58 #possibly deprecate

# NPC-related constants

#NPC companion changes begin
###troop��������
slot_troop_first_encountered          = 59
###troop�ļ���
slot_troop_home                       = 60

###troop����״̬
slot_troop_morality_state       = 61

tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

###troop��������
slot_troop_morality_type = 62
###�����
tmt_aristocratic = 1
###ƽ�ȵ�
tmt_egalitarian = 2
###�˵�����
tmt_humanitarian = 3
###��ʵ��
tmt_honest = 4
###�ϵ�
tmt_pious = 5

###troop����ֵ
slot_troop_morality_value = 63

###troop�ڶ���������
slot_troop_2ary_morality_type  = 64
###troop�ڶ�����״̬
slot_troop_2ary_morality_state = 65
###troop�ڶ�����ֵ
slot_troop_2ary_morality_value = 66

###npc�й�ϵ��ĳ���
slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 #1 are nobles, 2 are commons

###troop���´���
slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts ��Թ�ӵ��³�ͻ

###troop�����ɫ�Ը��ͻ����
slot_troop_personalityclash_object     = 71
#(0 - they have no problem, 1 - they have a problem)
###troop�����ɫ�Ը��ͻ״̬
slot_troop_personalityclash_state    = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
###troop�����ɫ�Ը��ͻ����2
slot_troop_personalityclash2_object   = 73
###troop�����ɫ�Ը��ͻ2״̬
slot_troop_personalityclash2_state    = 74

###troop�����ɫ�Ը�ƥ�����
slot_troop_personalitymatch_object   =  75
###troop�����ɫ�Ը�ƥ��״̬
slot_troop_personalitymatch_state   =  76

###troop�����ɫ�Ը��ͻ����
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78 #only for companions
slot_troop_discussed_rebellion   = 78 #only for pretenders

#courtship slots
slot_lady_courtship_heroic_recited 	    = 74
slot_lady_courtship_allegoric_recited 	= 75
slot_lady_courtship_comic_recited 		= 76
slot_lady_courtship_mystic_recited 		= 77
slot_lady_courtship_tragic_recited 		= 78



#NPC history slots ###NPC��ʷslots
slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82   ###troop������Ҷ�����ʷ pp_history_dismissed�����

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

slot_troop_custom_banner_bg_color_1      = 85 ###troop�Զ�������
slot_troop_custom_banner_bg_color_2      = 86 ###troop�Զ�������
slot_troop_custom_banner_charge_color_1  = 87 ###troop�Զ�������
slot_troop_custom_banner_charge_color_2  = 88 ###troop�Զ�������
slot_troop_custom_banner_charge_color_3  = 89 ###troop�Զ�������
slot_troop_custom_banner_charge_color_4  = 90 ###troop�Զ�������
slot_troop_custom_banner_bg_type         = 91 ###troop�Զ�������
slot_troop_custom_banner_charge_type_1   = 92 ###troop�Զ�������
slot_troop_custom_banner_charge_type_2   = 93 ###troop�Զ�������
slot_troop_custom_banner_charge_type_3   = 94 ###troop�Զ�������
slot_troop_custom_banner_charge_type_4   = 95 ###troop�Զ�������
slot_troop_custom_banner_flag_type       = 96 ###troop�Զ�������
slot_troop_custom_banner_num_charges     = 97 ###troop�Զ�������
slot_troop_custom_banner_positioning     = 98 ###troop�Զ�������λ��
slot_troop_custom_banner_map_flag_type   = 99 ###troop�Զ������Ĵ��ͼ��ǩ����

#conversation strings -- must be in this order! ###�Ի����������ڱ������ַ�
###troop���
slot_troop_intro 						= 101
###troop�����Ӧ1
slot_troop_intro_response_1 			= 102
###troop�����Ӧ2
slot_troop_intro_response_2 			= 103
###troop��������a
slot_troop_backstory_a 					= 104
###troop��������b
slot_troop_backstory_b 					= 105
###troop��������c
slot_troop_backstory_c 					= 106
###troop���������ӳ�
slot_troop_backstory_delayed 			= 107
###troop����������Ӧ1
slot_troop_backstory_response_1 		= 108
###troop����������Ӧ2
slot_troop_backstory_response_2 		= 109
slot_troop_signup   					= 110
slot_troop_signup_2 					= 111
slot_troop_signup_response_1 			= 112
slot_troop_signup_response_2 			= 113
slot_troop_mentions_payment 			= 114 #Not actually used
slot_troop_payment_response 			= 115 #Not actually used
slot_troop_morality_speech   			= 116
slot_troop_2ary_morality_speech 		= 117
slot_troop_personalityclash_speech 		= 118
slot_troop_personalityclash_speech_b 	= 119
slot_troop_personalityclash2_speech 	= 120
slot_troop_personalityclash2_speech_b 	= 121
slot_troop_personalitymatch_speech 		= 122
slot_troop_personalitymatch_speech_b 	= 123
slot_troop_retirement_speech 			= 124
slot_troop_rehire_speech 				= 125
slot_troop_home_intro           		= 126
slot_troop_home_description    			= 127
slot_troop_home_description_2 			= 128
slot_troop_home_recap         			= 129
###troop����ơ��������npc��γƺ���ң�����ӳ������¡�
slot_troop_honorific   					= 130
slot_troop_kingsupport_string_1			= 131
slot_troop_kingsupport_string_2			= 132
slot_troop_kingsupport_string_2a		= 133
slot_troop_kingsupport_string_2b		= 134
slot_troop_kingsupport_string_3			= 135
slot_troop_kingsupport_objection_string	= 136
slot_troop_intel_gathering_string	    = 137
slot_troop_fief_acceptance_string	    = 138
slot_troop_woman_to_woman_string	    = 139
slot_troop_turn_against_string	        = 140

slot_troop_strings_end 					= 141

###npc��Ӷ�۸�
slot_troop_payment_request 				= 141

#141, support base removed, slot now available

###npc֧�ֹ��״̬
slot_troop_kingsupport_state			= 142
###npc֧�ֹ������
slot_troop_kingsupport_argument			= 143
###npc֧�ֹ�Ҷ���
slot_troop_kingsupport_opponent			= 144
###npc֧�ֹ�ҿ���״̬ 0Ĭ�� 1��Ҫ���� 2��ʾ
slot_troop_kingsupport_objection_state  = 145 #0, default, 1, needs to voice, 2, has voiced

###��������
slot_troop_days_on_mission		        = 150
###��ǰ����
slot_troop_current_mission			    = 151
###����Ŀ��
slot_troop_mission_object               = 152
###npc֧�ֹ������
npc_mission_kingsupport					= 1
###npc�ռ���Ϣ����
npc_mission_gather_intel                = 2
###npc�����ƽ����
npc_mission_peace_request               = 3
###npc��Ѻ�������
npc_mission_pledge_vassal               = 4
###npcѰ��ʶ������
npc_mission_seek_recognition            = 5
###npc����ˮ������
npc_mission_test_waters                 = 6
###npc����������
npc_mission_non_aggression              = 7
###npc�����ܴ��
npc_mission_rejoin_when_possible        = 8

#Number of routed agents after battle ends. ###ս�������·�ɴ�����Ŀ��
###���·��agents
slot_troop_player_routed_agents                 = 146
###�Ѿ�·��agents
slot_troop_ally_routed_agents                   = 147
###�о�·��agents
slot_troop_enemy_routed_agents                  = 148

#Special quest slots ###���������
slot_troop_mission_participation        = 149
mp_unaware                              = 0
mp_stay_out                             = 1
mp_prison_break_fight                   = 2
mp_prison_break_stand_back              = 3
mp_prison_break_escaped                 = 4
mp_prison_break_caught                  = 5

#Below are some constants to expand the political system a bit. The idea is to make quarrels less random, but instead make them serve a rational purpose -- as a disincentive to lords to seek
###������һЩ������������ϵͳһ�㡣����뷨��Ϊ������������������Ϊ���Ե�Ŀ�ġ���Ϊ��ֹ����Ѱ��

###troop����
slot_troop_controversy                     = 150 #Determines whether or not a troop is likely to receive fief or marshalship ###ȷ���Ƿ�һ�������п��ܻ�÷�ػ�Ԫ˧

###troop�������ͣ�δ�ܼ����ӣ����֧�ֵ�ͬ��
slot_troop_recent_offense_type 	           = 151 #failure to join army, failure to support colleague
###troop����Ŀ�꣬���Ǹ�������
slot_troop_recent_offense_object           = 152 #to whom it happened
###troop����ʱ��
slot_troop_recent_offense_time             = 153
###troop��������Ӫ������
slot_troop_stance_on_faction_issue         = 154 #when it happened

###troop������ʧ��
tro_failed_to_join_army                    = 1
###troop֧��ͬ��ʧ��
tro_failed_to_support_colleague            = 2


#CONTROVERSY ###����
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
####��������������ϵ���θ�����ѡ��ģ�ͣ���������ս����������������ǽ�����Ϊ��ͻ���Ը�

#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
####���Ŀ����Ϊ���ǹ��Ķ��ǵ���������Ա������Ժ��һ���������ء����������ڲ���ϵ����ѫ���Ļ��ҡ�Ӣ���ý�壬���кܸߵġ����ۡ����ᱻ����Ϊ��������衱��

#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
###���������ҪӰ���ǣ����ų���һ��������һ���ػ�ԤԼ

#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.
###�ǹؼ��һ�����θ����Ϊ���ṩ�˴��������λ�ļ������磬��ɫ�ĸ߼���������Ķ��֣�����ɫ�߼��������õ�һ���̶��ĺ�ɫҪ�������ԣ�Ү�ͻ������ͽ��ɫ��Ϊ��ɫ�������꣬���������ڹ��������ȥ����ɫ������ɫ�ͺ�ɫ���������������������Ժ�����ڡ�

slot_troop_will_join_prison_break      = 161


troop_slots_reserved_for_relations_start        = 165 #this is based on id_troops, and might change

slot_troop_relations_begin				= 0 #this creates an array for relations between troops
											#Right now, lords start at 165 and run to around 290, including pretenders



########################################################
##  PLAYER SLOTS           #############################���slot
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_spawn_count                        = 39


########################################################
##  TEAM SLOTS             #############################��slot
########################################################

slot_team_flag_situation                       = 0




#Rebellion changes end ###���Ҹı����


# character backgrounds ###��������
cb_noble = 1              ###����
cb_merchant = 2           ###����
cb_guard = 3              ###����
cb_forester = 4           ###����١�����
cb_nomad = 5              ###��������
cb_thief = 6              ###С͵
cb_priest = 7             ###��ʦ

cb2_page = 0              ###
cb2_apprentice = 1        ###ѧͽ
cb2_urchin  = 2           ###��ͯ�������
cb2_steppe_child = 3      ###��ԭ�ĺ���
cb2_merchants_helper = 4  ###���˰���

cb3_poacher = 3           ###͵����
cb3_craftsman = 4         ###����
cb3_peddler = 5           ###С��
cb3_troubadour = 7        ###����ʫ��
cb3_squire = 8            ###����
cb3_lady_in_waiting = 9   ###�ȴ��е�Ů��
cb3_student = 10          ###ѧ��

cb4_revenge = 1           ###����
cb4_loss    = 2           ###��ʧ
cb4_wanderlust =  3       ###������
cb4_disown  = 5           ###���ϳ��˼���
cb4_greed  = 6            ###Ȩ��

#NPC system changes end ###npcϵͳ�ı����
#Encounter types ###��������
enctype_fighting_against_village_raid = 1   ###��ׯϴ��ս��ʱ
enctype_catched_during_village_raid   = 2   ###ץס�ڴ�ׯϴ��


### Troop occupations slot_troop_occupation
##slto_merchant           = 1
###����Ծ��
slto_inactive           = 0 #for companions at the beginning of the game###ͬ������Ϸ�Ŀ�ʼ

###��������
slto_kingdom_hero       = 2

###���ͬ��
slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
###����Ůʿ
slto_kingdom_lady       = 6 #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
###����ܼ�
slto_kingdom_seneschal  = 7
###ǿ����ʿ
slto_robber_knight      = 8
###����Ծ��αװ��
slto_inactive_pretender = 9


stl_unassigned          = -1  ###δ����Ĵ�ׯ
stl_reserved_for_player = -2  ###��������ҵĴ�ׯ
stl_rejected_by_player  = -3  ###��ұ����Ĵ�ׯ

#NPC changes begin
slto_retirement      = 11
#slto_retirement_medium    = 12
#slto_retirement_short     = 13
#NPC changes end

########################################################
##  QUEST SLOTS            #############################����slot
########################################################

slot_quest_target_center            = 1   ###���񴥷�����
slot_quest_target_troop             = 2   ###���񴥷�troop
slot_quest_target_faction           = 3   ###���񴥷���Ӫ
slot_quest_object_troop             = 4   ###����troopĿ��
##slot_quest_target_troop_is_prisoner = 5 ###���񴥷�troop�Ƿ�²
slot_quest_giver_troop              = 6   ###����troop���񣺰� �� �� �� �� ҽ �� {s3}�� �� {s1}
slot_quest_object_center            = 7   ###����Ŀ������
slot_quest_target_party             = 8   ###���񴥷�����
slot_quest_target_party_template    = 9   ###���񴥷�����ģ��
slot_quest_target_amount            = 10  ###���񴥷�����
slot_quest_current_state            = 11  ###����ǰ״̬
slot_quest_giver_center             = 12  ###������������
slot_quest_target_dna               = 13  ###���񴥷�dna
slot_quest_target_item              = 14  ###���񴥷���
slot_quest_object_faction           = 15  ###����Ŀ����Ӫ

slot_quest_target_state             = 16  ###���񴥷�״̬
slot_quest_object_state             = 17  ###����Ŀ��״̬

slot_quest_convince_value           = 19  ###����˵��ֵ
slot_quest_importance               = 20  ###������Ҫ��
slot_quest_xp_reward                = 21  ###�����齱��
slot_quest_gold_reward              = 22  ###�����Ǯ����
slot_quest_expiration_days          = 23  ###�����ֹ����
slot_quest_dont_give_again_period   = 24  ###��Ҫ�ٴθ�������ʱ��
slot_quest_dont_give_again_remaining_days = 25  ###��Ҫ�ٴθ�������ʣ�µ�����

slot_quest_failure_consequence      = 26  ###����ʧ�ܵĺ��
slot_quest_temp_slot      			= 27      ###������ʱslot

#add by llqs
slot_quest_eastgoddess               = 28

########################################################
##  PARTY TEMPLATE SLOTS   #############################����ģ��slot
########################################################

# Ryan BEGIN
slot_party_template_num_killed   = 1        ###����ģ��ɱ����
slot_party_template_lair_type    	 	= 3     ###����ģ�泲Ѩ����
slot_party_template_lair_party    		= 4   ###����ģ�泲Ѩ����
slot_party_template_lair_spawnpoint     = 5 ###����ģ�泲Ѩˢ���


# Ryan END


########################################################
##  SCENE PROP SLOTS       #############################��������slot
########################################################

###�������ߴ򿪻��ǹر�slot
scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
scene_prop_slots_end                = 6

########################################################
rel_enemy   = 0 ###����
rel_neutral = 1 ###����
rel_ally    = 2 ###�Ѿ�


#Talk contexts ###̸�������Ļ���
tc_town_talk                  = 0   ###����̸
tc_court_talk   	      	  = 1     ###��������̸
tc_party_encounter            = 2   ###��������
tc_castle_gate                = 3   ###�Ǳ�����
tc_siege_commander            = 4   ###����ָ�ӹ�
tc_join_battle_ally           = 5   ###�����Ѿ�ս��
tc_join_battle_enemy          = 6   ###�������ս��
tc_castle_commander           = 7   ###�Ǳ�ָ�ӹ�
tc_hero_freed                 = 8   ###�ͷ�Ӣ��
tc_hero_defeated              = 9   ###սʤӢ��
tc_entering_center_quest_talk = 10  ###������������̸
tc_back_alley                 = 11  ###�ص�С��
tc_siege_won_seneschal        = 12  ###����Ӯ�ùܼ�
tc_ally_thanks                = 13  ###�Ѿ��л
tc_tavern_talk                = 14  ###�ƹݽ�̸
tc_rebel_thanks               = 15  ###�췴�߸�л
tc_garden            		  = 16      ###��԰
tc_courtship            	  = 16    ###��
tc_after_duel            	  = 17    ###�ھ���
tc_prison_break               = 18  ###Խ��
tc_escape               	  = 19    ###����
tc_give_center_to_fief        = 20  ###����
tc_merchants_house            = 21  ###���˷���


#Troop Commentaries begin ###troop���ۿ�ʼ
#Log entry types ###��־��Ŀ����
#civilian ###ƽ��

###��ׯ�Ѳ��¼���־
logent_village_raided            = 1
###��ׯ�����¼���־
logent_village_extorted          = 2
###��ڨ�����¼���־
logent_caravan_accosted          = 3 #in caravan accosted, center and troop object are -1, and the defender's faction is the object ###�ڴ��񳵴�ڨ�����ĺͲ��ӵĶ�����1���ͺ�������ϵ�Ķ���
###���й����¼���־
logent_traveller_attacked        = 3 #in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object ###�ڹ�������Դ��Ŀ�ĵص����У������ġ�����Ķ��󣬺͹����ߵ���ϵ�Ķ���

###����ũ���¼���־
logent_helped_peasants           = 4

###����ó���¼���־
logent_party_traded              = 5

logent_castle_captured_by_player              = 10  ###�Ǳ���������¼���־
logent_lord_defeated_by_player                = 11  ###�����������¼���־
logent_lord_captured_by_player                = 12  ###������������¼���־
logent_lord_defeated_but_let_go_by_player     = 13  ###���������ҵ���������¼���־
logent_player_defeated_by_lord                = 14  ###��Ҵ�������¼���־
logent_player_retreated_from_lord             = 15  ###��Ҵ����������¼���־
logent_player_retreated_from_lord_cowardly    = 16  ###��Ҵ���С���������¼���־
logent_lord_helped_by_player                  = 17  ###������������¼���־
logent_player_participated_in_siege           = 18  ###��Ҳ��빥���¼���־
logent_player_participated_in_major_battle    = 19  ###��Ҳ�����Ҫ��ս���¼���־
logent_castle_given_to_lord_by_player         = 20  ###����ҳǱ��¼���־

logent_pledged_allegiance          = 21   ###��ŵЧ���¼���־
logent_liege_grants_fief_to_vassal = 22   ###��ظ������¼���־


logent_renounced_allegiance      = 23   ###����Ч���¼���־

logent_player_claims_throne_1    		               = 24 ###��������λ1�¼���־
logent_player_claims_throne_2    		               = 25 ###��������λ2�¼���־


logent_troop_feels_cheated_by_troop_over_land		   = 26     ###troop�о���ƭ��Ϊtroop����¼���־
logent_ruler_intervenes_in_quarrel                     = 27 ###���Ԥ�߶��¼���־
logent_lords_quarrel_over_land                         = 28 ###��������Ϊ����¼���־
logent_lords_quarrel_over_insult                       = 29 ###��������Ϊ�����¼���־
logent_marshal_vs_lord_quarrel                  	   = 30   ###Ԫ˧���������¼���־
logent_lords_quarrel_over_woman                        = 31 ###������ΪŮʿ���¼���־

logent_lord_protests_marshall_appointment			   = 32       ###��������Ԫ˧�����¼���־
logent_lord_blames_defeat						   	   = 33             ###����ָ��ʧ���¼���־

logent_player_suggestion_succeeded					   = 35         ###��ҽ���ɹ��¼���־
logent_player_suggestion_failed					       = 36         ###��ҽ���ʧ���¼���־

logent_liege_promises_fief_to_vassal				   = 37         ###��ŵ���������¼���־

logent_lord_insults_lord_for_cowardice                 = 38 ###������������ų���¼���־
logent_lord_insults_lord_for_rashness                  = 39 ###�����������������¼���־
logent_lord_insults_lord_for_abandonment               = 40 ###�����������������¼���־
logent_lord_insults_lord_for_indecision                = 41 ###����������������Ѷ��¼���־
logent_lord_insults_lord_for_cruelty                   = 42 ###�����������������¼���־
logent_lord_insults_lord_for_dishonor                  = 43 ###�������������������¼���־




logent_game_start                           = 45 ###��Ϸ��ʼ�¼���־
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

###���¼���־������һֱ�ǲ����ߣ����������troop����
#logent courtship - lady is always actor, suitor is always troop object
###Ůʿ������������¼���־
logent_lady_favors_suitor                   = 51 #basically for gossip ###����˵�л���
###Ůʿ��Ӧ�����δ������Ϊѡ���¼���־
logent_lady_betrothed_to_suitor_by_choice   = 52
###Ůʿ��Ӧ�����δ������Ϊ�����¼���־
logent_lady_betrothed_to_suitor_by_family   = 53
###Ůʿ�ܾ�������¼���־
logent_lady_rejects_suitor                  = 54
###Ůʿ���׾ܾ�������¼���־
logent_lady_father_rejects_suitor           = 55
###Ůʿ��������¼���־
logent_lady_marries_lord                    = 56
###Ůʿ������˽���¼���־
logent_lady_elopes_with_lord                = 57
###Ůʿ������߾ܾ�
logent_lady_rejected_by_suitor              = 58
###Ůʿ��Ӧ�����δ������Ϊѹ���¼���־
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip ###���Ϊ����

###Ůʿ������ߴ��ƶ����¼���־
logent_lady_and_suitor_break_engagement		= 60
###Ůʿ������߽���¼���־
logent_lady_marries_suitor				    = 61

###��������Ůʿ�����¼���־
logent_lord_holds_lady_hostages             = 62
###��ս��������ʧ���¼���־
logent_challenger_defeats_lord_in_duel      = 63
###������ս���������¼���־
logent_challenger_loses_to_lord_in_duel     = 64

###��ҴӴ�ׯ͵ţ�¼���־
logent_player_stole_cattles_from_village    = 66

###����ϣ��ս���ص�
logent_party_spots_wanted_bandits           = 70

###�߾�͵ţ�¼���־
logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
###�߾���������¼���־
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
###�߾�ɱ�������¼���־
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
###�߾�Ű���¼���־
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord   = 78


logent_policy_ruler_attacks_without_provocation 			= 80
logent_policy_ruler_ignores_provocation         			= 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon        			= 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction

logent_player_faction_declares_war						    = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity		    = 91
logent_faction_declares_war_to_regain_territory 		    = 92
logent_faction_declares_war_to_curb_power					= 93
logent_faction_declares_war_to_respond_to_provocation	    = 94
logent_war_declaration_types_end							= 95


#logent_lady_breaks_betrothal_with_lord      = 58
#logent_lady_betrothal_broken_by_lord        = 59



#lord reputation type, for commentaries ###����������������
#"Martial" will be twice as common as the other types ###��ս�Ľ�Ϊ�������͵�����

###lrep_quarrelsome�ñ��  lrep_debauched�ŵ���          lrep_goodnatured������   lrep_martial��ս��
###lrep_upstanding��ֱ��   lrep_selfrighteous������ֱ    lrep_roguish������        lrep_cunning�ƻ���
###lrep_adventurousð�յ� lrep_otherworldly����� lrep_conventional��ͳ�� lrep_moralist���µ� lrep_ambitiousҰ�Ĳ�����

lrep_none           = 0
###����ĵ���̫ͬ���ʡ���������ʨ���������ƽ���ʮ�����ͷ����о�
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
###����ģ��������׵ģ��е�ƫִ�����ܳ嶯���������޲���Graves����ԣ�һЩ���˹����������
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
###��Ѫ���̻����ײе�-���磬��������������ľ���ݴ�ά�������򲼣���Ȼ������ֱ���෴��������������룩
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
###��Ѫ�ģ���ʵ�ģ������µģ���·��˹������˹����Akbar Khan���������հ���������ɳ��
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
###����ģ������µģ��б���-���翨���������������˹���߶�
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
###����ģ��ʴȵģ�Ҳ���е�̫������һ���ܺõľ�������������һЩ�������ʷ�ϵ�����Ҳ�?��Ϊ���ȱ�������������쵼��������������
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
###˵�̣��ʴȵģ���ʵ�ģ����粮�ɵ�Cornwell�İ����׵£��������ۣ������ն�DIN��Sher Shah����
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

###���ڹ��?�ر���ǰ��ͬ�顣��ͼ���Ϊ����
lrep_roguish        = 8 #used for commons, specifically ex-companions. Tries to live life as a lord to the full
###������ ���ڹ��?�ر���ǰ��ͬ�顣�ܶ�����ͼ�������
lrep_benefactor     = 9 #used for commons, specifically ex-companions. Tries to improve lot of folks on land
###������ ���ڹ��?�ر���ǰ��ͬ�顣��ͼ����޶ȵĲ��ص�����Ǳ��
lrep_custodian      = 10 #used for commons, specifically ex-companions. Tries to maximize fief's earning potential


#lreps specific to dependent noblewomen
###ƽ���� ������Լ��SATC����1-2�����ܴ���������͹���
lrep_conventional    = 21 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
###��ð�յ���Ƥ�ġ�Ȼ���������ζ����ϲ�����к����ԣ�Ҳ��������ð�ա�Ȼ�������͹��帾Ů�����Ǻ���ģ�����Щ��ͼ���������˸��Ƿ�ë��ǣ�����õ�ͬ��һ�������ǰ�ű�
lrep_adventurous     = 22 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
###�����׵� �������������壬�������塣
lrep_otherworldly    = 23 #Prone to mysticism, romantic.
###�����ĵ� ��˰׷���
lrep_ambitious       = 24 #Lady Macbeth
###���¼� ֱ������ˡ����Ե�Чnobless��æ������Ϊ��ĵ��´�ͳ�Ľ�ɫ�������ء�������ɢ�Ŀ���˹���ȱ���
lrep_moralist        = 25 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa



###һ�����ӵ�ϵͳ���԰������µ�����
#a more complicated system of reputation could include the following...

#�ɹ��벻�ɹ��ġ������
#successful vs unlucky -- basic gauge of success
#�����������Ҳ�?�Ǳ�Ҫ��
#daring vs cautious -- maybe not necessary
#����/��/˼���벻��������ɫ��ִ����Ϊ���ⲿ���롣δ�ܲ�׽������ϲ�������򲼣������ԣ�Ҳ�?���Ǻõ�NPC
#honorable/pious/ideological vs unscrupulous -- character's adherance to an external code of conduct. Fails to capture complexity of people like Aurangzeb, maybe, but good for NPCs
#������/��������ͳ/����ͳ�Ŀ�����������һ���Ӽ������ض����ⲿ������Ա���һ����ǩ��
#(visionary/altruist and orthodox/unorthodox could be a subset of the above, or the specific external code could be another tag)
#�󷽡��ҳ������/����������ɫ�����θе�����ĸ��ˣ�����֮��Ĺ�ϵ�Ļ��ϡ����ҳϵľ�ӣ���
#generous/loyal vs manipulative/exploitative -- character's sense of duty to specific individuals, based on their relationship. Affects loyalty of troops, etc
#�ʴ���п����顢������ͬ�顪��/��ɫ��һ�������ϵġ�Sher Shah�����޼ɵ����ʴȵ����ӣ�������һ���̶��ϣ���
#������ǳ��桪�����ﱾ������ϰ�ס��ǳ���Ҫ�ģ����ʱ��
#merciful vs cruel/ruthless/sociopathic -- character's general sense of compassion. Sher Shah is example of unscrupulous and merciful (the latter to a degree).
#dignified vs unconventional -- character's adherance to social conventions. Very important, given the times


#########################������5��ʫ��
###ǿ���Ŀ�������������
courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
###Ų�������ŮӢ��
courtship_poem_heroic      = 2 #Norse sagas with female heroines
###�ص��ڶг�������contrasto��������ѧУ��̣�
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire)
###�շ�ʫ�衣����
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
###��Ů����Ϊһ����������������õ������������ĳǱ�Χ��
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

#courtship gifts currently deprecated ###Ŀǰʹ�õ������ʫ��


#Troop Commentaries end ###troop���۽���



tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end   = "trp_tutorial_archer_1"

#Walker types:
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers = 8
town_walker_entries_start = 32

reinforcement_cost_easy = 600
reinforcement_cost_moderate = 450
reinforcement_cost_hard = 300

###ͨ�зѹ�˰����Ч��Ϊ72Сʱ
merchant_toll_duration        = 72 #Tolls are valid for 72 hours

###������Ӣ��ս�����ܵıȽ�ֵ
hero_escape_after_defeat_chance = 70


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

bandits_begin = "trp_bandit"
bandits_end = "trp_black_khergit_horseman"

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = pretenders_begin

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = kings_begin

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin
#"active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
#If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

soldiers_begin = "trp_farmer"
soldiers_end = "trp_town_walker_1"

#Rebellion changes

##rebel_factions_begin = "fac_kingdom_1_rebels"
##rebel_factions_end =   "fac_kingdoms_end"

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = active_npcs_end
#Rebellion changes

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = "trp_kingdom_heroes_including_player_begin"

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = "trp_watchman"
mercenary_troops_end = "trp_mercenaries_end"

multiplayer_troops_begin = "trp_swadian_crossbowman_multiplayer"
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_ai_troops_begin = "trp_swadian_crossbowman_multiplayer_ai"
multiplayer_ai_troops_end = multiplayer_troops_begin

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_multi_scene_1"
multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_flag_projections_begin = "mesh_flag_project_sw"
multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_sw_miss"
multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_multi_game_types_end"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_6"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_11"
mayor_quests_end_2   = "qst_blank_quest_11"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_16"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

player_realm_quests_begin = "qst_resolve_dispute"
player_realm_quests_end = "qst_blank_quest_1"

player_realm_quests_begin_2 = "qst_blank_quest_26"
player_realm_quests_end_2 = "qst_blank_quest_26"

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end   = "p_salt_mine"

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_Bridge_1"

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

spawn_points_begin = "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

swadian_merc_parties_begin = "p_town_1_mercs"
swadian_merc_parties_end   = "p_town_8_mercs"

vaegir_merc_parties_begin  = "p_town_8_mercs"
vaegir_merc_parties_end    = "p_zendar"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

training_gound_trainers_begin    = "trp_trainer_1"
training_gound_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_1"
town_walkers_end = "trp_village_walker_1"

village_walkers_begin = "trp_village_walker_1"
village_walkers_end   = "trp_spy_walker_1"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

startup_merchants_begin = "trp_swadian_merchant"
startup_merchants_end = "trp_startup_merchants_end"

num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_smoked_fish"
food_end = "itm_siege_supply"
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_sumpter_horse"
horses_end = "itm_arrows"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_wooden_shield"
ranged_weapons_begin = "itm_darts"
ranged_weapons_end = "itm_torch"
armors_begin = "itm_leather_gloves"
armors_end = "itm_wooden_stick"
shields_begin = "itm_wooden_shield"
shields_end = ranged_weapons_begin

# Banner constants

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_f21"

arms_meshes_begin = "mesh_arms_a01"
arms_meshes_end_minus_one = "mesh_arms_f21"

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end = "spr_banner_a"

custom_banner_map_icons_begin = "icon_custom_banner_01"
custom_banner_map_icons_end = "icon_banner_01"

banner_map_icons_begin = "icon_banner_01"
banner_map_icons_end_minus_one = "icon_banner_136"

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end_minus_one = "spr_banner_f21"

khergit_banners_begin_offset = 63
khergit_banners_end_offset = 84

sarranid_banners_begin_offset = 105
sarranid_banners_end_offset = 125

banners_end_offset = 136

# Some constants for merchant invenotries
merchant_inventory_space = 30
num_merchandise_goods = 40

num_max_river_pirates = 25
num_max_zendar_peasants = 25
num_max_zendar_manhunters = 10

num_max_dp_bandits = 10
num_max_refugees = 10
num_max_deserters = 10

num_max_militia_bands = 15
num_max_armed_bands = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants = 25

num_max_frightened_farmers = 50
num_max_undead_messengers  = 20

num_forest_bandit_spawn_points = 1
num_mountain_bandit_spawn_points = 1
num_steppe_bandit_spawn_points = 1
num_taiga_bandit_spawn_points = 1
num_desert_bandit_spawn_points = 1
num_black_khergit_spawn_points = 1
num_sea_raider_spawn_points = 2

peak_prisoner_trains = 4
peak_kingdom_caravans = 12
peak_kingdom_messengers = 3


# Note positions
note_troop_location = 3

##########################ս��ս��
#battle tactics
btactic_hold = 1            ###����
btactic_follow_leader = 2   ###����
btactic_charge = 3          ###���
btactic_stand_ground = 4    ###վ��ԭ��

#default right mouse menu orders ###Ĭ�ϵ�����Ҽ�˵�����
cmenu_move = -7     ###�ƶ�
cmenu_follow = -6   ###����

# Town center modes - resets in game menus during the options ###�����ĵ�ģʽ��������Ϸ�˵��е�ѡ��
tcm_default 		= 0   ###Ĭ��
tcm_disguised 		= 1 ###Ǳ��
tcm_prison_break 	= 2 ###Խ��
tcm_escape      	= 3 ###����


# Arena battle modes ###������ս��ģʽ
#abm_fight = 0
abm_training = 1    ###ѵ��
abm_visit = 2       ###����
abm_tournament = 3  ###������

# Camp training modes ###ѵ��Ӫ��ѵ��ģʽ
ctm_melee    = 1  ###��ս
ctm_ranged   = 2  ###Ͷ��
ctm_mounted  = 3  ###����
ctm_training = 4  ###���

# Village bandits attack modes ###��ׯǿ������ģʽ
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 5
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 10
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 25
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 60
arena_grand_prize = 250


#Additions ###���ӵ�
price_adjustment = 25 #the percent by which a trade at a center alters price ###������ó�׸ı�۸�

fire_duration = 4 #fires takes 4 hours ###������Ҫ4Сʱ

###��ĳɾ�
#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

###������ɾͣ�
#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

###��ͼ��سɾ�
#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

###���ε���ɾ�
#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

###����ɾ�
#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

###�ۺϳɾ�
#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

ACHIEVEMENT_MAN_HANDLER = 75,
ACHIEVEMENT_GIRL_POWER = 76,
ACHIEVEMENT_QUEEN = 77,
ACHIEVEMENT_EMPRESS = 78,
ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
ACHIEVEMENT_LADY_OF_THE_LAKE = 80,
