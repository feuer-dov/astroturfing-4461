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

**Step 28:** Bot activity remains constant across the grid. While new posts continue to appear, a noticeable fraction (especially on the right) are banned early. Smaller red posts suggest detection before significant amplification occurs. Human likes increase once bot-influenced posts grow large enough to enter human influence radii.

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

**High Bot Count (100 bots, 1 human):** Despite adaptation being enabled, the overwhelming presence of bots leads to excessive post amplification. The moderation system is quickly saturated. Red posts proliferate, and bot likes dominate. Human engagement is negligible. Detection still functions to a degree but cannot match the scale of manipulation.

![image](https://github.com/user-attachments/assets/9599a76f-8d4c-45b5-9d4c-e1c8586d3a59)

**Interpretation:** There exists a critical threshold above which moderation collapses. Bot saturation overrides adaptive behavior, creating a content flood that moderation cannot suppress fast enough.

**Low Bot Count (15 bots, 100 humans):** In this configuration, bots successfully avoid detection entirely. Amplification occurs stealthily, never crossing moderation thresholds. Posts persist and grow slowly, offering ideal conditions for gradual human engagement.

![image](https://github.com/user-attachments/assets/b0679ef2-257b-4b62-9e90-1f756eac011b)

**Interpretation:** Below a certain bot-to-human ratio, bot influence becomes indistinguishable from organic behavior. The system's moderation fails to identify manipulation, allowing astroturfing to proceed undetected. Interestingly, increasing to 20 bots resumes detection, suggesting a fragile boundary between stealth and exposure.
________________________________________
**3.5 Emergent Behaviors and Surprises**

•	Geographic Avoidance: Bots organically migrate toward low-risk zones without explicit spatial logic. This reflects an emergent behavior based on moderation pressure.

•	Post Lifespan Shifts: Adaptive bot behavior prolongs the lifespan of posts. This results in more human exposure and higher human engagement.

•	Detection Saturation: A high enough bot population overwhelms moderation, even with adaptation enabled.

•	Suppressed Human Activity: In non-adaptive or highly bot-dominant runs, human engagement is stifled due to the early banning of posts, reducing opportunities for humans to interact with content.
________________________________________
**3.6 Conclusion**

The simulation demonstrates the delicate interplay between bot strategies and moderation effectiveness. Non-adaptive bots are easily caught but still exert considerable influence before bans. Adaptive bots, however, learn to survive and thrive under pressure, avoiding detection and amplifying content in moderation shadows. At extreme scales, bot activity can still override adaptation or overwhelm detection systems.
These findings offer real-world insights into how malicious actors might evade platform moderation using simple adaptive logic, and where current moderation schemes may fall short in identifying more subtle or geographically constrained astroturfing campaigns


# §5. Lessons Learned & Future Directions

________________________________________
**5.1 Design and Development Reflections**

Designing a simulation of astroturfing behavior using agent-based modeling (ABM) presented several key challenges, particularly around capturing the subtlety of bot strategies and the complex interactions between amplification and moderation. One of the earliest difficulties was ensuring that bots could realistically influence post visibility while also triggering detection mechanisms in a dynamic way. We needed to strike a balance where bots were neither overpowered nor completely ineffective.

A major technical hurdle was designing a content moderation mechanism that could meaningfully respond to the evolving behavior of bots. Since our goal was to simulate emergent behaviors, we deliberately avoided hardcoding any central coordination among bots. This forced us to rely on simple heuristics—like post location or like rate—as proxies for moderation triggers. Tuning these heuristics to allow for both successful and failed moderation outcomes required repeated testing and adjustment.

Implementing adaptive bot behavior was one of the most intellectually engaging parts of the project. Our bots began in a naïve state, but after contributing to banned posts, they shifted into a "safe mode" where they limited amplification to under-moderated zones. This required storing state within each bot and tracking banned post histories. The challenge here was not the implementation itself, but achieving a behavior that felt emergent rather than deterministic.

We also faced integration issues between the model logic and visualization tooling. For instance, sliders and real-time simulation tuning sometimes behaved unexpectedly or did not fully reset internal state. While these were mostly technical bugs, they reminded us of the importance of robustness in user-facing modeling tools.

**5.2 Model Limitations & Areas for Improvement**

Our model, while illustrative, necessarily simplifies several aspects of real-world astroturfing. Most notably, the bots in our simulation operate without any sophistication beyond random sampling and basic positional filtering. In reality, bots often exploit trends, language models, and coordinated timing to enhance influence. Introducing more complex behaviors like coordinated botnets or reinforcement learning agents could significantly improve realism.

The moderation model also operates on relatively simple heuristics based on post location and like rate. In practice, moderation systems are more nuanced and may rely on user reports, metadata, or behavioral histories. Expanding the moderation framework to include these variables would make the simulation more robust.
Another limitation is that our human users are passive and act only based on local influence. While this captures a core mechanism of information spread, it omits higher-order social dynamics, such as homophily, trust networks, or individual susceptibility to persuasion. Incorporating a network structure among humans could allow us to study how astroturfing cascades through connected groups.
From a computational perspective, our model scales well to small and medium agent populations but would likely struggle with large-scale simulations (e.g., thousands of posts and users). Optimizing agent selection and modularizing updates could help improve performance.
In future work, we also hope to integrate real-world datasets to calibrate parameters (e.g., bot-to-human ratios, like rates, moderation thresholds). This would allow for both greater external validity and meaningful comparisons with observed data.

**5.3 Future Applications**

The findings from this project suggest several avenues for future application. First, our results could inform social media platform policy. For instance, our observation that bots shift amplification behavior away from heavily moderated regions suggests that platforms could benefit from dynamic moderation schemes that adapt in response to behavioral shifts.
Second, the model offers insight for AI safety and adversarial behavior research. The concept of agents adapting their behavior to avoid detection parallels real-world adversarial strategies. Studying these dynamics in a controlled simulation can help inform the design of more resilient moderation algorithms.
Third, this model has educational potential as a tool to demonstrate how online manipulation operates at scale. Simplifying the interface for interactive classroom use could help communicate the risks of astroturfing to non-technical audiences.
Lastly, future extensions could explore coordinated bot activity (e.g., botnets) and countermeasures like decentralized moderation or collective human response. This could support the development of decentralized governance systems that are both resilient and democratic.
In sum, while the current model provides a strong foundation for illustrating astroturfing dynamics, there is considerable potential for future development both as a research tool and as a foundation for practical intervention strategies.


# § Citations

Radivojevic, K., McAleer, C., Conley, C., Kennedy, C., & Brenner, P. (2024, September 27). Social Media Bot Policies: Evaluating passive and active enforcement. arXiv.org. https://arxiv.org/abs/2409.18931 

Zerback, T., Töpfl, F., & Knöpfle, M. (2021). The disconcerting potential of online
disinformation: Persuasive effects of astroturfing comments and three strategies for
inoculation against them. New Media & Society, 23(5), 1080–1098.
https://doi.org/10.1177/1461444820908530


Keller, F. B., Schoch, D., Stier, S., & Yang, J. (2020). Political Astroturfing on Twitter: How to
Coordinate a Disinformation Campaign. Political Communication, 37(2), 256–280.
https://doi.org/10.1080/10584609.2019.1661888

