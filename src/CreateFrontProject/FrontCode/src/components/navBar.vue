
<template>
  <div class="navBar">
      <div class="trashIcon">
          <i class="fa fa-trash" aria-hidden="true"></i>
      </div>
      <div class="editIcon">
          <i class="fa fa-edit"></i>
      </div>
      <div class="postButton">
          <button>+ POST</button>
      </div>
  </div>    
</template>

<script>
export default {
    name:"navBar"
}
</script>

<style lang="scss" scoped>
.navBar{
    display:flex;
    justify-content:space-between;
    width: 100%;
    padding-left: 35px;
    padding-top: 35px;
}
.postButton{
    padding-top: 3px;
    button{
        background-color: #ffc809;
        width: 100px;
        color: #0f1136;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 20px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0 0 2px rgba(0,0,0,0.5);
        transition: all 0.3s ease 0s;
        &:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
            background-color: #0f1136;
            color: #ffc809;
        }
    }
}
.trashIcon, .editIcon{
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background-color: #0f1136;
    color: #ffc809;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease 0s;
    &:hover{
        transform: translateY(-3px);
        background-color: #ffc809;
    }
    i{
        font-size: 30px;
        padding: 9px;
        color: #ffc809;
        cursor: pointer;
        &:hover{
            color: #0f1136;
        }
    }
}
.trashIcon{
    i{
        padding: 9px;
        padding-left: 12px;
    }
}
</style>
  