<template>
  <v-app>
    <v-main>
      <router-view v-slot="{ Component }" style="background-color: #0e1525;">
        <transition name="fade">
          <keep-alive>
            <component :is="Component" class="text-white"></component>
          </keep-alive>
        </transition>
      </router-view>

      <Footer></Footer>
    </v-main>
  </v-app>
</template>

<script>
  import Footer from './components/Footer.vue'

  export default {
    name: 'App',
    components: {
      Footer
    }
  }
</script>

<style scoped>
  * {
    background-color: #0e1525;
  }
</style>
