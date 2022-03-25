

class Player:

    def __init__(self):             # constructor
        print("Player Initialized.......")

    def get_runs(self):
        print("Runs scored......")

    def __del__(self):
        print("Player deleted.......")

sachin = Player()
sourav = Player()

sachin.__init__()
sachin.get_runs()
sourav.get_runs()


