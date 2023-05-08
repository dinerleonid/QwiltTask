import json

from Caches.CacheA import CacheA
from Caches.CacheB import CacheB

""" == Tests == """
""" No states json file """
""" json file not writable """
""" json file not readable """
""" Cache A offline """
""" Cache B offline """


class Monitor:
    cache_a_state = CacheA()
    cache_b_state = CacheB()

    def set_states(self):
        state_a = self.cache_a_state.get_state()
        state_b = self.cache_b_state.get_state()

        # write states to file
        json_file = open('caches_state.json')

        states_dict = json.load(json_file)
        states_dict["cache_a"]["state"] = state_a
        states_dict["cache_b"]["state"] = state_b

        json_object = json.dumps(states_dict, indent=2)

        # Writing to sample.json
        with open("caches_state.json", "w") as outfile:
            outfile.write(json_object)

    def get_states(self):
        json_file = open('caches_state.json')
        # load states files and return them to router
        return json.load(json_file)

    def __init__(self):
        # load cache state by interval
        self.set_states()
