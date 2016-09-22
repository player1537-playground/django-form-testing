import Vue from 'expose?Vue!vue';
import router from './router';
import store from './vuex/store';
import { sync } from 'vuex-router-sync';
import resource from './resource';
import App from './components/App.vue';

sync(store, router);

router.start(App, '#app');
