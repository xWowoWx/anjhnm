<template>
  <v-app>
    <v-main>
      <v-container>

        <h1 class="justify-center d-flex text-center">Bad Apple</h1>
        <v-row class="mt-10">
          <v-col>
            <div class="justify-center py-4 content-box bad-apple"></div>
          </v-col>
        </v-row>
        <div class="justify-center d-flex">
          <v-btn @click="hidePlayButton" icon="mdi-play" class="start" variant="text"></v-btn>
        </div>
        <div class="justify-center d-flex">恭喜你發現了網站的彩蛋!</div>
        <div class="justify-center d-flex">手機可以左右滑動畫面</div>
        <div class="justify-center d-flex">聲音畫面不同步很正常、僅支持Chrome瀏覽器</div>

      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  import { Checkboxland } from 'checkboxland';

  export default {
    name: 'badapple',
    mounted() {
      const cbl = new Checkboxland({
        dimensions: '60x45',
        selector: '.bad-apple'
      });

      let playing = false;
      let played = false;
      let checkbox = document.querySelectorAll("input[type='checkbox']")[59];
      let start = document.querySelector(".start");

      start.addEventListener("click", () => {
        if (playing) return;
        checkbox.checked = true
        cbl.renderVideo("./badapple.mp4")
        setTimeout(() => {
          playing = true;
        }, 200);
      });

      let checkaudio = setInterval(function(){
        if (!checkbox.checked && playing && !played) {
          let audio = new Audio('./badapple.mp3');
          audio.play();
          played = true;
          setTimeout(() => {
            played = false;
          }, 218 * 1000);
        }
      }, 100);
    },
    methods: {
      hidePlayButton() {
        let start = document.querySelector(".start");
        start.style.display = "none";
      }
    }
  }
</script>

<style scoped>
  .content-box {
    background-color: #222231;
    border-radius: 5px;
    border-color: #494660;
    border-style: solid;
    border-width: 1px;
  }

</style>
