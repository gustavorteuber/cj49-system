<script>
import atualizarEstoque from "../components/atualizarEstoque.vue";
import estoque from "../components/estoque.vue";
import headerinfo from "../components/header.vue";

export default {
  components: { atualizarEstoque, estoque, headerinfo },
  data() {
    return {};
  },
  created() {
    setInterval(() => {
      location.reload();
    }, 60000);
  },
};
</script>

<template>
  <headerinfo />
  <div
    class="m-20 justify-center flex flex-col md:flex-row"
    style="margin-top: 17%"
  >
    <div class="shadow-lg p-1 bg-gray-100 md:w-1/2 border rounded-md shadow-md">
      <estoque />
    </div>
    <div class="m-2"></div>
    <div
      class="shadow-lg bg-gray-100 md:w-1/2 w-full p-1 border rounded-md shadow-md order-2 md:order-1"
    >
      <atualizarEstoque />
    </div>
  </div>
</template>
