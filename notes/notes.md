## New notes
The modeling from Andrey seems solid. I can't see many flaws for now. I want to do it too, but we have a presentation to do, so there's that. 
I want to do something productive. 

What could be done, aside from what has been done already.

So what should i do ? 
I can focus on the presentation. Find interesting thing to talk about. 

I want to do some coding, some clustering and ML. It's a lot of work, and we don't have much time. I could tweak Andrey. 
I want to understand and visualize the clusters a bit better, that would be nice. 


**Notes to Andrey**: forgot to include party id. Small detail. We could use see if we have a difference when we include it. 



#### What could be usefull : 
- see the clusters somehow. 
- start writing the presentation
- 

- We have the predictors of rel stab : cluster
What predicts relationship stability, by relationship time.
Which is to say, what predicts a relationship that last more than 1 year? More than 3? More than 5? More than 10? 20? 30+?
This is interesting actually.



Could we power bi something together? maybe see something interactively? maybe reproduce the way people met through time, but more condensed?

_QUESTIONS_: 
- Who wants to break up more? men or women?
- What advice to give the dating website? 

- Does similarity matter?
Small age difference, same salaries, political leanings, education, etc...

- Effect of kids on sex.




# Old notes


Columns that do no start with w1, w2, or w3:
['caseid_new', 'xpartner_type_cohab', 'yr_breakup_combo', 'change_in_rel_quality_w1w2']

xpartner_type_cohab
 byte %33.0g xpartner_type_cohab
 partnerships status at w1 for w2
 respondents based on
 xpartner_type and xcohab 


yr_breakup_combo:
 the year in which the relationship broke, 

change_in_rel_quality_w1w2 =w2_rel_qual_combo -w1_q34 
I guess that's the change in relationship quality between wave 1 and 2. 

## To do
divide data
Clean data
PCA (Principal Component Analysis) : this boils down the columns into components. instead of looking at 300 columns, the math lumps them in groups, that are then used for the clustering. This means that to understand the components, we have to look back at the original data to understand it. after




### What am i trying to do then?
I don't even know. 
Cleaning the data is the work. What is needed? 
What are the 


## My questions
how to handle categorical that are already divided one hot?


### Column work For Wave 2:
w2_surveyed : either yes or no. If no, drop, it's an empty record.




#### To change


## How people met VS relationship stability:

Rows: only use people who have answered in all 3 waves.

Columns:
survey sections : section w1_section : (partenered, never partnerd, etc..)


**KEEP:**
basic demo age, race, education gender, sexual orientation, 
Maybe the same for the partner too?.?


**DEMO**
w1_ppgender : gender
w1_ppincimp byte %8.0g PPINCIMP Household Income
w1_ppincimp_cat byte %10.0g w1_ppincimp_cat w1 ppincimp in 4 categories
w1_same_sex_couple
w1_same_sex_couple_gender
w1_ppmarit : marital status

w1_section : section 1: partnered adults, section 2: adults with past partners, never partnered: not surveyed in wave 1 but included for backround vars and follow-up




**Q24** : how met
summaries or recaps:
w1_q24_met_online
w1_either_internet_adjusted : met online, combo of q24 and q32


w1_how_met_online interp of w1_q24 if either_internet_adjusted==1
w1_q32 : did you use an internet service to meet? summary column


details : not relevant
w1_q24_metonline_no_phone_apps : met online excluding phone



To collapse for q24: 
met through
- relation : friend, coworker, family, intermediary, neighbour etc... 
  - w1_q24_R_cowork, w1_q24_R_friend, w1_q24_R_family, w1_q24_R_sig_other, w1_q24_R_neighbor, w1_q24_P_cowork, w1_q24_P_friend, w1_q24_P_family, w1_q24_P_sig_other, w1_q24_P_neighbor, w1_q24_I_cowork, w1_q24_I_friend, w1_q24_I_family, w1_q24_I_sig_other, w1_q24_I_neighbor
summary:
w1_q24_met_through_family, w1_q24_met_through_friend, w1_q24_met_through_as_nghbrs, w1_q24_met_as_through_cowork

- place : work, church, school, military, curstomer, bar-restaurant, 
    - w1_q24_school, w1_q24_college, w1_q24_mil, w1_q24_church, w1_q24_vol_org , w1_q24_customer, w1_q24_bar_restaurant, w1_q24_public, w1_q24_vacation, w1_q24_singles_serve_nonint, w1_q24_work_neighbors,  
- event : party, 
  - w1_q24_party, w1_q24_blind_date, w1_q24_business_trip
- internet: internet dating, internet non-dating, 
- w1_q24_met_online : (all kinds)
  - w1_q24_internet_dating
  - w1_q24_internet_soc_network, w1_q24_internet_game, w1_q24_internet_chat, w1_q24_internet_org, 

w1_q24_summary_all_codes : summary of all codes from above. ???

w1_q32 Q32 did you use an Internet service
to meet partner?
+

w1_q32_met_online_phone_apps


**later waves**:

**Time of meetings:**
w3_Q21A_year : in what Year did you first meet partner_name?
w3_Q21A_month : [Month] In what Year and Month did you first meet [Partner_Name]?
w3_Q21B_year: [Year] In what year and month did your romantic relationship with [Partner_Name] begin?
w3_Q21B_month : [Month] In what year and month did your romantic relationship with [Partner_Name] begin?


w3_Q21C_year int %8.0g [Year] In what year and month did
you first live together with
[Partner_Name]?
w3_Q21C_month byte %9.0g months [Month] In what year and month
did you first live together
with [Partner_Name]?
w3_Q21D_year int %8.0g [Year] In what Year and Month did
you marry [Partner_Name]?
w3_Q21D_month byte %9.0g months [Month] In what Year and Month
did you marry [Partner_Name]?

_Break up_
w3_Q21E_year int %8.0g year of breakup new relationship
How Couples Meet and Stay Together public data v 2.2 codebook Page 7
reported in w3
w3_Q21E_month byte %9.0g months month of breakup new relationship
reported in w3


_Durations_
w3_month_rel_started months after jan 1960 when relationship started for rels active in w3, from q21b
w3_relationship_duration_mos : duration in months of relationships still intact at wave 3
w3_relationship_duration_yrs : duration in years of relationships still intact at wave 3


**Q32** : rel stability, quaity


w1_q34 byte %9.0g Q34 how would you describe the
quality of your relationship
with partner?
w1_q34_reduced byte %24.0g w1_q34_reduced
w1_q34 with collapsed categories



w1_how_met_online : interp of w1_q24 if either_internet_adjusted==1
w1_max_relation_status : highest status this relationship has achieved


w1_age_when_met float
w1_time_from_met_to_rel
w1_year_fraction_first_cohab
w1_time_from_rel_to_cohab

w1_weekly_sex_frequency

durations:
w1_year_fraction_met = = w1_q21a_year+(( w1_q21a_month-0.5)/12)
w1_year_fraction_relstart = w1_q21b_year+(( w1_q21b_month-0.5)/12)

Extra
w1_sex_frequency : frequency of sex

w1_otherdate byte %8.0g W6_OTHER * In the past year, have you ever
met someone for dating, for
romance, or for sex
w1_how_many byte %105.0g W6_HOW_M * How many Different people besides
[Partner name] have you met for
dating, or romance, or sex in the
past year?

w1_q19 byte %8.0g Q19 Are you currently living with
[partner name]?
w1_q20 byte %8.0g Q20 ever lived with partner?


w1_q21a_year int %8.0g year subject first met partner
w1_q21a_month byte %9.0g Q21A_MON month subject first met partner

**later waves**:
w3_rel_qual
w3_sex_frequency
w3_weekly_sex_frequency
w3_how_many
w3_p_monogamy
w3_monogamy
w3_relationship_end_combo
w3_breakup_year float
w3_breakup_month
w3_partner_passaway_year
w3_partner_passaway_month
w3_new_relationship






**Changes**: 
change_in_rel_quality_w1w2
w3_relationship_end_combo
w1w2_sex_freq_diff




WAVES:

_Relevant:_

w1_otherdate_all
byte %105.0g W6_OTHER In past yr have you met anyone
for dating romance or sex (not incl current partner?)
w1_how_many_all byte %120.0g W6_HOW_M how many ppl did you meet (not
including current partner if
partnered) last yr
w1_otherdate_app_all
byte %106.0g w1_otherdate_app
not incl current partner (if
partnered) did you use phone
app last year to meet someone?
w1_how_many_app_all
byte %119.0g W6_HOW_M how many ppl did you meet (not
including partner) last year
through phone apps?
w1_q40 app_list which phone app do you use most?

w1_number_people_met
float %8.0g based on w1_how_many_all and
w1_otherdate_all

w1_time_from_rel_to_cohab
float %9.0g year_fraction_first_cohab-
year_fraction_relstart, neg
reset to zero

w1_weekly_sex_frequency
float %9.0g weekly sex w partner based on
w1_sex_frequency
w1w2_sex_freq_diff
float %9.0g diff in weekly sex frequency =
w2_weekly_sex_frequency-
w1_weekly_sex_frequency


**drop**
**basic demography :** 
w1_ppethm (race/ethnicity)
w1_ppincimp (HH income)
w1_ppreg9 (US region)
w1_ppmsacat (metro residence)
w1_ppwork (employment status)
w1_PPT01, w1_PPT25, w1_PPT612,
w1_PPT1317, w1_PPT18OV (# of
children in the HH of different ages)
w1_partyid7 (political party
affiliation)
w1_ppp20071 (born-again status)
w1_ppp20072 (religious service
attendance)
w1_q14 (mother’s education)
w1_q15a1 (country where grew up)
w1_q17 (times married)
w1_q16 (number of relatives seen
each month)
w1_attraction (gender of attraction)
w1_identity_all_modified see also
p17_pppa_lgb (sexual identity)
w1_outness_all (LGB outness)
w1_otherdate_all (did subject meet
any new partners in past 12 months
[and if partnered, any new partners
besides main partner])?
w1_how_many_all (how many new
partners in past 12 months)
political movement affiliations from
p17_ppp10206 (tea party affiliation)
to p17_pppa1705 (Black Lives
Matter


**Basic demography of partners**
w1_q4 (partner gender)
w1_q9 (partner age)
w1_q6a (partner Hispanicity)
w1_q6b (partner race)
w1_q10 (partner education)
w1_q11 (partner’s mother’s
education)
w1_q12 (partner’s political party ID)


**Basic demography of couples** 
(subject
and partner). For most timing
variables, month is also available.
Note: this is not a complete list!

w1_same_sex_couple (same-sex ID)
w1_q19 (cohabiting w partner)
w1_q20 (ever lived w partner)
w1_married
w1_sex_frequency
month as well as year is available for
almost all timing variables:
w1_q21a_year (year first met partner)
w1_q21b_year (year relationship
began)
w1_q21c_year (year first lived w
partner)
w1_q21d_year (year married partner)
w1_q21e_year (year broke up w
partner)
w1_q21f_year (year partner died)
w1_q23 (who earned more)
w1_q24* (how couples met coded
from text answers)
w1_q32 (how met closed-ended)
w1_q34 (relationship quality)
w1_who_breakup_combo (who
wanted the breakup)
w1_partnership_status (relationship
status at w1)
w1_relationship_end_nonmar and
w1_relationship_end_mar (how past
relationships ended)
w1_relate_duration_in2017_years
(relationship duration in years for
current relationships)



COVID-related variables
w2_coronavirus_effect_combo (is
relationship better or worse during
the pandemic?)
w2cov* (a series of variables coded
from open-ended answers about how
the pandemic affected subjects’
primary relationships)
w2_pandemic_income_combo (has
income gone up or down during the
pandemic?)
w2_app_use_combo (for single
subjects: more or less dating app use
during the pandemic)
w2_how_many_corona_combo (for
single subjects: texting with more or
fewer potential partners during the
pandemic?)
w2_corona_longing_combo (for
single subjects: longing for a
relationship more or less than before
the pandemic)
w2_corona_effect_dating_combo
(did the pandemic make it easier or
harder to meet people?)
w2_shelter_combo_months (how
long sheltering in place)


**Open-ended variables coded**, codes
included in the first release of public
data. See rubrics in the documents for
how questions were coded

*q24, how couples meet

Lot's of columns, some duplicates, we can look at only the online ones in detail, or collapse into online, not online.



Did people know each other before? we should be careful to maybe only include those who didn't know each other.
w1_friend_connect_4_all 


_For more waves_
*q35, relationship quality
*why broke up
*q35, relationship quality
*why broke up
*COVID effect on relationship
*q35, relationship quality
*why broke up
*Preference for marriage versus
domestic partnership for subjects in
same-sex unions
*Reasons for nonmonogamy
*COVID effect on relationship
*COVID effect on dating



_Did people know each other before?_ DROP
w1_q25  Q25 did subject and partner attend same H.S.
w1_q26 byte %8.0g w1_q26 did subject and partner attend
same college
w1_q27 byte %8.0g Q27 did subject and partner grow up
in same city or town
w1_q28 byte %8.0g Q28 did subject's parents know
partner's parents before
subject knew partner?
w1_friend_connect_1_all
byte %8.0g yesno subject knew partner's friends
before meeting partner
w1_friend_connect_2_all
byte %8.0g yesno partner knew subjects friends
before meeting subject
w1_friend_connect_3_all
byte %8.0g yesno subject's friends knew partner's
friends before subject and
partner met
w1_friend_connect_4_all
byte %8.0g yesno no prior connection between
subject's friends and partner's
friends



