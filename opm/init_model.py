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
kg_per_m3_id = db['unit'].insert({'unit_code': 'kg_per_m3', 'conversion': 1., 'unit_type': -1})
g_per_cm3_id = db['unit'].insert({'unit_code': 'g_per_cm3', 'conversion': 1e3, 'unit_type': -1})

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

db['unit_description'].insert({'unit': kg_per_m3_id, 'language': en_id, 'unit_sdesc': 'kg/m³', 'unit_ldesc': 'Kilogram par cube meter'})
db['unit_description'].insert({'unit': kg_per_m3_id, 'language': fr_id, 'unit_sdesc': 'kg/m³', 'unit_ldesc': 'Kilogramme par mètre cube'})
db['unit_description'].insert({'unit': kg_per_m3_id, 'language': es_id, 'unit_sdesc': 'kg/m³', 'unit_ldesc': 'Kilogramo por metro cubo'})
db['unit_description'].insert({'unit': g_per_cm3_id, 'language': en_id, 'unit_sdesc': 'g/cm³', 'unit_ldesc': 'Gram par cube centimeter'})
db['unit_description'].insert({'unit': g_per_cm3_id, 'language': fr_id, 'unit_sdesc': 'g/cm³', 'unit_ldesc': 'Gramme par centimètre cube'})
db['unit_description'].insert({'unit': g_per_cm3_id, 'language': es_id, 'unit_sdesc': 'g/cm³', 'unit_ldesc': 'Gramo por centimetro cubo'})

length_id = db['unit_type'].insert({'unit_type_code': 'length', 'default_unit': mm_id})
surface_id = db['unit_type'].insert({'unit_type_code': 'surface', 'default_unit': mm2_id})
volume_id = db['unit_type'].insert({'unit_type_code': 'volume', 'default_unit': mm3_id})
mass_id = db['unit_type'].insert({'unit_type_code': 'mass', 'default_unit': g_id})
force_id = db['unit_type'].insert({'unit_type_code': 'force', 'default_unit': N_id})
volumique_mass_id = db['unit_type'].insert({'unit_type_code': 'volumic_mass', 'default_unit': 'kg/m3'})

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
db['unit'].update({'unit_code': 'kg_per_m3', 'unit_type': volumique_mass_id}, ['unit_code'])
db['unit'].update({'unit_code': 'g_per_cm3', 'unit_type': volumique_mass_id}, ['unit_code'])

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

# ###########
# Materials #
# ###########

metal_id = db['material_category'].insert({'material_category_code': 'METAL'})
polymer_id = db['material_category'].insert({'material_category_code': 'POLYMER'})
wood_id = db['material_category'].insert({'material_category_code': 'WOOD'})
ceramic_id = db['material_category'].insert({'material_category_code': 'CERAMIC'})
composite_id = db['material_category'].insert({'material_category_code': 'COMPOSITE'})

db['material_category_description'].insert({'material_category': metal_id, 'language': en_id, 'material_category_sdesc': 'Metal', 'material_category_ldesc': 'Metal'})
db['material_category_description'].insert({'material_category': metal_id, 'language': fr_id, 'material_category_sdesc': 'Métal', 'material_category_ldesc': 'Métal'})
db['material_category_description'].insert({'material_category': metal_id, 'language': es_id, 'material_category_sdesc': 'Metal', 'material_category_ldesc': 'Metal'})
db['material_category_description'].insert({'material_category': polymer_id, 'language': en_id, 'material_category_sdesc': 'Polymer', 'material_category_ldesc': 'Polymer'})
db['material_category_description'].insert({'material_category': polymer_id, 'language': fr_id, 'material_category_sdesc': 'Polymère', 'material_category_ldesc': 'Polymère'})
db['material_category_description'].insert({'material_category': polymer_id, 'language': es_id, 'material_category_sdesc': 'Polímero', 'material_category_ldesc': 'Polímero'})
db['material_category_description'].insert({'material_category': wood_id, 'language': en_id, 'material_category_sdesc': 'Wood', 'material_category_ldesc': 'Wood'})
db['material_category_description'].insert({'material_category': wood_id, 'language': fr_id, 'material_category_sdesc': 'Bois', 'material_category_ldesc': 'Bois'})
db['material_category_description'].insert({'material_category': wood_id, 'language': es_id, 'material_category_sdesc': 'Madera', 'material_category_ldesc': 'Madera'})
db['material_category_description'].insert({'material_category': ceramic_id, 'language': en_id, 'material_category_sdesc': 'Ceramic', 'material_category_ldesc': 'Ceramic'})
db['material_category_description'].insert({'material_category': ceramic_id, 'language': fr_id, 'material_category_sdesc': 'Céramique', 'material_category_ldesc': 'Céramique'})
db['material_category_description'].insert({'material_category': ceramic_id, 'language': es_id, 'material_category_sdesc': 'Cerámico', 'material_category_ldesc': 'Cerámico'})
db['material_category_description'].insert({'material_category': composite_id, 'language': en_id, 'material_category_sdesc': 'Composite', 'material_category_ldesc': 'Composite material'})
db['material_category_description'].insert({'material_category': composite_id, 'language': fr_id, 'material_category_sdesc': 'Composite', 'material_category_ldesc': 'Matériau composite'})
db['material_category_description'].insert({'material_category': composite_id, 'language': es_id, 'material_category_sdesc': 'Compuesto', 'material_category_ldesc': 'Material compuesto'})

aluminium_id = db['material_subcategory'].insert({'material_category': metal_id, 'material_subcategory_code': 'ALUMINIUM'})
steel_id = db['material_subcategory'].insert({'material_category': metal_id, 'material_subcategory_code': 'STEEL'})
titanium_id = db['material_subcategory'].insert({'material_category': metal_id, 'material_subcategory_code': 'TITANIUM'})
thermoplastic_id = db['material_subcategory'].insert({'material_category': polymer_id, 'material_subcategory_code': 'THERMOPLASTIC'})
thermoset_id = db['material_subcategory'].insert({'material_category': polymer_id, 'material_subcategory_code': 'THERMOSET'})
softwood_id = db['material_subcategory'].insert({'material_category': wood_id, 'material_subcategory_code': 'SOFTWOOD'})
hardwood_id = db['material_subcategory'].insert({'material_category': wood_id, 'material_subcategory_code': 'HARDWOOD'})
cermet_id = db['material_subcategory'].insert({'material_category': composite_id, 'material_subcategory_code': 'CERMET'})
cfrp_id = db['material_subcategory'].insert({'material_category': composite_id, 'material_subcategory_code': 'CFRP'})

db['material_subcategory_description'].insert({'material_subcategry': aluminium_id, 'language': en_id, 'material_subcategory_sdesc': 'Aluminium', 'material_subcategory_ldesc': 'Aluminium'})
db['material_subcategory_description'].insert({'material_subcategry': aluminium_id, 'language': fr_id, 'material_subcategory_sdesc': 'Alu', 'material_subcategory_ldesc': 'Aluminium'})
db['material_subcategory_description'].insert({'material_subcategry': aluminium_id, 'language': es_id, 'material_subcategory_sdesc': 'Aluminio', 'material_subcategory_ldesc': 'Aluminio'})
db['material_subcategory_description'].insert({'material_subcategry': steel_id, 'language': en_id, 'material_subcategory_sdesc': 'Steel', 'material_subcategory_ldesc': 'Steel'})
db['material_subcategory_description'].insert({'material_subcategry': steel_id, 'language': fr_id, 'material_subcategory_sdesc': 'Acier', 'material_subcategory_ldesc': 'Acier'})
db['material_subcategory_description'].insert({'material_subcategry': steel_id, 'language': es_id, 'material_subcategory_sdesc': 'Acero', 'material_subcategory_ldesc': 'Acero'})
db['material_subcategory_description'].insert({'material_subcategry': titanium_id, 'language': en_id, 'material_subcategory_sdesc': 'Titanium', 'material_subcategory_ldesc': 'Titanium'})
db['material_subcategory_description'].insert({'material_subcategry': titanium_id, 'language': fr_id, 'material_subcategory_sdesc': 'Titane', 'material_subcategory_ldesc': 'Titane'})
db['material_subcategory_description'].insert({'material_subcategry': titanium_id, 'language': es_id, 'material_subcategory_sdesc': 'Titanio', 'material_subcategory_ldesc': 'Titanio'})
db['material_subcategory_description'].insert({'material_subcategry': thermoplastic_id, 'language': en_id, 'material_subcategory_sdesc': 'Thermoplastic', 'material_subcategory_ldesc': 'Thermoplastic polymer'})
db['material_subcategory_description'].insert({'material_subcategry': thermoplastic_id, 'language': fr_id, 'material_subcategory_sdesc': 'Thermoplastique', 'material_subcategory_ldesc': 'Polymère thermoplastique'})
db['material_subcategory_description'].insert({'material_subcategry': thermoplastic_id, 'language': es_id, 'material_subcategory_sdesc': 'Termoplástico', 'material_subcategory_ldesc': 'Termoplástico'})
db['material_subcategory_description'].insert({'material_subcategry': thermoset_id, 'language': en_id, 'material_subcategory_sdesc': 'Theroset', 'material_subcategory_ldesc': 'Thermoset polymer'})
db['material_subcategory_description'].insert({'material_subcategry': thermoset_id, 'language': fr_id, 'material_subcategory_sdesc': 'Thermodurcissable', 'material_subcategory_ldesc': 'Polymère thermodurcissable'})
db['material_subcategory_description'].insert({'material_subcategry': thermoset_id, 'language': es_id, 'material_subcategory_sdesc': 'Termoestable', 'material_subcategory_ldesc': 'Polímero termoestable'})
db['material_subcategory_description'].insert({'material_subcategry': softwood_id, 'language': en_id, 'material_subcategory_sdesc': 'Softwood', 'material_subcategory_ldesc': 'Softwood'})
db['material_subcategory_description'].insert({'material_subcategry': softwood_id, 'language': fr_id, 'material_subcategory_sdesc': 'Bois tendre', 'material_subcategory_ldesc': 'Bois tendre'})
db['material_subcategory_description'].insert({'material_subcategry': softwood_id, 'language': es_id, 'material_subcategory_sdesc': 'Madera blanda', 'material_subcategory_ldesc': 'Madera blanda'})
db['material_subcategory_description'].insert({'material_subcategry': hardwood_id, 'language': en_id, 'material_subcategory_sdesc': 'Hardwood', 'material_subcategory_ldesc': 'Hardwood'})
db['material_subcategory_description'].insert({'material_subcategry': hardwood_id, 'language': fr_id, 'material_subcategory_sdesc': 'Bois dur', 'material_subcategory_ldesc': 'Bois dur'})
db['material_subcategory_description'].insert({'material_subcategry': hardwood_id, 'language': es_id, 'material_subcategory_sdesc': 'Madera dura', 'material_subcategory_ldesc': 'Madera dura'})
db['material_subcategory_description'].insert({'material_subcategry': cermet_id, 'language': en_id, 'material_subcategory_sdesc': 'Cermet', 'material_subcategory_ldesc': 'Ceramic-metal composite'})
db['material_subcategory_description'].insert({'material_subcategry': cermet_id, 'language': fr_id, 'material_subcategory_sdesc': 'Cermet', 'material_subcategory_ldesc': 'Composite céramique-métal'})
db['material_subcategory_description'].insert({'material_subcategry': cermet_id, 'language': es_id, 'material_subcategory_sdesc': 'Cermet', 'material_subcategory_ldesc': 'Compuesto metal-cerámico'})
db['material_subcategory_description'].insert({'material_subcategry': cfrp_id, 'language': en_id, 'material_subcategory_sdesc': 'CFRP', 'material_subcategory_ldesc': 'Carbon fiber reinforced polymer'})
db['material_subcategory_description'].insert({'material_subcategry': cfrp_id, 'language': fr_id, 'material_subcategory_sdesc': 'PRFC', 'material_subcategory_ldesc': 'Polymère renforcé de fibres de carbone'})
db['material_subcategory_description'].insert({'material_subcategry': cfrp_id, 'language': es_id, 'material_subcategory_sdesc': 'PRFC', 'material_subcategory_ldesc': 'Polímero consolidado de fibras de carbonio'})


modulus_id = db['material_property'].insert({'material_property_code': 'MODULUS'})
volumic_mass_id = db['material_property'].insert({'material_property_code': 'VOLUMIC_MASS'})
resistivity_id = db['material_property'].insert({'material_property_code': 'RESISTIVITY'})

db['material_property_description'].insert({'material_property': modulus_id, 'language': en_id, 'material_property_sdesc': 'Modulus', 'material_property_ldesc': 'Young modulus'})
db['material_property_description'].insert({'material_property': modulus_id, 'language': fr_id, 'material_property_sdesc': 'Module', 'material_property_ldesc': "Module d'Young"})
db['material_property_description'].insert({'material_property': modulus_id, 'language': es_id, 'material_property_sdesc': 'Módulo', 'material_property_ldesc': "Módulo de Young"})
db['material_property_description'].insert({'material_property': volumic_mass_id, 'language': en_id, 'material_property_sdesc': 'Density', 'material_property_ldesc': 'Density'})
db['material_property_description'].insert({'material_property': volumic_mass_id, 'language': fr_id, 'material_property_sdesc': 'Densité', 'material_property_ldesc': "Densité"})
db['material_property_description'].insert({'material_property': volumic_mass_id, 'language': es_id, 'material_property_sdesc': 'Desnidad', 'material_property_ldesc': "Densidad"})
db['material_property_description'].insert({'material_property': resistivity_id, 'language': en_id, 'material_property_sdesc': 'Resistivity', 'material_property_ldesc': 'Resistivity'})
db['material_property_description'].insert({'material_property': resistivity_id, 'language': fr_id, 'material_property_sdesc': 'Résistivité', 'material_property_ldesc': "Résistivité"})
db['material_property_description'].insert({'material_property': resistivity_id, 'language': es_id, 'material_property_sdesc': 'Resistividad', 'material_property_ldesc': "Resistividad"})

stainless_A4_id = db['material'].insert({'material_code': 'STAINLESS_A4', 'material_subcategory': steel_id})
stainless_A2_id = db['material'].insert({'material_code': 'STAINLESS_A2', 'material_subcategory': steel_id})
alu_7075_t6_id = db['material'].insert({'material_code': 'ALU7075-T6', 'material_subcategory': aluminium_id})

db['material_description'].insert({'material': stainless_A4_id, 'language': en_id, 'material_sdesc': "A4 stainless steel", 'material_ldesc': "A4 stainless steel"})
db['material_description'].insert({'material': stainless_A4_id, 'language': fr_id, 'material_sdesc': "Inox A4", 'material_ldesc': "Acier inoxydable A4"})
db['material_description'].insert({'material': stainless_A4_id, 'language': es_id, 'material_sdesc': "Inoxidable A4", 'material_ldesc': "Acero inoxidable A4"})
db['material_description'].insert({'material': stainless_A2_id, 'language': en_id, 'material_sdesc': "A2 stainless steel", 'material_ldesc': "A2 stainless steel"})
db['material_description'].insert({'material': stainless_A2_id, 'language': fr_id, 'material_sdesc': "Inox A2", 'material_ldesc': "Acier inoxydable A2"})
db['material_description'].insert({'material': stainless_A2_id, 'language': es_id, 'material_sdesc': "Inoxidable A2", 'material_ldesc': "Acero inoxidable A2"})
db['material_description'].insert({'material': alu_7075_t6_id, 'language': en_id, 'material_sdesc': "7075-T6", 'material_ldesc': "Aluminium 7075-T6"})
db['material_description'].insert({'material': alu_7075_t6_id, 'language': fr_id, 'material_sdesc': "7075-T6", 'material_ldesc': "Aluminium 7075-T6, aka Zicral, Ergal et Fortal Constructal"})
db['material_description'].insert({'material': alu_7075_t6_id, 'language': es_id, 'material_sdesc': "7075-T6", 'material_ldesc': "Aluminio 7075-T6"})

db['material_properties'].insert({'material': alu_7075_t6_id, 'material_property': volumic_mass_id, 'value': 2.81, 'unit': g_per_cm3_id})
db['material_properties'].insert({'material': stainless_A4_id, 'material_property': volumic_mass_id, 'value': 8000, 'unit': kg_per_m3_id})

# todo : properties may depend on temperature

# ############
# Composites #
# ############


# ##########
# Coatings #
# ##########


# #############
# Simulations #
# #############


# ###########
# Documents #
# ###########


# ############
# Suppliers #
# ############


# ############
# Tolerances #
# ############


# ################
# Physical model #
# ################


# ##############
# Requirements #
# ##############


