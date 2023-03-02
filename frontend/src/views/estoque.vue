<script>
import atualizarEstoque from "../components/atualizarEstoque.vue";
import estoque from "../components/estoque.vue";

export default {
  components: { atualizarEstoque, estoque },
  data() {
    return {};
  },
  // created() {
  //   setInterval(() => {
  //     location.reload();
  //   }, 60000);
  // },
};
</script>

<template>
  <div class="justify-center flex flex-col md:flex-row">
    <div class="bg-white md:w-1/2">
      <estoque />
    </div>
    <div class="bg-white md:w-1/2 w-full order-2 md:order-1">
      <atualizarEstoque />
    </div>
  </div>
</template>
