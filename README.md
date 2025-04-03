# astroturfing-4461

## §A. Overview of the phenomenon 
This simulation models astroturfing, a form of artificial online influence where bots amplify content to simulate grassroots popularity. Using agent-based modeling, we explore how bot-driven manipulation can boost posts, influence human engagement, and evade or adapt to moderation. The simulation demonstrates the emergence of organic-looking popularity from inauthentic origins, the role of content moderators, and the strategic adaptation of bots to avoid detection.

## §B. How to run the simulation
1. Clone the repository from Github, and create a python virtual environment.
2. Install the requirements: `pip install -r requirements.txt`
3. To run the solara visualization, execute `solara run src/visualize.py`
4. (Optional) To run the simulation n number of times and to see the average results, execute `python src/app.py`

## §C. Key findings.

- Bots can rapidly inflate post visibility, triggering human engagement.
- Content moderators are effective at detecting early surges, especially in high-moderation zones.
- Bots adapt by targeting low-moderation regions, reducing detection.
- A small number of bots can evade moderation entirely; too many bots trigger mass post removal.
- Human-like engagement can emerge from artificial origins, masking manipulation.
