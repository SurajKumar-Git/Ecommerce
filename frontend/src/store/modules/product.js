import httpClient from "@/AxiosConfig";

export default {
  state: {
    products: [],
    product: null,
    selected_variant: null,
    product_inventory: null,
    categories: [],
  },
  getters: {
    getProductColors(state) {
      const colors = [];
      const map = new Map();
      for (const varient of state.product.product_variants) {
        if (!map.has(varient.color.id)) {
          map.set(varient.color.id, true);
          colors.push(varient.color);
        }
      }
      return colors;
    },
    getProductSize(state) {
      return (selected_color) => {
        const sizes = [];
        if (!selected_color) {
          selected_color = state.selected_variant.color;
        }
        for (const variant of state.product.product_variants) {
          if (variant.color.id === selected_color.id) {
            sizes.push(variant.size);
          }
        }
        return sizes;
      };
    },

    getProductImages(state) {
      let images = [];
      if (state.selected_variant != null) {
        for (let image of state.product.product_images) {
          if (image.color === state.selected_variant.color.id) {
            images.push(image.image);
          }
        }
      }
      return images;
    },
    checkInStock(state) {
      if (state.product_inventory != null)
        return state.product_inventory.stock > 0;
      return null;
    },
    getVariants(state) {
      return (color, size) => {
        let variants = [];
        if (color && size) {
          return state.product.product_variants.find((variant) => {
            return variant.color.id == color.id && variant.size.id == size.id;
          });
        }
        for (const variant of state.product.product_variants) {
          if (variant.color.id === color.id) {
            variants.push(variant);
          }
        }
        return variants;
      };
    },
  },
  actions: {
    async fetchProducts({ commit }, params) {
      const response = await httpClient.get("product/", {
        params: params,
      });
      commit("setProducts", response.data);
    },

    async fetchProductDetail({ commit }, product_id) {
      const response = await httpClient.get(`product/${product_id}`);
      commit("setProduct", response.data);
    },
    async fetchProductInventory({ commit, state }) {
      const response = await httpClient.get(
        state.selected_variant.product_inventory
      );
      commit("setProductInventory", response.data);
    },
    updateSelectVariant({ commit, state, getters, dispatch }, { color, size }) {
      let variant = null;
      if (color) {
        variant = getters.getVariants(color)[0];
      } else {
        const color = state.selected_variant.color;
        variant = getters.getVariants(color, size);
      }
      commit("setSelectedVariant", variant);
      dispatch("fetchProductInventory");
    },
    async fetchCategories({ commit }) {
      const response = await httpClient.get("categories/");
      commit("setCategories", response.data);
    },
  },
  mutations: {
    setProducts: (state, products) => (state.products = products),
    setProduct(state, product) {
      state.product = product;
    },
    setDefaultSelectedVariant(state) {
      const default_variant = state.product.product_variants[0];
      state.selected_variant = default_variant;
    },

    setSelectedVariant(state, variant) {
      state.selected_variant = variant;
    },
    setProductInventory(state, product_inventory) {
      state.product_inventory = product_inventory;
    },
    setCategories(state, categories) {
      state.categories = categories;
    },
  },
};
