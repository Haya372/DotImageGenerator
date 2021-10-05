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
      <v-btn @click="onUpload">Upload</v-btn>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

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
    async onUpload(){
      try {
        let img = new FormData();
        img.append("image",this.image)
        const res = await axios.post('/img', img);
        console.log(res);
      } catch (err) {
        console.log(err);
      }
    }
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