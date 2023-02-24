<script>
import pedido from '../components/pedido.vue';

export default {
  components: { pedido },
  data() {
    return {};
  },
};

</script>

<template>
  <div class="flex items-center justify-center h-screen" style="margin: 20px">
    <div class="p-1 bg-gray-100 md:w-1/2 border rounded-md shadow-md">
        <pedido />
    </div>
    </div>
</template>
