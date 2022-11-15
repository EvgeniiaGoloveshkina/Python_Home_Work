from view import get_value, get_action
import model
from logger import calculation_logger


def data_collection():
    return (get_value(), get_action(), get_value())

def calculate():
    data = data_collection()
    value_a, action, value_b = data

    # action = get_action()
    # value_b = get_value()

    actions = {'+': model.summarize(value_a, value_b),
               '-': model.subtract(value_a, value_b),
               '/': model.divide(value_a, value_b),
               '*': model.multiply(value_a, value_b),
            }
    result = actions[action]
    calculation_logger(value_a, action, value_b, result)
    return result
