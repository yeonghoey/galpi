<template>
  <b-button-toolbar
    class="mx-1 bg-light d-flex align-items-center">
    <div class="px-2 flex-fill">
      <b-form-input v-if="editing" placeholder="Link" :value="linkto"></b-form-input>
      <b-link v-else :href="linkto" class="mx-2 text-secondary">{{ linkto }}</b-link>
    </div>
    <b-dropdown text="Save" split right>
      <b-dropdown-item>Delete</b-dropdown-item>
    </b-dropdown>
    <b-button
      class="m-1"
      variant="success"
      @click="toggleEditing">
      +
    </b-button>
  </b-button-toolbar>
</template>

<script>
export default {
  name: 'ItemSelfToolButtons',

  props: {
    username: String,
    pathkey: String,
    linkto: String,
  },

  data() {
    return {
      editing: false,
    };
  },

  methods: {
    toggleEditing() {
      this.editing = !this.editing;
    },
    startEditing() {
      this.editing = true;
      this.$emit('startediting');
    },
  },
};
</script>
