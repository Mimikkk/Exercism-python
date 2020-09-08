from typing import *

class InputCell(object):
    def __init__(self, value: float = None):
        self._value = value
        self.observers = []
        self.updated = True

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        for observer in self.observers:
            observer.updated = False
        for observer in self.observers:
            observer.update_value()

    def register_observer(self, observer: 'ComputeCell'):
        self.observers.append(observer)


class ComputeCell(InputCell):
    def __init__(
            self,
            inputs: Union[List[InputCell], List['ComputeCell']],
            compute_function: Callable):
        super().__init__()
        self.callbacks: List[Callable] = []

        self.inputs = inputs
        self.compute_function = compute_function
        for cell in self.inputs: cell.register_observer(self)
        self.value = compute_function([inp.value for inp in self.inputs])

    def update_value(self):
        if all(inp.updated for inp in self.inputs):
            old_value, self.value = self.value, self.compute_function([inp.value for inp in self.inputs])
            self.updated = True

            for observer in self.observers: observer.update_value()

            if old_value != self.value:
                for callback in self.callbacks: callback(self.value)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks: self.callbacks.remove(callback)
