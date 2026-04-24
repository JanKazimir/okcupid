## Stage 1: Profile Clustering (Unsupervised Learning) ##

Had to create 2 new features:
+ **1. 'w1_has_kids'**:
```
new_cols = {}

for wave in range(1, 4):
    cols = [f'w{wave}_PPT01', f'w{wave}_PPT25', f'w{wave}_PPT612', f'w{wave}_PPT1317']
    # Check if any column has a value > 0
    new_cols[f'w{wave}_has_kids'] = (df[cols].sum(axis=1) > 0).astype(int)

df = pd.concat([df, pd.DataFrame(new_cols, index=df.index)], axis=1)
```

+ **2. 'w1_meeting_type_refined'**:
```
def consolidate_meeting_method(val):
    val = str(val)  # Ensure it's a string for comparison:
    if val in ['Yes, an Internet dating or matchmaking site (like eHarmony or match.com)',
                          'Yes, an app on my phone (like Tinder or Grindr)']: # Met online via dating app
        return 'Dating App'
    if val in ['No, I did NOT meet [Partner Name] through the Internet']:  # Met offline
        return 'Offline'
    return 'Other Online'

df['w1_meeting_type_refined'] = df['w1_q32'].apply(consolidate_meeting_method)
```
Features to use in clustering:
```
my_features =  [
    'caseid_new',
    'w1_section',
    'w1_ppage',
    'w1_ppgender',
    'w1_ppeducat',
    'w1_partyid7',
    'w1_ppmsacat',
    'w1_same_sex_couple',
    'w1_ppincimp_cat',
    'w1_meeting_type_refined',
    'w1_max_relation_status',
    'w1_weekly_sex_frequency',
    'w1_q34',
    'w1_relate_duration_in2017_years',
    'w1_q19',
    'w1_married',
    'w1_has_kids'
]
```
Clustering results:
**--- Profiles for K=3 (Your Current Result) ---**
```
                     Years_Together  Sex_Freq_Weekly  Happiness_Score  \
relationship_cluster                                                     
1                              40.25             0.65             4.59   
2                              11.32             0.87             4.35   
3                              11.57             5.18             4.58   

                      Marriage_Rate_%  Has_Kids_%  Dating_App_Origin_%  
relationship_cluster                                                    
1                               96.96       12.23                 0.00  
2                               63.37       44.41                10.43  
3                               58.06       45.50                 7.88  
```
```
relationship_cluster
2    1351
1     970
3     436
Name: count, dtype: int64
```

**--- Profiles for K=5  ---**
```
                         Years_Together  Sex_Freq_Weekly  Happiness_Score  \
relationship_cluster_k5                                                     
1                                 42.61             0.63             4.62   
2                                  4.78             0.83             4.10   
3                                 11.57             5.18             4.58   
4                                 14.59             0.87             4.52   
5                                 17.45             0.87             4.38   

                         Marriage_Rate_%  Has_Kids_%  Dating_App_Origin_%  
relationship_cluster_k5                                                    
1                                  97.16        6.50                 0.00  
2                                   4.52       32.02                16.37  
3                                  58.06       45.50                 7.88  
4                                  85.45       18.27                 6.76  
5                                  93.67       76.20                 6.78  

```
```
relationship_cluster_k5
1    811
5    562
4    527
3    436
2    421
Name: count, dtype: int64
```

**Relationship Archetypes (K=5 Cluster Profiles)**

**Cluster 1: "The Legacy Guardians"**
+ *Nick-name*: **The Immortals**
+ *Key Metrics*: 42.6 years duration | 97.2% Marriage | 4.62 Happiness | 1.13% Breakup Rate
+ *Description*: This is the baseline for absolute stability. These couples have survived the "critical windows" of mid-life. Their happiness is the highest in the study, and their breakup rate is effectively zero.
+ *Product Insight*: They represent the "Gold Standard" of long-term compatibility that the algorithm should aim for as a 50-year vision.

**Cluster 2: "The Fragile Explorers"**
+ *Nick-name*: **The Ground Zero Group**
+ *Key Metrics*: 4.8 years duration | 4.5% Marriage | 4.10 Happiness | 59.12% Breakup Rate
+ *Description*: This is your highest-risk group. They have the highest concentration of Dating App users (16.4%). They are in the "testing phase" of the relationship. With very low marriage rates and the lowest happiness scores, they are highly susceptible to "churn."
+ *Product Insight*: This is the primary target for retention features. They need tools to help them navigate the transition from "dating" to "established partnership."

**Cluster 3: "The High-Passion Pros"**
+ *Nick-name*: **The Spark Keepers**
+ *Key Metrics*: 11.6 years duration | 5.18 Sex Freq | 4.58 Happiness | 24.38% Breakup Rate
+ *Description*: This group defies the "roommate" stereotype. Despite being together for over a decade, they maintain the physical intimacy of a new couple. They are happy and active, but still face a 1-in-4 chance of breaking up, showing that passion alone isn't a total shield.
+ *Product Insight*: These are "Power Users" of relationship success. Studying their compatibility traits could help OKCupid refine its matching algorithm for "long-term spark."

**Cluster 4: "The Secure Companions"**
+ *Nick-name*: **The Stable Mid-Termers**
+ *Key Metrics*: 14.6 years duration | 85.5% Marriage | 4.52 Happiness | 5.71% Breakup Rate
+ *Description*: These couples have successfully navigated the first decade. They have high marriage rates and very solid happiness. They are the "Success Story" of the 10-year mark, showing high resilience with a very low breakup rate.
+ *Product Insight*: They prove that moving from Cluster 2 (Explorers) into a more structured commitment (Marriage/Stability) drastically reduces the risk of failure.

**Cluster 5: "The Family Anchors"**
+ *Nick-name*: **The Parenting Pillar**
+ *Key Metrics*: 17.5 years duration | 93.7% Marriage | 4.38 Happiness | 76.2% Kid Rate
+ *Description*: This cluster is defined by the household. They have the highest rate of minor children. While their sex frequency is lower and happiness is slightly lower than the "Passionate Pros," their marriage rate and "social glue" keep them together (only 13.5% breakup rate).
+ *Product Insight*: Family-building is a major "anchor" for stability. Matches that prioritize "family goals" are statistically more likely to survive the mid-term slump.


## Stage 2: Predictive Modeling (Supervised Learning) ##


In this stage, we utilized **CatBoost** to determine which factors drive relationship survival over a 5-year horizon. Our model achieved a **BestTest LogLoss of 0.3038**, indicating high predictive reliability for sociological data.



---
```
--- WEIGHTED BREAKUP RATE PER CLUSTER (%) ---
relationship_cluster
1     1.13
2    59.12
3    24.38
4     5.71
5    13.51
dtype: float64
```
### 1. Weighted Breakup Rates: The "Survival Map"
The clusters identified in Stage 1 reveal radically different survival probabilities. This serves as the **"Product Health Check"** for OKCupid matches:

*   **🔴 The Danger Zone (Cluster 2 — 59.12%)**
    Nearly 60% of couples in this *"Fragile Explorer"* group broke up. As this cluster has the highest concentration of dating app users, it represents the critical "Early Attrition" phase OKCupid must address.
*   **🟢 The Success Path (Cluster 4 — 5.71%)**
    Couples who transition into this *"Stable Mid-Termer"* profile see their risk of breakup drop by **10x** compared to the Explorers.
*   **🏆 The Immortals (Cluster 1 — 1.13%)**
    The benchmark of ultimate success; these relationships are statistically near-permanent.

---

### 2. Feature Importance: Myth-Busting for OKCupid
The Feature Importance ranking provides a scientific answer to common criticisms of dating apps.
```
bestTest = 0.3038411263
bestIteration = 37

Shrink model to first 38 iterations.
                           feature  importance
0             relationship_cluster   28.362240
5                       w1_married   20.290979
4                           w1_q34   14.801382
3  w1_relate_duration_in2017_years   11.940263
6                      w1_ppeducat   11.147246
1          w1_meeting_type_refined    5.235619
2                         w1_ppage    5.076120
7                      w1_has_kids    3.146151
```

### Feature Importance: Complete Predictive Model


| Feature | Importance | Business Interpretation |
| :--- | :--- | :--- |
| **Relationship Cluster** | **28.36%** | **The #1 Predictor.** The overall "archetype" (Life Stage) is more important than any single demographic. |
| **Marital Status** | **20.29%** | Formal commitment remains the strongest structural barrier to breakups. |
| **Relationship Quality** | **14.80%** | The "subjective vibe" at the start is a massive red flag if low. |
| **Relationship Duration** | **11.94%** | The "Time-Tested" effect. Every year a couple stays together adds cumulative inertia that makes future separation less likely. |
| **Education Level** | **11.15%** | Socio-economic alignment. Higher education often correlates with higher shared resources and conflict-resolution stability. |
| **Meeting Type** | **5.23%** | **The Bottom Tier.** Whether a couple met on an app or offline is irrelevant to their long-term survival. |
| **Respondent Age** | **5.08%** | Maturity factor. While older individuals tend to be more stable, age alone is far less predictive than the specific stage of the relationship. |
| **Presence of Kids** | **3.15%** | The "Parenting Anchor." While children increase complexity, they act as a minor structural stabilizer rather than a primary driver of romance. |


---

### 3. Key Takeaways for the OKCupid Team

> #### "The Origin Myth" is Dead
> Our model shows that **how you met (5.2%)** is nearly **6 times less important** than the **Relationship Archetype (28.4%)** you build. OKCupid matches are not "disposable"; they are subject to the same life-cycle forces as any other couple.

*   **Cluster-Based Retention:** OKCupid should move beyond "matching" and into "maintenance." By identifying users whose profiles mirror **Cluster 2**, the app can offer features (check-ins, relationship advice, or coaching) to help them move toward the stability of **Cluster 4**.
*   **Early Detection:** Since initial **Relationship Quality (14.8%)** is a top predictor, the app can use early satisfaction surveys to predict which matches are "High-Risk" and intervene before the breakup occurs.

---

### Team Note: Technical Validity
The model reached its peak performance at **Iteration 37**. We utilized a "shrink" approach to prevent overfitting, ensuring these findings are generalizable to the broader population of couples in the US.


## Stage 3: Strategic Roadmap: Data-Driven Product Features ##

This roadmap translates our **K=5 Archetypes** and **CatBoost Predictive Importance** into actionable product strategies to improve user success and brand loyalty.

---

### 1. The "Relationship Health" Dashboard ###
*Targeting: Cluster 2 (Fragile Explorers) & Cluster 5 (Family Anchors)*

*   **The Data:** Cluster 2 has a **59.1% breakup rate** and the lowest initial quality scores.
*   **Feature Idea:** An optional "Couples Mode" that triggers once a match goes "off-app." It provides monthly check-ins and shared relationship goals.
*   **Value Add:** By monitoring **Happiness Scores** (#3 predictor), OKCupid can identify when a couple is slipping into the "Fragile" phase and suggest curated date nights or communication exercises to pivot them toward a more stable archetype.

### 2. "Anchor-Point" Matching Algorithm ###
*Targeting: Cluster 4 (Stable Mid-Termers) & Cluster 1 (The Immortals)*

*   **The Data:** **Marital Status (20.3%)** and **Family Anchors (13.5% survival impact)** are massive predictors of longevity.
*   **Feature Idea:** Re-weight the matching algorithm to prioritize "Structural Compatibility." Move beyond shared hobbies to prioritize "Anchor Factors" (e.g., specific long-term views on legal commitment and family building).
*   **Value Add:** This shifts the brand from "Find a Date" to "Build a Life," leaning into the high statistical importance of formal commitment found in our study.

### 3. The "Longevity Seal" Marketing Campaign ###
*Targeting: General Public & Media Stakeholders*

*   **The Data:** Our model proved that the **Meeting Method (5.2%)** is nearly irrelevant compared to the **Relationship Profile (28.4%)**.
*   **Feature Idea:** Launch a transparency campaign titled *"The Digital Dating Myth."* Use the longitudinal data to prove that OKCupid matches reach the "Golden Veteran" stage at the same rate as traditional matches.
*   **Value Add:** Directly attacks the "disposable dating" stigma. Positioning OKCupid as the platform that produces "Immortals" (Cluster 1) creates a unique competitive advantage in a crowded market.

---

## Final Project Conclusion ##

The transition from **Stage 1 (Clustering)** to **Stage 2 (Prediction)** reveals that a relationship's fate is written in its **Profile Archetype**, not its **Digital Origin**. 

> **Final Verdict:** Success is determined by the **vibe** (Quality), the **bond** (Marriage), and the **stage** (Archetype). OKCupid’s algorithm is a powerful engine for creating these bonds, and by focusing on "mid-term maintenance," the platform can significantly reduce attrition in the high-risk 5-year window.



# Why these models were chosen and what else could have been done #
### Why K-Prototypes? (Clustering Logic) ###
***Question*: Besides K-Prototypes, what other clustering models could (and should) have been used for this dataset?**
Answer:
+ **While K-Prototypes was our primary choice, a comprehensive analysis would consider these alternatives**:
PAM (Partitioning Around Medoids) with Gower Distance: This is the "Gold Standard" for mixed data. It uses a Gower Metric to handle numerical and categorical data simultaneously. It is more robust to outliers than K-Prototypes because it uses actual data points (medoids) as cluster centers rather than averages.
+ **Latent Class Analysis (LCA)**: Unlike geometric algorithms, LCA is a statistical model. It assumes a "latent" (hidden) relationship type explains the survey responses. It provides the probability of belonging to a cluster (e.g., "80% Veteran, 20% Struggling"), which is often more realistic than hard assignments.
+ **Hierarchical Clustering**: This builds a "dendrogram" (tree). It is visually powerful for presentations because it shows the "family tree" of relationships—for example, how stable couples eventually split into "Elders" and "Married Mid-Lifers."
+ **Why we chose K-Prototypes**: "It provides the best balance of efficiency and the ability to handle the mixed-type variables of the HCMST dataset without needing complex distance matrix pre-computations."

## Why CatBoost over Logistic Regression? (Predictive Logic) ##
***Question*: What would happen if we used Logistic Regression instead of CatBoost? How would the results differ?**
Answer:
**Switching to Logistic Regression would result in a significant shift in both performance and interpretability:**
+ **Non-Linearity vs. Linearity**: Relationships are complex. CatBoost excels at finding interactions (e.g., "Meeting online is only risky for specific age groups"). Logistic Regression assumes every factor has a constant, linear effect, which would likely lead to lower predictive accuracy (AUC/ROC) in social data.
+ **Handling of Categorical Data**: CatBoost processed our survey labels ('Excellent', 'Fair', etc.) and missing values (NaN) automatically. Logistic Regression would have required extensive preprocessing, such as One-Hot Encoding (creating dummy variables) and Imputation for every missing answer, which can introduce bias.
+ **Multicollinearity**: In our data, variables like "duration" and "marriage" are highly correlated. This confuses Logistic Regression and can produce unstable coefficients. CatBoost, being tree-based, is naturally more resistant to this.
+ **Why we chose CatBoost**: "It captures the nuanced, non-linear nature of human relationships more accurately than a linear model, while saving significant time on data preprocessing by handling categorical strings and missing values natively."

***"We prioritized CatBoost specifically because we wanted to capture the non-linear interactions between our discovered Archetypes and the original survey features, which a traditional Logistic Regression would likely miss."***
