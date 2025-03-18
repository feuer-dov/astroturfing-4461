from mesa import Model
from agent import BotAmplifier, HumanUser


class Post:
    def __init__(self, post_id):
        self.likes = 0
        self.post_id = post_id
        self.visibility = 0
        self.liked_by = [] # Store agents who liked a post
    
    def add_like(self, agent):

        # Adds agents to the liked_by list if they arent in it
        if agent not in self.liked_by:
            self.liked_by.append(agent)
            
            self.likes += 1
            self.visibility = min(0.05 * self.likes, 1.0)
        else: 
            pass
    
        # Print out the post's details: ID, number of likes, and the list of agent unique IDs
    def print_info(self):
        liked_ids = [agent.unique_id for agent in self.liked_by]
        print(f"Post {self.post_id}: {self.likes} likes, liked by {liked_ids}")

    
class AstroturfingModel(Model):
    def __init__(self):
        super().__init__()
        self.posts = [Post(post_id=i) for i in range(20)]

        #self.agent_id = 0         I dont think these arent neccessary, mesa automatically assigns and increments ID's

        # Create bots
        for i in range(3):
            bot = BotAmplifier(model=self)
           # self.agent_id += 1

        # Create humans
        for i in range(3):
            human = HumanUser(model=self)
            #self.agent_id += 1

    def step(self):
        self.agents.shuffle_do("step")

