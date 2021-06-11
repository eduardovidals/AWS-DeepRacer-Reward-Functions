def reward_function(params):
    """
    Example of trusting the agent to do all the work. It motivates itself to finish the track. 
    """

    # read input parameters
    all_wheels_on_track = params["all_wheels_on_track"]
    steps = params["steps"]
    progress = params["progress"]
    speed = params["speed"]

    if all_wheels_on_track and steps > 0:
        reward = ((progress / steps) * 100) + (speed ** 2)
    else:
        reward = 0.01

    return float(reward)
