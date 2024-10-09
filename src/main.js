
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '../src/assets/index.css'
import axios from 'axios'

const app = createApp(App)

app.directive('click-outside', {
    mounted(el, binding) {
      el.clickOutsideEvent = function (event) {
        if (!(el === event.target || el.contains(event.target))) {
          binding.value(event);
        }
      };
      document.body.addEventListener('click', el.clickOutsideEvent);
    },
    unmounted(el) {
      document.body.removeEventListener('click', el.clickOutsideEvent);
    },
  });
  
app.use(router)

app.mount('#app')

