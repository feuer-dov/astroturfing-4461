# Final Report

# §1. Phenomenon Overview

Astroturfing is a form of online disinformation that involves coordinated bots spreading a certain message to create the illusion of widespread support. With advancements in AI, many bots have become much more sophisticated (Radivojevic et al., 2024). AI is not only used to generate these bots but also to counter it, providing a unique AI to AI interaction. Disinformation bots use AI to automate engagement, generate realistic comments and coordinate with each other to avoid detection. Meanwhile, social media platforms use AI to detect suspicious patterns, flag fake accounts and limit the spread of manipulated content. This back-and-forth results in an evolving battle between AI, media platforms attempt to build better detection software while bot creators design algorithms to evade detection. 

It is important for misinformation bots to be caught and banned however, as they have real-world consequences. They are often used in political campaigns to discredit or support certain candidates. Court published records showed that they were used in a 2012 campaign in South Korea (Zerback et al., 2021). It is highly likely they have also been used in several US elections (Keller et al., 2020). Studies show that astroturfing does have an impact on participants opinions, even when counter strategies are used against it. Furthermore, the influence of astroturfing has a lasting impact on a person’s opinion (Keller et al., 2020). 

Agent-Based Modeling is an effective approach to studying astroturfing as it allows for large-scale simulations of interactions between bots, human users and platform detection mechanisms (human moderators or AI). By modeling these interactions, we can gain a deeper understanding of how bots influence users and develop better counter measures for it. ABM also allows us to modify agent behaviour to mimic how agents would act in a real media ecosystem. 

![image](https://github.com/user-attachments/assets/9ab0d39d-01fe-49d8-8f1e-7c3ea1ffce36)
Step 0: The Setup

*At the beginning of the simulation, posts are not liked yet. Only a few humans interact with content (blue dots), and no meaningful popularity has emerged yet.*

![image](https://github.com/user-attachments/assets/c983ec24-6b3e-4001-a753-cdd64d3e00ef)
Step 3: Artificial Momentum

*A surge of bot activity drives rapid growth in engagement for select posts (orange circles), inflating their visibility. These posts begin to appear legitimate due to the volume of likes—even though this growth is artificial. Some posts are already being flagged and removed (red).*

![image](https://github.com/user-attachments/assets/db174cc3-0238-4c36-9af8-3cecc46130d8)
Step 9: Illusion of grassroots support

*As bot engagement plateaus, human users begin interacting with these highly visible posts. The human like count surpasses the bot like count, giving the illusion that the content is gaining traction organically.*

