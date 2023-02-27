<script>
import pedido from "../components/pedido.vue";
import headerinfo from "../components/header.vue";

export default {
  components: { pedido, headerinfo },
  data() {
    return {};
  },
};
</script>

<template>
  <headerinfo />
  <div class="flex items-center justify-center h-screen" style="margin: 20px">
    <div class="p-1 bg-gray-100 md:w-1/2 border rounded-md shadow-md">
      <pedido />
    </div>
  </div>
</template>
