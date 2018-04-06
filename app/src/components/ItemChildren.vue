<template>
  <div id="item-children">
    <b-table hover
             :fields="fields"
             :items="children">


      <template slot="name" slot-scope="data">
        <b-link :to="`/${user}/${data.value}/`"
                class="text-">
          {{ data.value }}
        </b-link>
      </template>

      <template slot="to"
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
    user: String,
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
