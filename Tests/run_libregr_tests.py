import pyjion
import gc
from test.libregrtest import main

pyjion.enable()
pyjion.set_optimization_level(1)
pyjion.enable_pgc()
pyjion.enable_graphs()
main()
pyjion.disable()
gc.collect()
