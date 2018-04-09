<template>
  <div>
    <b-breadcrumb>
      <b-breadcrumb-item
        :text="user"
        :to="`/${user}`"
        class="font-weight-bold"
      />
      <b-breadcrumb-item
        v-for="(sub, index) in subs"
        :key="index"
        v-bind="sub"
      />
      <div class="ml-auto">
        <b-link
          :href="to"
          class="text-secondary"
        >
          {{ to }}
        </b-link>
      </div>
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

    to: {
      type: String,
      required: false,
      default: '',
    },
  },
  data() {
    // 'a/b/c' => ['a', 'b', 'c']
    const terms = _.split(this.name, '/');

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
      return { text: t, to: `/${this.user}/${p}/` };
    });

    _.last(subs).active = true;

    return {
      subs,
    };
  },
};
</script>
