<template>
  <div id="item-children">
    <b-table
      hover
      :fields="fields"
      :items="children"
    />
  </div>
</template>

<script>
export default {
  name: 'ItemChildren',

  props: {
    children: Array,
  },

  data() {
    return {
      fields: [
        {
          key: 'name',
        },
        {
          key: 'to',
        },
      ],
    };
  },
};
</script>

<style scoped>
#item-children >>> .b-table th {
  display: none !important;
}
</style>
