# coding: utf-8

from os.path import basename, splitext
import imp

import dataset

from opm.stepzip import extract_stepzip


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
    import re
    anchors = dict()
    stepfile_path, anchorsfile_path = extract_stepzip(stepzip)
    with open(anchorsfile_path) as f:
        lines = f.readlines()
        for line in lines:
            if line not in ["\n", "\r\n"] and not line.startswith("#"):
                items = re.findall(r'\S+', line)
                key = items[0]
                data = [float(v) for v in items[1].split(",")]
                p = (data[0], data[1], data[2])
                u = (data[3], data[4], data[5])
                v = (data[6], data[7], data[8])
                anchors[key] = {"p": p, "u": u, "v": v}

    db['part_definition'].insert({'part_definition_code': code,
                                  'cad_file': stepfile_path,
                                  'parts_library': None,
                                  'parts_library_ref': None,
                                  'script_file': None})

    for k, v in anchors.items():
        db['anchor'].insert({'part_definition': code,
                             'anchor_code': k,
                             'p_x': v['p'][0],
                             'p_y': v['p'][1],
                             'p_z': v['p'][2],
                             'u_x': v['u'][0],
                             'u_y': v['u'][1],
                             'u_z': v['u'][2],
                             'v_x': v['v'][0],
                             'v_y': v['v'][1],
                             'v_z': v['v'][2],
                             'tolerance': ""  # todo -> tolerance
                             })


def _add_part_definition_script(db, code, script):
    # from os.path import basename, splitext
    # code = splitext(basename(script))[0]
    db['part_definition'].insert({'part_definition_code': code,
                                  'cad_file': None,
                                  'parts_library': None,
                                  'parts_library_ref': None,
                                  'script_file': script})

    module_ = imp.load_source(splitext(basename(script))[0], script)
    anchors = module_.anchors
    for anchor in anchors:
        db['anchor'].insert({'part_definition': code,
                             'anchor_code': anchor.name,
                             'p_x': anchor.p[0],
                             'p_y': anchor.p[1],
                             'p_z': anchor.p[2],
                             'u_x': anchor.u[0],
                             'u_y': anchor.u[1],
                             'u_z': anchor.u[2],
                             'v_x': anchor.v[0],
                             'v_y': anchor.v[1],
                             'v_z': anchor.v[2],
                             'tolerance': ""  # todo -> tolerance
                             })


def _add_part_definition_library(db, code, library, ref):
    db['part_definition'].insert({'part_definition_code': code,
                                  'cad_file': None,
                                  'parts_library': library,
                                  'parts_library_ref': ref,
                                  'script_file': None})
    # todo : feed the anchors table -> requires modification in party library


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


def add_assembly(db, assembly_code):
    r"""
    
    Parameters
    ----------
    db
    assembly_code

    Note
    ----
    product refers to an assembly but an assembly can be used in different
    products

    """
    db['assembly'].insert({'assembly_code': assembly_code})


def assembly_add_part(db, assembly, part_definition, part_occurence_code):

    # create a part occurrence from the part definition
    db['part_occurrence'].insert({'part_occurrence_code': part_occurence_code,
                                 'part_definition': part_definition})

    # link the assembly to the part occurrence
    db['assembly_parts'].insert({'assembly': assembly,
                                 'part_occurrence': part_occurence_code})


def assembly_add_constraint(db,
                            assembly,
                            master_part_occurrence,
                            master_part_occurrence_anchor,
                            slave_part_occurrence,
                            slave_part_occurrence_anchor,
                            joint_type,
                            joint_tx=0,
                            joint_ty=0,
                            joint_tz=0,
                            joint_rx=0,
                            joint_ry=0,
                            joint_rz=0):
    # make sure the part occurrences exist
    m = db['assembly_parts'].find_one(assembly=assembly,
                                      part_occurrence=master_part_occurrence)
    s = db['assembly_parts'].find_one(assembly=assembly,
                                      part_occurrence=slave_part_occurrence)
    if m is None:
        raise ValueError("The master part occurrence is undefined")
    if s is None:
        raise ValueError("The slave part occurrence is undefined")

    # make sure the joint type exists
    j = db['joint_type'].find_one(joint_type_code=joint_type)
    if j is None:
        raise ValueError("The joint type is undefined")

    # add an entry in the joint table
    db['joints'].insert({'part_occurrence_master': master_part_occurrence,
                         'part_occurrence_master_anchor': master_part_occurrence_anchor,
                         'part_occurrence_slave': slave_part_occurrence,
                         'part_occurrence_slave_anchor': slave_part_occurrence_anchor,
                         'joint_type': joint_type,
                         'tx': joint_tx, 'ty': joint_ty, 'tz': joint_tz,
                         'rx': joint_rx, 'ry': joint_ry, 'rz': joint_rz})

    # compute the slave position / transformation matrix

    # update the part occurrence data with the position / transformation matrix


# ##########
# Read API #
# ##########


def product_shape(db, product_code):
    raise NotImplementedError
