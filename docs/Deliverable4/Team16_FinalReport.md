# Final Report

# §1. Phenomenon Overview

Astroturfing is a form of online disinformation that involves coordinated bots spreading a certain message to create the illusion of widespread support. With advancements in AI, many bots have become much more sophisticated (Radivojevic et al., 2024). AI is not only used to generate these bots but also to counter it, providing a unique AI to AI interaction. Disinformation bots use AI to automate engagement, generate realistic comments and coordinate with each other to avoid detection. Meanwhile, social media platforms use AI to detect suspicious patterns, flag fake accounts and limit the spread of manipulated content. This back-and-forth results in an evolving battle between AI, media platforms attempt to build better detection software while bot creators design algorithms to evade detection. 

It is important for misinformation bots to be caught and banned however, as they have real-world consequences. They are often used in political campaigns to discredit or support certain candidates. Court published records showed that they were used in a 2012 campaign in South Korea (Zerback et al., 2021). It is highly likely they have also been used in several US elections (Keller et al., 2020). Studies show that astroturfing does have an impact on participants opinions, even when counter strategies are used against it. Furthermore, the influence of astroturfing has a lasting impact on a person’s opinion (Keller et al., 2020). As Jovy Chan (2023) notes, this manipulation of crowd perception is uniquely dangerous because it hijacks both informational and normative conformity. Bots don't need to spread outright lies—merely simulating broad public support is enough to change how real users think and behave. Once users perceive a crowd backing a message, even falsely, they may adopt and reinforce it themselves, making the deception self-sustaining and harder to unwind.

To better understand these dynamics, our project uses Agent-Based Modeling (ABM) to simulate a digital media environment populated with bots, human users, and content moderation agents. ABM is an effective approach to studying astroturfing as it allows for large-scale simulations of interactions between bots, human users and platform detection mechanisms (human moderators or AI). By modeling these interactions, we can gain a deeper understanding of how bots influence users and develop better counter measures for it. ABM also allows us to modify agent behaviour to mimic how agents would act in a real media ecosystem. 

![image](https://github.com/user-attachments/assets/9ab0d39d-01fe-49d8-8f1e-7c3ea1ffce36)

Step 0: The Setup

*At the beginning of the simulation, posts are not liked yet. Only a few humans interact with content (blue dots), and no meaningful popularity has emerged yet.*

![image](https://github.com/user-attachments/assets/c983ec24-6b3e-4001-a753-cdd64d3e00ef)

Step 3: Artificial Momentum

*A surge of bot activity drives rapid growth in engagement for select posts (orange circles), inflating their visibility. These posts begin to appear legitimate due to the volume of likes—even though this growth is artificial. Some posts are already being flagged and removed (red).*

![image](https://github.com/user-attachments/assets/db174cc3-0238-4c36-9af8-3cecc46130d8)

Step 9: Illusion of grassroots support

*As bot engagement plateaus, human users begin interacting with these highly visible posts. The human like count surpasses the bot like count, giving the illusion that the content is gaining traction organically.*

# §2. Simulation Design & Implementation

Our model consists of agents interacting within a spatial grid environment to simulate the dynamics of social media recommendation algorithm-style amplification. The agents are Bot Amplifiers, who are tasked with liking Posts in order to amplify them; Human Users, who simulate real human social media users; and Content Moderators, who are tasked with looking for suspicious amplification and, with sufficient reason, banning bots and taking down Posts. Although Posts do not perform like actors, they are also considered agents in the system due to the way they interact with and influence other agents. A Post’s visibility changes dynamically as it accumulates engagement, and its reach directly affects the behaviour of Human Users. This central role in the feedback loop between engagement and exposure makes Posts essential to the emergent system behaviour, even though they do not act on their own.

The simulation takes place on a MultiGrid, where multiple agents can occupy the same grid cell. Posts are placed statically on the grid and do not move throughout the simulation. Human Users and Bot Amplifiers, by contrast, are mobile agents that move randomly across the grid. A Post has an influence radius, which determines how far its visibility extends across the grid. In each step, a Human User can encounter any Post whose influence radius encompasses their current cell. This simulates a social media “For-You” page style interaction, where a Post is more likely to appear to a Human User the more likes it has. The influence radius increases with the number of likes a Post receives—regardless of whether those likes come from bots or humans—creating a feedback loop where initial engagement leads to greater exposure. While the influence radius is implemented as a literal distance within the grid (i.e., spatial proximity), it functions as an abstraction for algorithmic visibility, modelling how platforms recommend popular content to a wider audience.

The key parameters at the start of the simulation are the initial number of Bots, Human Users, and Posts, which each impact the degree and success of astroturfing. A higher number of Bot Amplifiers increases the number of likes that can be artificially applied to Posts early in the simulation. This can in turn boost the influence radius of those Posts, increasing their visibility to Human Users. The number of Human Users affects how much organic interaction can occur, and the number of Posts sets the density and distribution of content across the grid. These parameters shape the emergent behavior of the system and allow for the simulation of different environments, from bot-heavy manipulation campaigns to more balanced content ecosystems.

A Bot Amplifier’s rule-based interaction is designed to simulate strategic engagement rather than indiscriminate liking. Instead of liking every Post it sees, each Bot Amplifier likes a subset of Posts—currently set to 25%. This staggered liking behavior helps simulate coordinated bot activity that is attempting to appear more human-like and evade detection. Bots are not hardcoded to act identically every round, and the selection of liked Posts is randomized per bot, simulating decentralized or noisy coordination. As new Posts are introduced to the system, Bot Amplifiers check to ensure that the Posts they have liked aren't being banned too quickly. If they detect a high rate of takedowns among their liked content, the Bot Amplifier enters a "safe mode," where it becomes more cautious in its rate of likes. This rule models the adaptive behaviour of bots that are aware of moderation risks and adjust their behaviour accordingly.

As mentioned, Human Users interact with a Post when its influence radius is sufficiently large to reach them. Once a Human User encounters a Post, they make a decision to like it based on a `chance_to_like` parameter.  If they like the post, their like contributes to the Post’s reach in the same way as a bot’s like. This equivalence reflects the way many social media algorithms treat engagement data, where a like is added to the post regardless of who gave it. The Post does not distinguish between a Bot Amplifier and a Human User—the like is treated as an identical unit of value, and the influence radius grows accordingly.

The Content Moderator is responsible for evaluating Posts and removing those that appear suspicious. The primary criteria for suspicion is the like rate of a Post—defined as the number of likes it receives per step—relative to a threshold determined by the moderation intensity. Moderation intensity varies based on a Post’s position on the x-axis of the grid. On the far left side of the grid, moderation intensity is set to 0%, meaning Posts in that region are never removed, regardless of how fast they gain likes. On the far right, moderation intensity is 100%, meaning even modest rates of engagement can trigger a takedown. Between these extremes, the intensity scales linearly with the Post’s x-axis position. This creates a spectrum of enforcement across the grid and allows for testing different content environments—ranging from highly moderated to completely unmoderated—within the same simulation. If a Post’s like rate exceeds the threshold determined by its x-position, it is banned by the Content Moderator. Once banned, the Post is removed from the grid entirely, and all likes—both human and bot—are erased. This models the way platforms often remove content based on suspicious or abnormal activity, cutting off visibility and resetting its impact.

For the scheduler, we used the `agents.shuffle_do("step")`, which is the newer version of `RandomActivation`. This causes a random shuffle of Human Users, Bot Amplifiers, and Content Moderators each step. Each agent takes one action per timestep: Human Users decide whether to like visible Posts, Bot Amplifiers execute their staggered liking strategy or enter safe mode, and Content Moderators check Posts for abnormal like rates. The rationale for the scheduler used is that the random shuffle simulates the unpredictable and asynchronous sequence of events that takes place in a real social media environment. In practice, social media interactions do not occur in a fixed or deterministic order. People log on at different times, bots are scheduled or randomized, and moderation may act immediately or with delay. Using a shuffled schedule avoids introducing artificial patterns of causality and maintains fairness in activation while still incorporating randomness. Bot-to-bot interactions in the simulation are not always direct, but instead emerge implicitly through interactions between the agents. Given the rival goals of the Bot Amplifiers and the Content Moderators, there is an emergent tug-of-war between the two agents, where one tries to effectively amplify and the other tries to take down suspicious Posts. Additionally, Bot Amplifiers and Human Agents interact with posts as a kind of conduit, where the Bot Amplifiers are able to boost a Post and increase its visibility, creating enough exposure for a Post to come into the view of a Human Agent.

The data being collected in each simulation consists of the total number of likes by Human Users and the total number of likes by Bot Amplifier users, recorded at each step. These data allow us to trace how overall engagement in the system evolves, how much of it comes from artificial sources versus organic ones, and how interventions like content removal affect aggregate engagement metrics. When a Post is taken down, all associated likes are stripped from the system, leading to a drop in both human and bot likes. 

The simulation is designed to capture the dynamics of amplification, manipulation, and moderation. Through the interaction of Posts, Bot Amplifiers, Human Users, and Content Moderators, the model illustrates how rule-based agents can produce realistic patterns of content visibility and strategic adaptation. The use of a spatial grid provides a clear and intuitive abstraction of algorithmic reach, while the influence radius, staggered liking, and moderation intensity encode the core mechanics of recommendation systems and enforcement mechanisms. Together, these elements allow the model to simulate key dynamics in algorithmically curated media ecosystems.


# §3. Observation and Results

This section presents the simulation results of astroturfing dynamics under various bot behavior conditions. We analyze how the presence, quantity, and adaptability of bots influence both human engagement and the effectiveness of moderation mechanisms.
________________________________________
# 3.1 Overview

Our simulations model the spread and suppression of artificially boosted content through bot amplification and content moderation. We tested three main configurations:
1.	No Bot Adaptation (baseline)
2.	Bot Adaptation Enabled
3.	Extreme Bot Configurations (very high or low bot-to-human ratios)
   
Each simulation was run using a consistent setup of 100x100 grid space, 100 human agents, 10 posts (with new posts introduced every 10 steps), and either 25 bots, 15 bots, or 100 bots depending on the scenario.
________________________________________
**3.2 No Bot Adaptation**

In this baseline setting, bots uniformly amplify posts regardless of their position or moderation risk.

**Step 12:** Initial posts received rapid boosts from bots, and several were quickly flagged and banned. Red dots in the far right region illustrate effective early detection. As bots show no risk aversion, their actions frequently trigger moderation.

![image](https://github.com/user-attachments/assets/d79e529d-3c16-46d3-8625-90b237e12ef1)

**Step 28:** Bot activity remains constant across the grid. While new posts continue to appear, a noticeable fraction (especially on the right) are banned early. Smaller red posts suggest detection before significant amplification occurs. Human likes increase once bot-influenced posts grow large enough to enter human influence radius.

![image](https://github.com/user-attachments/assets/f53b3e67-add3-4abb-bc56-75e53f6c80c8)

**Step 105:** A steady stream of bans persists. Some posts avoid detection, particularly those seeded toward the left or center. The system achieves a dynamic equilibrium: posts rise, attract bots, and are either banned or remain if they grow subtly. Bot likes stabilize as moderation throttles bot efficacy. Human engagement climbs significantly over time as surviving posts reach sufficient visibility.

![image](https://github.com/user-attachments/assets/e7204c29-1c4b-47ef-8bbe-f698d85893cf)

**Interpretation:** In the absence of adaptation, bots play an aggressive role, often triggering moderation. The system moderately suppresses astroturfing, but detection blind spots remain, especially in under-moderated regions.
________________________________________
**3.3 Bot Adaptation Enabled** 

Here, bots enter "safe mode" after their likes contribute to banned posts. In this mode, they limit their activity to low-risk regions (left side of the grid).

Step 12: Bot adaptation begins. Few posts are banned early, suggesting bots quickly identify and avoid high-moderation zones. The grid exhibits a spatial shift: most orange (amplified) posts emerge on the left. Small right-side posts remain unamplified.

![image](https://github.com/user-attachments/assets/3b8eb56e-3423-486d-868e-da3a3233b159)


**Step 28:** Adaptation intensifies. Nearly all boosted content appears in moderation-safe zones. The right-side is effectively "avoided" by bots, which correlates with reduced detection and fewer red posts. Human engagement is improved slightly, as bots now avoid posts likely to be banned.

![image](https://github.com/user-attachments/assets/ed0d7ef6-1d5d-420a-9ce7-0ddf22afd47f)


**Step 105:** The adaptation mechanism fully stabilizes. Amplification is now geographically constrained. Bots avoid bans and persistently grow posts in safe regions. Human likes outpace bot likes over time. This could reflect increased human exposure to long-lived, bot-boosted posts. Bans still occur but at lower frequencies.

![image](https://github.com/user-attachments/assets/15bd52d7-7989-4dac-96c0-40095d5d5449)

**Interpretation:** Adaptation enables bots to evade detection effectively. While this may reduce moderation success, it also avoids the aggressive surges that attract human moderators. The system demonstrates emergent spatial self-regulation: bots herd in low-risk zones, making moderation more difficult.
________________________________________
**3.4 Extreme Bot Configurations**

**High Bot Count (100 bots, 1 human):** Even with adaptation enabled, the sheer number of bots makes evasion nearly impossible. The moderation system successfully detects and removes the majority of manipulated posts, as the scale of bot activity draws clear patterns of suspicion. Red posts are widespread, demonstrating this. 

![image](https://github.com/user-attachments/assets/9599a76f-8d4c-45b5-9d4c-e1c8586d3a59)

**Interpretation:** There exists a critical threshold above which adaptation fails. Bot saturation overrides adaptive behavior, creating a content flood that the moderator easily catches. 

**Low Bot Count (15 bots, 100 humans):** In this configuration, bots successfully avoid detection entirely. Amplification occurs stealthily, never crossing moderation thresholds. Posts persist and grow slowly, offering ideal conditions for gradual human engagement.

![image](https://github.com/user-attachments/assets/b0679ef2-257b-4b62-9e90-1f756eac011b)

**Interpretation:** Below a certain bot-to-human ratio, bot influence becomes indistinguishable from organic behavior. The system's moderation fails to identify manipulation, allowing astroturfing to proceed undetected. Interestingly, increasing to 20 bots resumes detection, suggesting a fragile boundary between stealth and exposure.
________________________________________
**3.5 Emergent Behaviors and Surprises**

•	Geographic Avoidance: Bots organically migrate toward low-risk zones without explicit spatial logic. This reflects an emergent behavior based on moderation pressure.

•	Post Lifespan Shifts: Adaptive bot behavior prolongs the lifespan of posts. This results in more human exposure and higher human engagement.

•	Suppressed Human Activity: In non-adaptive or highly bot-dominant runs, human engagement is stifled due to the early banning of posts, reducing opportunities for humans to interact with content.
________________________________________
**3.6 Conclusion**

The simulation demonstrates the delicate interplay between bot strategies and moderation effectiveness. Non-adaptive bots are easily caught but still exert considerable influence before bans. Adaptive bots, however, learn to survive, avoiding detection and amplifying content in low moderation zones. 
These findings offer real-world insights into how malicious actors might evade platform moderation using simple adaptive logic, and where current moderation schemes may fall short in identifying more subtle or geographically constrained astroturfing campaigns

# §4. Ethical & Societal Reflections

## Ethical Considerations

Because this simulation does not incorporate real user data or scraped social media content, there were no direct privacy or data usage issues encountered during the project. All agents and behaviours are entirely synthetic and rule-based, designed to abstract key features of social media dynamics without requiring actual personal or behavioural data. Posts, Human Users, and Bot Amplifiers are defined through internal parameters rather than real-world identifiers or histories, and the simulation operates on a self-contained grid rather than drawing on live social network structures. Nevertheless, the simulation engages with scenarios that touch on real-world phenomena, including algorithmic manipulation and content moderation, which raise important ethical questions by analogy.

One major ethical consideration is how this kind of modelling could be misused. Although our implementation is intended as a research and teaching tool, the logic embedded in the simulation—particularly the modelling of amplification dynamics and moderation thresholds—could conceivably be repurposed to test strategies for evading detection or maximizing the spread of disinformation. For example, the concept of bots entering "safe mode" in response to bans closely resembles tactics observed in real disinformation campaigns, where malicious actors adapt their timing, language, or coordination strategies based on platform feedback. Simulations like this can serve both beneficial and harmful ends, depending on who uses them and for what purpose. While we do not use or integrate real-world datasets, the behavior patterns we abstract can offer insights into vulnerabilities in current platform design and moderation policies, which could be exploited if taken out of ethical context.

Further, although the simulation avoids direct privacy risks, it indirectly raises questions about data transparency and algorithmic opacity in real media ecosystems. Platforms like TikTok, Facebook, and Twitter do not disclose exactly how recommendation algorithms weigh engagement, nor how moderation thresholds are determined or adapted. As Zeynep Tufekci (2015) argues, such algorithmic systems increasingly shape public discourse while evading meaningful scrutiny, creating what she calls “computational agency” where users are subject to invisible nudges and feedback loops. By modelling these mechanisms in simplified, inspectable form, our simulation can illuminate the kinds of assumptions that may be baked into real systems—often invisibly. In that sense, it also provides an ethical opportunity: to expose and demystify the logic behind amplification and moderation, helping scholars and developers alike reflect on how such systems should be designed or regulated in the public interest.

## Societal Implications

At the societal level, the model illustrates how a relatively small number of coordinated bots can exert disproportionate influence on content visibility, even in environments with many more Human Users. This aligns closely with real-world research showing how manipulation campaigns—whether for commercial, political, or ideological purposes—can exploit recommendation systems to surface inauthentic content. By amplifying a post early and increasing its initial visibility, bots can trigger feedback loops where real users engage with content they might otherwise never have seen. This dynamic occurs not through deception alone, but through the mechanical operation of visibility thresholds and recommendation incentives, which are often agnostic to authenticity. The simulation helps explain why detection and mitigation of these strategies are so challenging: once human engagement has been sparked by artificial amplification, distinguishing organic virality from manipulation becomes increasingly difficult.

This has implications at the micro, meso, and macro levels. On the micro level, individual users may unknowingly engage with, share, or internalize content that has been surfaced through manipulation rather than merit. On the meso level, groups or communities may experience shifts in discourse, polarization, or engagement norms due to repeated exposure to inauthentically amplified narratives. And on the macro level, institutions—such as media outlets, public health authorities, or democratic governments—may face degraded trust or legitimacy when platform dynamics amplify fringe voices or coordinated propaganda.

The simulation also models uneven enforcement by encoding moderation intensity as a function of spatial location. This reflects how, in practice, moderation is often inconsistently applied across topics, languages, and geographic regions. Research on real-world platforms shows that some political or cultural contexts receive rigorous enforcement, while others are overlooked due to lack of resources, expertise, or will. By making this gradient explicit in the simulation, we are able to observe how moderation asymmetry can itself shape content dynamics—permitting some manipulation to thrive while suppressing other content that may not be harmful at all. This raises important questions about fairness, bias, and accountability in automated content governance.

While the dynamics modeled in the simulation are stylized, they are strongly grounded in empirical observations. Bot behaviour such as staggered liking, retreat after takedown, and targeting visibility thresholds have all been documented in real-world influence campaigns. Likewise, human susceptibility to popularity signals—particularly when platform affordances such as like counts and trending labels are present—is a well-established feature of online behaviour. By abstracting these features into a simplified model, the simulation helps clarify how they interact over time, and what structural vulnerabilities they may reveal in media ecosystems governed by opaque algorithms.

# §5. Lessons Learned & Future Directions

________________________________________
**5.1 Design and Development Reflections**

Designing a simulation of astroturfing behavior using agent-based modeling (ABM) presented several key challenges, particularly around capturing the subtlety of bot strategies and the complex interactions between amplification and moderation. One of the earliest difficulties was ensuring that bots could realistically influence post visibility while also triggering detection mechanisms in a dynamic way. We needed to strike a balance where bots were neither overpowered nor completely ineffective.

A major technical hurdle was designing a content moderation mechanism that could meaningfully respond to the evolving behavior of bots. Since our goal was to simulate emergent behaviors, we deliberately avoided hardcoding any central coordination among bots. This forced us to rely on simple heuristics—like post location or like rate—as proxies for moderation triggers. Tuning these heuristics to allow for both successful and failed moderation outcomes required repeated testing and adjustment.

Implementing adaptive bot behavior was one of the most intellectually engaging parts of the project. Our bots began in a naive state, but after contributing to banned posts, they shifted into a "safe mode" where they limited amplification to under-moderated zones. This required storing state within each bot and tracking banned post histories. The challenge here was not the implementation itself, but achieving a behavior that felt emergent rather than deterministic.


**5.2 Model Limitations & Areas for Improvement**

Our model, while illustrative, simplifies several aspects of real-world astroturfing. Most notably, the bots in our simulation operate without any sophistication beyond random sampling and basic positional filtering. In reality, bots often exploit trends, language models, and coordinated timing to enhance influence. Introducing more complex behaviors like coordinated botnets or reinforcement learning agents could significantly improve realism.

The moderation model also operates on relatively simple heuristics based on post location and like rate. In practice, moderation systems are more nuanced and may rely on user reports, metadata, or behavioral histories. Expanding the moderation framework to include these variables would make the simulation more robust.
Another limitation is that our human users are passive and act only based on local influence. While this captures a core mechanism of information spread, it omits higher-order social dynamics such as trust networks, or individual susceptibility to persuasion. Incorporating a network structure among humans could allow us to study how astroturfing cascades through connected groups.
From a computational perspective, our model scales well to small and medium agent populations but would likely struggle with large-scale simulations (e.g., thousands of posts and users). Optimizing agent selection could help improve performance.


**5.3 Future Applications**

The findings from this project suggest several avenues for future application. First, our results could inform social media platform policy. For instance, our observation that bots shift amplification behavior away from heavily moderated regions suggests that platforms could benefit from dynamic moderation schemes that adapt in response to behavioral shifts.
Second, the model offers insight for AI safety and adversarial behavior research. The concept of agents adapting their behavior to avoid detection parallels real-world adversarial strategies. Studying these dynamics in a controlled simulation can help inform the design of more resilient moderation algorithms.
Third, this model has educational potential as a tool to demonstrate how online manipulation operates at scale. Simplifying the interface for interactive classroom use could help communicate the risks of astroturfing to non-technical audiences.
Lastly, future extensions could explore coordinated bot activity (e.g., botnets) and countermeasures like decentralized moderation or collective human response. This could support the development of decentralized governance systems that are both resilient and democratic.
In sum, while the current model provides a strong foundation for illustrating astroturfing dynamics, there is considerable potential for future development both as a research tool and as a foundation for practical intervention strategies.

# §6. References

Keller, F. B., Schoch, D., Stier, S., & Yang, J. (2020). Political Astroturfing on Twitter: How to
Coordinate a Disinformation Campaign. Political Communication, 37(2), 256–280.
https://doi.org/10.1080/10584609.2019.1661888

Radivojevic, K., McAleer, C., Conley, C., Kennedy, C., & Brenner, P. (2024, September 27). Social Media Bot Policies: Evaluating passive and active enforcement. arXiv.org. https://arxiv.org/abs/2409.18931 

Tufekci, Zeynep. (2015). Algorithmic harms beyond facebook and google: emergent challenges of computational agency. _Colorado Technology Law Journal, 13(2),_ 203-218.

Zerback, T., Töpfl, F., & Knöpfle, M. (2021). The disconcerting potential of online
disinformation: Persuasive effects of astroturfing comments and three strategies for
inoculation against them. New Media & Society, 23(5), 1080–1098.
https://doi.org/10.1177/1461444820908530

Chan, J. (2022b). Online astroturfing: A problem beyond disinformation. Philosophy &amp; Social Criticism, 50(3), 507–528. https://doi.org/10.1177/01914537221108467 


# §7. Attestation

This final report represents a collaborative effort by all group members, with clear and substantial contributions from each participant. The following summary outlines the specific roles and responsibilities undertaken by Aziz and Dov in accordance with the Contributor Role Taxonomy (CRediT).
## Aziz   
- **Writing – Original Draft** – Authored Sections 1, 3 , and 5, including the explanation of agent behaviours, simulation design choices, and interpretation of key results.  
- **Software** – Contributed to development of the Mesa model by writing key components related to bot behaviour and the logic for the proliferation of posts during the simulation.   
- **Investigation** – Designed and executed multiple simulation runs, collecting and interpreting the resulting data to support the findings discussed in the report.  
- **Visualization** – Assisted in formatting figures and explaining visualizations within the Method and Results sections. 
- **Validation** – Debugged and tested various simulation configurations to ensure stability and consistency of results.  
- **Review & Editing** – Provided detailed feedback on drafts of Sections 2 and 4, ensuring coherence and clarity across the full report.
## Dov  
- **Conceptualization** – Participated in developing the overall direction of the simulation, helping to shape the research questions and goals. 
- **Software** – Contributed to the implementation of the simulation using the Mesa framework. Built the architecture for agent movement, amplification dynamics, and content moderation logic. 
- **Writing – Original Draft** – Wrote Sections 2  and 4, with a focus on explaining the architecture of the model and analyzing its broader implications.  
- **Validation** – Debugged and tested various simulation configurations to ensure stability and consistency of results.  
- **Review & Editing** – Reviewed and refined Sections 1, 3, and 5, offering improvements to structure and language, and ensuring technical accuracy of descriptions relating to the simulation logic.

Both Aziz and Dov were actively involved in project planning and communication throughout the process. They collaborated closely during model development and report writing, holding regular check-ins to ensure alignment and shared responsibility for the overall success of the project.




