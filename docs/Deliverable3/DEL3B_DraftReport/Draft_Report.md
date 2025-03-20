# Interim Report 

# §1. Phenomenon Overview

Astroturfing is a form of online disinformation that involves coordinated bots spreading a certain message to create the illusion of widespread support. With advancements in AI, many bots have become much more sophisticated (Radivojevic et al., 2024). AI is not only used to generate these bots but also to counter it, providing a unique AI to AI interaction. Disinformation bots use AI to automate engagement, generate realistic comments and coordinate with each other to avoid detection. Meanwhile, social media platforms use AI to detect suspicious patterns, flag fake accounts and limit the spread of manipulated content. This back-and-forth results in an evolving battle between AI, media platforms attempt to build better detection software while bot creators design algorithms to evade detection. 

It is important for misinformation bots to be caught and banned however, as they have real-world consequences. They are often used in political campaigns to discredit or support certain candidates. Court published records showed that they were used in a 2012 campaign in South Korea (Zerback et al., 2021). It is highly likely they have also been used in several US elections (Keller et al., 2020). Studies show that astroturfing does have an impact on participants opinions, even when counter strategies are used against it. Furthermore, the influence of astroturfing has a lasting impact on a person’s opinion (Keller et al., 2020). 

Agent-Based Modeling is an effective approach to studying astroturfing as it allows for large-scale simulations of interactions between bots, human users and platform detection mechanisms (human moderators or AI). By modeling these interactions, we can gain a deeper understanding of how bots influence users and develop better counter measures for it. ABM also allows us to modify agent behaviour to mimic how agents would act in a real media ecosystem. 


<img width="1025" alt="Figure 1" src="https://github.com/user-attachments/assets/e0c14650-bd7e-4200-b13b-733ef572f2bd" />

Figure 1

Left: The blue dots represent human agents, while red dots represent posts. The size of a red dot indicates the number of likes it has received. At step 1, only a few posts have been amplified by bots. 

Right: The graph shows the total number of bot and human likes over time. Bot-driven amplification starts immediately, while human engagement begins at a lower rate.


<img width="1025" alt="Figure 1" src="https://github.com/user-attachments/assets/96c92d09-a178-44dd-b535-e3b40cb8b028" />

Figure 2

Left: By step 2 more posts have been amplified by bots, leading to an increase in size and more human agents seeing them. 

Right: The line graph shows a sharp increase in human likes, suggesting that bot driven amplification has successfully boosted a post enough to get real engagement.


<img width="1025" alt="Figure 1" src="https://github.com/user-attachments/assets/8a6aed7b-abce-45ef-bf99-0e108e795920" />

Figure 3

Left: By step 10 the bot amplified posts have become very large, presenting the illusion that there is a lot of support behind it. 

Right: Bot activity has slowed down at this point as they are no longer needed.  


# §2. Simulation Design & Implementation

Our model consists of agents interacting within a spatial grid environment to simulate the dynamics of social media recommendation algorithm-style amplification.  The agents are Bot Amplifiers, who are tasked with liking posts in order to amplify them, Human Users, who simulate real human social media users, and Content Moderators (not yet implemented) who are tasked with looking for suspicious amplification, and with sufficient reason, banning bots and taking down posts. Although posts do not perform like an actor, Posts are also considered an agent, and interact with Bot Amplifiers and Human Users. The simulation takes place on a grid, where Posts and Human Users exist in cells. A Post has an influence radius, and in each step, a Human User can encounter a Post with a sufficient radius. This simulates a social media "For-You" page style interaction, where a Post is more likely to appear to a Human User the more likes it has. We would like to add more parameters for engagement, such as comments and time spent looking at a post, which will contribute to the "size" of the post. A Bot Amplifiers's rule based interaction is to approach likes in a staggered manner, not liking every Post at once, but liking a subset of posts (25%). As mentioned, the Human Users interact with a Post when its influence radius is sufficiently large. Once the Human User interacts with the post, it makes a decision to like the post based on his/her interest and susceptibility (parameters which will be even further developed with added metrics). The Human User then chooses to like the Post, boosting its reach as equivalently as a Bot Amplifier like, since a Post is blind to the identity of its liker. Once implemented, a Content Moderator will scoure for posts that have suspicious qualities such as an abnormally fast like rate, likes without comments, etc. The Content Moderator will ban suspected bots, resulting in an adjustment of strategy from the Bot Amplifiers (staggered likes, commenting, slowing down, etc.). For the scheduler, we used the `agents.shuffle_do("step")`, which is the newer version of RandomActivation. This causes a random shuffle of Human Users, Bot Amplifiers, and soon Content Moderators, liking, staggered liking, and banning, respectively. The data being collected right now in each simulation is the total number of likes by Human Users, and the total number of likes by Bot Amplifier users. The trend that seems to be emerging is that even with a large number of Human Users, Bot Amplifiers have an impact on the spread of Posts, to the point where a lack of Bot Amplifiers has a significant impact on the likelihood of a Human User encountering a post at all. We plan on collecting even more data and have a preliminary usage of pandas and Matplotlib to run hundreds of simulations for further analysis. 

<img width="1025" alt="Screenshot 2025-03-19 at 10 40 16 PM" src="https://github.com/user-attachments/assets/b539a077-6bfe-435e-8f02-9687c780b57d" />
<img width="1037" alt="Screenshot 2025-03-19 at 10 41 56 PM" src="https://github.com/user-attachments/assets/b98c5f27-64c3-4759-812c-d88620e987d2" />


# §3. Preliminary Observations & Results 

Early simulation results illustrate astroturfing dynamics by comparing different levels of bot activity and how they influence human engagement. These simulations were ran with varying parameters. 

1) Baseline human engagement
   
In the first simulation (20 humans, 0 bots per step) there are no bots and humans interact with posts naturally. Engagement is linear and there are no sudden spikes anywhere. This represents organic social media behaviour. Since no bots artificially boost any content, posts rely on human driven interactions to gain visibility.

<img width="800" alt="Screenshot 2025-03-19 at 10 41 56 PM" src="https://github.com/user-attachments/assets/1e87a06b-d390-4ee3-9bee-858d8ab7a9bd" />

2) Single bot
   
In the second simulation (20 humans, 1 bot per step) there is one bot being created at every step which engages with certain posts. We can observe a noticeable increase in the total amount of human likes. There are tiny spikes in likes that are mirrored in the blue and orange lines, suggesting that even a single bot can influence the visibility of a post.

<img width="800" alt="Screenshot 2025-03-19 at 10 41 56 PM" src="https://github.com/user-attachments/assets/cdecce01-f012-4efb-8a01-40a3f2ffb717" />

3) Five bots
   
In the third simulation (20 humans, 5 bots per step) there are 5 bots that are created at each step. This is when the simulation really shows how fast bot amplification can drive human engagement. As more bots boost posts, visibility increased dramatically leading to a large spike in humans engaging with a post. This can be seen in the large spikes that are mirrored. Initially the bots are engaging with the posts far more than humans as can be seen by the blue line. However, once human engagement takes off bots fall off into the background and human likes dominate. This behaviour demonstrates what astroturfing is like. The bots create an image of support and popularity behind a post which is then engaged with by real users who believe real users are behind it. 


<img width="800" alt="Screenshot 2025-03-19 at 10 41 56 PM" src="https://github.com/user-attachments/assets/202a0cb8-263c-4047-9a3e-6edfd7f26758" />


One unexpected behaviour we encountered is bot activity stagnating. As can be seen by the blue line in graph 3, the bot likes stagnate until step 6 and then abruptly jump and then stagnate again. This may be due to the parameter where they stop engaging with posts once a post reaches a certain number of human likes. However, that does not explain the abrupt jump. That may be due to how the scheduler works. Bot are only able to like a post once and if the randomized scheduler keeps selecting bots that have already liked a post, then there is no activity until a fresh bot is selected. 

# §4. Challenges & Next Steps 
Development Challenges:

Implementing the simulation posed many challenges for our group. Neither of us were familiar with python, nor the mesa framework, so that was a learning experience and challenge we had to overcome. In terms of the simulation itself, making agents interact in a realistic way was quite difficult. Initially humans and bots would like every post on the feed but then we had to find a way to make them act more organic. We solved this by having bots choose a random subset of posts to target, mimicking real world astroturfing. These posts could resemble political campaigns or advertisements. For human agents, we added a chance parameter for them to like a post which increased based on the post’s visibility (total likes). Another challenge which remains unsolved is managing the lifecycle of the bots. We create x number of new bots at every step and old bots don’t do anything after they have liked certain posts. 

Planned Refinements for the Final Report:

There is a lot that needs to be further developed for the final simulation. Bots need to be looked at further and adjusted so they behave less predictably. Additionally, there needs to be some sort of tracking for the bots lifespan (i.e account age). Adding lifespan to bots would allow for unique behaviours such as bots waiting to reach a certain “age” before acting to avoid suspicion. On that topic, the most important feature that remains to be added is a moderator agent. The moderator agent would have some way of detecting bots/bot amplified posts. Then they could delete those posts and ban the bots. This would add a new element to the simulation and make it more akin to how real social media operates. Additionally, due to this element the bots will now have to adapt as to avoid detection by the moderator. Hence, there will be a sort of interesting back and forth between the moderator agent and the bots. We also plan on introducing further refinement to the human agent. They will have further susceptibility to bot generated posts and may be able to dislike or report a post if they find it suspicious. Furthermore, the post entities themselves could use some additional attributes. Some ideas are adding comments to them or a lifespan as well. Posts should also have further data collection such as how many bot versus human likes on an individual post. 

# §6. References


Radivojevic, K., McAleer, C., Conley, C., Kennedy, C., & Brenner, P. (2024, September 27). Social Media Bot Policies: Evaluating passive and active enforcement. arXiv.org. https://arxiv.org/abs/2409.18931 

Zerback, T., Töpfl, F., & Knöpfle, M. (2021). The disconcerting potential of online
disinformation: Persuasive effects of astroturfing comments and three strategies for
inoculation against them. New Media & Society, 23(5), 1080–1098.
https://doi.org/10.1177/1461444820908530

Keller, F. B., Schoch, D., Stier, S., & Yang, J. (2020). Political Astroturfing on Twitter: How to
Coordinate a Disinformation Campaign. Political Communication, 37(2), 256–280.
https://doi.org/10.1080/10584609.2019.1661888


# §7. Attestation
All group members contributed to the report. Dov contributed mainly to sections 2 and 4, and Aziz to sections 1 and 3, but both Dov and Aziz worked together and evenly allocated the work completed.
