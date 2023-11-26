from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AwSWMod(Mod):
    """
    This mod adds boobs to the game.
    """

    name = "Boobmod"
    version = "0.0"
    author = "4onenm"
    nsfw = True
    dependencies = []

    @staticmethod
    def mod_load():
        pass

    @staticmethod
    def mod_complete():
        pass