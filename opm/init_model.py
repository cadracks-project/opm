#!/usr/bin/env python
# coding: utf-8

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
language_table = db.create_table('language', primary_id='language_code', primary_type=db.types.text)
en_id = language_table.insert({'language_code': 'en', 'language_name': 'English'})
fr_id = language_table.insert({'language_code': 'fr', 'language_name': 'Français'})
es_id = language_table.insert({'language_code': 'es', 'language_name': 'Español'})

currency_table = db.create_table('currency', primary_id='currency_code', primary_type=db.types.text)
eur_id = currency_table.insert({'currency_code': 'EUR', 'is_ref': True, 'rate': 1.0})
usd_id = currency_table.insert({'currency_code': 'USD', 'is_ref': False, 'rate': 0.8})
gbp_id = currency_table.insert({'currency_code': 'GBP', 'is_ref': False, 'rate': 1.2})

country_table = db.create_table('country', primary_id='country_code', primary_type=db.types.text)
fra_id = country_table.insert({'country_code': 'FRA'})
eng_id = country_table.insert({'country_code': 'ENG'})
usa_id = country_table.insert({'country_code': 'USA'})

currency_description_table = db.create_table('currency_description', primary_id=False)
currency_description_table.create_column('currency', db.types.text)
currency_description_table.create_column('language', db.types.text)
currency_description_table.create_index(['currency', 'language'], name='currency_description_ix', unique=True)
currency_description_table.insert({'currency': eur_id, 'language': en_id, 'currency_sdesc': 'Euro', 'currency_ldesc': 'Euro'})
currency_description_table.insert({'currency': eur_id, 'language': fr_id, 'currency_sdesc': 'Euro', 'currency_ldesc': 'Euro'})
currency_description_table.insert({'currency': eur_id, 'language': es_id, 'currency_sdesc': 'Euro', 'currency_ldesc': 'Euro'})
currency_description_table.insert({'currency': usd_id, 'language': en_id, 'currency_sdesc': 'US Dollar', 'currency_ldesc': 'Unites States of America Dollar'})
currency_description_table.insert({'currency': usd_id, 'language': fr_id, 'currency_sdesc': 'Dollar US', 'currency_ldesc': 'Dollar Américain'})
currency_description_table.insert({'currency': usd_id, 'language': es_id, 'currency_sdesc': 'Dollar US', 'currency_ldesc': 'Dollar Americano'})
currency_description_table.insert({'currency': gbp_id, 'language': en_id, 'currency_sdesc': 'Pound', 'currency_ldesc': 'British Pound'})
currency_description_table.insert({'currency': gbp_id, 'language': fr_id, 'currency_sdesc': 'Livre', 'currency_ldesc': 'Livre sterling'})
currency_description_table.insert({'currency': gbp_id, 'language': es_id, 'currency_sdesc': 'Libra', 'currency_ldesc': 'Libra sterling'})

country_description_table = db.create_table('country_description', primary_id=False)
country_description_table.create_column('country', db.types.text)
country_description_table.create_column('language', db.types.text)
country_description_table.create_index(['country', 'language'], name='country_description_ix', unique=True)
country_description_table.insert({'country': fra_id, 'language': fr_id, 'country_sdesc': "France", 'country_ldesc': 'République Française'})
country_description_table.insert({'country': fra_id, 'language': en_id, 'country_sdesc': "France", 'country_ldesc': 'French Republic'})
country_description_table.insert({'country': fra_id, 'language': es_id, 'country_sdesc': "Francia", 'country_ldesc': 'Republica Francesa'})
country_description_table.insert({'country': eng_id, 'language': fr_id, 'country_sdesc': "Angleterre", 'country_ldesc': 'Angleterre'})
country_description_table.insert({'country': eng_id, 'language': en_id, 'country_sdesc': "England", 'country_ldesc': 'England'})
country_description_table.insert({'country': eng_id, 'language': es_id, 'country_sdesc': "Inglaterra", 'country_ldesc': 'Inglaterra'})
country_description_table.insert({'country': usa_id, 'language': fr_id, 'country_sdesc': "USA", 'country_ldesc': "Etats Unis d'Amérique"})
country_description_table.insert({'country': usa_id, 'language': en_id, 'country_sdesc': "USA", 'country_ldesc': 'Unites States of America'})
country_description_table.insert({'country': usa_id, 'language': es_id, 'country_sdesc': "EUA", 'country_ldesc': 'Estados Unidos de America'})

# #######
# Units #
#########
unit_table = db.create_table('unit', primary_id='unit_code', primary_type=db.types.text)
mm_id = unit_table.insert({'unit_code': 'mm', 'conversion': 1e3, 'unit_type': -1})
cm_id = unit_table.insert({'unit_code': 'cm', 'conversion': 1e2, 'unit_type': -1})
m_id = unit_table.insert({'unit_code': 'm', 'conversion': 1., 'unit_type': -1})
mm2_id = unit_table.insert({'unit_code': 'mm2', 'conversion': 1e6, 'unit_type': -1})
cm2_id = unit_table.insert({'unit_code': 'cm2', 'conversion': 1e4, 'unit_type': -1})
m2_id = unit_table.insert({'unit_code': 'm2', 'conversion': 1., 'unit_type': -1})
mm3_id = unit_table.insert({'unit_code': 'mm3', 'conversion': 1e9, 'unit_type': -1})
cm3_id = unit_table.insert({'unit_code': 'cm3', 'conversion': 1e6, 'unit_type': -1})
m3_id = unit_table.insert({'unit_code': 'm3', 'conversion': 1., 'unit_type': -1})
g_id = unit_table.insert({'unit_code': 'g', 'conversion': 1e3, 'unit_type': -1})
kg_id = unit_table.insert({'unit_code': 'kg', 'conversion': 1., 'unit_type': -1})
N_id = unit_table.insert({'unit_code': 'N', 'conversion': 1., 'unit_type': -1})
kg_per_m3_id = unit_table.insert({'unit_code': 'kg_per_m3', 'conversion': 1., 'unit_type': -1})
g_per_cm3_id = unit_table.insert({'unit_code': 'g_per_cm3', 'conversion': 1e3, 'unit_type': -1})

unit_description_table = db.create_table('unit_description', primary_id=False)
unit_description_table.create_column('unit', db.types.text)
unit_description_table.create_column('language', db.types.text)
unit_description_table.create_index(['unit', 'language'], name='unit_description_ix', unique=True)
unit_description_table.insert({'unit': mm_id, 'language': en_id, 'unit_sdesc': 'mm', 'unit_ldesc': 'Millimeter'})
unit_description_table.insert({'unit': mm_id, 'language': fr_id, 'unit_sdesc': 'mm', 'unit_ldesc': 'Millimètre'})
unit_description_table.insert({'unit': mm_id, 'language': es_id, 'unit_sdesc': 'mm', 'unit_ldesc': 'Millimetro'})
unit_description_table.insert({'unit': cm_id, 'language': en_id, 'unit_sdesc': 'cm', 'unit_ldesc': 'Centimeter'})
unit_description_table.insert({'unit': cm_id, 'language': fr_id, 'unit_sdesc': 'cm', 'unit_ldesc': 'Centimètre'})
unit_description_table.insert({'unit': cm_id, 'language': es_id, 'unit_sdesc': 'cm', 'unit_ldesc': 'Centimetro'})
unit_description_table.insert({'unit': m_id, 'language': en_id, 'unit_sdesc': 'm', 'unit_ldesc': 'Meter'})
unit_description_table.insert({'unit': m_id, 'language': fr_id, 'unit_sdesc': 'm', 'unit_ldesc': 'Mètre'})
unit_description_table.insert({'unit': m_id, 'language': es_id, 'unit_sdesc': 'm', 'unit_ldesc': 'Metro'})

unit_description_table.insert({'unit': mm2_id, 'language': en_id, 'unit_sdesc': 'mm²', 'unit_ldesc': 'Square millimeter'})
unit_description_table.insert({'unit': mm2_id, 'language': fr_id, 'unit_sdesc': 'mm²', 'unit_ldesc': 'Millimètre carré'})
unit_description_table.insert({'unit': mm2_id, 'language': es_id, 'unit_sdesc': 'mm²', 'unit_ldesc': 'Millimetro cuadrado'})
unit_description_table.insert({'unit': cm2_id, 'language': en_id, 'unit_sdesc': 'cm²', 'unit_ldesc': 'Square centimeter'})
unit_description_table.insert({'unit': cm2_id, 'language': fr_id, 'unit_sdesc': 'cm²', 'unit_ldesc': 'Centimètre carré'})
unit_description_table.insert({'unit': cm2_id, 'language': es_id, 'unit_sdesc': 'cm²', 'unit_ldesc': 'Centimetro cuadrado'})
unit_description_table.insert({'unit': m2_id, 'language': en_id, 'unit_sdesc': 'm²', 'unit_ldesc': 'Square meter'})
unit_description_table.insert({'unit': m2_id, 'language': fr_id, 'unit_sdesc': 'm²', 'unit_ldesc': 'Mètre carré'})
unit_description_table.insert({'unit': m2_id, 'language': es_id, 'unit_sdesc': 'm²', 'unit_ldesc': 'Metro cuadrado'})

unit_description_table.insert({'unit': mm3_id, 'language': en_id, 'unit_sdesc': 'mm³', 'unit_ldesc': 'Cube millimeter'})
unit_description_table.insert({'unit': mm3_id, 'language': fr_id, 'unit_sdesc': 'mm³', 'unit_ldesc': 'Millimètre cube'})
unit_description_table.insert({'unit': mm3_id, 'language': es_id, 'unit_sdesc': 'mm³', 'unit_ldesc': 'Millimetro cubo'})
unit_description_table.insert({'unit': cm3_id, 'language': en_id, 'unit_sdesc': 'cm³', 'unit_ldesc': 'Cube centimeter'})
unit_description_table.insert({'unit': cm3_id, 'language': fr_id, 'unit_sdesc': 'cm³', 'unit_ldesc': 'Centimètre cube'})
unit_description_table.insert({'unit': cm3_id, 'language': es_id, 'unit_sdesc': 'cm³', 'unit_ldesc': 'Centimetro cubo'})
unit_description_table.insert({'unit': m3_id, 'language': en_id, 'unit_sdesc': 'm³', 'unit_ldesc': 'Cube meter'})
unit_description_table.insert({'unit': m3_id, 'language': fr_id, 'unit_sdesc': 'm³', 'unit_ldesc': 'Mètre cube'})
unit_description_table.insert({'unit': m3_id, 'language': es_id, 'unit_sdesc': 'm³', 'unit_ldesc': 'Metro cubo'})

unit_description_table.insert({'unit': g_id, 'language': en_id, 'unit_sdesc': 'g', 'unit_ldesc': 'Gram'})
unit_description_table.insert({'unit': g_id, 'language': fr_id, 'unit_sdesc': 'g', 'unit_ldesc': 'Gramme'})
unit_description_table.insert({'unit': g_id, 'language': es_id, 'unit_sdesc': 'g', 'unit_ldesc': 'Gramo'})
unit_description_table.insert({'unit': kg_id, 'language': en_id, 'unit_sdesc': 'kg', 'unit_ldesc': 'Kilogram'})
unit_description_table.insert({'unit': kg_id, 'language': fr_id, 'unit_sdesc': 'kg', 'unit_ldesc': 'Kilogramme'})
unit_description_table.insert({'unit': kg_id, 'language': es_id, 'unit_sdesc': 'kg', 'unit_ldesc': 'Kilogramo'})

unit_description_table.insert({'unit': N_id, 'language': en_id, 'unit_sdesc': 'N', 'unit_ldesc': 'Newton'})
unit_description_table.insert({'unit': N_id, 'language': fr_id, 'unit_sdesc': 'N', 'unit_ldesc': 'Newton'})
unit_description_table.insert({'unit': N_id, 'language': es_id, 'unit_sdesc': 'N', 'unit_ldesc': 'Newton'})

unit_description_table.insert({'unit': kg_per_m3_id, 'language': en_id, 'unit_sdesc': 'kg/m³', 'unit_ldesc': 'Kilogram par cube meter'})
unit_description_table.insert({'unit': kg_per_m3_id, 'language': fr_id, 'unit_sdesc': 'kg/m³', 'unit_ldesc': 'Kilogramme par mètre cube'})
unit_description_table.insert({'unit': kg_per_m3_id, 'language': es_id, 'unit_sdesc': 'kg/m³', 'unit_ldesc': 'Kilogramo por metro cubo'})
unit_description_table.insert({'unit': g_per_cm3_id, 'language': en_id, 'unit_sdesc': 'g/cm³', 'unit_ldesc': 'Gram par cube centimeter'})
unit_description_table.insert({'unit': g_per_cm3_id, 'language': fr_id, 'unit_sdesc': 'g/cm³', 'unit_ldesc': 'Gramme par centimètre cube'})
unit_description_table.insert({'unit': g_per_cm3_id, 'language': es_id, 'unit_sdesc': 'g/cm³', 'unit_ldesc': 'Gramo por centimetro cubo'})

unit_type_table = db.create_table('unit_type', primary_id='unit_type_code', primary_type=db.types.text)
length_id = unit_type_table.insert({'unit_type_code': 'length', 'default_unit': mm_id})
surface_id = unit_type_table.insert({'unit_type_code': 'surface', 'default_unit': mm2_id})
volume_id = unit_type_table.insert({'unit_type_code': 'volume', 'default_unit': mm3_id})
mass_id = unit_type_table.insert({'unit_type_code': 'mass', 'default_unit': g_id})
force_id = unit_type_table.insert({'unit_type_code': 'force', 'default_unit': N_id})
volumique_mass_id = unit_type_table.insert({'unit_type_code': 'volumic_mass', 'default_unit': 'kg/m3'})

unit_table.update({'unit_code': 'mm', 'unit_type': length_id}, ['unit_code'])
unit_table.update({'unit_code': 'cm', 'unit_type': length_id}, ['unit_code'])
unit_table.update({'unit_code': 'm', 'unit_type': length_id}, ['unit_code'])
unit_table.update({'unit_code': 'mm2', 'unit_type': surface_id}, ['unit_code'])
unit_table.update({'unit_code': 'cm2', 'unit_type': surface_id}, ['unit_code'])
unit_table.update({'unit_code': 'm2', 'unit_type': surface_id}, ['unit_code'])
unit_table.update({'unit_code': 'mm3', 'unit_type': volume_id}, ['unit_code'])
unit_table.update({'unit_code': 'cm3', 'unit_type': volume_id}, ['unit_code'])
unit_table.update({'unit_code': 'm3', 'unit_type': volume_id}, ['unit_code'])
unit_table.update({'unit_code': 'g', 'unit_type': mass_id}, ['unit_code'])
unit_table.update({'unit_code': 'kg', 'unit_type': mass_id}, ['unit_code'])
unit_table.update({'unit_code': 'N', 'unit_type': force_id}, ['unit_code'])
unit_table.update({'unit_code': 'kg_per_m3', 'unit_type': volumique_mass_id}, ['unit_code'])
unit_table.update({'unit_code': 'g_per_cm3', 'unit_type': volumique_mass_id}, ['unit_code'])

unit_type_description_table = db.create_table('unit_type_description', primary_id=False)
unit_type_description_table.create_column('unit_type', db.types.text)
unit_type_description_table.create_column('language', db.types.text)
unit_type_description_table.create_index(['unit_type', 'language'], name='unit_type_description_ix', unique=True)
unit_type_description_table.insert({'unit_type': length_id, 'language': en_id, 'unit_type_sdesc': 'Length', 'unit_type_ldesc': 'Length'})
unit_type_description_table.insert({'unit_type': length_id, 'language': fr_id, 'unit_type_sdesc': 'Longueur', 'unit_type_ldesc': 'Longueur'})
unit_type_description_table.insert({'unit_type': length_id, 'language': es_id, 'unit_type_sdesc': 'Longitud', 'unit_type_ldesc': 'Longitud'})
unit_type_description_table.insert({'unit_type': surface_id, 'language': en_id, 'unit_type_sdesc': 'Surface', 'unit_type_ldesc': 'Surface'})
unit_type_description_table.insert({'unit_type': surface_id, 'language': fr_id, 'unit_type_sdesc': 'Surface', 'unit_type_ldesc': 'Surface'})
unit_type_description_table.insert({'unit_type': surface_id, 'language': es_id, 'unit_type_sdesc': 'Superficie', 'unit_type_ldesc': 'Superficie'})
unit_type_description_table.insert({'unit_type': volume_id, 'language': en_id, 'unit_type_sdesc': 'Volume', 'unit_type_ldesc': 'Volume'})
unit_type_description_table.insert({'unit_type': volume_id, 'language': fr_id, 'unit_type_sdesc': 'Volume', 'unit_type_ldesc': 'Volume'})
unit_type_description_table.insert({'unit_type': volume_id, 'language': es_id, 'unit_type_sdesc': 'Volumen', 'unit_type_ldesc': 'Volumen'})
unit_type_description_table.insert({'unit_type': mass_id, 'language': en_id, 'unit_type_sdesc': 'Mass', 'unit_type_ldesc': 'Mass'})
unit_type_description_table.insert({'unit_type': mass_id, 'language': fr_id, 'unit_type_sdesc': 'Masse', 'unit_type_ldesc': 'Masse'})
unit_type_description_table.insert({'unit_type': mass_id, 'language': es_id, 'unit_type_sdesc': 'Masa', 'unit_type_ldesc': 'Masa'})
unit_type_description_table.insert({'unit_type': force_id, 'language': en_id, 'unit_type_sdesc': 'Force', 'unit_type_ldesc': 'Force'})
unit_type_description_table.insert({'unit_type': force_id, 'language': fr_id, 'unit_type_sdesc': 'Force', 'unit_type_ldesc': 'Force'})
unit_type_description_table.insert({'unit_type': force_id, 'language': es_id, 'unit_type_sdesc': 'Fuerza', 'unit_type_ldesc': 'Fuerza'})

# ###########
# Materials #
# ###########
material_category_table = db.create_table('material_category', primary_id='material_category_code', primary_type=db.types.text)
metal_id = material_category_table.insert({'material_category_code': 'METAL'})
polymer_id = material_category_table.insert({'material_category_code': 'POLYMER'})
wood_id = material_category_table.insert({'material_category_code': 'WOOD'})
ceramic_id = material_category_table.insert({'material_category_code': 'CERAMIC'})
composite_id = material_category_table.insert({'material_category_code': 'COMPOSITE'})

material_category_description_table = db.create_table('material_category_description', primary_id=False)
material_category_description_table.create_column('material_category', db.types.text)
material_category_description_table.create_column('language', db.types.text)
material_category_description_table.create_index(['material_category', 'language'], name='material_category_description_ix', unique=True)
material_category_description_table.insert({'material_category': metal_id, 'language': en_id, 'material_category_sdesc': 'Metal', 'material_category_ldesc': 'Metal'})
material_category_description_table.insert({'material_category': metal_id, 'language': fr_id, 'material_category_sdesc': 'Métal', 'material_category_ldesc': 'Métal'})
material_category_description_table.insert({'material_category': metal_id, 'language': es_id, 'material_category_sdesc': 'Metal', 'material_category_ldesc': 'Metal'})
material_category_description_table.insert({'material_category': polymer_id, 'language': en_id, 'material_category_sdesc': 'Polymer', 'material_category_ldesc': 'Polymer'})
material_category_description_table.insert({'material_category': polymer_id, 'language': fr_id, 'material_category_sdesc': 'Polymère', 'material_category_ldesc': 'Polymère'})
material_category_description_table.insert({'material_category': polymer_id, 'language': es_id, 'material_category_sdesc': 'Polímero', 'material_category_ldesc': 'Polímero'})
material_category_description_table.insert({'material_category': wood_id, 'language': en_id, 'material_category_sdesc': 'Wood', 'material_category_ldesc': 'Wood'})
material_category_description_table.insert({'material_category': wood_id, 'language': fr_id, 'material_category_sdesc': 'Bois', 'material_category_ldesc': 'Bois'})
material_category_description_table.insert({'material_category': wood_id, 'language': es_id, 'material_category_sdesc': 'Madera', 'material_category_ldesc': 'Madera'})
material_category_description_table.insert({'material_category': ceramic_id, 'language': en_id, 'material_category_sdesc': 'Ceramic', 'material_category_ldesc': 'Ceramic'})
material_category_description_table.insert({'material_category': ceramic_id, 'language': fr_id, 'material_category_sdesc': 'Céramique', 'material_category_ldesc': 'Céramique'})
material_category_description_table.insert({'material_category': ceramic_id, 'language': es_id, 'material_category_sdesc': 'Cerámico', 'material_category_ldesc': 'Cerámico'})
material_category_description_table.insert({'material_category': composite_id, 'language': en_id, 'material_category_sdesc': 'Composite', 'material_category_ldesc': 'Composite material'})
material_category_description_table.insert({'material_category': composite_id, 'language': fr_id, 'material_category_sdesc': 'Composite', 'material_category_ldesc': 'Matériau composite'})
material_category_description_table.insert({'material_category': composite_id, 'language': es_id, 'material_category_sdesc': 'Compuesto', 'material_category_ldesc': 'Material compuesto'})

material_subcategory_table = db.create_table('material_subcategory', primary_id='material_subcategory_code', primary_type=db.types.text)
aluminium_id = material_subcategory_table.insert({'material_category': metal_id, 'material_subcategory_code': 'ALUMINIUM'})
steel_id = material_subcategory_table.insert({'material_category': metal_id, 'material_subcategory_code': 'STEEL'})
titanium_id = material_subcategory_table.insert({'material_category': metal_id, 'material_subcategory_code': 'TITANIUM'})
thermoplastic_id = material_subcategory_table.insert({'material_category': polymer_id, 'material_subcategory_code': 'THERMOPLASTIC'})
thermoset_id = material_subcategory_table.insert({'material_category': polymer_id, 'material_subcategory_code': 'THERMOSET'})
softwood_id = material_subcategory_table.insert({'material_category': wood_id, 'material_subcategory_code': 'SOFTWOOD'})
hardwood_id = material_subcategory_table.insert({'material_category': wood_id, 'material_subcategory_code': 'HARDWOOD'})
cermet_id = material_subcategory_table.insert({'material_category': composite_id, 'material_subcategory_code': 'CERMET'})
cfrp_id = material_subcategory_table.insert({'material_category': composite_id, 'material_subcategory_code': 'CFRP'})
polyurethane_id = material_subcategory_table.insert({'material_category': polymer_id, 'material_subcategory_code': 'PU'})

material_subcategory_description_table = db.create_table('material_subcategory_description', primary_id=False)
material_subcategory_description_table.create_column('material_subcategory', db.types.text)
material_subcategory_description_table.create_column('language', db.types.text)
material_subcategory_description_table.create_index(['material_subcategory', 'language'], name='material_subcategory_description_ix', unique=True)
material_subcategory_description_table.insert({'material_subcategory': aluminium_id, 'language': en_id, 'material_subcategory_sdesc': 'Aluminium', 'material_subcategory_ldesc': 'Aluminium'})
material_subcategory_description_table.insert({'material_subcategory': aluminium_id, 'language': fr_id, 'material_subcategory_sdesc': 'Alu', 'material_subcategory_ldesc': 'Aluminium'})
material_subcategory_description_table.insert({'material_subcategory': aluminium_id, 'language': es_id, 'material_subcategory_sdesc': 'Aluminio', 'material_subcategory_ldesc': 'Aluminio'})
material_subcategory_description_table.insert({'material_subcategory': steel_id, 'language': en_id, 'material_subcategory_sdesc': 'Steel', 'material_subcategory_ldesc': 'Steel'})
material_subcategory_description_table.insert({'material_subcategory': steel_id, 'language': fr_id, 'material_subcategory_sdesc': 'Acier', 'material_subcategory_ldesc': 'Acier'})
material_subcategory_description_table.insert({'material_subcategory': steel_id, 'language': es_id, 'material_subcategory_sdesc': 'Acero', 'material_subcategory_ldesc': 'Acero'})
material_subcategory_description_table.insert({'material_subcategory': titanium_id, 'language': en_id, 'material_subcategory_sdesc': 'Titanium', 'material_subcategory_ldesc': 'Titanium'})
material_subcategory_description_table.insert({'material_subcategory': titanium_id, 'language': fr_id, 'material_subcategory_sdesc': 'Titane', 'material_subcategory_ldesc': 'Titane'})
material_subcategory_description_table.insert({'material_subcategory': titanium_id, 'language': es_id, 'material_subcategory_sdesc': 'Titanio', 'material_subcategory_ldesc': 'Titanio'})
material_subcategory_description_table.insert({'material_subcategory': thermoplastic_id, 'language': en_id, 'material_subcategory_sdesc': 'Thermoplastic', 'material_subcategory_ldesc': 'Thermoplastic polymer'})
material_subcategory_description_table.insert({'material_subcategory': thermoplastic_id, 'language': fr_id, 'material_subcategory_sdesc': 'Thermoplastique', 'material_subcategory_ldesc': 'Polymère thermoplastique'})
material_subcategory_description_table.insert({'material_subcategory': thermoplastic_id, 'language': es_id, 'material_subcategory_sdesc': 'Termoplástico', 'material_subcategory_ldesc': 'Termoplástico'})
material_subcategory_description_table.insert({'material_subcategory': thermoset_id, 'language': en_id, 'material_subcategory_sdesc': 'Theroset', 'material_subcategory_ldesc': 'Thermoset polymer'})
material_subcategory_description_table.insert({'material_subcategory': thermoset_id, 'language': fr_id, 'material_subcategory_sdesc': 'Thermodurcissable', 'material_subcategory_ldesc': 'Polymère thermodurcissable'})
material_subcategory_description_table.insert({'material_subcategory': thermoset_id, 'language': es_id, 'material_subcategory_sdesc': 'Termoestable', 'material_subcategory_ldesc': 'Polímero termoestable'})
material_subcategory_description_table.insert({'material_subcategory': softwood_id, 'language': en_id, 'material_subcategory_sdesc': 'Softwood', 'material_subcategory_ldesc': 'Softwood'})
material_subcategory_description_table.insert({'material_subcategory': softwood_id, 'language': fr_id, 'material_subcategory_sdesc': 'Bois tendre', 'material_subcategory_ldesc': 'Bois tendre'})
material_subcategory_description_table.insert({'material_subcategory': softwood_id, 'language': es_id, 'material_subcategory_sdesc': 'Madera blanda', 'material_subcategory_ldesc': 'Madera blanda'})
material_subcategory_description_table.insert({'material_subcategory': hardwood_id, 'language': en_id, 'material_subcategory_sdesc': 'Hardwood', 'material_subcategory_ldesc': 'Hardwood'})
material_subcategory_description_table.insert({'material_subcategory': hardwood_id, 'language': fr_id, 'material_subcategory_sdesc': 'Bois dur', 'material_subcategory_ldesc': 'Bois dur'})
material_subcategory_description_table.insert({'material_subcategory': hardwood_id, 'language': es_id, 'material_subcategory_sdesc': 'Madera dura', 'material_subcategory_ldesc': 'Madera dura'})
material_subcategory_description_table.insert({'material_subcategory': cermet_id, 'language': en_id, 'material_subcategory_sdesc': 'Cermet', 'material_subcategory_ldesc': 'Ceramic-metal composite'})
material_subcategory_description_table.insert({'material_subcategory': cermet_id, 'language': fr_id, 'material_subcategory_sdesc': 'Cermet', 'material_subcategory_ldesc': 'Composite céramique-métal'})
material_subcategory_description_table.insert({'material_subcategory': cermet_id, 'language': es_id, 'material_subcategory_sdesc': 'Cermet', 'material_subcategory_ldesc': 'Compuesto metal-cerámico'})
material_subcategory_description_table.insert({'material_subcategory': cfrp_id, 'language': en_id, 'material_subcategory_sdesc': 'CFRP', 'material_subcategory_ldesc': 'Carbon fiber reinforced polymer'})
material_subcategory_description_table.insert({'material_subcategory': cfrp_id, 'language': fr_id, 'material_subcategory_sdesc': 'PRFC', 'material_subcategory_ldesc': 'Polymère renforcé de fibres de carbone'})
material_subcategory_description_table.insert({'material_subcategory': cfrp_id, 'language': es_id, 'material_subcategory_sdesc': 'PRFC', 'material_subcategory_ldesc': 'Polímero consolidado de fibras de carbonio'})
material_subcategory_description_table.insert({'material_subcategory': polyurethane_id, 'language': en_id, 'material_subcategory_sdesc': 'PU', 'material_subcategory_ldesc': 'Polyurethane'})
material_subcategory_description_table.insert({'material_subcategory': polyurethane_id, 'language': fr_id, 'material_subcategory_sdesc': 'PU', 'material_subcategory_ldesc': 'Polyurethane'})
material_subcategory_description_table.insert({'material_subcategory': polyurethane_id, 'language': es_id, 'material_subcategory_sdesc': 'PU', 'material_subcategory_ldesc': 'Poliuretano'})

material_property_table = db.create_table('material_property', primary_id='material_property_code', primary_type=db.types.text)
modulus_id = material_property_table.insert({'material_property_code': 'MODULUS'})
volumic_mass_id = material_property_table.insert({'material_property_code': 'VOLUMIC_MASS'})
resistivity_id = material_property_table.insert({'material_property_code': 'RESISTIVITY'})

material_property_description_table = db.create_table('material_property_description', primary_id=False)
material_property_description_table.create_column('material_property', db.types.text)
material_property_description_table.create_column('language', db.types.text)
material_property_description_table.create_index(['material_property', 'language'], name='material_property_description_ix', unique=True)
material_property_description_table.insert({'material_property': modulus_id, 'language': en_id, 'material_property_sdesc': 'Modulus', 'material_property_ldesc': 'Young modulus'})
material_property_description_table.insert({'material_property': modulus_id, 'language': fr_id, 'material_property_sdesc': 'Module', 'material_property_ldesc': "Module d'Young"})
material_property_description_table.insert({'material_property': modulus_id, 'language': es_id, 'material_property_sdesc': 'Módulo', 'material_property_ldesc': "Módulo de Young"})
material_property_description_table.insert({'material_property': volumic_mass_id, 'language': en_id, 'material_property_sdesc': 'Density', 'material_property_ldesc': 'Density'})
material_property_description_table.insert({'material_property': volumic_mass_id, 'language': fr_id, 'material_property_sdesc': 'Densité', 'material_property_ldesc': "Densité"})
material_property_description_table.insert({'material_property': volumic_mass_id, 'language': es_id, 'material_property_sdesc': 'Densidad', 'material_property_ldesc': "Densidad"})
material_property_description_table.insert({'material_property': resistivity_id, 'language': en_id, 'material_property_sdesc': 'Resistivity', 'material_property_ldesc': 'Resistivity'})
material_property_description_table.insert({'material_property': resistivity_id, 'language': fr_id, 'material_property_sdesc': 'Résistivité', 'material_property_ldesc': "Résistivité"})
material_property_description_table.insert({'material_property': resistivity_id, 'language': es_id, 'material_property_sdesc': 'Resistividad', 'material_property_ldesc': "Resistividad"})

material_table = db.create_table('material', primary_id='material_code', primary_type=db.types.text)
stainless_A4_id = material_table.insert({'material_code': 'STAINLESS_A4', 'material_subcategory': steel_id})
stainless_A2_id = material_table.insert({'material_code': 'STAINLESS_A2', 'material_subcategory': steel_id})
alu_7075_t6_id = material_table.insert({'material_code': 'ALU7075-T6', 'material_subcategory': aluminium_id})
polyurethane_paint_id = material_table.insert({'material_code': 'PU_PAINT', 'material_subcategory': polyurethane_id})

material_description_table = db.create_table('material_description', primary_id=False)
material_description_table.create_column('material', db.types.text)
material_description_table.create_column('language', db.types.text)
material_description_table.create_index(['material', 'language'], name='material_description_ix', unique=True)
material_description_table.insert({'material': stainless_A4_id, 'language': en_id, 'material_sdesc': "A4 stainless steel", 'material_ldesc': "A4 stainless steel"})
material_description_table.insert({'material': stainless_A4_id, 'language': fr_id, 'material_sdesc': "Inox A4", 'material_ldesc': "Acier inoxydable A4"})
material_description_table.insert({'material': stainless_A4_id, 'language': es_id, 'material_sdesc': "Inoxidable A4", 'material_ldesc': "Acero inoxidable A4"})
material_description_table.insert({'material': stainless_A2_id, 'language': en_id, 'material_sdesc': "A2 stainless steel", 'material_ldesc': "A2 stainless steel"})
material_description_table.insert({'material': stainless_A2_id, 'language': fr_id, 'material_sdesc': "Inox A2", 'material_ldesc': "Acier inoxydable A2"})
material_description_table.insert({'material': stainless_A2_id, 'language': es_id, 'material_sdesc': "Inoxidable A2", 'material_ldesc': "Acero inoxidable A2"})
material_description_table.insert({'material': alu_7075_t6_id, 'language': en_id, 'material_sdesc': "7075-T6", 'material_ldesc': "Aluminium 7075-T6"})
material_description_table.insert({'material': alu_7075_t6_id, 'language': fr_id, 'material_sdesc': "7075-T6", 'material_ldesc': "Aluminium 7075-T6, aka Zicral, Ergal et Fortal Constructal"})
material_description_table.insert({'material': alu_7075_t6_id, 'language': es_id, 'material_sdesc': "7075-T6", 'material_ldesc': "Aluminio 7075-T6"})
material_description_table.insert({'material': polyurethane_paint_id, 'language': en_id, 'material_sdesc': "PU paint", 'material_ldesc': "Polyurethane paint"})
material_description_table.insert({'material': polyurethane_paint_id, 'language': fr_id, 'material_sdesc': "Peinture PU", 'material_ldesc': "Peinture polyurethane"})
material_description_table.insert({'material': polyurethane_paint_id, 'language': es_id, 'material_sdesc': "Pintura PU", 'material_ldesc': "Pintura poliuretano"})

material_properties_table = db.create_table('material_properties', primary_id=False)
material_properties_table.create_column('material', db.types.text)
material_properties_table.create_column('material_property', db.types.text)
material_properties_table.create_index(['material', 'material_property'], name='material_properties_ix', unique=True)
material_properties_table.insert({'material': alu_7075_t6_id, 'material_property': volumic_mass_id, 'value': 2.81, 'unit': g_per_cm3_id})
material_properties_table.insert({'material': stainless_A4_id, 'material_property': volumic_mass_id, 'value': 8000, 'unit': kg_per_m3_id})

# todo : properties may depend on temperature

# ############
# Composites #
# ############
composite_technology_table = db.create_table('composite_technology', primary_id='composite_technology_code', primary_type=db.types.text)
wet_layup_id = db['composite_technology'].insert({'composite_technology_code': 'WET_LAYUP'})
vacuum_id = db['composite_technology'].insert({'composite_technology_code': 'VACUUM'})
infusion_id = db['composite_technology'].insert({'composite_technology_code': 'INFUSION'})
prepreg_id = db['composite_technology'].insert({'composite_technology_code': 'PREPREG'})

composite_technology_description_table = db.create_table('composite_technology_description', primary_id=False)
composite_technology_description_table.create_column('composite_technology', db.types.text)
composite_technology_description_table.create_column('language', db.types.text)
composite_technology_description_table.create_index(['composite_technology', 'language'], name='composite_technology_description_ix', unique=True)
composite_technology_description_table.insert({'composite_technology': wet_layup_id, 'language': en_id, 'composite_technology_sdesc': 'Wet layup', 'composite_technology_ldesc': 'Manual wet layup'})
composite_technology_description_table.insert({'composite_technology': wet_layup_id, 'language': fr_id, 'composite_technology_sdesc': 'Voie humide', 'composite_technology_ldesc': 'Voie humide'})
composite_technology_description_table.insert({'composite_technology': wet_layup_id, 'language': es_id, 'composite_technology_sdesc': 'Bandeja húmeda', 'composite_technology_ldesc': 'Bandeja húmeda'})
composite_technology_description_table.insert({'composite_technology': vacuum_id, 'language': en_id, 'composite_technology_sdesc': 'Vacuum', 'composite_technology_ldesc': 'Vacuum bagging'})
composite_technology_description_table.insert({'composite_technology': vacuum_id, 'language': fr_id, 'composite_technology_sdesc': 'Vide', 'composite_technology_ldesc': 'Sous vide'})
composite_technology_description_table.insert({'composite_technology': vacuum_id, 'language': es_id, 'composite_technology_sdesc': 'Vacío', 'composite_technology_ldesc': 'Vacío'})
composite_technology_description_table.insert({'composite_technology': infusion_id, 'language': en_id, 'composite_technology_sdesc': 'Infusion', 'composite_technology_ldesc': 'Infusion'})
composite_technology_description_table.insert({'composite_technology': infusion_id, 'language': fr_id, 'composite_technology_sdesc': 'Infusion', 'composite_technology_ldesc': 'Infusion'})
composite_technology_description_table.insert({'composite_technology': infusion_id, 'language': es_id, 'composite_technology_sdesc': 'Infusión', 'composite_technology_ldesc': 'Infusión'})
composite_technology_description_table.insert({'composite_technology': prepreg_id, 'language': en_id, 'composite_technology_sdesc': 'Prepreg', 'composite_technology_ldesc': 'Pre-impregnated'})
composite_technology_description_table.insert({'composite_technology': prepreg_id, 'language': fr_id, 'composite_technology_sdesc': 'Prépreg', 'composite_technology_ldesc': 'Pré-imprégné'})
composite_technology_description_table.insert({'composite_technology': prepreg_id, 'language': es_id, 'composite_technology_sdesc': 'Preimpregnado', 'composite_technology_ldesc': 'Preimpregnado'})

composite_laminate_table = db.create_table('composite_laminate', primary_id='composite_laminate_code', primary_type=db.types.text)
composite_laminate_table.create_column('matrix_material', db.types.text)  # FK to material
composite_laminate_table.create_column('composite_technology', db.types.text)  # FK to composite_technology

composite_laminate_plies_table = db.create_table('composite_laminate_plies', primary_id=False)
composite_laminate_plies_table.create_column('composite_laminate', db.types.text)
composite_laminate_plies_table.create_column('composite_ply', db.types.text)
composite_laminate_plies_table.create_column('order', db.types.integer)
composite_laminate_plies_table.create_index(['composite_laminate', 'order'], name='composite_laminate_plies_ix', unique=True)

composite_ply_table = db.create_table('composite_ply', primary_id='composite_ply_code', primary_type=db.types.text)
composite_ply_table.create_column('composite_reinforcement', db.types.text)
composite_ply_table.create_column('material', db.types.text)  # FK to material
composite_ply_table.create_column('cad_file', db.types.text)
composite_ply_table.create_column('cad_file_flat', db.types.text)  # -> how to cut the reinforcement

# ############
# Suppliers #
# ############
supplier_table = db.create_table('supplier', primary_id='supplier_code', primary_type=db.types.text)
thepaintshop_id = supplier_table.insert({'supplier_code': 'THE_PAINT_SHOP', 'supplier_name': 'The Paint Shop', 'supplier_website': 'www.thepaintshop.com', 'supplier_email': 'info@thepaintshop.com', 'country': usa_id})

part_supplier_table = db.create_table('part_supplier', primary_id=False)
part_supplier_table.create_column('part_definition', db.types.text)  # FK
part_supplier_table.create_column('supplier', db.types.text)  # FK
part_supplier_table.create_column('preference_order', db.types.integer)
part_supplier_table.create_column('supplier_reference', db.types.text)
part_supplier_table.create_column('price', db.types.float)
part_supplier_table.create_column('price_currency', db.types.text)  # FK
part_supplier_table.create_column('price_unit', db.types.text)  # FK
part_supplier_table.create_index(['part_definition', 'supplier', 'preference_order'], name='part_supplier_ix_0', unique=True)
part_supplier_table.create_index(['part_definition', 'supplier'], name='part_supplier_ix_1', unique=False)


# ##########
# Coatings #
# ##########
coating_table = db.create_table('coating', primary_id='coating_code', primary_type=db.types.text)
pu_2c_id = coating_table.insert({'coating_code': 'PU_2C', 'material': polyurethane_paint_id})

coating_description_table = db.create_table('coating_description', primary_id=False)
coating_description_table.create_column('coating', db.types.text)
coating_description_table.create_column('language', db.types.text)
coating_description_table.create_index(['coating', 'language'], name='coating_description_ix', unique=True)
coating_description_table.insert({'coating': pu_2c_id, 'language': en_id, 'coating_sdesc': "2 part PU paint", 'coating_ldesc': '2 part polyurethane paint'})
coating_description_table.insert({'coating': pu_2c_id, 'language': fr_id, 'coating_sdesc': "Peinture PU 2 composants", 'coating_ldesc': 'Peinture polyurethane 2 composants'})
coating_description_table.insert({'coating': pu_2c_id, 'language': es_id, 'coating_sdesc': "Pintura PU 2 composantes", 'coating_ldesc': 'Pintura poliuretano 2 composantes'})

coating_supplier_table = db.create_table('coating_supplier', primary_id=False)
coating_supplier_table.create_column('coating', db.types.text)
coating_supplier_table.create_column('supplier', db.types.text)
coating_supplier_table.create_column('preference_order', db.types.integer)
coating_supplier_table.create_index(['coating', 'supplier', 'preference_order'], name='coating_supplier_ix', unique=True)
coating_supplier_table.insert({'coating': pu_2c_id, 'supplier': thepaintshop_id, 'preference_order': 1, 'supplier_reference': 'PU-00073', 'price': 0.05, 'price_currency': usd_id, 'price_unit': cm3_id})

part_coating_table = db.create_table('part_coating', primary_id=False)
part_coating_table.create_column('part_definition', db.types.text)
part_coating_table.create_column('part_occurrence', db.types.text)
part_coating_table.create_column('coating', db.types.text)
part_coating_table.create_column('order', db.types.integer)
part_coating_table.create_column('required_quantity', db.types.float)
part_coating_table.create_column('required_quantity_unit', db.types.text)  # FK to units


# #############
# Simulations #
# #############
simulation_type_table = db.create_table('simulation_type', primary_id='simulation_type_code', primary_type=db.types.text)
cfd_id = simulation_type_table.insert({'simulation_type_code': 'CFD'})
fea_id = simulation_type_table.insert({'simulation_type_code': 'FEA'})
fsi_id = simulation_type_table.insert({'simulation_type_code': 'FSI'})

simulation_type_description_table = db.create_table('simulation_type_description', primary_id=False)
simulation_type_description_table.create_column('simulation_type', db.types.text)
simulation_type_description_table.create_column('language', db.types.text)
simulation_type_description_table.create_index(['simulation_type', 'language'], name='simulation_type_description_ix', unique=True)
simulation_type_description_table.insert({'simulation_type': cfd_id, 'language': en_id, 'simulation_type_sdesc': "CFD", 'simulation_type_ldesc': 'Computational fluid dynamics'})
simulation_type_description_table.insert({'simulation_type': cfd_id, 'language': fr_id, 'simulation_type_sdesc': "CFD", 'simulation_type_ldesc': 'Dynamique des fluides numérique'})
simulation_type_description_table.insert({'simulation_type': cfd_id, 'language': es_id, 'simulation_type_sdesc': "CFD", 'simulation_type_ldesc': 'Dinamica numerica de los fluidos'})
simulation_type_description_table.insert({'simulation_type': fea_id, 'language': en_id, 'simulation_type_sdesc': "FEA", 'simulation_type_ldesc': 'Finite elements analysis'})
simulation_type_description_table.insert({'simulation_type': fea_id, 'language': fr_id, 'simulation_type_sdesc': "FEA", 'simulation_type_ldesc': 'Analyse éléments finis'})
simulation_type_description_table.insert({'simulation_type': fea_id, 'language': es_id, 'simulation_type_sdesc': "FEA", 'simulation_type_ldesc': 'Análisis de elementos finitos'})
simulation_type_description_table.insert({'simulation_type': fsi_id, 'language': en_id, 'simulation_type_sdesc': "FSI", 'simulation_type_ldesc': 'Fluid structure interaction'})
simulation_type_description_table.insert({'simulation_type': fsi_id, 'language': fr_id, 'simulation_type_sdesc': "IFS", 'simulation_type_ldesc': 'Interaction fluide structure'})
simulation_type_description_table.insert({'simulation_type': fsi_id, 'language': es_id, 'simulation_type_sdesc': "IEF", 'simulation_type_ldesc': 'Interacción estructura fluida'})

simulation_type_format_table = db.create_table('simulation_type_format', primary_id='simulation_type_format_code', primary_type=db.types.text)
code_saturne_id = simulation_type_format_table.insert({'simulation_type_format_code': 'CODE_SATURNE', 'simulation_type': cfd_id})
openfoam_id = simulation_type_format_table.insert({'simulation_type_format_code': 'OPENFOAM', 'simulation_type': cfd_id})
code_aster_id = simulation_type_format_table.insert({'simulation_type_format_code': 'CODE_ASTER', 'simulation_type': fea_id})

simulation_type_format_description_table = db.create_table('simulation_type_format_description', primary_id=False)
simulation_type_format_description_table.create_column('simulation_type_format', db.types.text)
simulation_type_format_description_table.create_column('language', db.types.text)
simulation_type_format_description_table.create_index(['simulation_type_format', 'language'], name='simulation_type_format_description_ix', unique=True)
simulation_type_format_description_table.insert({'simulation_type_format': code_saturne_id, 'language': en_id, 'simulation_type_format_sdesc': "Code Saturne", 'simulation_type_format_ldesc': 'Code Saturne'})
simulation_type_format_description_table.insert({'simulation_type_format': code_saturne_id, 'language': fr_id, 'simulation_type_format_sdesc': "Code Saturne", 'simulation_type_format_ldesc': 'Code Saturne'})
simulation_type_format_description_table.insert({'simulation_type_format': code_saturne_id, 'language': es_id, 'simulation_type_format_sdesc': "Code Saturne", 'simulation_type_format_ldesc': 'Code Saturne'})
simulation_type_format_description_table.insert({'simulation_type_format': openfoam_id, 'language': en_id, 'simulation_type_format_sdesc': "OpenFOAM", 'simulation_type_format_ldesc': 'OpenFOAM case'})
simulation_type_format_description_table.insert({'simulation_type_format': openfoam_id, 'language': fr_id, 'simulation_type_format_sdesc': "OpenFOAM", 'simulation_type_format_ldesc': 'Simulation OpenFOAM'})
simulation_type_format_description_table.insert({'simulation_type_format': openfoam_id, 'language': es_id, 'simulation_type_format_sdesc': "OpenFOAM", 'simulation_type_format_ldesc': 'OpenFOAM'})
simulation_type_format_description_table.insert({'simulation_type_format': code_aster_id, 'language': en_id, 'simulation_type_format_sdesc': "Code Aster", 'simulation_type_format_ldesc': 'Code Aster'})
simulation_type_format_description_table.insert({'simulation_type_format': code_aster_id, 'language': fr_id, 'simulation_type_format_sdesc': "Code Aster", 'simulation_type_format_ldesc': 'Code Aster'})
simulation_type_format_description_table.insert({'simulation_type_format': code_aster_id, 'language': es_id, 'simulation_type_format_sdesc': "Code Aster", 'simulation_type_format_ldesc': 'Code Aster'})

simulation_table = db.create_table('simulation', primary_id='simulation_code', primary_type=db.types.text)
simulation_table.create_column('simulation_code', db.types.text)
simulation_table.create_column('part_definition', db.types.text)
simulation_table.create_column('assembly', db.types.text)
simulation_table.create_column('product', db.types.text)
simulation_table.create_column('simulation_type_format', db.types.text)
simulation_table.create_column('simulation_path', db.types.text)

simulation_description_table = db.create_table('simulation_description', primary_id=False)
simulation_description_table.create_column('simulation', db.types.text)
simulation_description_table.create_column('language', db.types.text)
simulation_description_table.create_column('simulation_sdesc', db.types.text)
simulation_description_table.create_column('simulation_ldesc', db.types.text)
simulation_description_table.create_index(['simulation', 'language'], name='simulation_description_ix', unique=True)


# ###########
# Documents #
# ###########
document_type_table = db.create_table('document_type', primary_id='document_type_code', primary_type=db.types.text)
datasheet_id = document_type_table.insert({'document_type_code': 'DATASHEET'})
manual_id = document_type_table.insert({'document_type_code': 'MANUAL'})

document_type_description_table = db.create_table('document_type_description', primary_id=False)
document_type_description_table.create_column('document_type', db.types.text)
document_type_description_table.create_column('language', db.types.text)
document_type_description_table.create_index(['document_type', 'language'], name='document_type_description_ix', unique=True)
document_type_description_table.insert({'document_type': datasheet_id, 'language': en_id, 'document_type_sdesc': "Datasheet", 'document_type_ldesc': 'Datasheet'})
document_type_description_table.insert({'document_type': datasheet_id, 'language': fr_id, 'document_type_sdesc': "Fiche technique", 'document_type_ldesc': 'Fiche technique'})
document_type_description_table.insert({'document_type': datasheet_id, 'language': es_id, 'document_type_sdesc': "Ficha de datos", 'document_type_ldesc': 'Ficha de datos'})
document_type_description_table.insert({'document_type': manual_id, 'language': en_id, 'document_type_sdesc': "Manual", 'document_type_ldesc': 'Manual'})
document_type_description_table.insert({'document_type': manual_id, 'language': fr_id, 'document_type_sdesc': "Mode d'emploi", 'document_type_ldesc': "Mode d'emploi"})
document_type_description_table.insert({'document_type': manual_id, 'language': es_id, 'document_type_sdesc': "Manual", 'document_type_ldesc': 'Manual'})

document_format_table = db.create_table('document_format', primary_id='document_format_code', primary_type=db.types.text)
odt_id = document_format_table.insert({'document_format_code': 'ODT'})
pdf_id = document_format_table.insert({'document_format_code': 'PDF'})

document_format_description_table = db.create_table('document_format_description', primary_id=False)
document_format_description_table.create_column('document_format', db.types.text)
document_format_description_table.create_column('language', db.types.text)
document_format_description_table.create_index(['document_format', 'language'], name='document_format_description_ix', unique=True)
document_format_description_table.insert({'document_format': odt_id, 'language': en_id, 'document_format_sdesc': "ODT", 'document_format_ldesc': 'Open Document Text'})
document_format_description_table.insert({'document_format': odt_id, 'language': fr_id, 'document_format_sdesc': "ODT", 'document_format_ldesc': 'Texte Open Document'})
document_format_description_table.insert({'document_format': odt_id, 'language': es_id, 'document_format_sdesc': "ODT", 'document_format_ldesc': 'Texto Open Document'})
document_format_description_table.insert({'document_format': pdf_id, 'language': en_id, 'document_format_sdesc': "PDF", 'document_format_ldesc': 'Portable Document Format'})
document_format_description_table.insert({'document_format': pdf_id, 'language': fr_id, 'document_format_sdesc': "PDF", 'document_format_ldesc': 'Document PDF'})
document_format_description_table.insert({'document_format': pdf_id, 'language': es_id, 'document_format_sdesc': "PDF", 'document_format_ldesc': 'Documento PDF'})

document_table = db.create_table('document', primary_id='document_code', primary_type=db.types.text)
# document_table.create_column('document_code', db.types.text)
document_table.create_column('part_definition', db.types.text)  # FK
document_table.create_column('assembly', db.types.text)  # FK
document_table.create_column('product', db.types.text)  # FK
document_table.create_column('requirement', db.types.text)  # FK
document_table.create_column('document_type', db.types.text)  # FK to document_type
document_table.create_column('document_format', db.types.text)  # FK to document_format
document_table.create_column('document_language', db.types.text)  # FK to language
document_table.create_column('document_path', db.types.text)

document_description_table = db.create_table('document_description', primary_id=False)
document_description_table.create_column('document', db.types.text)
document_description_table.create_column('language', db.types.text)
document_description_table.create_column('document_sdesc', db.types.text)
document_description_table.create_column('document_ldesc', db.types.text)
document_description_table.create_index(['document', 'language'], name='document_description_ix', unique=True)

# ############
# Tolerances #
# ############
# todo : clearer model to what the tolerance applies
tolerance_type_table = db.create_table('tolerance_type', primary_id='tolerance_type_code', primary_type=db.types.text)
tolerance_type_table.insert({'tolerance_type_code': 'MAXIMUM'})
tolerance_type_table.insert({'tolerance_type_code': 'MINIMUM'})
tolerance_type_table.insert({'tolerance_type_code': 'RANGE'})
tolerance_type_table.insert({'tolerance_type_code': 'STANDARD'})

tolerance_type_description_table = db.create_table('tolerance_type_description', primary_id=False)
tolerance_type_description_table.create_column('tolerance_type', db.types.text)
tolerance_type_description_table.create_column('language', db.types.text)
tolerance_type_description_table.create_column('tolerance_type_sdesc', db.types.text)
tolerance_type_description_table.create_column('tolerance_type_ldesc', db.types.text)
tolerance_type_description_table.create_index(['tolerance_type', 'language'], name='tolerance_type_description_ix', unique=True)
# todo : tolerance type translations

tolerance_table = db.create_table('tolerance', primary_id='tolerance_code', primary_type=db.types.text)
tolerance_table.create_column('tolerance_type', db.types.text)  # FK
tolerance_table.create_column('standard', db.types.text)
tolerance_table.create_column('tolerance_value', db.types.text)

# todo : standards table

# ################
# Physical model #
# ################
status_table = db.create_table('status', primary_id='status_code', primary_type=db.types.text)
alpha_id = status_table.insert({'status_code': 'ALPHA'})
beta_id = status_table.insert({'status_code': 'BETA'})
ready_id = status_table.insert({'status_code': 'READY'})

status_description_table = db.create_table('status_description', primary_id=False)
status_description_table.create_column('status', db.types.text)
status_description_table.create_column('language', db.types.text)
status_description_table.create_index(['status', 'language'], name='status_description_ix', unique=True)
status_description_table.insert({'status': alpha_id, 'language': en_id, 'status_sdesc': "Alpha", 'status_ldesc': 'Alpha status'})
status_description_table.insert({'status': alpha_id, 'language': fr_id, 'status_sdesc': "Alpha", 'status_ldesc': 'Statut alpha'})
status_description_table.insert({'status': alpha_id, 'language': es_id, 'status_sdesc': "Alpha", 'status_ldesc': 'Estado alpha'})
status_description_table.insert({'status': beta_id, 'language': en_id, 'status_sdesc': "Beta", 'status_ldesc': 'Beta status'})
status_description_table.insert({'status': beta_id, 'language': fr_id, 'status_sdesc': "Beta", 'status_ldesc': 'Statut beta'})
status_description_table.insert({'status': beta_id, 'language': es_id, 'status_sdesc': "Beta", 'status_ldesc': 'Estado beta'})
status_description_table.insert({'status': ready_id, 'language': en_id, 'status_sdesc': "Ready", 'status_ldesc': 'Ready status'})
status_description_table.insert({'status': ready_id, 'language': fr_id, 'status_sdesc': "Prêt", 'status_ldesc': 'Statut prêt'})
status_description_table.insert({'status': ready_id, 'language': es_id, 'status_sdesc': "Listo", 'status_ldesc': 'Estado listo'})

product_table = db.create_table('product', primary_id='product_code', primary_type=db.types.text)
product_table.create_column('main_assembly', db.types.text)  # FK to assembly
product_table.create_column('product_status', db.types.text)  # FK to status

product_description_table = db.create_table('product_description', primary_id=False)
product_description_table.create_column('product', db.types.text)
product_description_table.create_column('language', db.types.text)
product_description_table.create_column('product_sdesc', db.types.text)
product_description_table.create_column('product_ldesc', db.types.text)
product_description_table.create_index(['product', 'language'], name='product_description_ix', unique=True)

assembly_table = db.create_table('assembly', primary_id='assembly_code', primary_type=db.types.text)

assembly_assembly_table = db.create_table('assembly_assembly', primary_id='assembly', primary_type=db.types.text)
assembly_assembly_table.create_column('sub_assembly', db.types.text)

assembly_parts_table = db.create_table('assembly_parts', primary_id='assembly', primary_type=db.types.text)
assembly_parts_table.create_column('part_occurrence', db.types.text)

part_definition_table = db.create_table('part_definition', primary_id='part_definition_code', primary_type=db.types.text)
part_definition_table.create_column('is_made', db.types.boolean)
part_definition_table.create_column('is_bought', db.types.boolean)
part_definition_table.create_column('cad_file', db.types.text)
part_definition_table.create_column('parts_library', db.types.text)
part_definition_table.create_column('parts_library_ref', db.types.text)
part_definition_table.create_column('script_file', db.types.text)
part_definition_table.create_column('material', db.types.text)  # FK to material
part_definition_table.create_column('cg_x', db.types.float)
part_definition_table.create_column('cg_y', db.types.float)
part_definition_table.create_column('cg_z', db.types.float)
part_definition_table.create_column('weight', db.types.float)
part_definition_table.create_column('weight_unit', db.types.text)  # FK to unit
part_definition_table.create_column('price_estimate', db.types.float)
part_definition_table.create_column('price_estimate_currency', db.types.text)  # FK to currency

part_occurrence_table = db.create_table('part_occurrence', primary_id='part_occurrence_code', primary_type=db.types.text)
part_occurrence_table.create_column('part_definition', db.types.text)  # FK to part_definition
# todo : add positionning info (can be derived from anchors and joints but should be cached)

anchor_table = db.create_table('anchor', primary_id=False)
anchor_table.create_column('part_definition', db.types.text)  # FK to part_definition
anchor_table.create_column('anchor_code', db.types.text)
anchor_table.create_column('p_x', db.types.float)
anchor_table.create_column('p_y', db.types.float)
anchor_table.create_column('p_z', db.types.float)
anchor_table.create_column('u_x', db.types.float)
anchor_table.create_column('u_y', db.types.float)
anchor_table.create_column('v_x', db.types.float)
anchor_table.create_column('v_y', db.types.float)
anchor_table.create_column('tolerance', db.types.text)  # FK to tolerance
anchor_table.create_index(['part_definition', 'anchor_code'], name='anchor_ix', unique=True)

joints_table = db.create_table('joints', primary_id=False)
joints_table.create_column('part_occurrence_master', db.types.text)
joints_table.create_column('part_occurrence_master_anchor', db.types.text)
joints_table.create_column('part_occurrence_slave', db.types.text)
joints_table.create_column('part_occurrence_slave_anchor', db.types.text)
joints_table.create_column('joint_type', db.types.text)
joints_table.create_column('tx', db.types.float)
joints_table.create_column('ty', db.types.float)
joints_table.create_column('tz', db.types.float)
joints_table.create_column('rx', db.types.float)
joints_table.create_column('ry', db.types.float)
joints_table.create_column('rz', db.types.float)
joints_table.create_index(['part_occurrence_master', 'part_occurrence_master_anchor', 'part_occurrence_slave', 'part_occurrence_slave_anchor'], name='joints_ix', unique=True)

joint_type_table = db.create_table('joint_type', primary_id='joint_type_code', primary_type=db.types.text)
joint_type_table.create_column('dofs', db.types.integer)
joint_type_table.create_column('tx', db.types.boolean)
joint_type_table.create_column('ty', db.types.boolean)
joint_type_table.create_column('tz', db.types.boolean)
joint_type_table.create_column('rx', db.types.boolean)
joint_type_table.create_column('ry', db.types.boolean)
joint_type_table.create_column('rz', db.types.boolean)
free_id = joint_type_table.insert({'joint_type_code': 'FREE', 'dofs': 6, 'tx': True, 'ty': True, 'tz': True, 'rx': True, 'ry': True, 'rz': True})
rigid_id = joint_type_table.insert({'joint_type_code': 'RIGID', 'dofs': 0, 'tx': False, 'ty': False, 'tz': False, 'rx': False, 'ry': False, 'rz': False})

joint_type_description_table = db.create_table('joint_type_description', primary_id=False)
joint_type_description_table.create_column('joint_type', db.types.text)
joint_type_description_table.create_column('language', db.types.text)
joint_type_description_table.create_column('joint_type_sdesc', db.types.text)
joint_type_description_table.create_column('joint_type_ldesc', db.types.text)
joint_type_description_table.create_index(['joint_type', 'language'], name='joint_type_description_ix', unique=True)
joint_type_description_table.insert({'joint_type': free_id, 'language': en_id, 'joint_type_sdesc': "Free", 'joint_type_ldesc': 'Free'})
joint_type_description_table.insert({'joint_type': free_id, 'language': fr_id, 'joint_type_sdesc': "Libre", 'joint_type_ldesc': 'Libre'})
joint_type_description_table.insert({'joint_type': free_id, 'language': es_id, 'joint_type_sdesc': "Libre", 'joint_type_ldesc': 'Libre'})
joint_type_description_table.insert({'joint_type': rigid_id, 'language': en_id, 'joint_type_sdesc': "Rigid", 'joint_type_ldesc': 'Rigid'})
joint_type_description_table.insert({'joint_type': rigid_id, 'language': fr_id, 'joint_type_sdesc': "Encastrement", 'joint_type_ldesc': 'Encastrement'})
joint_type_description_table.insert({'joint_type': rigid_id, 'language': es_id, 'joint_type_sdesc': "Rígido", 'joint_type_ldesc': 'Rígido'})


# ##############
# Requirements #
# ##############

requirement_table = db.create_table('requirement', primary_id='requirement_code', primary_type=db.types.text)
requirement_table.create_column('product', db.types.text)  # FK
requirement_table.create_column('requirement_origin', db.types.text)  # FK
requirement_table.create_column('met', db.types.boolean)

requirement_description_table = db.create_table('requirement_description', primary_id=False)
requirement_description_table.create_column('requirement', db.types.text)
requirement_description_table.create_column('language', db.types.text)
requirement_description_table.create_column('requirement_sdesc', db.types.text)
requirement_description_table.create_column('requirement_ldesc', db.types.text)
requirement_description_table.create_index(['requirement', 'language'], name='requirement_description_ix', unique=True)

requirement_origin_table = db.create_table('requirement_origin', primary_id='requirement_origin_code', primary_type=db.types.text)
rule_id = requirement_origin_table.insert({'requirement_origin_code': 'RULE'})
industrial_standard_id = requirement_origin_table.insert({'requirement_origin_code': 'INDUSTRIAL_STANDARD'})
market_id = requirement_origin_table.insert({'requirement_origin_code': 'MARKET'})
contract_id = requirement_origin_table.insert({'requirement_origin_code': 'CONTRACT'})
experience_id = requirement_origin_table.insert({'requirement_origin_code': 'EXPERIENCE'})

requirement_origin_description_table = db.create_table('requirement_origin_description', primary_id=False)
requirement_origin_description_table.create_column('requirement_origin', db.types.text)
requirement_origin_description_table.create_column('language', db.types.text)
requirement_origin_description_table.create_column('requirement_origin_sdesc', db.types.text)
requirement_origin_description_table.create_column('requirement_origin_ldesc', db.types.text)
requirement_origin_description_table.create_index(['requirement_origin', 'language'], name='requirement_origin_description_ix', unique=True)
requirement_origin_description_table.insert({'requirement_origin': rule_id, 'language': en_id, 'requirement_origin_sdesc': 'Rules', 'requirement_origin_ldesc': "Rules & Law"})
requirement_origin_description_table.insert({'requirement_origin': rule_id, 'language': fr_id, 'requirement_origin_sdesc': 'Réglementation', 'requirement_origin_ldesc': "Réglementations et lois"})
requirement_origin_description_table.insert({'requirement_origin': rule_id, 'language': es_id, 'requirement_origin_sdesc': 'Regulación', 'requirement_origin_ldesc': "Regulaciones y leyes"})
requirement_origin_description_table.insert({'requirement_origin': industrial_standard_id, 'language': en_id, 'requirement_origin_sdesc': 'Standard', 'requirement_origin_ldesc': "Standards and norms"})
requirement_origin_description_table.insert({'requirement_origin': industrial_standard_id, 'language': fr_id, 'requirement_origin_sdesc': 'Normes', 'requirement_origin_ldesc': "Normes et standards"})
requirement_origin_description_table.insert({'requirement_origin': industrial_standard_id, 'language': es_id, 'requirement_origin_sdesc': 'Normas', 'requirement_origin_ldesc': "Normas"})
requirement_origin_description_table.insert({'requirement_origin': market_id, 'language': en_id, 'requirement_origin_sdesc': 'Market', 'requirement_origin_ldesc': "Market"})
requirement_origin_description_table.insert({'requirement_origin': market_id, 'language': fr_id, 'requirement_origin_sdesc': 'Marché', 'requirement_origin_ldesc': "Marché"})
requirement_origin_description_table.insert({'requirement_origin': market_id, 'language': es_id, 'requirement_origin_sdesc': 'Mercado', 'requirement_origin_ldesc': "Mercado"})
requirement_origin_description_table.insert({'requirement_origin': contract_id, 'language': en_id, 'requirement_origin_sdesc': 'Contract', 'requirement_origin_ldesc': "Contract"})
requirement_origin_description_table.insert({'requirement_origin': contract_id, 'language': fr_id, 'requirement_origin_sdesc': 'Contrat', 'requirement_origin_ldesc': "Engagement contractuel"})
requirement_origin_description_table.insert({'requirement_origin': contract_id, 'language': es_id, 'requirement_origin_sdesc': 'Contrato', 'requirement_origin_ldesc': "Compromiso contractual"})
requirement_origin_description_table.insert({'requirement_origin': experience_id, 'language': en_id, 'requirement_origin_sdesc': 'Experience', 'requirement_origin_ldesc': "Experience"})
requirement_origin_description_table.insert({'requirement_origin': experience_id, 'language': fr_id, 'requirement_origin_sdesc': 'Expérience', 'requirement_origin_ldesc': "Expérience"})
requirement_origin_description_table.insert({'requirement_origin': experience_id, 'language': es_id, 'requirement_origin_sdesc': 'Experiencia', 'requirement_origin_ldesc': "Experiencia"})

for table in db.tables:
    print(table)

print("\n%i tables created" % len(db.tables))

