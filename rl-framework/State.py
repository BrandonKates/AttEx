''' 
	RLState contains the Action Space, State Space, and Replay Buffer for all the previously encountered states
'''
class RLState():
	def __init__(self):
		self.Q = {}
		self.action_space = {}
		self.state_space  = {}
		self.replayBuffer = ReplayBuffer()



class ReplayBuffer():
	def __init__(self):
		self.space_action_pairs = {}