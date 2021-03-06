import os
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export

if __name__ == '__main__':
    pyflies_mm = metamodel_from_file(
        os.path.join(os.path.dirname(__file__), 'pyflies.tx'), debug=True)
else:
    from pyflies.lang.model_processor import pyflies_model_processor
    pyflies_mm = metamodel_from_file(
        os.path.join(os.path.dirname(__file__), 'pyflies.tx'))
    pyflies_mm.register_model_processor(pyflies_model_processor)

