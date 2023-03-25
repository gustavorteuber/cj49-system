<script>
import { mapState } from "pinia";
import { useAuthStore } from "./stores/auth";
import estoque from "../master/etiqueta.vue";
import pedido from "../pedido.vue";
import update from "../produtos.vue";
import notify from "../master/notify.vue";
import istock from "../estoque.vue";
import axios from "axios";
export default {
  components: { estoque, notify, update, istock, pedido },
  data() {
    return {
      showDropDown: false,
      showSide: true,
      user: {},
      superuser: "",
    };
  },
  async created() {
    const res = await axios.get(`http://localhost:8000/usuario/${this.id}/`);
    this.user = res.data;
    console.log(this.user);
  },
  methods: {
    // hide show side bar
    toggleSideBar() {
      this.showSide = !this.showSide;
    },
    // toggle user
    toggleDrop() {
      this.showDropDown = !this.showDropDown;
    },
  },
  computed: {
    ...mapState(useAuthStore, [
      "id",
      "is_superuser",
      "username",
      "email",
      "foto",
    ]),
  },
};
</script>

<template>
  <body
    class="relative bg-gradient-to-r from-teal-100 to-lime-100 overflow-hidden max-h-screen"
  >
    <header
      class="fixed right-0 top-0 left-60 bg-gradient-to-r from-teal-100 to-lime-100 py-3 px-4 h-16"
    >
      <div class="max-w-4xl mx-auto">
        <div class="flex items-center justify-between">
          <div class="text-lg font-bold">Bem-vindo ao seu negocio</div>
          <notify />
        </div>
      </div>
    </header>

    <aside class="fixed inset-y-0 left-0 bg-white shadow-md max-h-screen w-60">
      <div class="flex flex-col justify-between h-full">
        <div class="flex-grow">
          <div class="px-4 py-6 text-center border-b">
            <h1 class="text-xl font-bold leading-none">
              <span class="text-emerald-700">Proative</span> App
            </h1>
          </div>
          <div class="p-4">
            <ul class="space-y-1">
              <li>
                <a
                  href="javascript:void(0)"
                  class="flex items-center bg-emerald-200 rounded-xl font-bold text-sm text-emerald-900 py-3 px-4"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1em"
                    height="1em"
                    fill="currentColor"
                    class="text-lg mr-4"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M4 .5a.5.5 0 0 0-1 0V1H2a2 2 0 0 0-2 2v1h16V3a2 2 0 0 0-2-2h-1V.5a.5.5 0 0 0-1 0V1H4V.5zM16 14V5H0v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2zm-3.5-7h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5z"
                    /></svg
                  >Dashboard
                </a>
              </li>
              <li>
                <a
                  href="javascript:void(0)"
                  class="flex bg-white hover:bg-emerald-50 rounded-xl font-bold text-sm text-gray-900 py-3 px-4"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1em"
                    height="1em"
                    fill="currentColor"
                    class="text-lg mr-4"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M12 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM5 4h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1 0-1zm-.5 2.5A.5.5 0 0 1 5 6h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5zM5 8h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1 0-1zm0 2h3a.5.5 0 0 1 0 1H5a.5.5 0 0 1 0-1z"
                    /></svg
                  >Registrar produtos
                </a>
              </li>
              <li>
                <a
                  href="javascript:void(0)"
                  class="flex bg-white hover:bg-emerald-50 rounded-xl font-bold text-sm text-gray-900 py-3 px-4"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1em"
                    height="1em"
                    fill="currentColor"
                    class="text-lg mr-4"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a1.99 1.99 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3zm-8.322.12C1.72 3.042 1.95 3 2.19 3h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981l.006.139z"
                    /></svg
                  >Planilhas
                </a>
              </li>
              <li>
                <a
                  href="javascript:void(0)"
                  class="flex bg-white hover:bg-emerald-50 rounded-xl font-bold text-sm text-gray-900 py-3 px-4"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="text-lg mr-4"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M2 1a1 1 0 0 0-1 1v4.586a1 1 0 0 0 .293.707l7 7a1 1 0 0 0 1.414 0l4.586-4.586a1 1 0 0 0 0-1.414l-7-7A1 1 0 0 0 6.586 1H2zm4 3.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"
                    /></svg
                  >Atualizar estoque
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div class="p-4">
          <div class="h-100 border-l mx-4"></div>
          <div class="flex flex-nowrap -space-x-3">
            <div
              class="flex items-center justify-start space-x-4"
              @click="toggleDrop"
            >
              <img
                v-if="user.foto != null"
                :src="user.foto.url"
                class="w-10 h-10 rounded-full"
                alt=""
              />
              <img
                v-if="user.foto == null"
                src="../master/stores/semfoto.png"
                class="w-10 h-10 rounded-full"
                alt="teste"
              />
            </div>

            <div class="flex flex-col pl-3">
              <div class="text-sm text-emerald-600">{{ username }}</div>
              <span class="text-xs text-[#acacb0] font-light tracking-tight">
                {{ email }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </aside>

    <main class="ml-60 pt-16 max-h-screen overflow-auto">
      <div class="px-6 py-8">
        <div class="max-w-4xl mx-auto">
          <div class="bg-white rounded-3xl p-8 mb-5">
            <div class="flex items-stretch">
              <div class="flex flex-nowrap -space-x-3"></div>
            </div>

            <div class="grid grid-cols-2 gap-x-20">
              <div>
                <h2
                  class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-lime-600 mb-4"
                >
                  Status do estoque
                </h2>

                <div class="grid grid-cols-2 gap-4">
                  <div class="col-span-2">
                    <div
                      class="p-4 bg-gradient-to-r from-teal-200 to-lime-200 rounded-xl"
                    >
                      <div class="font-bold text-xl text-gray-800 leading-none">
                        Olá, <br />{{ username }}
                      </div>
                      <div class="mt-5">
                        <button
                          type="button"
                          class="inline-flex items-center justify-center py-2 px-3 rounded-xl bg-white text-gray-800 hover:text-green-500 text-sm font-semibold transition"
                        >
                          Gerenciar perfil
                        </button>
                      </div>
                    </div>
                  </div>
                  <div class="col-span-2">
                    <div class="p-4 bg-purple-100 rounded-xl text-gray-800">
                      <estoque />
                    </div>
                  </div>
                </div>
              </div>
              <div>
                <h2
                  class="text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-lime-600 text-2xl font-bold mb-4"
                >
                  Atualizar estoque
                </h2>

                <div
                  class="p-4 bg-white border border-gray-300 rounded-xl text-gray-800"
                >
                  <update />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="rounded-xl"></div>
        <body
          class="relative bg-gradient-to-r from-teal-100 to-lime-100 overflow-hidden max-h-screen"
        >
          <istock />
        </body>
        <pedido />
      </div>
    </main>
  </body>
</template>

<style>
::-webkit-scrollbar {
  width: 0.5rem;
  height: 0.5rem;
}
::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.15);
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 0, 0, 0.3);
}
</style>
