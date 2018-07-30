# coding: utf-8

from opm.init_model import create_sqlite_db, init_db
from opm.api import add_product, add_part_definition, add_assembly, assembly_add_part, assembly_add_constraint

db = create_sqlite_db("test_project.db")
init_db(db)

# part definitions
add_part_definition(db,
                    code="PLATE_WITH_HOLES",
                    origin='script',
                    script="scripts/plate_with_holes.py")

add_part_definition(db,
                    code="ISO4014_M2_grade_Bx21",
                    origin='library',
                    library="libraries/ISO4014_library.json",
                    ref="ISO4014_M2_grade_Bx21")

add_part_definition(db,
                    code="ISO4032_Nut_M2.0",
                    origin='library',
                    library="libraries/ISO4032_library.json",
                    ref="ISO4032_Nut_M2.0")

# assemblies
main_assembly_code = 'MAIN_ASSEMBLY'


add_assembly(db, assembly_code=main_assembly_code)

add_product(db,
            product_code="TEST_PROJECT",
            main_assembly=main_assembly_code,
            status="ALPHA",
            descriptions={"fr": {'sdesc': "Test Project",
                                 'ldesc': "Le projet Test"},
                          "en": {'sdesc': "Test Project",
                                 'ldesc': "The Test Project"}})

assembly_add_part(db,
                  assembly=main_assembly_code,
                  part_definition="PLATE_WITH_HOLES",
                  part_occurence_code="PLATE_WITH_HOLES_0")

assembly_add_part(db,
                  assembly=main_assembly_code,
                  part_definition="ISO4014_M2_grade_Bx21",
                  part_occurence_code="ISO4014_M2_grade_Bx21_0")

assembly_add_constraint(db,
                        assembly=main_assembly_code,
                        master_part_occurrence="PLATE_WITH_HOLES_0",
                        master_part_occurrence_anchor="0",
                        slave_part_occurrence="ISO4014_M2_grade_Bx21_0",
                        slave_part_occurrence_anchor="1",
                        joint_type="RIGID")

# assemblies  of assemblies
