import math


def reward_function(params):
    """
    Example of a reward function that is universal for all tracks. Self motivation
    is used as it has been the most successful within the physical track.
    """

    # initialize variables
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = params['steering_angle']
    speed = params['speed']

    reward = 0.001

    if all_wheels_on_track:
        reward += 1

    if abs(steering_angle) < 5:
        reward += 1

    reward += (speed / 8)

    return float(reward)
