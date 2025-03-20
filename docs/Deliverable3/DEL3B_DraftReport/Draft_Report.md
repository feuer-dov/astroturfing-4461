# Interim Report 

# §1. Phenomenon Overview

# §2. Simulation Design & Implementation

Our model consists of agents interacting within a spatial grid environment to simulate the dynamics of social media recommendation algorithm-style amplification.  The agents are Bot Amplifiers, who are tasked with liking posts in order to amplify them, Human Users, who simulate real human social media users, and Content Moderators (not yet implemented) who are tasked with looking for suspicious amplification, and with sufficient reason, banning bots and taking down posts. Although posts do not perform like an actor, Posts are also considered an agent, and interact with Bot Amplifiers and Human Users. The simulation takes place on a grid, where Posts and Human Users exist in cells. A Post has an influence radius, and in each step, a Human User can encounter a Post with a sufficient radius. This simulates a social media "For-You" page style interaction, where a Post is more likely to appear to a Human User the more likes it has. We would like to add more parameters for engagement, such as comments and time spent looking at a post, which will contribute to the "size" of the post. A Bot Amplifiers's rule based interaction is to approach likes in a staggered manner, not liking every Post at once, but liking a subset of posts (25%). As mentioned, the Human Users interact with a Post when its influence radius is sufficiently large. Once the Human User interacts with the post, it makes a decision to like the post based on his/her interest and susceptibility (parameters which will be even further developed with added metrics). The Human User then chooses to like the Post, boosting its reach as equivalently as a Bot Amplifier like, since a Post is blind to the identity of its liker. Once implemented, a Content Moderator will scoure for posts that have suspicious qualities such as an abnormally fast like rate, likes without comments, etc. The Content Moderator will ban suspected bots, resulting in an adjustment of strategy from the Bot Amplifiers (staggered likes, commenting, slowing down, etc.). For the scheduler, we used the `agents.shuffle_do("step")`, which is the newer version of RandomActivation. This causes a random shuffle of Human Users, Bot Amplifiers, and soon Content Moderators, liking, staggered liking, and banning, respectively. The data being collected right now in each simulation is the total number of likes by Human Users, and the total number of likes by Bot Amplifier users. The trend that seems to be emerging is that even with a large number of Human Users, Bot Amplifiers have an impact on the spread of Posts, to the point where a lack of Bot Amplifiers has a significant impact on the likelihood of a Human User encountering a post at all. We plan on collecting even more data and have a preliminary usage of pandas and Matplotlib to run hundreds of simulations for further analysis. 

<img width="1025" alt="Screenshot 2025-03-19 at 10 40 16 PM" src="https://github.com/user-attachments/assets/b539a077-6bfe-435e-8f02-9687c780b57d" />
<img width="1037" alt="Screenshot 2025-03-19 at 10 41 56 PM" src="https://github.com/user-attachments/assets/b98c5f27-64c3-4759-812c-d88620e987d2" />


# §3. Preliminary Observations & Results (~500 words)
Provide a description of how early simulation results illustrate the phenomenon of interest. Provide initial quantitative metrics or qualitative descriptions of emergent behaviors. Include graphs, tables, or network diagrams showcasing agent interactions.

Describe unexpected behaviors and/or emergent dynamics. Identify and discuss any unexpected trends observed in early runs. Identify potential causes of these behaviors based on agent parameters. For the final report, you will expand and the findings, refine interpretations, and conduct additional simulations for completeness and robustness of results

# §4. Challenges & Next Steps (~500 words)
Development Challenges:

Describe the most difficult aspects of implementing the simulation.

Discuss any changes made to the model due to unforeseen challenges.

Planned Refinements for the Final Report:

Outline what needs to be further developed, tested, or refined before submission of DEL 4.B.

Identify additional data collection or analysis methods that will enhance findings.

# §6. References
include full references to a minimum of 3 works cited in the report. Use APA format.

# §7. Attestation
All group members contributed to the report. Dov contributed mainly to sections 2 and 4, and Aziz to sections 1 and 3, but both Dov and Aziz worked together and evenly allocated the work completed.
