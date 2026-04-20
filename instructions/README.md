# How Couples Meet and Stay Together (HCMST)

- Repository: `clustering`
- Type of Challenge: `Learning`
- Duration: `5 days`
- Deadline: `24/04/2026 13:00`
- Presentation: `24/04/2026 14:00` 10 minutes + 5 minutes Q&A
- Team challenge : 3 (max 4)

## Background
You are a Junior Data Scientist on the research team at OKCupid. You study love — and this week, you are going to revisit a famous dataset from Stanford's Social Science Data Collection called [How Couples Meet and Stay Together (HCMST)](https://data.stanford.edu/hcmst2017).
The data comes from a real academic research project led by Professor Michael Rosenfeld at Stanford University. It is one of the most cited datasets in the sociology of modern relationships, covered by the New York Times, The Economist, and NPR, and featured in Aziz Ansari's book Modern Romance.
The research started with a simple but surprisingly hard question: how do Americans actually meet their romantic partners — and does it matter for whether the relationship lasts?


## About this dataset
The version you are using covers three waves of data collection:

- Wave 1 (2017): 3,510 US adults surveyed about their current or most recent relationship — how they met, relationship quality, demographics, and dating app use
- Wave 2 (2020): 2,107 of the same respondents followed up, right in the middle of the COVID-19 pandemic
- Wave 3 (2022): 1,722 of the original respondents followed up again

Because the same people were tracked over five years, you can observe what actually happened to their relationships over time — not just what they predicted or remembered. This makes it a longitudinal dataset, which is rare and valuable in social science research.
A few things worth knowing before you start:

The dataset deliberately oversampled LGB respondents — gay, lesbian, and bisexual adults appear at a higher rate than in the general US population. This was intentional. The survey weights correct for this, and you are expected to understand why and apply them appropriately.
The data is nationally representative of English-speaking US adults, weighted to match the US population on gender, age, income, region, race, and ethnicity.
All three waves are merged into a single wide-format file — one row per respondent, with w1_, w2_, and w3_ prefixes on variables from each wave.


## The mission
### Part 1 — Clustering
Your first task is to explore the dataset through the lens of clustering.
- Can you group respondents into meaningful broad categories based on their relationship profiles?
- What are the characteristics of each group? What story does each cluster tell?
- How will you visualise and communicate those groups clearly?

There is no single right answer here. The quality of your work will be judged not by whether your clusters are "correct" — there is no ground truth — but by whether they are meaningful, interpretable, and honestly presented.

### Part 2 — Your own research question
Once you have explored the data through clustering, formulate your own research question and answer it using an appropriate model — classification, regression, or further statistical analysis.
Your question should be:
- Specific — not "what affects relationships?" but "does X predict Y, after controlling for Z?"
- Answerable with this dataset — check that the variables you need actually exist and have enough coverage before committing
- Honest about its limits — what would you need to answer this question properly that this dataset cannot give you?

#### Some directions to inspire you (but don't feel limited to these):

- Does meeting online predict whether a couple is still together five years later?
- Do couples with similar demographic profiles last longer?
- Does the context of meeting (friends, work, app, bar) predict relationship survival independently of demographics?
- What factors at wave 1 best predict relationship quality in 2022?
- Did the pandemic affect some types of couples more than others?

### Part 3 — Conclusions and recommendations
Based on both your clustering analysis and your research question, what are your conclusions? What would you recommend to OKCupid's product team, and why?
Be specific. "The data suggests X, which means OKCupid could consider Y — but only if Z assumption holds" is a good recommendation. "Online dating is good" is not.


## Tips to get started

- Explore the dataset pages (website documentation) thoroughly before writing a single line of code — read the user guide, investigate the data dictionnary, go through the survey instruments.
- Research clustering methods and understand the assumptions each one makes before choosing
- Research clustering visualisation methods — how you show your clusters is as important as how you build them
- For guidance on formulating good research questions: [The Art of Data Science](https://leanpub.com/artofdatascience)
- Document every decision you make and why — your reasoning is part of your deliverable, not just your results

*A note on critical thinking*
When working with real data there is no answer key. This means that at every step of this project, you are expected to actively question what you are doing:

**On your data:**
- Have you paid attention to the attrition of the repondents throughout the 3 waves of data collection? What does this attrition imply?
- What are the weights variables for? Did you account for it in your analysis and model?
- Do you understand what each variable you plan to use actually measures? Have you validated your understanding with the codebook and the user's guide?
- Are there missing values? Why might they be missing — is it random, or is there a pattern?
- Who is in this dataset, and who is not? What does that mean for the conclusions you can draw?

**On your clustering:**
- How did you choose the number of clusters? Did you try multiple values and compare?
- Do your clusters make sociological sense, or are they just mathematical artefacts?
- Would a different algorithm give different clusters? Does that matter?

**On your model:**
- Is your result statistically meaningful, or could it be noise?
- Are the variables you included as features genuinely independent of your target variable, or could they be measuring the same thing in a different way?
- What is your baseline? Before evaluating your model, ask yourself: what score would a completely naive prediction achieve — for instance, always predicting the most frequent class regardless of the input? If your model doesn't clearly beat that, it may not have learned anything meaningful at all.
- What does a high accuracy score hide? What does a low one reveal?

**On your conclusions:**
- Correlation is not causation. Can you tell the difference in your own findings?
- What alternative explanations exist for the pattern you observed?
- What would need to be true for your recommendation to be wrong?

__The best data scientists are not the ones who find the most impressive results. They are the ones who know exactly how much to trust their own findings — and are honest about it.__


## You've got this!

<p float="left">
  <img src="https://media.giphy.com/media/UadopVjBg5SQlcueNc/giphy.gif" height="200" />
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3dsaTNpejZsMzRkMTJnc3gzZWc5NDFwb2g2NjhucWNqazk0eHpnMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AEWVSewz8sSm3HFoib/giphy.gif" height="200" />
</p>

