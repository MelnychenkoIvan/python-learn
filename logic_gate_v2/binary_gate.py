from logic_gate.logic_gate import LogicGate


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        return int(input('Enter Pin A input for gate ' + self.getLabel() + '-->'))

    def get_pin_b(self):
        return int(input('Enter Pin B inpup for gate ' + self.getLabel() + '-->'))
