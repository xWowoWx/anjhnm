import { loadFonts } from './webfontloader'
import vuetify from './vuetify'
import router from '../router'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

export function registerPlugins (app) {
  loadFonts()
  app.use(vuetify).use(router).use(VueSweetalert2)
}
