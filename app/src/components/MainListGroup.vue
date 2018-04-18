<template>
  <b-list-group>
    <MainListGroupItem
      :owner="owner"
      path="/yeonghoey/gh/y/sls"
      name="sls"
      link="https://github.com/yeonghoey/yeonghoey/tree/master/serverless"
      />
  </b-list-group>
</template>

<script>
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
};
</script>
