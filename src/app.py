from model import AstroturfingModel

model = AstroturfingModel()

for i in range(3):
    print(f"\n--- Step {i} ---")
    model.step()