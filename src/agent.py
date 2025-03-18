from mesa import Agent

class BotAmplifier(Agent):
    def __init__(self, model):
        super().__init__(model)
        
    def step(self):
        # if liking a post is safe
        for post in self.model.posts:
            post.add_like(self) # Added self as a parameter so it can be stored in the liked_by list
            print(f"[Bot {self.unique_id}] liked Post {post.post_id}") #Added unique_id

        
class HumanUser(Agent):
    def __init__(self, model):
        super().__init__(model)
        
    def step(self):
        # encounters posts based on algorithm, decides to like and share
        for post in self.model.posts:
            if post.visibility > 0.6:
                post.add_like(self) # Added self as a parameter so it can be stored in the liked_by list
                print(f"[Human {self.unique_id}] liked Post {post.post_id}") #Added unique_id

        
class ContentModerator(Agent):
    def __init__(self, model):
        super().__init__(model)
        
    def step(self):
        # scoures for posts and deletes those which are highly likely to be bot boosted
        
            # when post is found to be bot boosted, finds likely bots and bans users
        pass

