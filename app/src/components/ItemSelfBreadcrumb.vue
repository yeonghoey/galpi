<template>
  <!-- Remove the b-breadcrumb's default margin bottom -->
  <b-breadcrumb class="mb-0 flex-fill">
    <b-breadcrumb-item
      :text="username"
      :to="`/${username}`"
      :active="noSubs"
      class="font-weight-bold"
      />
    <b-breadcrumb-item
      v-for="(sub, index) in subs"
      :key="index"
      v-bind="sub"
      />

  </b-breadcrumb>
</template>

<script>
import _ from 'lodash';

export default {
  name: 'ItemSelfBreadcrumb',

  props: {
    username: String,
    subs: Array,
    linkto: String,
    editing: Boolean,
  },

  computed: {
    noSubs() {
      return _.isEmpty(this.subs);
    },
  },
};
</script>
