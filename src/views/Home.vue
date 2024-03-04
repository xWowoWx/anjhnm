<template>
  <v-app>
    <v-main>
      <v-container>

        <v-row>
          <v-col cols="12" class="mt-10">
            <div class="content-box pa-4">
              <h1 class="text-center font-weight-black text-lg-h3 text-xl-h3 text-md-h3 text-sm-h3 text-h2">安南國中ANJH匿名發文平台</h1>
            </div>
          </v-col>
        </v-row>

        <v-row>
          <v-col lg="8" md="7" sm="6" cols="12">
            <div class="content-box pa-4 h-100">
              <h2 class="font-weight-bold">發文說明</h2>
              <ul v-for="(item, index) in postDescription" :key="item">
                <li data-nosnippet="data-nosnippet">{{ index + 1 }}. {{ item }}</li>
              </ul>
              <h3 class="mt-13">我們的Instagram: <a href="https://www.instagram.com/anjh_nm/" target="_blank">安南國中匿名發文平台</a></h3>
            </div>
          </v-col>

          <v-col lg="4" md="5" sm="6" cols="12">
            <div class="content-box pa-4 h-100">
              <h2 class="font-weight-bold">板規</h2>
              <ul v-for="(item, index) in postRules" :key="item">
                <li data-nosnippet="data-nosnippet">{{ index + 1 }}. {{ item }}</li>
              </ul>
            </div>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12">
            <div class="content-box pa-4 h-100">
              <h2 class="font-weight-bold">發文</h2>
              <p id="pendingReview">{{ pendingReview }}</p>
              <v-textarea clearable auto-grow v-model="content" label="請輸入發文內容" :rules="InputRule"></v-textarea>
              <v-btn @click="verifyContent" :loading="loading" class="w-100">發送</v-btn>
              <p class="mt-3">送出貼文後即表示您同意我們的<a href="/Privacy/" class="font-weight-black">隱私政策</a>、發文說明和板規 </p>
              <p class="mt-1" style="color: yellow">本站目前不支援大部分顏文字、簡體字和一些特殊符號。Emoji僅支援部分</p>
              <p class="mt-2" style="color: red">我們並非學校官方，如果學校想要刪掉這個匿名板，請在升旗的時候講，我們會立刻刪除。</p>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  import { ref } from '@vue/reactivity';
  import axios from 'axios';

  export default {
    name: 'Home',
    data() {
      return {
        loading: false,
        content: ref(""),
        postDescription: [
          "發文內容會發佈在Instagram上。",
          "送出發文內容後須等待我們的審核才會出現在貼文。",
          "如果發文後超過2天都沒有看到貼文，可能是有違規內容被刪除、眼殘沒看到或是小編懶惰沒去檢查，如果可以的話來Instagram私訊詢問我們。",
          "發出去的貼文可能會讓一些人覺得不喜歡，我們已經盡力以客觀以及當事人的角度去看，如果有遺漏的，請私訊我們，我們會刪掉，請見諒。",
          "如需刪除特定貼文，可以來Instagram私訊我們並講述原因。",
          "發文時請盡量不要打出全名，例如:陳xx、陳x名'(如有雷同，純屬巧合)。",
          "請不要問關於小編的'個人資訊'，例如: 班級、姓名等等。",
          "不要發讓小編不懂的詞，除非這個詞Google查的到，否則一律忽略。",
          "拜託拜託這不是你的抱怨或嘴人基地，有私人糾紛請自己私下解決或請導師協助。",
          "每個小編的審文標準不一樣，所以可能會遇到發出去然後又刪掉的，請見諒。",
          "我們有權利刪除任何違反規定或有爭議的貼文。",
        ],
        postRules: [
          "發文內容須按照現實狀況。",
          "發文內容不要發太多次相同的。",
          "發文字數不得小於1個和大於200字。",
          "發文內容不得包含但不限於含惡意連結、惡意代碼、副本、廣告、釣魚等等內容。",
          "發文內容不得包含但不限於人身攻擊、辱罵、抱怨、地域攻擊、種族、色情、政治、邪教、犯罪、毒品、自殺等等內容。",
        ],
        InputRule: [
          value => !!value || '必須輸入發文內容',
          value => (value && value.length < 200) || '文字數量不得大於200',
        ],
        postURL: 'https://api.anjhnm.me/send-post/',
        pendingReviewURL: 'https://api.anjhnm.me/pending-review/'
      }
    },
    computed: {
      pendingReview() {
        axios.get(this.pendingReviewURL).then((response) => {
          window.document.getElementById("pendingReview").innerHTML = `待審核貼文數量: ${response.data.pendingReviewNumber}`
        }).catch((error) => {
          window.document.getElementById("pendingReview").innerHTML = `待審核貼文數量: error`
        })
      }
    },
    methods: {
      verifyContent () {
        if (this.content.length < 1 || this.content.length > 200) {
          return this.$swal({
            title:"錯誤",
            icon: 'error',
            color: '#ffffff',
            background: '#222231',
            text:"發文字數不得小於1個字或大於200個字!",
          })
        }

        this.loading = true
        if (this.content.toLowerCase().replace(/\s*/g,"") === "badapple") {
          this.loading = false
          return this.$router.push('/badapple')
        }

        axios.post("https://api.fbhurl.fun/scan/dirt/", {
          content: this.content,
        }).then(() => {
          axios.post(this.postURL, {
            content: this.content,
          }).then((response) => {
            this.loading = false
            this.$swal({
              title:"成功",
              icon: 'success',
              color: '#ffffff',
              background: '#222231',
              text:"已成功發送貼文，請等待審核!",
            })
          }).catch((error) => {
            this.loading = false
            this.$swal({
              title:"錯誤",
              icon: 'error',
              color: '#ffffff',
              background: '#222231',
              text:`發送請求失敗! 錯誤代碼: ${error.response.status}`,
            })
          })
        }).catch((error) => {
          this.loading = false
          if (error.response.status == 403) {
            this.$swal({
              title: "錯誤",
              icon: 'error',
              color: '#ffffff',
              background: '#222231',
              text: `文字疑似包含髒話內容`,
            })
          }
          else {
            this.$swal({
              title: "錯誤",
              icon: 'error',
              color: '#ffffff',
              background: '#222231',
              text: `伺服器無響應，請稍後再試!`,
            })
          }
        })
      },
    },
  }
</script>

<style scoped>
  .content-box {
    background-color: #222231;
    border-radius: 10px;
    border-color: #494660;
    border-style: solid;
    border-width: 1px;
  }

  ul, li {
    list-style: none;
  }
  ul, li {
    font-size: 1.1rem;
  }

  a {
    color: #ffffff;
  }

  button {
    background-color: #494660;
    color: #ffffff;
  }
</style>
