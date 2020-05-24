from torch.nn import Softmax as _Softmax

class Softmax:
	def __init__(self, dim=None, name=None):
		# Checking the name field, this is an optional field,
		# if not provided generates a unique name for the activation function
		if name is not None and not (isinstance(name, str) and name is not ""):
			raise ValueError("Please provide a valid name")

		self.__name = name
		self.__dim = dim

	def get_input_dim(self, prev_input_dim):
		# Softmax does not need to n_input, so returning None
		return None

	def get_layer(self):
		# Returning all the details of the activation function
		return {
			'n_inputs': None,
			'n_nodes': None,
			'name': self.__name,
			'type': 'Softmax',
			'layer': _Softmax,
			"keyword_arguments": {
				'dim': self.__dim
			}
		}