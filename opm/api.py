# coding: utf-8

import dataset


def get_sqlite_db(filename_sqlite_db):
    r"""
    
    Parameters
    ----------
    filename_sqlite_db : str

    Returns
    -------
    dataset database object

    """
    return dataset.connect("sqlite:///%s" % filename_sqlite_db)

# #######
# Write #
# #######


# part definition


def _add_part_definition_stepzip(db, code, stepzip):
    raise NotImplementedError


def _add_part_definition_script(db, code, script):
    # from os.path import basename, splitext
    # code = splitext(basename(script))[0]
    db['part_definition'].insert({'part_definition_code': code,
                                  'cad_file': None,
                                  'parts_library': None,
                                  'parts_library_ref': None,
                                  'script_file': script})
    # todo : feed the anchors table


def _add_part_definition_library(db, code, library, ref):
    db['part_definition'].insert({'part_definition_code': code,
                                  'cad_file': None,
                                  'parts_library': library,
                                  'parts_library_ref': ref,
                                  'script_file': None})
    # todo : feed the anchors table


def add_part_definition(db, code, origin, *args, **kwargs):
    r"""
    
    Parameters
    ----------
    db
    origin : str in ['stepzip','script', 'library']
    args

    Returns
    -------
    str : the part definition code

    """
    if origin not in ['stepzip', 'library', 'script']:
        raise ValueError('Unknown origin for part definition')

    f = {'stepzip': _add_part_definition_stepzip,
         'library': _add_part_definition_library,
         'script': _add_part_definition_script}

    f[origin](db, code, *args, **kwargs)
    # todo : the returned code should comply with the nomenclature


# product


def add_product(db, product_code, main_assembly, status, descriptions=None):
    # checks
    # status is defined
    s = db['status'].find_one(status_code=status)
    if s is not None:
        db['product'].insert({'product_code': product_code,
                              'main_assembly': main_assembly,
                              'product_status': status})
        if descriptions is not None:
            for k, v in descriptions.items():
                add_product_description(db, product_code, k, v['sdesc'], v['ldesc'])
    else:
        raise ValueError('Undefined status')


def add_product_description(db, product_code, language, sdesc, ldesc):
    # checks
    # language is defined
    l = db['language'].find_one(language_code=language)

    if l is not None:
        db['product_description'].insert({'product': product_code,
                                          'language': language,
                                          'product_sdesc': sdesc,
                                          'product_ldesc': ldesc})
    else:
        raise ValueError('Undefined language')


# assembly


def add_assembly(db, product_code, assembly_code):
    raise NotImplementedError


def add_part(product_code, assembly_code, part_definition):
    raise NotImplementedError

# ##########
# Read API #
# ##########


def product_shape(product_code):
    raise NotImplementedError
