import math


def reward_function(params):
    """
    Example of object avoidance reward function.
    """

    # initialize variables
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    steps = params['steps']
    objects_location = params['objects_location']
    agent_x = params['x']
    agent_y = params['y']
    _, front_object_index = params['closest_objects']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']
    steering_angle = params['steering_angle']
    speed = params['speed']

    reward = 0.001

    # reward agent for the progress it makes
    if all_wheels_on_track and steps > 0:
        reward_progress = ((progress / steps) * 100) + (speed ** 2)
    else:
        reward_progress = 0.001

    if abs(steering_angle) < 5:
        reward += 50

    # get the location of the nearest object to the front
    front_object_loc = objects_location[front_object_index]

    # get the distance of the object to the agent (use distance formula)
    distance_closest_object = math.sqrt((agent_x - front_object_loc[0]) ** 2 + (agent_y - front_object_loc[1]) ** 2)

    # Decide if the agent and the next object is on the same lane
    is_same_lane = (objects_left_of_center[front_object_index] == is_left_of_center)

    reward_distance = 50.0

    # if they're on the same lane, do the following
    if is_same_lane:
        if 0.5 <= distance_closest_object < 0.8:
            reward_distance *= 0.5
        elif 0.3 <= distance_closest_object < 0.5:
            reward_distance *= 0.2
        elif distance_closest_object < 0.3:
            reward_distance = 0.001
    else:
        reward += 50.0

    reward += (3.0 * reward_progress) + (1.5 * reward_distance)

    return float(reward)
