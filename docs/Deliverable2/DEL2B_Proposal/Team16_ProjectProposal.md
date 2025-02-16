# Is the Grass Too Green?: A Study on Astroturfing
### Dov FEUER
### Aziz DURDYKLYCHEV
## https://github.com/feuer-dov/astroturfing-4461/tree/main

## Section 1: Phenomena of Interest
The phenomena that our group has chosen is astroturfing, the illusion of grassroots support or dissent, particularly on social media, and how bots can be used to interact with each other and with bot generated content to create this illusion. This topic is directly relevant to the course themes, which explores the effects of social bots, their interaction with human agents, and the entities within a social media ecosystem’s trophic structure which interact with one another. It further relates to the notion of a goal hierarchy, where each attempt at astroturfing can be characterized by low-level action (i.e., posting AI generated content, or reposts from fake accounts), intermediate behaviour (i.e., campaign to promote product or elect a political candidate), and high-level goals (dishonest brand promotion or building a perception of grassroots support for a political party).

## Section 2: Phenomena of Interest

> Keller, F. B., Schoch, D., Stier, S., & Yang, J. (2020). Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign. Political Communication, 37(2), 256–280. https://doi.org/10.1080/10584609.2019.1661888

Using the published court records elucidating a disinformation campaign carried out by the  South Korean National Information Service (NIS) in support of a certain presidential candidate in 2012, Keller et al. attempt to ground disinformation campaign detection more firmly in social science. Instead of focusing on the characteristics of certain accounts, this paper looks at the traces left by the coordination among astroturfing agents to identify additional likely astroturfing accounts. Further, it provides the details of one of the first online disinformation campaigns with offline information to help identify the accounts used. The paper also measures the impact of such a campaign, with metrics showing that the campaign actually had a limited impact.

> Zerback, T., Töpfl, F., & Knöpfle, M. (2021). The disconcerting potential of online disinformation: Persuasive effects of astroturfing comments and three strategies for inoculation against them. New Media & Society, 23(5), 1080–1098. https://doi.org/10.1177/1461444820908530

This paper describes a study conducted to see the effects of astroturfing and the strength of inoculation to counter it. 2,353 participants were exposed to Russian astroturfing comments on German news stories. The three topics were the poisoning of a former Russian intelligence officer, the manipulation of the 2016 US election, and the use of toxic gas by one of Russia’s allies. The study was conducted by showing the participants a fake Facebook news teaser which blamed Russia for the issue. Underneath the teaser there would be two comments which shifted the blame or offered alternative explanations that did not blame Russia. The results found that astroturfing had an effect on users' opinions and inoculation was only effective for the first two weeks. 

## Section 3: The Core Components of the Simulation

The entities for our simulation are human users, social bots tasked as amplifiers, posts, and a platform moderator bot. The simulation begins with a select number of posts, modelling real world posts created by content creators (political campaigns, marketing departments, etc.), and an average number of bots per post. This is meant to imitate how an astroturfing campaign can purchase bots to amplify content. Bots amplify by liking and sharing content in a staggered fashion as to avoid detection by a platform moderator bot. Successful amplification increases the likelihood of an authentic human user coming into contact with a post. Content moderator bots police the posts, shutting down suspected bot accounts and removing likes and shares from bot amplified posts.

Human users and amplifiers are afforded the ability to like and share, while the content moderator bot is afforded the ability to ban suspicious users and to take down the bot likes and shares on posts. The weights of each entity's parameters can be adjusted at the start of the simulation and throughout, with parameters such as human user susceptibility to bot amplified content, the number of amplification bots, the number of content moderators, etc.

In line with a user's affordances (both amplifiers and human users), an authentic user is more likely to encounter posts as the number of shares increases, which is a basic reduction of a social media algorithm. This is meant to simulate the effects of user engagement affordances on the visibility of posts, and how bot driven astroturfing can effectively amplify content to human users who, even when lacking susceptibility, may engage with the content as if it is organically generated. 

The closest mesa example model to this simulation is the Virus on a Network model, which also has a susceptibility parameter, and where posts can spread like a virus from susceptible humans to other humans, thus increasing the likelihood of infecting more people. While the Virus on a Network model deals with one virus and our simulation deals with multiple posts, the general analogy still applies well to our simulation. Another model which fits well with the content moderator bot entity is the Epstein Civil Unrest model, in which cops take on the role of arresting rebels, similar to how content moderator bot can ban a user if they are deemed a bot or take down a bot amplified post.

## Section 4: Simulation Anticipated Outcomes

The anticipated outcomes of this simulation are to show how given certain parameters and affordances, a bot driven astroturfing campaign can create authentic user engagement and participation, given a certain amount of susceptibility and a lack of strict content moderation. 

By adjusting the parameters we anticipate that even with a low level of susceptibility, bot driven astroturfing may be able to generate authentic support and human amplification, resulting in high levels of authentic human interaction, where a human user interacts with the post as if it has had no bot amplification. Although we expect high levels of content moderation to kill an astroturfing campaign, there is the potential for strict moderation to have other negative side effects undesirable for any social media company, such as incorrect determinations and bans, accusations of excessive censorship, etc. For the purposes of this simulation, stricter content moderation will likely result in curbing astroturfing campaigns, contingent on accurate and thorough content moderation defined in the parameters. As the number of bots and staggering techniques increase, the content moderator bots will have a more difficult time taking down inauthentic users and removing likes and shares on amplified posts. 

![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUffxQnrA1N7ca-ojVXE8ulN6lrs5ZLCoaF6rX7df43C_IPEL7XY4HYkf86l6KQKqM_u5LUfSlnOx2Q_jRjNkfulWoUholGGlsSkldLYrArd3AxZfwKyyoZbyp9XJV6Enc4R5TQ-bg=s2048?key=FtZKb4yEuhiKB7TFCrxaRGuN "Points scored")
*Potential line graph of a simulation result, where a successful astroturfing campaign results in a high number of authentic human users liking and sharing posts.*

![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdwZWxjbqPXf9eNLxjU8A29ox5oiO8wXWbl4lpquVPJ1HS1Tvf-o0MiabHVVWyTy6DSuDDSzBL1CPVlfp_V2a7Zs-zsg47Lt47Gcl2YVlXOl2OuONGTe_J390ZWFZumThPGhT2k0Q=s2048?key=FtZKb4yEuhiKB7TFCrxaRGuN)
*The Virus on a Network visual result, similar to how authentic human users can interact with astroturfed posts and engage with them positively.*


