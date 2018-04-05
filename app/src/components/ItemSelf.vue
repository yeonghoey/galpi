<template>
  <div>
    <b-breadcrumb>
      <b-breadcrumb-item
        :text="user"
        :to="`/${user}`"
      />
      <b-breadcrumb-item
        v-for="(sub, index) in subs"
        :key="index"
        v-bind="sub"
      />
    </b-breadcrumb>
  </div>
</template>

<script>
import _ from 'lodash';

export default {
  name: 'ItemSelf',
  props: {
    user: {
      type: String,
      required: true,
    },

    name: {
      type: String,
      required: false,
      default: '',
    },
  },
  data() {
    const terms = _.split(this.name, '/');
    const paths = _.reduce(terms, (ps, t) => {
      const last = _.last(ps);
      const p = last ? `${last}/${t}` : t;
      ps.push(p);
      return ps;
    }, []);
    const subs = _.zip(terms, paths).map((pair) => {
      const [t, p] = pair;
      // Make sure that navigating always gives list,
      // not direct redirection
      return { text: t, to: `/${this.user}/${p}/` };
    });

    return {
      subs,
    };
  },
};
</script>
