from model import AstroturfingModel

model = AstroturfingModel()

for i in range(3):
    print(f"\n--- Step {i} ---")
    model.step()
    for post in model.posts:
            post.print_info()