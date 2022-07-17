def create_card_design1 (filePath):
    with open(filePath, 'w') as f:
        f.write('''
<template>
  <div class="cardDesign">
    <div class="card-style" :style="backgroundStyle"></div>
    <div class="card-header">
      <h5 class="card-title">{{ title }}</h5>
    </div>
    <div class="card-body">
      <p class="card-text">{{ description }}</p>
    </div>
    <div class="card-bottom" :style="backgroundStyle">
      <router-link :to="title"><button>CLICK ME!</button></router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.cardDesign {
  max-width: 20em;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: white;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  padding: 15px;
  text-align: center;
  overflow: hidden;
  position: relative;
  border-radius: 30px;
}
.card-style {
  &:before {
    position: absolute;
    margin: -6em;
    margin-left: -1em;
    padding: 7em;
    border-radius: 50%;
    box-shadow: 0 0 7px rgb(122, 122, 121);
    background-color: var(--bg-color);
    content: "";
  }
}
.card-header {
  padding-top: 35px;
  .card-title {
    font-size: 25px;
    font-weight: 700;
    position: relative;
    z-index: 9;
    color: black;
  }
}
.card-body {
  .card-text {
    font-size: 17px;
    color: black;
  }
}
.card-bottom {
  padding-top: 25px;
  padding-bottom: 25px;
  button {
    width: 70%;
    height: 50px;
    padding: 15px;
    font-size: 17px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    color: var(--bg-color);
    letter-spacing: 1.8px;
    background-color: transparent;
    border: 2px solid var(--bg-color);
    border-radius: 25px;
    box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease 0s;
  }
  button:hover {
    background-color: var(--bg-color);
    box-shadow: 0px 15px 20px rgba(122, 122, 121, 0.4);
    color: white;
    transform: translateY(-3px);
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "cardDesign",
  props: {
    title: {
      type: String,
    },
    description: {
      type: String,
    },
  },
  computed: {
    ...mapState({
      themeColor: (state) => state.color_pallete.themeColor,
    }),
    backgroundStyle() {
      return {
        "--bg-color": this.themeColor,
      };
    },
  },
};
</script>

        ''')
 
def create_card_design2 (filePath):
    with open(filePath, 'w') as f:
        f.write('''
<template>
  <div class="cardDesign2" :style="backgroundStyle">
    <div class="card-style"></div>
    <div class="cardDesign2-header">
      <h5 class="card-title">{{ title }}</h5>
    </div>
    <div class="cardDesign2-body">
      <p class="card-text">{{ description }}</p>
    </div>
    <div class="cardDesign2-footer">
      <button>CLICK ME!</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.cardDesign2 {
  max-width: 20em;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: white;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  text-align: center;
  border-radius: 25px;
}
.card-style {
  padding-top: 17px;
  //background-color: var(--bg-color);
  background-image: linear-gradient(to bottom right, var(--bg-color), black);
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
}
.cardDesign2-header {
  padding-top: 30px;
  .card-title {
    margin-bottom: 10px;
    font-size: 25px;
    font-weight: 700;
  }
}
.cardDesign2-body {
  padding: 15px;
  .card-text {
    font-size: 17px;
    margin-bottom: 20px;
  }
}
.cardDesign2-footer {
  padding: 15px;
  padding-top: 25px;
  padding-bottom: 25px;
  button {
    width: 70%;
    height: 50px;
    padding: 15px;
    font-size: 17px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    color: var(--bg-color);
    letter-spacing: 1.8px;
    background-color: transparent;
    border: 2px solid var(--bg-color);
    box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease 0s;
  }
  button:hover {
    //background-color: var(--bg-color);
    background-image: linear-gradient(to bottom right, var(--bg-color), black);
    border: none;
    box-shadow: 0px 15px 20px rgba(122, 122, 121, 0.4);
    color: white;
    transform: translateY(-3px);
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "cardDesign2",
  props: {
    title: {
      type: String,
    },
    description: {
      type: String,
    },
  },
  computed: {
    ...mapState({
      themeColor: (state) => state.color_pallete.themeColor,
    }),
    backgroundStyle() {
      return {
        "--bg-color": this.themeColor,
      };
    },
  },
};
</script>

    ''')

def create_card_design3 (filePath):
    with open(filePath, 'w') as f:
        f.write('''
<template>
  <div class="cardDesign3" :style="backgroundStyle">
    <div class="cardDesign3-header">
      <h5 class="card-title">{{ title }}</h5>
    </div>
    <div class="cardDesign3-body">
      <p class="card-text">{{ description }}</p>
    </div>
    <div class="cardDesign3-footer">
      <button>CLICK ME!</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.cardDesign3 {
  max-width: 20em;
  margin-top: 20px;
  margin-bottom: 20px;
  background-image: linear-gradient(to bottom right, var(--bg-color), black);
  text-align: center;
  color: white;
  border-radius: 25px;
}
.cardDesign3-header {
  padding-top: 30px;
  .card-title {
    margin-bottom: 10px;
    font-size: 25px;
    font-weight: 700;
  }
}
.cardDesign3-body {
  padding: 15px;
  .card-text {
    font-size: 17px;
    margin-bottom: 20px;
  }
}
.cardDesign3-footer {
  padding: 15px;
  padding-top: 25px;
  padding-bottom: 25px;
  button {
    width: 70%;
    height: 50px;
    padding: 15px;
    font-size: 17px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    color: white;
    letter-spacing: 1.8px;
    background-color: transparent;
    border: 2px solid var(--bg-color);
    box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease 0s;
  }
  button:hover {
    background-color: var(--bg-color);
    box-shadow: 0px 3px 8px rgba(122, 122, 121, 0.4);
    transform: translateY(-3px);
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "cardDesign3",
  props: {
    title: {
      type: String,
    },
    description: {
      type: String,
    },
  },
  computed: {
    ...mapState({
      themeColor: (state) => state.color_pallete.themeColor,
    }),
    backgroundStyle() {
      return {
        "--bg-color": this.themeColor,
      };
    },
  },
};
</script>

        ''')

def create_card_design4 (filePath):
    with open(filePath, 'w') as f:
        f.write('''
<template>
  <div class="card_wrapper">
    <card-with-tag
      v-for="card in cardsData"
      :key="card.id"
      :title="card.title"
      :text="card.text"
      :color-hex="cardsColor"
      :button-text="card.buttonText"
    ></card-with-tag>
  </div>
</template>
<style lang="scss">
.card_wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  padding: 0 100px;
}
</style>

<script>
export default {
  name: "CardWrapper",
  props: {
    cardsColor: { type: String },
    cardsData: { type: Array },
  },
};
</script>

        ''')

def create_color_pallete (filePath):
    with open(filePath, 'w') as f:
        f.write('''
<template>
  <chrome-color-picker
    :value="themeColor"
    @input="setThemeColor($event.hex)"
    :disableAlpha="true"
  />
</template>

<script>
import { Chrome } from "vue-color";
import { mapGetters, mapMutations } from "vuex";

export default {
  components: {
    "chrome-color-picker": Chrome,
  },
  computed: {
    ...mapGetters(["themeColor"]),
  },
  methods: {
    ...mapMutations(["setThemeColor"]),
  },
};
</script>
        ''')

def create_color_pallete_module (filePath):
  with open (filePath , 'w') as f:
    f.write('''
    const state = {
  themeColor: "#f90",
};

const mutations = {
  setThemeColor(state, color) {
    state.themeColor = color;
  },
};

const getters = {
  themeColor: (state) => state.themeColor,
};

export default {
  state,
  mutations,
  getters,
};
    ''')