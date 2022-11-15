# Задача: Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.

from controller import calculate
from view import show_result

show_result(calculate())