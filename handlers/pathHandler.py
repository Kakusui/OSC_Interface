## built-in libaries
import os

class pathHandler:

    """
    
    Assembles paths for backup/transfer of SCF.\n

    """

##--------------------start-of-__init__()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        # Sample value for scf_actual_dir for demonstration purposes
        self.scf_actual_dir = "/some/path"

        # Let's say names_from_file is a list of names read from your file
        names_from_file = self._read_names_from_file()

        self.dirs = {}
        self.iteration_dirs = {}
        self.iteration_paths = {}

        for name in names_from_file:
            # Construct directories dynamically
            self.dirs[name] = os.path.join(self.scf_actual_dir, name)
            self.iteration_dirs[name] = os.path.join(self.dirs[name], "Current Iteration")
            self.iteration_paths[name] = os.path.join(self.iteration_dirs[name], "iteration.txt")

    def _read_names_from_file(self):
        # Here, read your file and return the list of names.
        # This is just a mock implementation.
        return ["tafunuha", "rahahinukawa", "NuharunuNihamemekayahame", "NisoMehademaRakasuni", "MehademaRakasuniKasunu", "TaninMehademaRakasuni"]

# Usage
obj = YourClass()
print(obj.dirs)
print(obj.iteration_dirs)
print(obj.iteration_paths)
