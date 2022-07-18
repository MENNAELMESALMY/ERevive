def createForm (requirments,cluster_name,endpoint,filePath,isPut=False,get_endpoint='',pks=[]):
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
        for req in requirments[cluster_name]:
            disabled = "disabled" if isPut and req["isRequired"] else ""
            required = "required" if req["isRequired"] else ""
            file.write(f'''
            <h2>{req["field_name"]}</h2>
            ''')
            if req["field_type"] == "text" :
                textinput = True
                file.write(f'''
            <input type="{req["field_type"]}" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" {required} {disabled} />
            <br />
                    ''')
            elif req["field_type"] == "email":
                file.write(f'''
            <input type="email" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" {required} {disabled}/>
            <br />
                    ''')
            elif req["field_type"] == "tel":
                file.write('''
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="%s" %s %s/>
            <br />
                    ''' %req["field_name"].replace(' ','_') %required %disabled )
            elif req["field_type"] == "password":
                file.write(f'''
            <input type="password" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" {required} {disabled}/>
            <br />
                    ''')
            elif req["field_type"] == "url":
                file.write(f'''
            <input type="url" id="textinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" {required} {disabled}/>
            <br />
                    ''')
            elif req["field_type"] == "number":
                numberinput = True
                file.write(f'''
            <input type="number" id="numberinputId" placeholder="Enter {req["field_name"]}" v-model="{req["field_name"].replace(' ','_')}" {required} {disabled}/>
            <br />
                    ''')
            elif req["field_type"] == "radiobutton":
                radio = True
                for option in req["options"]:
                        file.write(f'''
            <input type="radio" id="radiobuttonId" value={option} v-model= "{req["field_name"].replace(' ','_')}" {required} {disabled}/>
            <label>{option}</label>
                        ''')
            elif req["field_type"] == "checklist":
                checkbox = True
                for option in req["options"]:
                        file.write(f'''
            <input type="checkbox" id="checkboxId" value={option} v-model= "{req["field_name"].replace(' ','_')}" {required} {disabled}/>
            <label>{option}</label>
                        ''')
            elif req["field_type"] == "textarea":
                textarea = True
                file.write(f'''
            <textarea id="textareaId" placeholder="Enter {req["field_name"]}" v-model= "{req["field_name"].replace(' ','_')}" {required} {disabled}></textarea>
                    ''')
            elif req["field_type"] == "list":
                file.write(f'''
            <select id="textinputId" v-model="{req["field_name"].replace(' ','_')}" {required} {disabled}>
                <option value="" disabled selected>Select {req["field_name"]}</option>
                    ''')
                for option in req["options"]:
                    file.write(f'''
                <option value="{option}">{option}</option>
                    ''')
                file.write("</select>")                
            elif req["field_type"] == "date":
                dateinput = True
                file.write(f'''
            <input type="date" id="inputdateId" v-model= "{req["field_name"].replace(' ','_')}" {required} {disabled}/>
            <br />
                    ''')
        file.write('''
            <input type="submit" id="submitbuttonId" value="submit" />
            <input type="reset" id="submitbuttonId" value="reset"/>
        </form>
    </div>
</template>
        ''')
        file.write('''
<style lang="scss" scoped>
form {
  width: 80%;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
  //border-radius: 7px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
h2 {
  margin-bottom: 3px;
}
#submitbuttonId {
  width: 20%;
  background-color: #0f1136;
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
    background-color: #ffc809;
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
        if not isPut:
            file.write('''
    <script>
    import moment from "moment";
    export default {
        name:"formDesign",
        data(){
            return{
            ''')
            for req in requirments[cluster_name]:
                file.write(f'''
                {req["field_name"].replace(' ','_')}:"",
            ''')
                
            file.write('''
        }
        },
        methods:{
            async submitForm(){
                let formData = {};
                let feild = "";
            ''')
            for req in requirments[cluster_name]:
                file.write(f'''
                    feild = this.{req["field_name"].replace(' ','_')};
                    if(feild != "" && feild != null && feild != "None")
                ''')
                if req["field_type"] == "date":
                    file.write(f'''
                    formData["{req["field_name"].replace(' ','_')}"]= moment(String(this.{req["field_name"].replace(' ','_')})).format('YYYY-MM-DD HH:mm:ss'); ;
                ''')
                else:
                    file.write(f'''
                    formData["{req["field_name"].replace(' ','_')}"]=this.{req["field_name"].replace(' ','_')};
                ''')
                    
            file.write(f'''
                await this.$store.dispatch("{cluster_name}_cluster/{endpoint["endpoint_name"]}", formData);
                this.$router.push("{cluster_name}_cluster_{get_endpoint}");
            
            ''')
            file.write('''
            }
        }
    }
    </script>   
            ''')
        else:
            file.write('''
    <script>
    import { mapState } from "vuex";
    import moment from "moment";

    export default {
        name:"formDesign",
        data(){
            return{
            ''')
            for req in requirments[cluster_name]:
                file.write(f'''
                {req["field_name"].replace(' ','_')}:"",
            ''')
            file.write('''
        }
        },
        methods:{
            async submitForm(){
                let formData = {};
                let feild = "";
            ''')
            for req in requirments[cluster_name]:
                file.write(f'''
                    feild = this.{req["field_name"].replace(' ','_')};
                    if(feild != "" && feild != null && feild != "None")
                ''')
                if req["field_type"] == "date":
                    file.write(f'''
                    formData["{req["field_name"].replace(' ','_')}"]= moment(String(this.{req["field_name"].replace(' ','_')})).format('YYYY-MM-DD HH:mm:ss'); ;
                ''')
                else:
                    file.write(f'''
                    formData["{req["field_name"].replace(' ','_')}"]=this.{req["field_name"].replace(' ','_')};
                ''')


            file.write(f'''
                await this.$store.dispatch("{cluster_name}_cluster/{endpoint["endpoint_name"]}", formData);
                this.$router.push("/App/{cluster_name}_cluster_{get_endpoint}");
            ''')
            file.write('''
            }
            },
            computed: {
            ...mapState({
            ''')
            file.write(f'''
            cur_item_in_store: state => state.{cluster_name}_cluster.cur_item_in_store,''')
            file.write('''
            }),},
            ''')
            file.write('''
            mounted() {
                let obj = this.cur_item_in_store;
            ''')

            link_data_string = ""
            for req in requirments[cluster_name]:
                if req["field_type"] == "date":
                    link_data_string += f"this.{req['field_name'].replace(' ','_')} = moment(String(obj.{req['field_name'].replace(' ','_')})).format('YYYY-MM-DD');"
                else:
                    link_data_string += f"this.{req['field_name']}=obj.{req['field_name']};\n"
            file.write(link_data_string)
            file.write('''
                },
            }
        </script>   
                ''')
