<template>
  <v-app>
    <div class="wrapper">
      <router-view />
      <PortalTarget name="portal"></PortalTarget>
    </div>
  </v-app>
</template>

<script>
import { PortalTarget } from 'portal-vue';
export default {
  name: "App",
  components: { PortalTarget }
}
</script>

<style scoped>
.wrapper {
  margin: 16px auto;
  flex-grow: 1;
  text-align: center;
  max-width: 820px;
}
</style>