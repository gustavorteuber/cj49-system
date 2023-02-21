import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "leaflet/dist/leaflet.css";
import "leaflet/dist/leaflet.js";
import { LMap, LTileLayer, LMarker } from "vue3-leaflet";

createApp(App)
  .component("LMap", LMap)
  .component("LTileLayer", LTileLayer)
  .component("LMarker", LMarker)
  .mount("#app");
