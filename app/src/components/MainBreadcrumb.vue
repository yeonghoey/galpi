<template>
  <b-breadcrumb class="align-items-center">
    <b-breadcrumb-item
      v-for="(item, index) in items"
      :key="index"
      :active="index === items.length-1"
      :class="index === 0 ? classUser : []"
      v-bind="item"
      />
    <b-button
      v-if="owner"
      class="ml-auto"
      variant="success"
      >
      New
    </b-button>
  </b-breadcrumb>
</template>

<script>
import _ from 'lodash';

export default {
  name: 'MainBreadcrumb',

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
    classUser() {
      return { user: true, owner: this.owner };
    },
    items() {
      const base = _.get(this.item, 'base', []);
      const paths = _.transform(base, (ps, s) => {
        ps.push(`${_.last(ps) || ''}/${s}`);
      }, []);

      const result = _.zip(base, paths).map((pair) => {
        const [b, p] = pair;
        // Make sure that navigating always gives list,
        // not direct redirection
        return { text: b, to: p };
      });

      return result;
    },
  },
};
</script>

<style lang="scss" scoped>
.user {
  font-size: $font-size-lg;
  font-weight: $font-weight-bold;
}

.owner::after {
  margin-left: 0.1rem;
  content: "(you)";
  color: $secondary;
  font-size: $font-size-sm;
  font-weight: $font-weight-light;
}
</style>
