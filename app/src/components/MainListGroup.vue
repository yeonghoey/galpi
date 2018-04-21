<template>
  <b-list-group>
    <MainListGroupItem
      v-for="(item, name) in subs"
      :key="name"
      :owner="owner"
      :base="base"
      :name="name"
      :item="item"
      />
  </b-list-group>
</template>

<script>
import _ from 'lodash';
import MainListGroupItem from '@/components/MainListGroupItem';

export default {
  name: 'MainListGroup',

  components: {
    MainListGroupItem,
  },

  props: {
    owner: {
      type: Boolean,
      required: true,
    },
    item: {
      type: Object,
      required: true,
    },
  },

  computed: {
    base() {
      return _.get(this.item, 'base', []);
    },
    subs() {
      return _.get(this.item, 'subs', {});
    },
  },
};
</script>
