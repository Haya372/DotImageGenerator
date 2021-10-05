<template>
  <div>
    <v-file-input
      accept="image/*"
      label="File input"
      v-model="image"
      full-width
    />
    <div v-if="image != null">
      <v-img :src="imageUrl" />
    </div>
  </div>
</template>

<script>
export default {
  name: "FileUpload",
  data() {
    return {
      image: null,
    };
  },
  methods: {
    onChangeFile(file) {
      if(file){
        this.image = URL.createObjectURL(file);
      }else{
        this.image = null;
      }
    },
  },
  computed: {
    imageUrl(){
      if(this.image){
        return URL.createObjectURL(this.image);
      }
      return null;
    }
  }
}
</script>