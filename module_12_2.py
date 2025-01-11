import unittest
from HumanMoveTest import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усейн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            final_result = '{'+','.join(f'{place}:{runner}'for place, runner in result.items()) +'}'
            print(final_result)

    def test_usain_nick(self):
        self.tour_1 = Tournament(90, self.usain, self.nick)
        self.all_results = self.tour_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_andrey_nick(self):
        self.tour_2 = Tournament(90, self.andrey, self.nick)
        self.all_results = self.tour_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_usain_andrey_nick(self):
        self.tour_3 = Tournament(90, self.usain, self.andrey, self.nick)
        self.all_results = self.tour_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results

if __name__ == "__main__":
    unittest.main()




