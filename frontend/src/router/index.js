import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/login.vue";
import Pedido from "../views/pedido.vue";
import Estoque from "../views/estoque.vue";
import Registro from "../views/registers.vue";

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
  {
    path: "/registro",
    name: "Registro",
    component: Registro,
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
