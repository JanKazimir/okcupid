## Features to Use:


_ADMIN & DEMO_ Let's ignore race it's too complicated
caseid_new : id number or subject 
w1_section : in rel or not?

RESPONDANT DEMO
w1_ppage (age)
w1_ppgender : gender
w1_ppeducat (education categories)
w1_partyid7 : party identification (7 categories)
w1_ppmsacat : (metro residence)

PARTNER DEMO (not for clustering)
w1_q9 : partner's age
w1_q10 : partner educations !!needs reworking !!
w1_q12 (partner’s political party ID)


COUPLE:
w1_same_sex_couple : gay couple or not 
w1_ppincimp_cat :  HH income in 4 categories


_WEIGHTS_ 
w3_Weight : Qualified respondents from 2017 Genpop sample, N=1539
w3_Weight_LGB : Qualified LGB respondents across all samples, N=249
w3_combo_weight:  wave 3 combined weights taking LGB oversample into account
w3_attrition_adj_weight: w3_combo_weight adjusted for attrition from 2017 to 2022

w2_weight_genpop: Qualified respondents from 2017 Genpop sample, n=1866
w2_weight_LGB: Qualified LGB respondents across all samples, n=324
w2_combo_weight: combo of w2_weight_LGB and w2_weight_genpop, weighting the lgb down by 3.59
w2_attrition_adj_weights : inverse of prob of w2 answer times old w2 weight, inv_est_prob_wave2_complete*w2

w1_weight_combo :  weight that combines all LGB subjects weighted down, with gen pop
w1_weight_combo_freqwt: frequency weight version of weight_combo



**HOW MET**
w1_q32 : online + how and not online
!! needs work!

_ONLINE:_
w1_q24_met_online : doesn't match the others.
w1_either_internet_adjusted : highest number. seems like the best.
w1_q32 : how online? NO, or yes + details almost matches the W1_either_internet

_OFFLINE:_
w1_q24_met_through_family, 
w1_q24_met_through_friend, 
w1_q24_met_through_as_nghbrs, 
w1_q24_met_as_through_cowork



**REL QUALITY**

_TIME_
w1_year_fraction_relstart : one number for "when relationship started" = w1_q21b_year+(( w1_q21b_month-0.5)/12) 
w1_relate_duration_in2017_years

w1_q21b_year : Year romantic relationship began
w1_q21b_month: month romantic relationship began


_BREAKUP_
w1_q21e_year :  year of breakup
w1_q21e_month : month of breakup
w1_q21f_year : year partner died
w1_q21f_month : month partner died

w1_who_breakup_combo (who wanted the breakup)

_REL DURATION_

w2_relationship_duration

w3_month_rel_started months after jan 1960 when relationship started for rels active in w3, from q21b
w3_relationship_duration_mos : duration in months of relationships still intact at wave 3
w3_relationship_duration_yrs : duration in years of relationships still intact at wave 3

_QUALITY_
w1_max_relation_status
w1_weekly_sex_frequency



_ANDREY_
w1_q34   -> w2_rel_qual_combo -> w3_rel_qual
w1_relate_duration_in2017_years -> w2_relationship_duration -> w3_relationship_duration_years
w1_q19 -> w2_cohab -> w3_cohab
w1_married -> w2_married -> w3_married


**Final selection for clustering:**
needs work on q32!
w1_partnership_status = collapse several others. Let's not use it.
df_cluster = df[['caseid_new', 'w1_section', 'w1_ppage','w1_ppgender','w1_ppeducat','w1_partyid7','w1_ppmsacat', 'w1_same_sex_couple','w1_ppincimp_cat','w1_q32','w1_year_fraction_relstart','w1_max_relation_status','w1_weekly_sex_frequency', 'w1_q34', 'w1_relate_duration_in2017_years', 'w1_q19', 'w1_married']]


Imporved with andrey:
df_cluster = df[['caseid_new', 'w1_section', 'w1_ppage','w1_ppgender','w1_ppeducat','w1_partyid7','w1_ppmsacat', 'w1_same_sex_couple','w1_ppincimp_cat','w1_q32','w1_max_relation_status','w1_weekly_sex_frequency', 'w1_q34', 'w1_relate_duration_in2017_years', 'w1_q19', 'w1_married']]
