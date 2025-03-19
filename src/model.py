from mesa import Model
from agent import BotAmplifier, HumanUser
from mesa.datacollection import DataCollector

class Post:
    def __init__(self, post_id):
        self.likes = 0
        self.post_id = post_id
        self.visibility = 0
        self.liked_by = [] # Array to store agents who have liked a post
    
    def add_like(self, agent): #added agent as a parameter

        # Checks whether the agent is a human or a bot and stores their respective id in agent_identity
        if hasattr(agent, "bot_id"):
             agent_identity = "bot_" + str(agent.bot_id) #(This just turns bot_ into bot_0 or bot_1 etc )
        elif hasattr(agent, "human_id"):
            agent_identity = "human_" + str(agent.human_id) # Same here
      
    
    # Only add a like if this agent hasn't already liked the post otherwise add them to the list
        if agent_identity not in self.liked_by:
            self.liked_by.append(agent_identity)
            self.likes += 1
            self.visibility = min(0.05 * self.likes, 1.0)


    def print_info(self):
        # Print post info with the like history.
            print(f"Post {self.post_id}: {self.likes} likes, liked by: {', '.join(self.liked_by)}")

    def count_likes_by_type(self, agent_type_prefix):
        return sum(1 for agent_id in self.liked_by if agent_id.startswith(agent_type_prefix))

    
class AstroturfingModel(Model):
    def __init__(self):
        super().__init__()
        self.posts = [Post(post_id=i) for i in range(5)]
        self.bots = []
        
        sample_size = int(0.6 * len(self.posts))
        self.posts_to_like = self.random.sample(self.posts, sample_size)


        #counters for each id
        self.bot_id = 0
        self.human_id = 0
      
         # Create humans
        for i in range(10):
            human = HumanUser(model=self, human_id=self.human_id, chance_to_like=0.05)
            self.human_id += 1

          # Create bots but do not activate them yet
        for i in range(10):
            bot = BotAmplifier(model=self, bot_id=self.bot_id)
            self.bots.append(bot)
            self.bot_id += 1

        reporters = {}
       
        reporters["Total_Bot_Likes"] = lambda m: sum(post.count_likes_by_type("bot_") for post in m.posts)
        reporters["Total_Human_Likes"] = lambda m: sum(post.count_likes_by_type("human_") for post in m.posts)

        self.datacollector = DataCollector(model_reporters=reporters)

    def step(self):

        for i in range(1):

           new_post_id = self.posts[-1].post_id + 1 if self.posts else 0
           new_post = Post(post_id=new_post_id)
           self.posts.append(new_post)
            
        # Add new posts to the bot's targeted posts with some probability
        for post in self.posts[-3:]:  # Only consider newly created posts
            if self.random.random() < 0.1:  # 20% chance to be targeted
                self.posts_to_like.append(post)
       
      

      # Activate 2 random bots per step
        active_bots = self.random.sample(self.bots, min(3, len(self.bots)))
        for bot in active_bots:
            bot.step()

        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
