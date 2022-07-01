
<template>
  <div id="home">
   <div class="mainContent">
      <h2>Welcome to ERvive</h2>
      <h3>Learning Management System</h3>
      <p>
        sum is simply dummy text of the printing and typesetting industry. Lorem
        Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a
        type specimen book. It has survived not only five centuries.
      </p>
      <button>CONTINUE</button>
    </div>

    <div class="animation-area">
      <ul class="box-area">
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
      </ul>
    </div>
  </div>
</template>

<script>
</script>

<style lang='scss' scoped >
.mainContent {
  width: 100%;
  position: absolute;
  text-align: center;
  z-index: 1;
}
.mainContent h2,
h3,
p {
  text-align: center;
  color: white;
}
.mainContent h2 {
  margin-top: 15%;
  font-size: 50px;
  margin-bottom: 0;
  padding: 10px;
}
.mainContent h3 {
  margin-top: 12px;
  font-size: 40px;
  padding: 10px;
  margin-bottom: 0;
}
.mainContent p {
  padding-left: 30%;
  padding-right: 30%;
  font-size: 18px;
}
.mainContent button {
  margin-top: 27px;
  margin-left: auto;
  text-align: center;
  background-color: white;
  border-radius: 25px;
  width: 22%;
  height: 50px;
  padding: 15px;
  font-size: 17px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  letter-spacing: 1.8px;
  box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
   &:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  }
}
.animation-area {
  background: linear-gradient(to left, #ffc809, #0f1136);
  width: 100%;
  height: 100vh;
}
.box-area {
  position: absolute;
  padding: 0;
  margin: 0;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.box-area li {
  position: absolute;
  display: block;
  list-style: none;
  width: 25px;
  height: 25px;
  background: rgba(255, 255, 255, 0.2);
  animation: animate 20s linear infinite;
  bottom: -150px;
}
.box-area li:nth-child(1) {
  left: 86%;
  width: 80px;
  height: 80px;
  animation-delay: 0s;
}
.box-area li:nth-child(2) {
  left: 12%;
  width: 30px;
  height: 30px;
  animation-delay: 1.5s;
  animation-duration: 10s;
}
.box-area li:nth-child(3) {
  left: 70%;
  width: 100px;
  height: 100px;
  animation-delay: 5.5s;
}
.box-area li:nth-child(4) {
  left: 42%;
  width: 150px;
  height: 150px;
  animation-delay: 0s;
  animation-duration: 15s;
}
.box-area li:nth-child(5) {
  left: 65%;
  width: 40px;
  height: 40px;
  animation-delay: 0s;
}
.box-area li:nth-child(6) {
  left: 15%;
  width: 110px;
  height: 110px;
  animation-delay: 3.5s;
}
@keyframes animate {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: translateY(-800px) rotate(360deg);
    opacity: 0;
  }
}
</style>
    