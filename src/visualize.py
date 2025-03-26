from mesa.visualization import make_plot_component, make_space_component, SolaraViz, Slider
from model import AstroturfingModel
from agent import HumanUser, PostAgent, BotAmplifier

# Default values
num_humans = 85
num_bots = 25
num_posts = 10

def astroturfing_portrayal(agent):
    if isinstance(agent, HumanUser):
        return {"color": "blue", "size": 30, "layer": 1}
    elif isinstance(agent, PostAgent):
        size = agent.get_visual_size()
        color = "red" if agent.removed else "orange"
        return {"color": color, "size": size, "layer": 0}

space_component = make_space_component(astroturfing_portrayal, draw_grid=False)

chart_component = make_plot_component({
    "Total_Bot_Likes": "green",
    "Total_Human_Likes": "blue",
})

model_params = {
    "num_bots": Slider("Number of Bots", num_bots, 0, 100, 1),
    "num_humans": Slider("Number of Humans", num_humans, 1, 100, 1),
    "num_posts": Slider("Number of Posts", num_posts, 1, 20, 1),
    "grid_size": Slider("Grid Size", 100, 10, 150, 10),
}

model = AstroturfingModel(
    num_bots=num_bots,
    num_humans=num_humans,
    num_posts=num_posts,
    grid_size=100
)

page = SolaraViz(
    model,
    components=[space_component, chart_component],
    model_params=model_params,
    name="Astroturfing Simulation"
)

page