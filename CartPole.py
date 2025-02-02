import gymnasium as gym
# env = gym.make('CartPole-v1',render_mode = "human")

# #Checking Observation
# obs = env.reset()
# print(obs)
# #array([-0.04290572, -0.04512029,  0.03191308, -0.00870085], dtype=float32), {})
# print(env.action_space)
# print(env.observation_space)
# print(env.observation_space.sample())
if __name__=="__main__":
    env = gym.make('CartPole-v0',render_mode = "human")
    total_reward = 0.0
    total_steps=0
    obs = env.reset()
    while True:
        action = env.action_space.sample() # taking random
        obs,reward,done,_,_ = env.step(action)
        total_reward += reward
        total_steps +=1
        if done :
            break
        print(f"Eposide done in {total_steps} steps and rewards is {total_reward}")

