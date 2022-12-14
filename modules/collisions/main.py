from modules.collisions.model import enc_gen as eg
from modules.collisions.model import file_gen as fg

root = eg.root()

y = fg.save_path(6, root)
z = fg.position_import(6, root)
w = fg.data_import(6, root)

print(z, w)