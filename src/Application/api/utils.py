 
from flask_restx import fields 
def convert_db_model_to_restx_model(model): 

    fields_dict = {} 
    for column in model.__table__.columns: 
        if column.type.python_type == int: 
            fields_dict[column.name] = fields.Integer() 
        elif column.type.python_type == str: 
            fields_dict[column.name] = fields.String() 
        elif column.type.python_type == float: 
            fields_dict[column.name] = fields.Float() 
        elif column.type.python_type == bool: 
            fields_dict[column.name] = fields.Boolean() 
        elif column.type.python_type == list: 
            fields_dict[column.name] = fields.List(fields.String()) 
        elif column.type.python_type == dict: 
            fields_dict[column.name] = fields.String() 
        else: 
            fields_dict[column.name] = fields.String() 
    return fields_dict 
