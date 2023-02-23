import { createApp } from "vue";
import "./style.css";
import { createPinia } from "pinia";
import router from "./router/index";
import "./plugins/axios";
import App from "./App.vue";

const app = createApp(App);
createApp(App).mount("#app");
app.use(router);
app.mount("#app");
app.use(createPinia());
