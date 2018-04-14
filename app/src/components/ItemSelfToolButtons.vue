<template>
  <div>
    <b-button
      variant="secondary"
      @click="startEditing">
      Edit
    </b-button>
  </div>
</template>

<script>
export default {
  name: 'ItemSelfToolButtons',

  props: {
    username: String,
  },

  data() {
    return {
      editing: false,
    };
  },

  methods: {
    startEditing() {
      this.editing = true;
      this.$emit('startediting');
    },
  },
};
</script>
