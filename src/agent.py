from mesa import Agent
import math

class BotAmplifier(Agent):
    def __init__(self, model, bot_id):
        super().__init__(model)
        self.bot_id = bot_id
        self.banned_likes = 0
        self.safe_mode = False
       

    def step(self):
        # Check if any of this bot's liked posts were banned
        for post in self.model.removed_posts:
            if self in post.liked_by:
                self.banned_likes += 1
           

        # If too many bans, enter safe mode permanently
        if self.banned_likes >= 2 and not self.safe_mode:
            self.safe_mode = True
            print(f"[Bot {self.bot_id}] entering SAFE MODE due to {self.banned_likes} banned posts.")

        # Pick posts to like
        valid_posts = [p for p in self.model.posts if not p.removed and self not in p.liked_by]
        sample_size = int(0.25 * len(valid_posts))

        if self.safe_mode:
            # Only like posts on the left side (low X values)
            safe_zone = [p for p in valid_posts if p.pos[0] <= self.model.grid.width * 0.4]
            posts_to_like = self.random.sample(safe_zone, min(sample_size, len(safe_zone))) if safe_zone else []
        else:
            # Normal behavior
            posts_to_like = self.random.sample(valid_posts, min(sample_size, len(valid_posts)))

        for post in posts_to_like:
            post.add_like(self)
            self.model.total_bot_likes += 1



         
class HumanUser(Agent):
    def __init__(self, model, human_id, chance_to_like):
        super().__init__(model)
        self.human_id = human_id
        self.chance_to_like = chance_to_like 

    def step(self):
        x, y = self.pos  # Human's position

        for post in self.model.posts:
            post_x, post_y = post.pos
            dist_x = abs(post_x - x)
            dist_y = abs(post_y - y)

            # Within influence radius of the post
            if dist_x <= post.get_influence_radius() and dist_y <= post.get_influence_radius():
                if self not in post.liked_by and self.chance_to_like >= 0.3:
                    post.add_like(self)
                    self.model.total_human_likes += 1
                    # print(f"[Human {self.human_id}] liked Post {post.post_id}")
            
class PostAgent(Agent):
    def __init__(self, model, post_id):
        super().__init__(model)
        self.visibility = 0
        self.liked_by = []
        self.post_id = post_id
        self.influence_radius = 1
        self.removed = False
        self.expected_likes = 0
        self.created_at_step = self.model.steps


    def get_radius(self):
        return max(1, int(self.visibility * 10))  # visibility 0.5 = 5-cell radius
    
    def get_influence_area(self):
        # Returns total number of grid squares visibile by post
        r = self.get_influence_radius()
        influence_area = (2 * r + 1) ** 2
        
        return influence_area

    
    def add_like(self, agent): #added agent as a parameter
        if agent not in self.liked_by:
            self.liked_by.append(agent)

    def get_total_likes(self):
        return len(self.liked_by)
    
    def print_info(self):
        # Print post info with the like history.
            print(f"Post {self.post_id}: {self.get_total_likes()} likes, influence radius: {self.get_influence_radius()}")
    
    def get_influence_radius(self):
        base = 1.15
        grid_area = self.model.grid_size ** 2
        max_radius = int((grid_area ** 0.5 - 1) // 2)
        return min(max_radius, int(base ** self.get_total_likes()))
    
    def get_visual_size(self):
        return int(30 * self.get_influence_radius())
    
    def get_like_rate(self):
        steps_alive = max(1, self.model.steps - self.created_at_step)
        like_rate = self.get_total_likes() / steps_alive

        return like_rate


    def get_expected_like_rate(self):
        return self.expected_likes / self.model.steps
    
    def prepare_remove(self):
        # Reduces human and bot likes since post is removed, and sets removed flag to true for visualization
        for agent in self.liked_by:
            if isinstance(agent, BotAmplifier):
                self.model.total_bot_likes -= 1
            elif isinstance(agent, HumanUser):
                self.model.total_human_likes -= 1
        self.removed = True

    
    # def step(self):
    #     # area = number of visible squares by post
    #     r = self.get_influence_radius()
    #     influence_area = (2 * r + 1) ** 2
    #     grid_area = (self.model.grid_size ** 2)
        
    #     user_proportion = self.model.total_users / grid_area
    #     self.expected_likes += user_proportion * influence_area
        
class ContentModerator(Agent): 
    def __init__(self, model):
        super().__init__(model)
        
    def step(self):
        # # scoures for posts and deletes those which are highly likely to be bot boosted
        # for post in self.model.posts:
        #     rate = post.get_like_rate() 
        #     expected_rate = post.get_expected_like_rate()
            
        #     print(f"rate: {rate}")  
        #     print(f"expected rate: {expected_rate}")
        #     print(f"post area: {post.get_influence_area()}")
            
        #     influence_area = post.get_influence_area()
        #     expected_rate = influence_area * 0.1
        #     # Based on the post's position on the x axis

        #     threshold_rate = expected_rate
            
        #     if rate >= threshold_rate:
        #         post.removed = True
        #         self.model.posts.remove(post)
        # # when post is found to be bot boosted, finds likely bots and bans users
        
        to_remove = []
        
        for post in self.model.posts:
            # number_of_likes = post.get_total_likes()
            # influence_area = post.get_influence_area()
            # total_grid_spaces = self.model.grid_size ** 2
            
            # num_users = self.model.total_users
            # users_percentage = num_users / total_grid_spaces
            # human_percentage = 1 * users_percentage
            
            
            # expected_human_likes = influence_area * human_percentage
            # print(f"expected likes human: {expected_human_likes}, actual likes {number_of_likes}")
            # suspicion_margin = number_of_likes - expected_human_likes
            
            # if suspicion_margin >= 1000:
            #     to_remove.append(post)
            
            x, y = post.pos
            
            mod_intensity = x / self.model.grid.width
            like_threshold = (1 - mod_intensity) * 10
            
            total_likes = post.get_total_likes()
            like_rate = post.get_like_rate()

            if total_likes > 20 and like_rate > like_threshold:
                to_remove.append(post)

        
           

                
         
        for post in to_remove:
            post.prepare_remove()
            self.model.removed_posts.append(post)
            self.model.posts.remove(post)      
            

