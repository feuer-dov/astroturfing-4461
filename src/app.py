import pandas as pd
from model import AstroturfingModel
import matplotlib.pyplot as plt


def run_simulation(steps=20, **model_kwargs):
    model = AstroturfingModel(**model_kwargs)
    for _ in range(steps):
        model.step()
    return model.datacollector.get_model_vars_dataframe()

# Run multiple simulations
all_runs = []

for i in range(100):  # Runs the model 100 times
    df = run_simulation(steps=30, num_bots=10, num_humans=20, num_posts=5, grid_size=100)
    df["Run"] = i  
    all_runs.append(df)

result_df = pd.concat(all_runs)

avg_likes = result_df.groupby(result_df.index)[["Total_Human_Likes", "Total_Bot_Likes"]].mean()

avg_likes.plot()
plt.title("Average Likes over Time (100 runs)")
plt.xlabel("Step")
plt.ylabel("Average Likes")
plt.legend()
plt.show()