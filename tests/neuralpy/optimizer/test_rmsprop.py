import pytest
from torch.optim import RMSprop as _RMSprop
from neuralpy.optimizer import RMSprop

# Possible values that are invalid
learning_rates = [-6 , False, ""]
alphas = [False, ""]
epses = [-6 , False, ""]
momentums = [-6 , False, ""]
weight_decays = [-0.36, 'asd', '', False]
centeredes = [12, "", 30.326]

@pytest.mark.parametrize(
	"learning_rate, alpha, eps, weight_decay, momentum, centered", 
	[(learning_rate, alpha, eps, weight_decay, momentum, centered) for learning_rate in learning_rates
																   for alpha in alphas
																   for eps in epses
																   for weight_decay in weight_decays
														           for momentum in momentums
														           for centered in centeredes]
)
def test_rmsprop_should_throw_value_error(learning_rate, alpha, eps, weight_decay, momentum, centered):
    with pytest.raises(ValueError) as ex:
        x = RMSprop(learning_rate=learning_rate, alpha=alpha, eps=eps, weight_decay=weight_decay, 
        			momentum=momentum, centered=centered)

# Possible values that are valid
learning_rates = [0.0, 0.1]
alphas = [0.2, 1.0]
epses = [0.2, 1.0]
momentums = [0.32]
weight_decays = [0.32]
centeredes = [False, True]

@pytest.mark.parametrize(
	"learning_rate, alpha, eps, weight_decay, momentum, centered", 
	[(learning_rate, alpha, eps, weight_decay, momentum, centered) for learning_rate in learning_rates
																   for alpha in alphas
																   for eps in epses
																   for weight_decay in weight_decays
														           for momentum in momentums
														           for centered in centeredes]
)
def test_rmsprop_get_layer_method(learning_rate, alpha, eps, weight_decay, momentum, centered):
	x = RMSprop(learning_rate=learning_rate, alpha=alpha, eps=eps, weight_decay=weight_decay, 
        			momentum=momentum, centered=centered)
		
	details = x.get_optimizer()

	assert isinstance(details, dict) == True

	assert issubclass(details["optimizer"], _RMSprop) == True

	assert isinstance(details["keyword_arguments"], dict) == True

	assert details["keyword_arguments"]["lr"] == learning_rate

	assert details["keyword_arguments"]["alpha"] == alpha

	assert details["keyword_arguments"]["eps"] == eps

	assert details["keyword_arguments"]["momentum"] == momentum

	assert details["keyword_arguments"]["weight_decay"] == weight_decay

	assert details["keyword_arguments"]["centered"] == centered