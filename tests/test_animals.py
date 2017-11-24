import animals


class TestAnimals:
    def test_cat_init(self, capsys):
        cat_instance = animals.grab('cat', name='kitty')

        cat_instance.make_sound()
        out, err = capsys.readouterr()
        assert out == 'meowwww! :3\n'

        cat_instance.move()
        out, err = capsys.readouterr()
        assert out == 'the cat walks\n'

        cat_instance.purr()
        out, err = capsys.readouterr()
        assert out == 'purrrrr!<3\n'

    def test_dog_init(self, capsys):
        cat_instance = animals.grab('dog')

        cat_instance.make_sound()
        out, err = capsys.readouterr()
        assert out == 'woof, woof! :3\n'

        cat_instance.move()
        out, err = capsys.readouterr()
        assert out == 'the dog walks\n'

    def test_goldfish_init(self, capsys):
        goldfish_instance = animals.grab('fish.goldfish', '')

        goldfish_instance.make_sound()
        out, err = capsys.readouterr()
        assert out == 'oooOOOooooOOO..(this is supposed to be bubbles :P)\n'

        goldfish_instance.move()
        out, err = capsys.readouterr()
        assert out == 'the gold swims across the tank\n'


