<template>
  <div>
    <b-breadcrumb>
      <b-breadcrumb-item
        :text="username"
        :to="`/${username}`"
        class="font-weight-bold"
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
    username: {
      type: String,
      required: true,
    },

    pathquery: {
      type: String,
      required: false,
      default: '',
    },

    linkto: {
      type: String,
      required: false,
      default: '',
    },
  },
  data() {
    // 'a/b/c' => ['a', 'b', 'c']
    const terms = _.split(this.pathquery, '/');

    // ['a', 'b', 'c'] => ['a', 'a/b', 'a/b/c']
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
      return { text: t, to: `/${this.username}/${p}/` };
    });

    _.last(subs).active = true;

    return {
      subs,
    };
  },
};
</script>
