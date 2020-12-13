// src/plugins/vuetify.js

import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import {UserVuetifyPreset} from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

const opts: UserVuetifyPreset = {
    icons:{
        iconfont: 'mdiSvg'
    }
}

export default new Vuetify(opts)
Vue.use(Vuetify)