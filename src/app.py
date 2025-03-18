from model import AstroturfingModel

model = AstroturfingModel()

for i in range(6):
    print(f"\n--- Step {i} ---")
    model.step()
    for post in model.posts:  # prints the post info
        post.print_info()

