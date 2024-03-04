<template>
  <v-app>
    <v-main class="text-white">
      <v-container>

        <v-row>
          <v-col cols="12" class="mt-10">
            <div class="content-box pa-4">
              <h1 class="text-center font-weight-black text-lg-h3 text-xl-h3 text-md-h3 text-sm-h3 text-h2">安南國中ANJH匿名發文平台</h1>
            </div>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" >
            <div class="content-box pa-4 h-100">
              <a href=".." class="font-weight-black text-h6">↼返回主頁</a>
              <h2 class="font-weight-bold">隱私政策</h2>
              <p>非常歡迎您光臨「安南國中ANJH匿名發文平台」 (以下簡稱本網站)<br>
                為了讓您能夠安心的使用本網站的各項服務與資訊，特此向您說明本網站的隱私權保護政策，以保障您的權益，請您詳閱下列內容:</p>
              <ul v-for="(item) in Privacy" :key="item">
                <li class="my-2">{{ item.title }}</li>
                <p v-for="(item2) in item.description" :key="item2">
                  {{ item2 }}
                </p>
              </ul>
              <br><br>
              <h3>如果您對此條款有疑問或顧忌，歡迎來IG私訊我們。</h3>
              <p class="mt-3">最後更新日期: 10/15/2023</p>
            </div>
          </v-col>
        </v-row>
        <Footer></Footer>

      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  import Footer from '../../src/components/Footer.vue'

  export default {
    name: 'Privacy',
    components: {
      Footer
    },
    data() {
      return {
        Privacy: [
          {
            title: "一、隱私權保護政策的適用範圍",
            description: ["隱私權保護政策內容，包括本網站如何處理在您使用網站服務時收集到的個人識別資料。隱私權保護政策不適用於本網站以外的相關連結網站，也不適用於非本網站所委託或參與管理的人員。"]
          },
          {
            title: "二、個人資料的蒐集、處理及利用方式",
            description: ["本網站只會蒐集您的瀏覽器客戶端、國家和IP訊息。IP訊息只適用於訪問本網站時判斷使否為網路攻擊(DDoS, CC攻擊等等)，請放心使用。"]
          },
          {
            title: "三、資料之保護",
            description: ["本網站主機均設有防火牆、防毒系統等相關的各項資訊安全設備及必要的安全防護措施，加以保護網站及您的個人資料採用嚴格的保護措施。"]
          },
          {
            title: "四、網站對外的相關連結",
            description: ["本網站的網頁提供其他網站的網路連結，您也可經由本網站所提供的連結，點選進入其他網站。但該連結網站不適用本網站的隱私權保護政策，您必須參考該連結網站中的隱私權保護政策。"]
          },
          {
            title: "五、與第三人共用個人資料之政策",
            description: ["本網站絕不會提供、交換、出租或出售任何您的個人資料給其他個人、團體、私人企業或公務機關，但有法律依據或合約義務者，不在此限。",
                          "前項但書之情形包括不限於:",
                          "• 經由您書面同意。",
                          "• 法律明文規定。",
                          "• 為免除您生命、身體、自由或財產上之危險。",
                          "• 與公務機關或學術研究機構合作，基於公共利益為統計或學術研究而有必要，且資料經過提供者處理或蒐集者依其揭露方式無從識別特定之當事人。",
                          "• 當您在網站的行為，違反服務條款或可能損害或妨礙網站與其他使用者權益或導致任何人遭受損害時，經網站管理單位研析揭露您的個人資料是為了辨識、聯絡或採取法律行動所必要者。",
                          "• 有利於您的權益。",]
          },
          {
            title: "六、Cookie 之使用",
            description: ["本網站會在您的電腦上存放一個cookie，該cookie僅為網路安全防護使用。"]
          },
          {
            title: "七、隱私權保護政策之修正",
            description: ["本網站隱私權保護政策將因應需求隨時進行修正，修正後的條款將刊登於網站上。"]
          },
        ]
      }
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

  ul {
    list-style: none;
  }

  ul li {
    font-size: 1.1rem;
  }

  a {
    color: #ffffff;
  }
</style>
