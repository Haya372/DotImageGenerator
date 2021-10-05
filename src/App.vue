<template>
  <v-app>
    <div class="wrapper">
      <router-view />
    </div>
  </v-app>
</template>

<script>
export default {
  name: "App",
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