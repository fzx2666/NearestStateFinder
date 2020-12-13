import Vue from 'vue'
import App from './App.vue'
import store from './store'
import * as VueGoogleMaps from 'vue2-google-maps'
import vuetify from '@/plugins/vuetify' // path to vuetify export
import { exec } from 'child_process'


Vue.use(VueGoogleMaps,{
  load:{
    key:'AIzaSyCq_ytJah-ekYRnnG-_PsKcvuctU-Sa4wc'
  },
  installComponents: true
})
Vue.config.productionTip = false
new Vue({
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
