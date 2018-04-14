<template>
  <div class="m-1 d-flex">
    <!-- Remove the b-breadcrumb's default margin bottom -->
    <b-breadcrumb class="mb-0 p-2 flex-fill">
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

      <b-form-input
        v-if="editing"
        class="w-50 ml-auto"
        placeholder="Test"
        >
      </b-form-input>
      <b-link
        v-else
        class="ml-auto text-secondary"
        :href="linkto"
        >
        {{ linkto }}
      </b-link>
    </b-breadcrumb>

    <div>
      <b-button
        variant="secondary"
        @click="toggleEditing">
        Edit
      </b-button>
    </div>
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

    self: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      editing: false,
    };
  },

  computed: {
    pathkey() {
      return _.get(this.self, 'pathkey', '');
    },

    linkto() {
      return _.get(this.self, 'linkto', '');
    },

    subs() {
      // 'a/b/c' => ['a', 'b', 'c']
      const terms = _.split(this.pathkey, '/').filter(t => t !== '');

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

      if (!_.isEmpty(subs)) {
        _.last(subs).active = true;
      }
      return subs;
    },

    noSubs() {
      return _.isEmpty(this.subs);
    },
  },

  methods: {
    toggleEditing() {
      this.editing = !this.editing;
    },
  },
};
</script>
