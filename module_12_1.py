import MoveTest
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        test_walk- метод, в котором создается объект класса Runner с произвольным именем.
        Вызываем метод walk у объекта 10 раз. Методом assertEqual сравниваем distance
        этого объекта со значением 50.
        :return:
        """
        walk1 = MoveTest.Runner('Ivan')
        for i in range(10):
            walk1.walk()
        self.assertEqual(walk1.distance, 50)

    def test_run(self):
        """
        test_run- метод, в котором создается объект класса Runner с произвольным именем.
        Вызываем метод run у объекта 10 раз. Методом assertEqual сравниваем distance
        этого объекта со значением 100.
        :return:
        """
        run1 = MoveTest.Runner('Ivan')
        for i in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)

    def test_challenge(self):
        """
        test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Вызываем у объектов методы walk и run 10 раз соответственно.
        Используем метод assertNotEqual чтобы убедиться в неравенстве результатов.
        :return:
        """
        walk2 = MoveTest.Runner('David')
        run2 = MoveTest.Runner('Alex')
        for i in range(10):
            walk2.walk()
            run2.run()
        self.assertNotEqual(walk2.distance, run2.distance)

if __name__ == "__main__":
    unittest.main()

