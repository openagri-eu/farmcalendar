
URN_BASE_NAMESPACE = 'urn:farmcalendar'

def generate_urn_prefix(*class_names):
    urn_prefix = ':'.join([URN_BASE_NAMESPACE] + list(*class_names))
    return urn_prefix

def generate_urn(*class_names, obj_id):
    urn_prefix = generate_urn_prefix(class_names)
    return f'{urn_prefix}:{obj_id}'


OCSM_SCHEMA = {}
