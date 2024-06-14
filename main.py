from utils.openspace import Openspace
from utils.table import Table
from utils.file_utils import list_of_becodian

becodians = list_of_becodian()

table = Table()
openspace = Openspace(6, 4)

openspace.organize(becodians)
openspace.display()
openspace.store()

