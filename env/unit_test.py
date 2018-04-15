from macros import *
from gworld import *
from visualize import *
import random

a = GridWorld(7, 7)

bwalls = a.get_boundwalls()
a.add_rocks(bwalls)

a.add_agents_rand(4)

vis = Visualize(a)

vis.draw_world()
vis.draw_agents()

vis.canvas.pack()
vis.canvas.update()
vis.canvas.after(200)


agents = a.get_agents()

for tstep in range(0, 10):

    for agent in agents:
        states = a.get_agent_state(agent)

        obs_quad = random.randint(Observe.Quadrant1, Observe.Quadrant4)
        a.observe_quadrant(agent, obs_quad)

        action = random.randint(Actions.RIGHT,Actions.WAIT)
        act_reward = a.agent_action(agent, action)
        step_reward = act_reward + a.check_formation(agent) * RWD_GOAL_FORMATION

        vis.canvas.update()
        vis.canvas.after(250)

vis.canvas.update()
vis.canvas.after(2500)