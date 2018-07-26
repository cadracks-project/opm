# coding: utf-8

from opm.init_model import create_sqlite_db, init_db
from opm.api import add_product, add_part_definition

db = create_sqlite_db("test_project.db")
init_db(db)

add_product(db, product_code="TEST_PROJECT",
            main_assembly=None,
            status="ALPHA",
            descriptions={"fr": {'sdesc': "Test Project", 'ldesc': "Le projet Test"},
                          "en": {'sdesc': "Test Project", 'ldesc': "The Test Project"}})

# part definitions
add_part_definition(db,
                    "PLATE_WITH_HOLES",
                    origin='script',
                    script="scripts/plate_with_holes.py")

add_part_definition(db,
                    "ISO4014_M2_grade_Bx21",
                    origin='library',
                    library="libraries/ISO4014_library.json",
                    ref="ISO4014_M2_grade_Bx21")

add_part_definition(db,
                    "ISO4032_Nut_M2.0",
                    origin='library',
                    library="libraries/ISO4032_library.json",
                    ref="ISO4032_Nut_M2.0")


# assemblies


# assemblies  of assemblies
