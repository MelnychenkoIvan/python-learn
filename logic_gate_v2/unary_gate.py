from logic_gate.logic_gate import LogicGate


class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def get_pin(self):
        return int(input('Enter Pin input for gate ' + self.getLabel() + '-->'))
    