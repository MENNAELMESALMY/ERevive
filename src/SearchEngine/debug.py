

def addJoinAttrs(joins,whereAttrs):
    sep = 'and'
    for idx,join in enumerate(joins):
        join = join.strip()
        join = join.split(" ")
        if idx == len(joins)-1 and len(whereAttrs)==0:
            sep = ''
        joins[idx] =[join[0],join[1],join[2],sep]
    for attr in whereAttrs:
        for join in joins:
            if join[0] == attr[0] and join[1] == attr[1] and join[2] == attr[2]:
                join[3] = attr[3]
                whereAttrs.remove(attr)
    joins.extend(whereAttrs)
    return joins
    
best_joins = [" EMPLOYEE.ssn = DEPARTMENT.EMPLOYEE_Manages_ssn"," DEPARTMENT.name = DEPARTMENT_location.DEPARTMENT_name"]
where_attr = [
            [
                [
                    "DEPARTMENT_location.DEPARTMENT_name",
                    "str"
                ],
                "like",
                "value",
                ""
            ]
        ]

print(addJoinAttrs(best_joins,where_attr))
