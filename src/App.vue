<template>
  <div>
    <SearchBox />
    <Map :latitude="37.7749" :longitude="-122.4194" />
  </div>
</template>

<script>
import Map from "./components/Map.vue";
import SearchBox from "./components/SearchBox.vue";
export default {
  components: {
    Map,
    SearchBox,
  },
};
</script>
