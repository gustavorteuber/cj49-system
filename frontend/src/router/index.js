import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/login.vue";
import Pedido from "../views/pedido.vue";
import Estoque from "../views/estoque.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },

  {
    path: "/pedido",
    name: "Pedido",
    component: Pedido,
  },
  {
    path: "/estoque",
    name: "Estoque",
    component: Estoque,
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
