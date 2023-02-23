import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/login.vue";
import Caixa from "../views/caixa.vue";
import Tesouraria from "../views/tesouraria.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/caixa",
    name: "Caixa",
    component: Caixa,
  },
  {
    path: "/tesouraria",
    name: "Tesouraria",
    component: Tesouraria,
  },
];
const router = Router();
export default router;
function Router() {
  const router = new createRouter({
    history: createWebHistory(),
    routes,
  });
  return router;
}
