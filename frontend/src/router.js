import Vue from 'vue';
import VueRouter from 'vue-router';

import DefaultRoute from './components/DefaultRoute.vue';
import CatalogRoute from './components/CatalogRoute.vue';
import LoginRoute from './components/LoginRoute.vue';
import ProfileRoute from './components/ProfileRoute.vue';
import ReductionRoute from './components/ReductionRoute.vue';
import ReductionTabRoute from './components/ReductionTabRoute.vue';
import FormTestRoute from './components/FormTestRoute.vue';

Vue.use(VueRouter);

const router = new VueRouter();

router.map({
  '/': {
    name: 'default',
    component: DefaultRoute,
  },
  '/catalog': {
    name: 'catalog',
    component: CatalogRoute,
  },
  '/login': {
    name: 'login',
    component: LoginRoute,
  },
  '/profile': {
    name: 'profile',
    component: ProfileRoute,
  },
  '/reduction': {
    name: 'reduction',
    component: ReductionRoute,
  },
  '/form-test': {
    name: 'form-test',
    component: FormTestRoute,
  },
});

export default router;
