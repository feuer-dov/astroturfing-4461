from mesa import Model
from agent import BotAmplifier, HumanUser


class Post:
    def __init__(self, post_id):
        self.likes = 0
        self.post_id = post_id
        self.visibility = 0
    
    def add_like(self):
        self.likes += 1
        self.visibility = min(0.05 * self.likes, 1.0)
    
class AstroturfingModel(Model):
    def __init__(self):
        super().__init__()
        self.posts = [Post(post_id=i) for i in range(20)]

        agent_id = 0

        # Create bots
        for i in range(3):
            bot = BotAmplifier(model=self)
            agent_id += 1

        # Create humans
        for i in range(3):
            human = HumanUser(model=self)
            agent_id += 1

    def step(self):
        self.agents.shuffle_do("step")

