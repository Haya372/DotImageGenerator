<template>
  <div class="home-wrapper">
    <div>Home</div>
    <FileUpload />
  </div>
</template>

<script>
import FileUpload from '../components/FileUpload';

export default {
  name: "Home",
  components: { FileUpload },
}
</script>

<style scoped>
.home-wrapper {
  min-width: 640px;
}
</style>