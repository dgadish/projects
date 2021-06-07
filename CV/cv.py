# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Text Variables
Header = "This CV was made with python.\nView my GitHub page for the source code."

Name = "Daniel Gadish"

Contact = "London, United Kingdom\n+447948285743\ndgadish99@gmail.com\nlinkedin.com/in/daniel-gadish\ngithub.com/dgadish"

ProjectsHeader = "Projects"
ProjectOneTitle = "r/Python Topic Classification"
ProjectOneDesc = "- Scraped submission data from the r/Python subreddit.\n- Using python with pandas, nltk and gensim packages.\n- Classified the topics for each submission using LDA."
ProjectTwoTitle = "Anaylst Progress Automation"
ProjectTwoDesc = "- Automated the reporting process allowing delivery managers\n  to view their analysts' training progress.\n- Cleaned and combined data from multiple sources using pandas.\n- Produced a csv file with the required information."
ProjectThreeTitle = "Survey Analysis and Improvement"
ProjectThreeDesc = "- Voluntary analysis for a Grayce charity partner.\n- Cleaned and processed the survey results using python with pandas.\n- Re-wrote the surveys to allow for more repeatable, faster analysis in future."
WorkHeader = "Experience"
WorkOneTitle = "RSA: Data Analyst/ Floorwalker"
WorkOneTime = "01/2021 - Present"
WorkOneDesc = "- Understood and amended existing SQL queries to extract relevant\n  data from Systrack.\n- Worked with a number of stakeholders to obtain meaningful\n  insights using data from a range of sources in Excel.\n- Supported around 500 RSA employees with the set-up of new laptops\n  including running sessions for groups of 15 - 20 people."
WorkTwoTitle = "Grayce: Data Analyst"
WorkTwoTime = "09/2020 - Present"
WorkTwoDesc = "- Developed the solution for the afformentioned reporting automation\n  project in collaboration with stakeholders to ensure their\n  requirements were met.\n- Provided recommendations to improve the current data model\n  to ensure that it more closely follows the first three normal forms.\n- Gave a talk on how python can be used in the workplace, including a\n  walkthrough of the afformentioned topic classification project."
EduHeader = "Education"
EduOneTitle = "The University of Birmingham, BSc Physics"
EduOneTime = "2017-2020"
EduOneDesc = "- 1st Class with honours.\n- Included a lab project where I collected magnetic field strength data,\n  and then used python to clean, process and visualise the data."
EduTwoTitle = "The Castle School, Thornbury"
EduTwoTime = "2010-2017"
EduTwoDesc = "- A* in physics, maths and further maths A-levels.\n- A* in an EPQ researching the viability of nuclear fusion as a sustainable\n  power source.\n- A in chemistry AS level.\n- 12 GCSE's with 6 A*'s, including maths and physics,\n  4 A's, including English literature, and 2 B's including English language\n  and the Free Standing Maths Qualification."
SkillsHeader = "Skills"
SkillsDesc = "- Python:\n   - Pandas\n   - NumPy\n   - Scikit-Learn\n- SQL\n- Excel\n- Data Visualization\n- Data Cleaning"
ExtrasOneTitle = "DataQuest\nData Analyst Path"
ExtrasOneDesc = "Learned python, popular data\nrelated packages, data cleaning,\nmanipulation and visualisation.\nAdditionally, an intro to SQL,\nusing the command line\nand git version control."
ExtrasTwoTitle = "AgilePM Foundation"
ExtrasTwoDesc = "Learned about the principles of\nan Agile project and the focus \non iterative development to \nbest meet the customers'\nneeds."



# Plotting

fig, ax = plt.subplots(figsize=(8.27, 11.69))

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

# Decorative Lines
plt.axvline(x=0, color='#00008b', alpha= 0.8, linewidth=300)
plt.axhline(y=0.89, color='#ffffff', xmin=0.0, xmax=0.323, linewidth=1.5)
plt.axhline(y=0.815, color='#ffffff', xmin=0.0, xmax=0.323, linewidth=1.5, alpha = 0.3)
plt.axhline(y=0.58 , color='#ffffff', xmin=0.0, xmax=0.323, linewidth=1.5, alpha = 0.3)
plt.axhline(y=0.393 , color='#ffffff', xmin=0.0, xmax=0.323, linewidth=1.5, alpha = 0.3)
plt.axhline(y=0.92, color='k', xmin=0.34, xmax=0.97, linewidth=1.2)
plt.axhline(y=0.614, color='k', xmin=0.34, xmax=0.97, linewidth=1.2)
plt.axhline(y=0.26, color='k', xmin=0.34, xmax=0.97, linewidth=1.2)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text

plt.annotate(Name, (0.53, 0.97), weight='bold', fontsize=16)
plt.annotate(Contact, (0.02, 0.917), fontsize=9, color='#ffffff')
plt.annotate(ProjectsHeader, (0.34, 0.93), weight='bold', fontsize=12)
plt.annotate(ProjectOneTitle, (0.34, 0.9), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (0.36, 0.85), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (0.34, 0.82), weight='bold', fontsize=10)
plt.annotate(ProjectTwoDesc, (0.36, 0.755), weight='regular', fontsize=9)
plt.annotate(ProjectThreeTitle, (0.34, 0.725), weight='bold', fontsize=10)
plt.annotate(ProjectThreeDesc, (0.36, 0.674), weight='regular', fontsize=9)
plt.annotate(WorkHeader, (0.34, 0.624), weight='bold', fontsize=12)
plt.annotate(WorkOneTitle, (0.34, 0.594), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (0.34, 0.574), weight='regular', fontsize=9, alpha=.8)
plt.annotate(WorkOneDesc, (0.36, 0.478), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (0.34, 0.448), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (0.34, 0.428), weight='regular', fontsize=9, alpha=.8)
plt.annotate(WorkTwoDesc, (0.36, 0.318), weight='regular', fontsize=9)
plt.annotate(EduHeader, (0.34, 0.268), weight='bold', fontsize=12)
plt.annotate(EduOneTitle, (0.34, 0.238), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (0.34, 0.218), weight='regular', fontsize=9, alpha=.8)
plt.annotate(EduOneDesc, (0.36, 0.168), weight='regular', fontsize=9)
plt.annotate(EduTwoTitle, (0.34, 0.138), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (0.34, 0.118), weight='regular', fontsize=9, alpha=.8)
plt.annotate(EduTwoDesc, (0.36, 0.008), weight='regular', fontsize=9)
plt.annotate(SkillsHeader, (0.02, 0.825), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (0.02, 0.66), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(ExtrasOneTitle, (0.02, 0.59), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ExtrasOneDesc, (0.02, 0.463), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTwoTitle, (0.02, 0.403), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTwoDesc, (0.02, 0.295), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(Header, (0.01, 0.01), weight='regular', fontsize=8, alpha=.75)


plt.savefig('cv.pdf', dpi=300, bbox_inches='tight')