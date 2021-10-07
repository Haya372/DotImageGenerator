import Vue from 'vue'
import vuetify from './plugins/vuetify' // path to vuetify export
import App from './App.vue';
import "@fontsource/roboto"; // Defaults to weight 400.
import router from './router';
import PortalVue from 'portal-vue';

Vue.use(PortalVue);

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app');