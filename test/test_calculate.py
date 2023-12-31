import time
import unittest 
from toolkit_package.toolkit import Result_metrics, Loss
import torch
import torch.nn as nn

class TestStringMethods(unittest.TestCase):

    def test_Loss(self):
        m = nn.Sigmoid()
        loss = nn.BCELoss()

        input_1 = torch.randn(3, requires_grad=True)
        target_1 = torch.empty(3).random_(2)

        output_1 = loss(m(input_1), target_1)

        loss = Loss()
        loss.update(m(input_1),target_1 )
        sub_output = loss.compute()

        self.assertEqual(sub_output, output_1)

if __name__ == '__main__':
    unittest.main()