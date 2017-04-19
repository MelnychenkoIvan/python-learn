from logic_gate_v2.binary_gate import BinaryGate


class OrGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        pin_a = self.get_pin_a()
        pin_b = self.get_pin_b()

        if pin_a != 0 and pin_b != 0:
            return 1
        else:
            return 0
