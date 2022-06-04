<template>
  <div class="form">
    <form @submit.prevent="submitForm">
      <h2>First Name</h2>

      <input
        type="text"
        id="textinputId"
        placeholder="Enter First Name"
        v-model="First_Name"
        required
      />
      <br />

      <h2>Last Name</h2>

      <input
        type="text"
        id="textinputId"
        placeholder="Enter Last Name"
        v-model="Last_Name"
        required
      />
      <br />

      <h2>Email</h2>

      <input
        type="email"
        id="textinputId"
        placeholder="Enter Email"
        v-model="Email"
        required
      />
      <br />

      <h2>Phone Number</h2>

      <input
        type="tel"
        id="textinputId"
        placeholder="123-12-123"
        pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}"
        v-model="Phone_Number"
        required
      />
      <br />

      <h2>Password</h2>

      <input
        type="password"
        id="textinputId"
        placeholder="Enter Password"
        v-model="Password"
        required
      />
      <br />

      <h2>Github Url</h2>

      <input
        type="url"
        id="textinputId"
        placeholder="Enter Github Url"
        v-model="Github_Url"
        required
      />
      <br />

      <h2>Age</h2>

      <input
        type="number"
        id="numberinputId"
        placeholder="Enter Age"
        min="18"
        max="40"
        v-model="Age"
        required
      />
      <br />

      <h2>Gender</h2>

      <input
        type="radio"
        id="radiobuttonId"
        value="Male"
        v-model="radio_buttons"
        required
      />
      <label>Male</label>

      <input
        type="radio"
        id="radiobuttonId"
        value="Female"
        v-model="radio_buttons"
        required
      />
      <label>Female</label>

      <h2>Subjects</h2>

      <select id="textinputId" v-model="select_list" required>
        <option value="" disabled selected>Select Subjects</option>

        <option value="Math">Math</option>

        <option value="Physics">Physics</option>

        <option value="Machine Learning">Machine Learning</option>

        <option value="Data Science">Data Science</option>
      </select>
      <h2>Languages</h2>

      <input
        type="checkbox"
        id="checkboxId"
        value="Arabic"
        v-model="check_list"
      />
      <label>Arabic</label>

      <input
        type="checkbox"
        id="checkboxId"
        value="English"
        v-model="check_list"
      />
      <label>English</label>

      <input
        type="checkbox"
        id="checkboxId"
        value="French"
        v-model="check_list"
      />
      <label>French</label>

      <h2>Description</h2>

      <textarea
        id="textareaId"
        placeholder="Enter Description"
        v-model="text_area"
      ></textarea>

      <h2>Birth Date</h2>

      <input type="date" id="inputdateId" v-model="date" />
      <br />

      <input type="submit" id="submitbuttonId" />
      <input type="reset" id="submitbuttonId" />
    </form>
  </div>
</template>

<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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

#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}

#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}

label {
  margin-left: 5px;
  font-size: 22px;
}

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

#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}

#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}

#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}

@media screen and (max-width: 999px) {
  #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,
  #submitbuttonId {
    width: 70%;
  }
}
</style>

<script>
export default {
  name: "formDesign",
  data() {
    return {
      First_Name: "",

      Last_Name: "",

      Email: "",

      Phone_Number: "",

      Password: "",

      Github_Url: "",

      Age: "",

      radio_buttons: "",

      select_list: null,

      check_list: [],

      text_area: "",

      date: "",
    };
  },
  methods: {
    submitForm() {
      let formData = {
        First_Name: this.First_Name,

        Last_Name: this.Last_Name,

        Email: this.Email,

        Phone_Number: this.Phone_Number,

        Password: this.Password,

        Github_Url: this.Github_Url,

        Age: this.Age,

        radio_buttons: this.radio_buttons,

        select_list: this.select_list,

        check_list: this.check_list,

        text_area: this.text_area,

        date: this.date,
      };
      console.log(formData);
    },
  },
};
</script>

<template>
  <div class="form">
    <form @submit.prevent="submitForm">
      <h2>First Name</h2>

      <input
        type="text"
        id="textinputId"
        placeholder="Enter First Name"
        v-model="First_Name"
        required
      />
      <br />

      <h2>Last Name</h2>

      <input
        type="text"
        id="textinputId"
        placeholder="Enter Last Name"
        v-model="Last_Name"
        required
      />
      <br />

      <h2>Email</h2>

      <input
        type="email"
        id="textinputId"
        placeholder="Enter Email"
        v-model="Email"
        required
      />
      <br />

      <h2>Phone Number</h2>

      <input
        type="tel"
        id="textinputId"
        placeholder="123-12-123"
        pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}"
        v-model="Phone_Number"
        required
      />
      <br />

      <h2>Password</h2>

      <input
        type="password"
        id="textinputId"
        placeholder="Enter Password"
        v-model="Password"
        required
      />
      <br />

      <h2>Github Url</h2>

      <input
        type="url"
        id="textinputId"
        placeholder="Enter Github Url"
        v-model="Github_Url"
        required
      />
      <br />

      <h2>Age</h2>

      <input
        type="number"
        id="numberinputId"
        placeholder="Enter Age"
        min="18"
        max="40"
        v-model="Age"
        required
      />
      <br />

      <h2>Gender</h2>

      <input
        type="radio"
        id="radiobuttonId"
        value="Male"
        v-model="radio_buttons"
        required
      />
      <label>Male</label>

      <input
        type="radio"
        id="radiobuttonId"
        value="Female"
        v-model="radio_buttons"
        required
      />
      <label>Female</label>

      <h2>Subjects</h2>

      <select id="textinputId" v-model="select_list" required>
        <option value="" disabled selected>Select Subjects</option>

        <option value="Math">Math</option>

        <option value="Physics">Physics</option>

        <option value="Machine Learning">Machine Learning</option>

        <option value="Data Science">Data Science</option>
      </select>
      <h2>Languages</h2>

      <input
        type="checkbox"
        id="checkboxId"
        value="Arabic"
        v-model="check_list"
      />
      <label>Arabic</label>

      <input
        type="checkbox"
        id="checkboxId"
        value="English"
        v-model="check_list"
      />
      <label>English</label>

      <input
        type="checkbox"
        id="checkboxId"
        value="French"
        v-model="check_list"
      />
      <label>French</label>

      <h2>Description</h2>

      <textarea
        id="textareaId"
        placeholder="Enter Description"
        v-model="text_area"
      ></textarea>

      <h2>Birth Date</h2>

      <input type="date" id="inputdateId" v-model="date" />
      <br />

      <input type="submit" id="submitbuttonId" />
      <input type="reset" id="submitbuttonId" />
    </form>
  </div>
</template>

<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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

#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}

#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}

label {
  margin-left: 5px;
  font-size: 22px;
}

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

#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}

#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}

#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}

@media screen and (max-width: 999px) {
  #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,
  #submitbuttonId {
    width: 70%;
  }
}
</style>

<script>
export default {
  name: "formDesign",
  data() {
    return {
      First_Name: "",

      Last_Name: "",

      Email: "",

      Phone_Number: "",

      Password: "",

      Github_Url: "",

      Age: "",

      radio_buttons: "",

      select_list: null,

      check_list: [],

      text_area: "",

      date: "",
    };
  },
  methods: {
    submitForm() {
      let formData = {
        First_Name: this.First_Name,

        Last_Name: this.Last_Name,

        Email: this.Email,

        Phone_Number: this.Phone_Number,

        Password: this.Password,

        Github_Url: this.Github_Url,

        Age: this.Age,

        radio_buttons: this.radio_buttons,

        select_list: this.select_list,

        check_list: this.check_list,

        text_area: this.text_area,

        date: this.date,
      };
      console.log(formData);
    },
  },
};
</script>

<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        
<template>
    <div class="form">
        <form @submit.prevent="submitForm">
        
            <h2>First Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter First Name" v-model="First_Name" required/>
            <br />
                    
            <h2>Last Name</h2>
            
            <input type="text" id="textinputId" placeholder="Enter Last Name" v-model="Last_Name" required/>
            <br />
                    
            <h2>Email</h2>
            
            <input type="email" id="textinputId" placeholder="Enter Email" v-model="Email" required/>
            <br />
                    
            <h2>Phone Number</h2>
            
            <input type="tel" id="textinputId" placeholder="123-12-123" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" v-model="Phone_Number" required/>
            <br />
                    
            <h2>Password</h2>
            
            <input type="password" id="textinputId" placeholder="Enter Password" v-model="Password" required/>
            <br />
                    
            <h2>Github Url</h2>
            
            <input type="url" id="textinputId" placeholder="Enter Github Url" v-model="Github_Url" required/>
            <br />
                    
            <h2>Age</h2>
            
            <input type="number" id="numberinputId" placeholder="Enter Age" min="18" max="40" v-model="Age" required/>
            <br />
                        
            <h2>Gender</h2>
            
            <input type="radio" id="radiobuttonId" value=Male v-model= "radio_buttons" required/>
            <label>Male</label>
                        
            <input type="radio" id="radiobuttonId" value=Female v-model= "radio_buttons" required/>
            <label>Female</label>
                        
            <h2>Subjects</h2>
            
            <select id="textinputId" v-model="select_list" required>
                <option value="" disabled selected>Select Subjects</option>
                    
                <option value="Math">Math</option>
                    
                <option value="Physics">Physics</option>
                    
                <option value="Machine Learning">Machine Learning</option>
                    
                <option value="Data Science">Data Science</option>
                    </select>
            <h2>Languages</h2>
            
            <input type="checkbox" id="checkboxId" value=Arabic v-model= "check_list" />
            <label>Arabic</label>
                        
            <input type="checkbox" id="checkboxId" value=English v-model= "check_list" />
            <label>English</label>
                        
            <input type="checkbox" id="checkboxId" value=French v-model= "check_list" />
            <label>French</label>
                        
            <h2>Description</h2>
            
            <textarea id="textareaId" placeholder="Enter Description" v-model= "text_area" ></textarea>
                    
            <h2>Birth Date</h2>
            
            <input type="date" id="inputdateId" v-model= "date" />
            <br />
                    
            <input type="submit" id="submitbuttonId" />
            <input type="reset" id="submitbuttonId" />
        </form>
    </div>
</template>
        
<style lang="scss" scoped>
form {
  width: 80%;
  height: 80%;
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
        
#radiobuttonId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
        
#checkboxId {
  margin-left: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}            
            
label {
  margin-left: 5px;
  font-size: 22px;
}
        
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
        
#numberinputId {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#textinputId {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
#inputdateId {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
  font-size: 17px;
  border-radius: 4px;
}
            
@media screen and (max-width: 999px) {      
          #textareaId,
  #numberinputId,
  #textinputId,
  #inputdateId,

  #submitbuttonId {
    width: 70%;
  }
}
</style>
        
<script>
export default {
    name:"formDesign",
    data(){
        return{
        
            First_Name:"",
        
            Last_Name:"",
        
            Email:"",
        
            Phone_Number:"",
        
            Password:"",
        
            Github_Url:"",
        
            Age:"",
        
            radio_buttons:"",
        
            select_list:null,
        
            check_list:[],
        
            text_area:"",
        
            date:"",
        
      }
    },
    methods:{
        submitForm(){
            let formData = {
        
            First_Name:this.First_Name,
        
            Last_Name:this.Last_Name,
        
            Email:this.Email,
        
            Phone_Number:this.Phone_Number,
        
            Password:this.Password,
        
            Github_Url:this.Github_Url,
        
            Age:this.Age,
        
            radio_buttons:this.radio_buttons,
        
            select_list:this.select_list,
        
            check_list:this.check_list,
        
            text_area:this.text_area,
        
            date:this.date,
        
            }
            console.log(formData);
        }
    }
}
</script>   
        