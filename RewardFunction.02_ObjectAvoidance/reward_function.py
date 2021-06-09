import math


def reward_function(params):
    """
    Example of rewarding the agent to stay inside two borders
    and penalizing getting too close to the objects in front
    """

    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # array that stores the location of objects within the track
    objects_location = params['objects_location']
    # x-axis of agent
    agent_x = params['x']
    # y-axis of agent
    agent_y = params['y']
    # array that stores the two nearest objects (back/front)
    _, front_object_index = params['closest_objects']
    # returns true if the object is on the left, false if it's on the right
    objects_left_of_center = params['objects_left_of_center']
    # returns true if the agent is on the left, false if it's on the right
    is_left_of_center = params['is_left_of_center']

    # initialize reward to something small (0 means crashed)
    reward = 1e-3

    # reward if the agent stays inside the two borders of the track
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward_lane = 1.0
    else:
        reward_lane = 1e-3

    # get the location of the nearest object to the front
    front_object_loc = objects_location[front_object_index]

    # get the distance of the object to the agent (use distance formula)
    distance_closest_object = math.sqrt((agent_x - front_object_loc[0]) ** 2 + (agent_y - front_object_loc[1]) ** 2)

    # Decide if the agent and the next object is on the same lane
    is_same_lane = (objects_left_of_center[front_object_index] == is_left_of_center)

    # penalize if the agent is too close to the next object
    reward_avoid = 1.0

    # if they're on the same lane, do the following
    if is_same_lane:
        # if you're between 0.5 and 0.8 distance away from the object, you get rewarded 1/2 for avoiding
        if 0.5 <= distance_closest_object < 0.8:
            reward_avoid *= 0.5
        # if you're between 0.3 and 0.5 distance away from the object, you get rewarded 1/5 for avoiding
        elif 0.3 <= distance_closest_object < 0.5:
            reward_avoid *= 0.2
        # if you're less than 0.3, then you probably crashed so you will be penalized
        elif distance_closest_object < 0.3:
            reward_avoid = 1e-3  # Likely crashed

    # calculate reward by putting different weights on the two aspects above
    reward += 1.0 * reward_lane + 4.0 * reward_avoid

    return reward
