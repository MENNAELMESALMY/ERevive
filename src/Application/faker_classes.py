from faker import Faker

faker = Faker()
faker_classes_mapper = {"first_name":faker.first_name,"last_name":faker.last_name,"name":faker.name,"address":faker.address,\
    "building_number":faker.building_number,"city":faker.city,"country":faker.country,"country_code":faker.country_code,\
    "current_country":faker.current_country,"current_country_code":faker.current_country_code,"postcode":faker.postcode,\
    "street_address":faker.street_address,"street_name":faker.street_name,"street_suffix":faker.street_suffix,\
    "license_plate":faker.license_plate,"bank_country":faker.bank_country,"bban":faker.bban,"iban":faker.iban,\
    "swift":faker.swift,"color":faker.color,"color_name":faker.color_name,"company":faker.company,"company_suffix":faker.company_suffix,\
    "credit_card_number":faker.credit_card_number,"credit_card_provider":faker.credit_card_provider,\
    "credit_card_security_code":faker.credit_card_security_code,"currency_code":faker.currency_code,"time_object":faker.time_object,\
    "currency_name":faker.currency_name,"pricetag":faker.pricetag,"century":faker.century,"day_of_month":faker.day_of_month,\
    "day_of_week":faker.day_of_week,"month":faker.month,"month_name":faker.month_name,"time":faker.time,"timezone":faker.timezone,\
    "year":faker.year,"file_name":faker.file_name,"file_path":faker.file_path,"mime_type":faker.mime_type,"company_email":faker.company_email,\
    "email":faker.email,"uri":faker.uri,"user_name":faker.user_name,"job":faker.job,"text":faker.text,"word":faker.word,\
    "language_name":faker.language_name,"name_female":faker.name_female,"name_male":faker.name_male,"prefix":faker.prefix,\
    "suffix":faker.suffix,"phone_number":faker.phone_number,"ssn":faker.ssn}  

pk_faker_classes = {"first_name":faker.unique.first_name,"last_name":faker.unique.last_name,"name":faker.unique.name,"address":faker.unique.address,\
    "building_number":faker.unique.building_number,"city":faker.unique.city,"country":faker.unique.country,"country_code":faker.unique.country_code,\
    "current_country":faker.unique.current_country,"current_country_code":faker.unique.current_country_code,"postcode":faker.unique.postcode,\
    "street_address":faker.unique.street_address,"street_name":faker.unique.street_name,"street_suffix":faker.unique.street_suffix,\
    "license_plate":faker.unique.license_plate,"bank_country":faker.unique.bank_country,"bban":faker.unique.bban,"iban":faker.unique.iban,\
    "swift":faker.unique.swift,"color":faker.unique.color,"color_name":faker.unique.color_name,"company":faker.unique.company,"company_suffix":faker.unique.company_suffix,\
    "credit_card_number":faker.unique.credit_card_number,"credit_card_provider":faker.unique.credit_card_provider,\
    "credit_card_security_code":faker.unique.credit_card_security_code,"currency_code":faker.unique.currency_code,"time_object":faker.unique.time_object,\
    "currency_name":faker.unique.currency_name,"pricetag":faker.unique.pricetag,"century":faker.unique.century,"day_of_month":faker.unique.day_of_month,\
    "day_of_week":faker.unique.day_of_week,"month":faker.unique.month,"month_name":faker.unique.month_name,"time":faker.unique.time,"timezone":faker.unique.timezone,\
    "year":faker.unique.year,"file_name":faker.unique.file_name,"file_path":faker.unique.file_path,"mime_type":faker.unique.mime_type,"company_email":faker.unique.company_email,\
    "email":faker.unique.email,"uri":faker.unique.uri,"user_name":faker.unique.user_name,"job":faker.unique.job,"text":faker.unique.text,"word":faker.unique.word,\
    "language_name":faker.unique.language_name,"name_female":faker.unique.name_female,"name_male":faker.unique.name_male,"prefix":faker.unique.prefix,\
    "suffix":faker.unique.suffix,"phone_number":faker.unique.phone_number,"ssn":faker.unique.ssn} 

defaults = {
    "str":faker.pystr,
    "int":faker.pyint,
    "bool":faker.pybool,
    "float":faker.pyfloat,
    "datetime":faker.date_time
}

pk_defaults = {
    "str":faker.unique.pystr,
    "int":faker.unique.pyint,
    "float":faker.unique.pyfloat,
    "datetime":faker.unique.date
}

faker_classes_mapper.update(defaults)
pk_faker_classes.update(pk_defaults)

