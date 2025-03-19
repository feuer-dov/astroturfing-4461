from mesa import Agent

class BotAmplifier(Agent):
    def __init__(self, model, bot_id):
        super().__init__(model)
        self.bot_id = bot_id
     
        
        
    def step(self):  # added self as a parameter so it can be passed into add_like
    # Define the bot's identity string
        bot_identity = "bot_" + str(self.bot_id)
    
        for post in self.model.posts_to_like:  # Iterates through the subset of posts
        # Only boost if humans haven't liked it too much
            human_likes = post.count_likes_by_type("human_")
            if human_likes < 20:  # e.g. stop boosting if 20 humans have liked it
                if bot_identity not in post.liked_by:
                    post.add_like(self)
                    print(f"[Bot {self.bot_id}] liked Post {post.post_id}")

         

        
class HumanUser(Agent):
    def __init__(self, model, human_id, chance_to_like):
        super().__init__(model)
        self.human_id = human_id
        self.chance_to_like = chance_to_like # starts at 0.05 and increases to 1 once visibility >= 60

    def step(self):
        human_identity = "human_" + str(self.human_id)
        for post in self.model.posts:
            # Only act if this human hasn't already liked the post.
            if human_identity not in post.liked_by:

                # Determine effective chance based on post visibility.
                if post.visibility >= 0.6:
                    effective_chance = 0.95
                else:
                    effective_chance = self.chance_to_like

                # Debug print: show the post visibility and effective chance for this human.
             #  print(f"[DEBUG] Human {self.human_id} evaluating Post {post.post_id}: visibility = {post.visibility:.2f}, effective_chance = {effective_chance}")

                # Decide whether to like the post.
                if self.random.random() <= effective_chance:
                    post.add_like(self)
                    print(f"[Human {self.human_id}] liked Post {post.post_id}")
                 
        
class ContentModerator(Agent): 
    def __init__(self, model):
        super().__init__(model)
        
    def step(self):
        # scoures for posts and deletes those which are highly likely to be bot boosted
        
            # when post is found to be bot boosted, finds likely bots and bans users
        pass

