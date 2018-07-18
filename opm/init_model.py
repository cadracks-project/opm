from os import remove
from os.path import isfile

import dataset

db_filename = "opm.db"

if isfile(db_filename):
    remove(db_filename)

db = dataset.connect("sqlite:///%s" % db_filename)

# ######
# Core #
########
en_id = db['language'].insert({'language_code': 'en', 'language_name': 'English'})
fr_id = db['language'].insert({'language_code': 'fr', 'language_name': 'Français'})
es_id = db['language'].insert({'language_code': 'es', 'language_name': 'Español'})

eur_id = db['currency'].insert({'currency_code': 'EUR', 'is_ref': True, 'rate': 1.0})
usd_id = db['currency'].insert({'currency_code': 'USD', 'is_ref': False, 'rate': 0.8})
gbp_id = db['currency'].insert({'currency_code': 'GBP', 'is_ref': False, 'rate': 1.2})

fra_id = db['country'].insert({'country_code': 'FRA'})
eng_id = db['country'].insert({'country_code': 'ENG'})
usa_id = db['country'].insert({'country_code': 'USA'})

db['currency_description'].insert({'currency': eur_id, 'language': en_id, 'currency_sdesc': 'Euro', 'currency_ldesc': 'Euro'})
db['currency_description'].insert({'currency': eur_id, 'language': fr_id, 'currency_sdesc': 'Euro', 'currency_ldesc': 'Euro'})
db['currency_description'].insert({'currency': eur_id, 'language': es_id, 'currency_sdesc': 'Euro', 'currency_ldesc': 'Euro'})
db['currency_description'].insert({'currency': usd_id, 'language': en_id, 'currency_sdesc': 'US Dollar', 'currency_ldesc': 'Unites States of America Dollar'})
db['currency_description'].insert({'currency': usd_id, 'language': fr_id, 'currency_sdesc': 'Dollar US', 'currency_ldesc': 'Dollar Américain'})
db['currency_description'].insert({'currency': usd_id, 'language': es_id, 'currency_sdesc': 'Dollar US', 'currency_ldesc': 'Dollar Americano'})
db['currency_description'].insert({'currency': gbp_id, 'language': en_id, 'currency_sdesc': 'Pound', 'currency_ldesc': 'British Pound'})
db['currency_description'].insert({'currency': gbp_id, 'language': fr_id, 'currency_sdesc': 'Livre', 'currency_ldesc': 'Livre sterling'})
db['currency_description'].insert({'currency': gbp_id, 'language': es_id, 'currency_sdesc': 'Libra', 'currency_ldesc': 'Libra sterling'})

db['country_description'].insert({'country': fra_id, 'language': fr_id, 'country_sdesc': "France", 'country_ldesc': 'République Française'})
db['country_description'].insert({'country': fra_id, 'language': en_id, 'country_sdesc': "France", 'country_ldesc': 'French Republic'})
db['country_description'].insert({'country': fra_id, 'language': es_id, 'country_sdesc': "Francia", 'country_ldesc': 'Republica Francesa'})
db['country_description'].insert({'country': eng_id, 'language': fr_id, 'country_sdesc': "Angleterre", 'country_ldesc': 'Angleterre'})
db['country_description'].insert({'country': eng_id, 'language': en_id, 'country_sdesc': "England", 'country_ldesc': 'England'})
db['country_description'].insert({'country': eng_id, 'language': es_id, 'country_sdesc': "Inglaterra", 'country_ldesc': 'Inglaterra'})
db['country_description'].insert({'country': usa_id, 'language': fr_id, 'country_sdesc': "USA", 'country_ldesc': "Etats Unis d'Amérique"})
db['country_description'].insert({'country': usa_id, 'language': en_id, 'country_sdesc': "USA", 'country_ldesc': 'Unites States of America'})
db['country_description'].insert({'country': usa_id, 'language': es_id, 'country_sdesc': "EUA", 'country_ldesc': 'Estados Unidos de America'})

# #######
# Units #
#########
mm_id = db['unit'].insert({'unit_code': 'mm', 'conversion': 1e3, 'unit_type': -1})
cm_id = db['unit'].insert({'unit_code': 'cm', 'conversion': 1e2, 'unit_type': -1})
m_id = db['unit'].insert({'unit_code': 'm', 'conversion': 1., 'unit_type': -1})
mm2_id = db['unit'].insert({'unit_code': 'mm2', 'conversion': 1e6, 'unit_type': -1})
cm2_id = db['unit'].insert({'unit_code': 'cm2', 'conversion': 1e4, 'unit_type': -1})
m2_id = db['unit'].insert({'unit_code': 'm2', 'conversion': 1., 'unit_type': -1})
mm3_id = db['unit'].insert({'unit_code': 'mm3', 'conversion': 1e9, 'unit_type': -1})
cm3_id = db['unit'].insert({'unit_code': 'cm3', 'conversion': 1e6, 'unit_type': -1})
m3_id = db['unit'].insert({'unit_code': 'm3', 'conversion': 1., 'unit_type': -1})
g_id = db['unit'].insert({'unit_code': 'g', 'conversion': 1e3, 'unit_type': -1})
kg_id = db['unit'].insert({'unit_code': 'kg', 'conversion': 1., 'unit_type': -1})
N_id = db['unit'].insert({'unit_code': 'N', 'conversion': 1., 'unit_type': -1})

db['unit_description'].insert({'unit': mm_id, 'language': en_id, 'unit_sdesc': 'mm', 'unit_ldesc': 'Millimeter'})
db['unit_description'].insert({'unit': mm_id, 'language': fr_id, 'unit_sdesc': 'mm', 'unit_ldesc': 'Millimètre'})
db['unit_description'].insert({'unit': mm_id, 'language': es_id, 'unit_sdesc': 'mm', 'unit_ldesc': 'Millimetro'})
db['unit_description'].insert({'unit': cm_id, 'language': en_id, 'unit_sdesc': 'cm', 'unit_ldesc': 'Centimeter'})
db['unit_description'].insert({'unit': cm_id, 'language': fr_id, 'unit_sdesc': 'cm', 'unit_ldesc': 'Centimètre'})
db['unit_description'].insert({'unit': cm_id, 'language': es_id, 'unit_sdesc': 'cm', 'unit_ldesc': 'Centimetro'})
db['unit_description'].insert({'unit': m_id, 'language': en_id, 'unit_sdesc': 'm', 'unit_ldesc': 'Meter'})
db['unit_description'].insert({'unit': m_id, 'language': fr_id, 'unit_sdesc': 'm', 'unit_ldesc': 'Mètre'})
db['unit_description'].insert({'unit': m_id, 'language': es_id, 'unit_sdesc': 'm', 'unit_ldesc': 'Metro'})

db['unit_description'].insert({'unit': mm2_id, 'language': en_id, 'unit_sdesc': 'mm²', 'unit_ldesc': 'Square millimeter'})
db['unit_description'].insert({'unit': mm2_id, 'language': fr_id, 'unit_sdesc': 'mm²', 'unit_ldesc': 'Millimètre carré'})
db['unit_description'].insert({'unit': mm2_id, 'language': es_id, 'unit_sdesc': 'mm²', 'unit_ldesc': 'Millimetro cuadrado'})
db['unit_description'].insert({'unit': cm2_id, 'language': en_id, 'unit_sdesc': 'cm²', 'unit_ldesc': 'Square centimeter'})
db['unit_description'].insert({'unit': cm2_id, 'language': fr_id, 'unit_sdesc': 'cm²', 'unit_ldesc': 'Centimètre carré'})
db['unit_description'].insert({'unit': cm2_id, 'language': es_id, 'unit_sdesc': 'cm²', 'unit_ldesc': 'Centimetro cuadrado'})
db['unit_description'].insert({'unit': m2_id, 'language': en_id, 'unit_sdesc': 'm²', 'unit_ldesc': 'Square meter'})
db['unit_description'].insert({'unit': m2_id, 'language': fr_id, 'unit_sdesc': 'm²', 'unit_ldesc': 'Mètre carré'})
db['unit_description'].insert({'unit': m2_id, 'language': es_id, 'unit_sdesc': 'm²', 'unit_ldesc': 'Metro cuadrado'})

db['unit_description'].insert({'unit': mm3_id, 'language': en_id, 'unit_sdesc': 'mm³', 'unit_ldesc': 'Cube millimeter'})
db['unit_description'].insert({'unit': mm3_id, 'language': fr_id, 'unit_sdesc': 'mm³', 'unit_ldesc': 'Millimètre cube'})
db['unit_description'].insert({'unit': mm3_id, 'language': es_id, 'unit_sdesc': 'mm³', 'unit_ldesc': 'Millimetro cubo'})
db['unit_description'].insert({'unit': cm3_id, 'language': en_id, 'unit_sdesc': 'cm³', 'unit_ldesc': 'Cube centimeter'})
db['unit_description'].insert({'unit': cm3_id, 'language': fr_id, 'unit_sdesc': 'cm³', 'unit_ldesc': 'Centimètre cube'})
db['unit_description'].insert({'unit': cm3_id, 'language': es_id, 'unit_sdesc': 'cm³', 'unit_ldesc': 'Centimetro cubo'})
db['unit_description'].insert({'unit': m3_id, 'language': en_id, 'unit_sdesc': 'm³', 'unit_ldesc': 'Cube meter'})
db['unit_description'].insert({'unit': m3_id, 'language': fr_id, 'unit_sdesc': 'm³', 'unit_ldesc': 'Mètre cube'})
db['unit_description'].insert({'unit': m3_id, 'language': es_id, 'unit_sdesc': 'm³', 'unit_ldesc': 'Metro cubo'})

db['unit_description'].insert({'unit': g_id, 'language': en_id, 'unit_sdesc': 'g', 'unit_ldesc': 'Gram'})
db['unit_description'].insert({'unit': g_id, 'language': fr_id, 'unit_sdesc': 'g', 'unit_ldesc': 'Gramme'})
db['unit_description'].insert({'unit': g_id, 'language': es_id, 'unit_sdesc': 'g', 'unit_ldesc': 'Gramo'})
db['unit_description'].insert({'unit': kg_id, 'language': en_id, 'unit_sdesc': 'kg', 'unit_ldesc': 'Kilogram'})
db['unit_description'].insert({'unit': kg_id, 'language': fr_id, 'unit_sdesc': 'kg', 'unit_ldesc': 'Kilogramme'})
db['unit_description'].insert({'unit': kg_id, 'language': es_id, 'unit_sdesc': 'kg', 'unit_ldesc': 'Kilogramo'})

db['unit_description'].insert({'unit': N_id, 'language': en_id, 'unit_sdesc': 'N', 'unit_ldesc': 'Newton'})
db['unit_description'].insert({'unit': N_id, 'language': fr_id, 'unit_sdesc': 'N', 'unit_ldesc': 'Newton'})
db['unit_description'].insert({'unit': N_id, 'language': es_id, 'unit_sdesc': 'N', 'unit_ldesc': 'Newton'})

length_id = db['unit_type'].insert({'unit_type_code': 'length', 'default_unit': 'mm'})
surface_id = db['unit_type'].insert({'unit_type_code': 'surface', 'default_unit': 'mm2'})
volume_id = db['unit_type'].insert({'unit_type_code': 'volume', 'default_unit': 'mm3'})
mass_id = db['unit_type'].insert({'unit_type_code': 'mass', 'default_unit': 'g'})
force_id = db['unit_type'].insert({'unit_type_code': 'force', 'default_unit': 'N'})

db['unit'].update({'unit_code': 'mm', 'unit_type': length_id}, ['unit_code'])
db['unit'].update({'unit_code': 'cm', 'unit_type': length_id}, ['unit_code'])
db['unit'].update({'unit_code': 'm', 'unit_type': length_id}, ['unit_code'])
db['unit'].update({'unit_code': 'mm2', 'unit_type': surface_id}, ['unit_code'])
db['unit'].update({'unit_code': 'cm2', 'unit_type': surface_id}, ['unit_code'])
db['unit'].update({'unit_code': 'm2', 'unit_type': surface_id}, ['unit_code'])
db['unit'].update({'unit_code': 'mm3', 'unit_type': volume_id}, ['unit_code'])
db['unit'].update({'unit_code': 'cm3', 'unit_type': volume_id}, ['unit_code'])
db['unit'].update({'unit_code': 'm3', 'unit_type': volume_id}, ['unit_code'])
db['unit'].update({'unit_code': 'g', 'unit_type': mass_id}, ['unit_code'])
db['unit'].update({'unit_code': 'kg', 'unit_type': mass_id}, ['unit_code'])
db['unit'].update({'unit_code': 'N', 'unit_type': force_id}, ['unit_code'])

db['unit_type_description'].insert({'unit_type': length_id, 'language': en_id, 'unit_type_sdesc': 'Length', 'unit_type_ldesc': 'Length'})
db['unit_type_description'].insert({'unit_type': length_id, 'language': fr_id, 'unit_type_sdesc': 'Longueur', 'unit_type_ldesc': 'Longueur'})
db['unit_type_description'].insert({'unit_type': length_id, 'language': es_id, 'unit_type_sdesc': 'Longitud', 'unit_type_ldesc': 'Longitud'})
db['unit_type_description'].insert({'unit_type': surface_id, 'language': en_id, 'unit_type_sdesc': 'Surface', 'unit_type_ldesc': 'Surface'})
db['unit_type_description'].insert({'unit_type': surface_id, 'language': fr_id, 'unit_type_sdesc': 'Surface', 'unit_type_ldesc': 'Surface'})
db['unit_type_description'].insert({'unit_type': surface_id, 'language': es_id, 'unit_type_sdesc': 'Superficie', 'unit_type_ldesc': 'Superficie'})
db['unit_type_description'].insert({'unit_type': volume_id, 'language': en_id, 'unit_type_sdesc': 'Volume', 'unit_type_ldesc': 'Volume'})
db['unit_type_description'].insert({'unit_type': volume_id, 'language': fr_id, 'unit_type_sdesc': 'Volume', 'unit_type_ldesc': 'Volume'})
db['unit_type_description'].insert({'unit_type': volume_id, 'language': es_id, 'unit_type_sdesc': 'Volumen', 'unit_type_ldesc': 'Volumen'})
db['unit_type_description'].insert({'unit_type': mass_id, 'language': en_id, 'unit_type_sdesc': 'Mass', 'unit_type_ldesc': 'Mass'})
db['unit_type_description'].insert({'unit_type': mass_id, 'language': fr_id, 'unit_type_sdesc': 'Masse', 'unit_type_ldesc': 'Masse'})
db['unit_type_description'].insert({'unit_type': mass_id, 'language': es_id, 'unit_type_sdesc': 'Masa', 'unit_type_ldesc': 'Masa'})
db['unit_type_description'].insert({'unit_type': force_id, 'language': en_id, 'unit_type_sdesc': 'Force', 'unit_type_ldesc': 'Force'})
db['unit_type_description'].insert({'unit_type': force_id, 'language': fr_id, 'unit_type_sdesc': 'Force', 'unit_type_ldesc': 'Force'})
db['unit_type_description'].insert({'unit_type': force_id, 'language': es_id, 'unit_type_sdesc': 'Fuerza', 'unit_type_ldesc': 'Fuerza'})
