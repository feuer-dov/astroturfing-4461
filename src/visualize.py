from mesa.visualization import make_plot_component, make_space_component, SolaraViz, Slider
from model import AstroturfingModel
from agent import HumanUser, PostAgent, BotAmplifier

def astroturfing_portrayal(agent):
    if isinstance(agent, HumanUser):
        return {"color": "blue", "size": 30, "layer": 1}
    elif isinstance(agent, PostAgent):
        size = agent.get_visual_size()
        return {"color": "red", "size": size, "layer": 0}

space_component = make_space_component(astroturfing_portrayal, draw_grid=False)
chart_component = make_plot_component({
    "Total_Bot_Likes": "blue",
    "Total_Human_Likes": "orange"
})

model_params = {
    "num_bots": Slider("Number of Bots", 20, 0, 100, 1),
    "num_humans": Slider("Number of Humans", 20, 1, 100, 1),
    "num_posts": Slider("Number of Posts", 5, 1, 20, 1),
    "grid_size": Slider("Grid Size", 10, 10, 150, 10),
}

model = AstroturfingModel(
    num_bots=20,
    num_humans=20,
    num_posts=5,
    grid_size=10
)

page = SolaraViz(
    model,
    components=[space_component, chart_component],
    model_params=model_params,
    name="Astroturfing Simulation"
)

page