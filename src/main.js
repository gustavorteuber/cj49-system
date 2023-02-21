import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { initializeApp } from "firebase/app";

import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyDXvAxBtbkIkRTBruMd2QK7NdpyOGNyDSY",

  authDomain: "caixaeletronico-25ee9.firebaseapp.com",

  projectId: "caixaeletronico-25ee9",

  storageBucket: "caixaeletronico-25ee9.appspot.com",

  messagingSenderId: "930777439684",

  appId: "1:930777439684:web:57d2e1f3cfa2a0bb46d891",

  measurementId: "G-FRJW7BXL30",
};

const app = initializeApp(firebaseConfig);

const analytics = getAnalytics(app);

createApp(App).mount("#app");
