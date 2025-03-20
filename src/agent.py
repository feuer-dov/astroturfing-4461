from mesa import Agent

class BotAmplifier(Agent):
    def __init__(self, model, bot_id):
        super().__init__(model)
        self.bot_id = bot_id
        self.posts = self.model.posts_to_like
     
        
        
    def step(self):  # added self as a parameter so it can be passed into add_like
    
        for post in self.model.posts_to_like:  # Iterates through the subset of posts
        # # Only boost if humans haven't liked it too much
        #     total_likes = post.get_total_likes()
        #     if total_likes < 5000:  # e.g. stop boosting if 20 humans have liked it
                if self not in post.liked_by:
                    post.add_like(self)
                    self.model.total_bot_likes += 1
                    print(f"[Bot {self.bot_id}] liked Post {post.post_id}")

         
class HumanUser(Agent):
    def __init__(self, model, human_id, chance_to_like):
        super().__init__(model)
        self.human_id = human_id
        self.chance_to_like = chance_to_like # starts at 0.05 and increases to 1 once visibility >= 60

    def step(self):
        x, y = self.pos  # Human's position

        for post in self.model.posts:
            post_x, post_y = post.pos
            dist_x = abs(post_x - x)
            dist_y = abs(post_y - y)

            # Within influence radius of the post
            if dist_x <= post.get_influence_radius() and dist_y <= post.get_influence_radius():
                if self not in post.liked_by:
                    post.add_like(self)
                    self.model.total_human_likes += 1
                    print(f"[Human {self.human_id}] liked Post {post.post_id}")
            
class PostAgent(Agent):
    def __init__(self, model, post_id):
        super().__init__(model)
        self.visibility = 0
        self.liked_by = []
        self.post_id = post_id
        self.influence_radius = 1

    def get_radius(self):
        return max(1, int(self.visibility * 10))  # visibility 0.5 = 5-cell radius
    
    def add_like(self, agent): #added agent as a parameter
        if agent not in self.liked_by:
            self.liked_by.append(agent)

    def get_total_likes(self):
        return len(self.liked_by)
    
    def print_info(self):
        # Print post info with the like history.
            print(f"Post {self.post_id}: {self.get_total_likes()} likes, influence radius: {self.get_influence_radius()}")
    
    def get_influence_radius(self):
        return self.get_total_likes()+1   
    
    def get_visual_size(self):
        return int(30 * self.get_influence_radius())
        
class ContentModerator(Agent): 
    def __init__(self, model):
        super().__init__(model)
        
    def step(self):
        # scoures for posts and deletes those which are highly likely to be bot boosted
        
            # when post is found to be bot boosted, finds likely bots and bans users
        pass

