 
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

def serialize_result(res):
    res_dict = res._asdict() if hasattr(res, "_asdict") else res.__dict__ if hasattr(res, "__dict__") else res
    table = None
    if res_dict.get("_sa_instance_state"):
        table = res_dict["_sa_instance_state"].class_.__table__.name+"."

    res_dict.pop("_sa_instance_state", None)
    serialized_result = res_dict.copy()
    for attr_key, attr_value in res_dict.items():
        print(attr_key, attr_value)
        if hasattr(attr_value, "__dict__"):
            model_dict = attr_value.serialize()
            model_dict_updated = {}
            for key, value in model_dict.items():
                model_dict_updated[attr_key + "." + key] = value
            model_dict_updated = serialize_result(model_dict_updated)
            serialized_result.pop(attr_key)
            serialized_result.update(model_dict_updated)
        elif table:
            serialized_result[table+attr_key] = attr_value
            serialized_result.pop(attr_key)

    return serialized_result

def serialize(results):

    return [serialize_result(row) for row in results]

