#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Alexandre Coninx
    ISIR CNRS/UPMC
    05/06/2019
""" 

import gym, gym_fastsim
import time

display= True

env = gym.make('FastsimSimpleNavigation-v0')
print(" == Reset to the default initial position ==")
env.reset()
action=[10,11]

if(display):
    env.enable_display()

then = time.time()

for i in range(100):
        env.render()
        o,r,eo,info=env.step(action)
        print("Step %d Obs=%s  reward=%f  dist. to objective=%f  robot position=%s  End of ep=%s" % (i, str(o), r, info["dist_obj"], str(info["robot_pos"]), str(eo)))
        if(display):
        	time.sleep(0.01)
        if eo:
            break

pos=[55, 55, 0]
print(" == Reset to a position given as argument: "+str(pos)+" ==")
# reset from a position given as argument instead of the default position
env.reset2(pos)

for i in range(100):
        env.render()
        o,r,eo,info=env.step(action)
        print("Step %d Obs=%s  reward=%f  dist. to objective=%f  robot position=%s  End of ep=%s" % (i, str(o), r, info["dist_obj"], str(info["robot_pos"]), str(eo)))
        if(display):
            time.sleep(0.01)
        if eo:
            break


now = time.time()

print("%d timesteps took %f seconds" % (i, now - then))

env.close()
