<template>
  <!-- Remove the b-breadcrumb's default margin bottom -->
  <b-breadcrumb class="mb-0 p-2">
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

    <!-- <b-form-input -->
    <!--   v-if="editing" -->
    <!--   class="w-50 ml-auto" -->
    <!--   placeholder="Test" -->
    <!--   > -->
    <!-- </b-form-input> -->
    <!-- <b-link -->
    <!--   v-else -->
    <!--   class="ml-auto text-secondary" -->
    <!--   :href="linkto" -->
    <!--   > -->
    <!--   {{ linkto }} -->
    <!-- </b-link> -->
  </b-breadcrumb>
</template>

<script>
import _ from 'lodash';

export default {
  name: 'ItemSelfBreadcrumb',

  props: {
    username: String,
    subs: Array,
  },

  data() {
    return {
      editing: false,
    };
  },

  computed: {
    noSubs() {
      return _.isEmpty(this.subs);
    },
  },
};
</script>
