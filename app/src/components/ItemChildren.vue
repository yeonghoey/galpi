<template>
  <div id="item-children">
    <b-table hover
             :fields="fields"
             :items="children">

      <template slot="pathkey" slot-scope="data">
        <b-link :to="`/${username}/${data.value}/`"
                class="text-">
          {{ data.value }}
        </b-link>
      </template>

      <template slot="linkto"
                slot-scope="data">
        <b-link :href="data.value"
                class="text-secondary">
          {{ data.value }}
        </b-link>
      </template>

    </b-table>
  </div>
</template>

<script>
export default {
  name: 'ItemChildren',

  props: {
    username: String,
    children: Array,
  },

  data() {
    return {
      fields: [
        {
          key: 'pathkey',
        },
        {
          key: 'linkto',
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
