from model import AstroturfingModel
import matplotlib.pyplot as plt
from agent import HumanUser, BotAmplifier, PostAgent

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

model = AstroturfingModel()


def run_simulation_with_plot():
    model = AstroturfingModel()
    for i in range(5):
        print(f"\n--- Step {i} ---")
        model.step()
        for post in model.posts:
            post.print_info()

    # Plot total bot vs. human likes
    data = model.datacollector.get_model_vars_dataframe()
    data[["Total_Bot_Likes", "Total_Human_Likes"]].plot()
    plt.title("Total Likes Over Time by Entity Type")
    plt.xlabel("Time Step")
    plt.ylabel("Total Likes")
    plt.legend()
    plt.show()

def launch_visual_grid():
    def agent_portrayal(agent):
        if isinstance(agent, HumanUser):
            return {"Shape": "circle", "Color": "blue", "r": 0.5, "Layer": 1}
        elif isinstance(agent, PostAgent):
            size = max(0.2, agent.visibility)
            return {"Shape": "rect", "Color": "red", "w": size, "h": size, "Layer": 0}
        elif isinstance(agent, BotAmplifier):
            return {"Shape": "circle", "Color": "green", "r": 0.4, "Layer": 1}

    grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

    server = ModularServer(
        AstroturfingModel,
        [grid],
        "Astroturfing Simulation",
        {}
    )
    server.port = 8530
    server.launch()

# --- Run either or both ---
if __name__ == "__main__":
    # Run simulation & show chart
    run_simulation_with_plot()

    # Launch the grid (optional)
    launch_visual_grid()

