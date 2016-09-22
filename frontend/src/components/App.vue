<template>
  <div class="App">
    <nav-bar></nav-bar>
    <div class="App__main-page">
      <main-page></main-page>
    </div>
    <footer-bar></footer-bar>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';
import FooterBar from './FooterBar.vue';
import MainPage from './MainPage.vue';
import store from '../vuex/store';

export default {
  name: 'App',

  components: {
    NavBar,
    MainPage,
    FooterBar
  },

  store,
};
</script>

<style>
.App__main-page {
  margin-top: 50px;
  padding: 20px;
}
</style>
