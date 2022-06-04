def createForm (requirments,endpoint,filePath):
    responsiveList = []
    textinput = False
    textarea = False
    radio = False
    checkbox = False
    dateinput = False
    numberinput = False
    with open(filePath, 'a') as file: 
        file.write('''
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        ''') 
        for req in requirments:
            file.write(f'''
            <h2>{req["field_name"]}</h2>
            ''')
            if req["field_type"] == "text":
                textinput = True
                if req["isRequired"] == True:
                    file.write(f'''
            <input type="text" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" required/>
            <br />
                    ''')
                else:
                    file.write(f'''
            <input type="text" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" />
            <br />
                    ''')
            elif req["field_type"] == "email":
                if req["isRequired"] == True:
                    file.write(f'''
            <input type="email" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" required/>
            <br />
                    ''')
                else:
                    file.write(f'''
            <input type="email" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" />
            <br />
                    ''')
            elif req["field_type"] == "tel":
                if req["isRequired"] == True:
                    file.write('''
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="%s" required/>
            <br />
                    ''' %req["field_name"].replace(' ','_'))
                else:
                    file.write('''
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="%s" />
            <br />
                    ''' %req["field_name"].replace(' ','_'))
            elif req["field_type"] == "password":
                if req["isRequired"] == True:
                    file.write(f'''
            <input type="password" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" required/>
            <br />
                    ''')
                else:
                    file.write(f'''
            <input type="password" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" />
            <br />
                    ''')
            elif req["field_type"] == "url":
                if req["isRequired"] == True:
                    file.write(f'''
            <input type="url" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" required/>
            <br />
                    ''')
                else:
                    file.write(f'''
            <input type="url" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" />
            <br />
                    ''')
            elif req["field_type"] == "number":
                numberinput = True
                if req["minRange"] > 0 and req["maxRange"] == 0:
                    if req["isRequired"] == True:
                        file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" min="{req["minRange"]}" v-model="{req["field_name"].replace(' ','_')}" required/>
            <br />
                        ''')
                    else:
                        file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" min="{req["minRange"]}" v-model="{req["field_name"].replace(' ','_')}" />
            <br />
                        ''')
                if req["minRange"] == 0 and req["maxRange"] > 0:
                    if req["isRequired"] == True:
                        file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" max="{req["maxRange"]}" v-model="{req["field_name"].replace(' ','_')}" required/>
            <br />
                        ''')
                    else:
                        file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" max="{req["maxRange"]}" v-model="{req["field_name"].replace(' ','_')}" />
            <br />
                        ''')
                if req["minRange"] > 0 and req["maxRange"] > 0:
                    if req["isRequired"] == True:
                        file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" min="{req["minRange"]}" max="{req["maxRange"]}" v-model="{req["field_name"].replace(' ','_')}" required/>
            <br />
                        ''')
                    else:
                        file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" min="{req["minRange"]}" max="{req["maxRange"]}" v-model="{req["field_name"].replace(' ','_')}" />
            <br />
                        ''')
                if req["minRange"] == 0 and req["maxRange"] == 0:
                    if req["isRequired"] == True:
                        file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" required/>
            <br />
                        ''')
                    else:
                        file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" />
            <br />
                        ''')
            elif req["field_type"] == "radiobutton":
                radio = True
                if req["isRequired"] == True:
                    for option in req["options"]:
                        file.write(f'''
            <input type="radio" id="radiobuttonId" value={option} v-model= "radio_buttons" required/>
            <label>{option}</label>
                        ''')
                else:
                    for option in req["options"]:
                        file.write(f'''
            <input type="radio" id="radiobuttonId" value={option} v-model= "radio_buttons" />
            <label>{option}</label>
                        ''')
            elif req["field_type"] == "checklist":
                checkbox = True
                if req["isRequired"] == True:
                    for option in req["options"]:
                        file.write(f'''
            <input type="checkbox" id="checkboxId" value={option} v-model= "check_list" required/>
            <label>{option}</label>
                        ''')
                else:
                    for option in req["options"]:
                        file.write(f'''
            <input type="checkbox" id="checkboxId" value={option} v-model= "check_list" />
            <label>{option}</label>
                        ''')
            elif req["field_type"] == "textarea":
                textarea = True
                if req["isRequired"] == True:
                    file.write(f'''
            <textarea id="textareaId" placeholder="Enter {req["field_name"]}" v-model= "text_area" required></textarea>
                    ''')
                else:
                    file.write(f'''
            <textarea id="textareaId" placeholder="Enter {req["field_name"]}" v-model= "text_area" ></textarea>
                    ''')
            elif req["field_type"] == "list":
                if req["isRequired"] == True:
                    file.write(f'''
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select {req["field_name"]}</option>
                    ''')
                else:
                    file.write(f'''
            <select id="textinputId" v-model="select_list">
                <option value="" disabled selected>Select {req["field_name"]}</option>
                    ''')
                for option in req["options"]:
                    file.write(f'''
                <option value="{option}">{option}</option>
                    ''')
                file.write("</select>")                
            elif req["field_type"] == "date":
                dateinput = True
                if req["isRequired"] == True:
                    file.write(f'''
            <input type="date" id="inputdateId" v-model= "date" required/>
            <br />
                    ''')
                else:
                    file.write(f'''
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    ''')
        file.write('''
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        ''')
        file.write('''
<style lang="scss" scoped>
form {
  width: 80%;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
  border-radius: 7px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
h2 {
  margin-bottom: 3px;
}
#submitbuttonId {
  width: 20%;
  background-color: #649790;
  color: white;
  font-size: 18px;
  padding: 14px 20px;
  margin: 17px 20px 12px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  &:hover {
    background-color: #05a38e;
    transform: scale(1.05);
  }
}
        ''')
        if radio == True:
            file.write('''
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        ''')
        if checkbox == True:
            file.write('''
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            ''')
        if checkbox == True or radio == True:
            file.write('''
label {
  margin-left: 5px;
  font-size: 22px;
}
        ''')
        if textarea == True:
            responsiveList.append("#textareaId,\n")
            file.write('''
#textareaId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
  min-width: 50%;
  min-height: 100px;
}
        ''')
        if numberinput == True:
            responsiveList.append("#numberinputId,\n")
            file.write('''
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            ''')
        if textinput == True:
            responsiveList.append("#textinputId,\n")
            file.write('''
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            ''')
        if dateinput == True:
            responsiveList.append("#inputdateId,\n")
            file.write('''
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            ''')
        file.write('''
@media screen and (max-width: 999px) {      
        ''')
        for id in responsiveList:
            file.write(f'''  {id}''')
        file.write('''
  #submitbuttonId {
    width: 70%;
  }
}
</style>
        ''')
        file.write('''
<script>
export default {
    name:"formDesign",
    data(){
        return{
        ''')
        for req in requirments:
            if req["field_type"] == "text" or req["field_type"] == "email" or req["field_type"] == "tel" or req["field_type"] == "url" or req["field_type"] == "password" or req["field_type"] == "number":
                file.write(f'''
            {req["field_name"].replace(' ','_')}:"",
        ''')
            elif req["field_type"] == "radiobutton":
                file.write(f'''
            radio_buttons:"",
        ''')
            elif req["field_type"] == "checklist":
                file.write(f'''
            check_list:[],
        ''')
            elif req["field_type"] == "textarea":
                file.write(f'''
            text_area:"",
        ''')
            elif req["field_type"] == "list":
                file.write(f'''
            select_list:null,
        ''')
            elif req["field_type"] == "date":
                file.write(f'''
            date:"",
        ''')
        file.write('''
      }
    },
    methods:{
        submitForm(){
            let formData = {
        ''')
        for req in requirments:
            if req["field_type"] == "text" or req["field_type"] == "email" or req["field_type"] == "tel" or req["field_type"] == "url" or req["field_type"] == "password" or req["field_type"] == "number":
                file.write(f'''
            {req["field_name"].replace(' ','_')}:this.{req["field_name"].replace(' ','_')},
        ''')
            elif req["field_type"] == "radiobutton":
                file.write(f'''
            radio_buttons:this.radio_buttons,
        ''')
            elif req["field_type"] == "checklist":
                file.write(f'''
            check_list:this.check_list,
        ''')
            elif req["field_type"] == "textarea":
                file.write(f'''
            text_area:this.text_area,
        ''')
            elif req["field_type"] == "list":
                file.write(f'''
            select_list:this.select_list,
        ''')
            elif req["field_type"] == "date":
                file.write(f'''
            date:this.date,
        ''')
        file.write('''
            }
            console.log(formData);
        }
    }
}
</script>   
        ''')
            

# requirments = [
#     {
#         "field_name": "First Name",
#         "field_type": "text",
#         "isRequired": True,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": []
#     },
#     {
#         "field_name": "Last Name",
#         "field_type": "text",
#         "isRequired": True,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": []
#     },
#     {
#         "field_name": "Email",
#         "field_type": "email",
#         "isRequired": True,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": []
#     },
#     {
#         "field_name": "Phone Number",
#         "field_type": "tel",
#         "isRequired": True,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": []
#     },
#     {
#         "field_name": "Password",
#         "field_type": "password",
#         "isRequired": True,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": []
#     },
#     {
#         "field_name": "Github Url",
#         "field_type": "url",
#         "isRequired": True,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": []
#     },
#     {
#         "field_name": "Age",
#         "field_type": "number",
#         "isRequired": True,
#         "maxRange": 40,
#         "minRange": 18,
#         "options": []
#     },
#     {
#         "field_name": "Gender",
#         "field_type": "radiobutton",
#         "isRequired": True,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": ["Male","Female"]
#     },
#     {
#         "field_name": "Subjects",
#         "field_type": "list",
#         "isRequired": True,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": ["Math","Physics","Machine Learning","Data Science"]
#     },
#     {
#         "field_name": "Languages",
#         "field_type": "checklist",
#         "isRequired": False,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": ["Arabic","English","French"]
#     },
#     {
#         "field_name": "Description",
#         "field_type": "textarea",
#         "isRequired": False,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": []
#     },
#     {
#         "field_name": "Birth Date",
#         "field_type": "date",
#         "isRequired": False,
#         "maxRange": 0,
#         "minRange": 0,
#         "options": []
#     }
# ]
