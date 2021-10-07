<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-file-input
          accept="image/*"
          label="png/jpeg形式の画像を入力してください"
          v-model="image"
        />
      </v-col>
    </v-row>
    <v-row v-if="image != null">
      <v-col cols="12">
        <v-img :src="imageUrl" />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-subheader class="mb-8 pl-0">
          使用する色数
        </v-subheader>
        <v-slider
          max="20"
          min="1"
          hint="出力画像の色の数を変更できます"
          thumb-label="always"
          v-model="use_colors"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-subheader class="mb-8 pl-0">
          圧縮率
        </v-subheader>
        <v-slider
          max="1"
          min="0"
          step="0.01"
          hint="ドット絵にするための圧縮率を変更できます"
          thumb-label="always"
          v-model="ratio"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-btn
          @click="onUpload"
          :disabled="!image"
          color="primary"
        >Upload</v-btn>
      </v-col>
    </v-row>
    <div v-if="download != null">
      <ImageModal
        :url="downloadUrl"
        @close="onClose"
      />
    </div>
  </v-container>
</template>

<script>
import axios from 'axios';
import ImageModal from './ImageModal';

export default {
  name: "FileUpload",
  components: { ImageModal },
  data() {
    return {
      image: null,
      download: null,
      use_colors: 5,
      ratio: 0.2
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
        img.append("image",this.image);
        img.append("ratio", this.ratio);
        img.append("colors", this.use_colors);
        const res = await axios.post('/img', img, {responseType: 'arraybuffer'});
        this.download = new Blob([res.data], { type: 'image/jpeg' });
      } catch (err) {
        console.log(err);
      }
    },
    onClose(){
      this.download = null;
    }
  },
  computed: {
    imageUrl(){
      if(this.image){
        return URL.createObjectURL(this.image);
      }
      return null;
    },
    downloadUrl(){
      if(this.download){
        return URL.createObjectURL(this.download);
      }
      return null;
    }
  }
}
</script>