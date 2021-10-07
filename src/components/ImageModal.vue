<template>
  <Portal to="portal">
    <div class="modal-background">
      <v-container>
        <v-card class="centerd pa-4">
          <v-row>
            <v-col cols="12">
              <v-img :src="url" />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="6">
              <v-btn @click="onSave" color="success">画像を保存</v-btn>
            </v-col>
            <v-col cols="6">
              <v-btn @click="onClose" color="warning">画像を閉じる</v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-container>
    </div>
  </Portal>
</template>

<script>
import { Portal } from 'portal-vue';
export default {
  name: "ImageModal",
  components: { Portal },
  props: {
    url: {
      type: String
    }
  },
  methods: {
    onSave(){
      let link = document.createElement('a');
      link.href = this.url;
      link.download = 'generatedImage.jpg';
      link.click();
      this.$emit('close');
    },
    onClose(){
      this.$emit('close');
    }
  }
}
</script>
<style scoped>
.modal-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(15, 15, 15, 0.5);
}

.centered {
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
</style>