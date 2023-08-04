"""
Script that manages the utilities in common.
"""
from fastapi.encoders import jsonable_encoder
from taxdata.app.utils.dates import convert_datetime_to_str


def get_parse_data(item):
    """
    Data parsing
    """
    json = jsonable_encoder(item)
    del json['birth_date']
    birthdate = convert_datetime_to_str(item.birth_date)
    return {'birth_date': birthdate, **json}
