from opm.init_model import create_sqlite_db, init_db
from opm.api import add_product, add_part_definition

db = create_sqlite_db("osv.db")
init_db(db)

add_product(db, product_code="OSV",
            main_assembly=None,
            status="ALPHA",
            descriptions={"fr": {'sdesc': "OSV", 'ldesc': "Véhicule Open Source"},
                          "en": {'sdesc': "OSV", 'ldesc': "Open Source Vehicle"}})

# part definitions
add_part_definition(db,
                    code="CAR_CHASSIS_ARCHLEFT_705#515#184#mm_STEEL__",
                    origin='stepzip',
                    stepzip="stepzips/CAR_CHASSIS_ARCHLEFT_705#515#184#mm_STEEL__.stepzip")


# assemblies


# assemblies  of assemblies
