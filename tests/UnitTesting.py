import unittest
from Main.Ball import new_ball
from Main.Food import new_food

class MyTestCase(unittest.TestCase):
    def test_something(self):

        ball = new_ball()
        is_right_position = False
        if 800 > ball.x > 0:
            is_right_position = True
        self.assertEqual(is_right_position, True)

        if 800 > ball.y > 0:
            is_right_position = True
        self.assertEqual(is_right_position, True)

        food = new_food()
        is_right_position = False
        if 800 > food.x > 0:
            is_right_position = True
        self.assertEqual(is_right_position, True)

        if 800 > food.y > 0:
            is_right_position = True
        self.assertEqual(is_right_position, True)


if __name__ == '__main__':
    unittest.main()
