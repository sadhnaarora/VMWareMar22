"""
__main__    => double underscore    => dunder-main
"""
class Player:
    def disp(self):
        pass

    def get_runs(self):
        print(self.__class__)
        print("Runs scored.....")
        print("-" * 30)
        print(dir(self))


sachin = Player()
print(type(sachin))
sachin.get_runs()

print(isinstance(sachin, Player))
print(isinstance(Player, object))
print(isinstance(sachin, str))
