from mesa import Agent

class BotAmplifier(Agent):
    def __init__(self, model, bot_id):
        super().__init__(model)
        self.bot_id = bot_id
        
        
    def step(self): #added self as a parameter 
        # Define the bot's identity string
        bot_identity = "bot_" + str(self.bot_id)
        for post in self.model.posts:
            # If bot hasnt liked the post already then it will
            if bot_identity not in post.liked_by:
                post.add_like(self)
                print(f"[Bot {self.bot_id}] liked Post {post.post_id}")
         

        
class HumanUser(Agent):
    def __init__(self, model, human_id):
        super().__init__(model)
        self.human_id = human_id
        
         # encounters posts based on algorithm, decides to like and share
    def step(self): #added self as a parameter 
        human_identity = "human_" + str(self.human_id)
        for post in self.model.posts:
            # If human hasnt already liked a post then it will
            if human_identity not in post.liked_by:
                if post.visibility >= 0.6:
                 post.add_like(self)
                 print(f"[Human {self.human_id}] liked Post {post.post_id}")

        
class ContentModerator(Agent): 
    def __init__(self, model):
        super().__init__(model)
        
    def step(self):
        # scoures for posts and deletes those which are highly likely to be bot boosted
        
            # when post is found to be bot boosted, finds likely bots and bans users
        pass

