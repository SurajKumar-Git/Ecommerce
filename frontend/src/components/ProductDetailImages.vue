<template>
  <div class="row sticky-top">
    <div class="d-flex flex-column col-2 other_images">
      <b-icon-chevron-up font-scale="2" class="icon align-self-center" @click="previous()"></b-icon-chevron-up>
      <div class="d-flex flex-column images-container flex-wrap w-100 h-100">
        <img
          :src="getFullUrl(img)"
          alt="productImage"
          v-for="(img, index) in images"
          :key="index"
          class="images"
          @mouseenter="setImage(img)"
        />
      </div>
      <b-icon-chevron-down font-scale="2" class="icon align-self-center" @click="next()"></b-icon-chevron-down>
    </div>
    <div class="image col-10">
      <img :src="current_image" alt="productImage" class="w-100" />
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  name: "ProductDetailImages",
  data() {
    return {
      current_image: null,
      current_index: 0,
      limit: 5,
    };
  },
  methods: {
    setImage(image) {
      this.current_image = this.getFullUrl(image);
    },
    next() {
      if (this.current_index + this.limit < this.getImages.length) {
        this.current_index++;
      }
    },
    previous() {
      if (this.current_index > 0) {
        this.current_index--;
      }
    },
  },
  computed: {
    ...mapGetters({
      getImages: "getProductImages",
      getFullUrl: "getFullUrl",
    }),
    images() {
      const images = this.getImages.slice(
        this.current_index,
        this.current_index + this.limit
      );
      this.setImage(images[0]);
      return images;
    },
  },
};
</script>

<style scoped>
.other_images {
  border: 1px solid lightgray;
}

.image {
  max-width: 450px;
  max-height: 700px;
}

.images {
  width: 100%;
  min-width: 100%;
  min-height: 70px;
  max-width: 100%;
  max-height: 100px;
  margin: 10px 0px;
}

.images-container {
  max-width: 100%;
  max-height: 530px;
  overflow: hidden;
}

.icon {
  height: 20px;
  width: 100%;
}

.icon:hover {
  background: lightgray;
}
</style>