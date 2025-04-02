from mesa import Model
from agent import BotAmplifier, HumanUser, PostAgent, ContentModerator
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
import random

class AstroturfingModel(Model):
    def __init__(self, num_bots=3, num_humans=20, num_posts=5, grid_size=10):
        super().__init__()
        self.grid_size = grid_size
        self.grid = MultiGrid(width=grid_size, height=grid_size, torus=False)
        self.space = self.grid
        self.num_bots = num_bots
        self.num_humans = num_humans
        self.num_posts = num_posts
        self.posts_to_like = []
        self.removed_posts = []
        self.steps = 0
        
        
        # Track removals, add implemenation
        
        
        # total number of users
        self.total_users = num_bots + num_humans
        
        self.total_bot_likes = 0
        self.total_human_likes = 0
        
        #counters for each id
        self.bot_id = 0
        self.human_id = 0
        self.post_id = 0
        
        # PostAgent setup
        self.posts = []
        for i in range(self.num_posts):
            post = PostAgent(model=self, post_id=self.post_id)
            self.post_id += 1
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(post, (x, y))
            self.posts.append(post)

    
         # Create humans
        for i in range(self.num_humans):
            chance_to_like = random.random()
            human = HumanUser(model=self, human_id=self.human_id, chance_to_like=chance_to_like)
            self.human_id += 1
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(human, (x, y))
            
        # Create bots
        for i in range(self.num_bots):
            bot = BotAmplifier(model=self, bot_id=self.bot_id)
            self.bot_id += 1
            
        # Create content moderator
        
        content_moderator = ContentModerator(model=self)

        reporters = {}
       
        reporters["Total_Bot_Likes"] = lambda m: m.total_bot_likes
        reporters["Total_Human_Likes"] = lambda m: m.total_human_likes

        self.datacollector = DataCollector(model_reporters=reporters)
        

    def add_new_posts(self):
            post = PostAgent(model=self, post_id=self.post_id)
            self.post_id += 1
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(post, (x, y))
            self.posts.append(post)   

    def step(self):

        self.steps += 1
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)

        if self.steps % 10 == 0:
            self.add_new_posts()  # Add new posts
            

        print(f"Step {self.steps} complete:")
        print(f"\nBot Likes: {self.total_bot_likes}. Human Likes: {self.total_human_likes}")
        print("Posts:")
        # for post in self.posts:
        #     post.print_info()
        
        # for i in range(10):
        #     bot = BotAmplifier(model=self, bot_id=self.bot_id)
        #     self.bot_id += 1
