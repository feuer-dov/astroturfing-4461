from model import AstroturfingModel
import matplotlib.pyplot as plt


model = AstroturfingModel()

for i in range(100):
    print(f"\n--- Step {i} ---")
    model.step()
    for post in model.posts:  # prints the post info
        post.print_info()
        
data = model.datacollector.get_model_vars_dataframe()
data[["Total_Bot_Likes", "Total_Human_Likes"]].plot()
plt.title("Total Likes Over Time by Entity Type")
plt.xlabel("Time Step")
plt.ylabel("Total Likes")
plt.legend()
plt.show()

