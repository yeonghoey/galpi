<template>
  <div class="m-1 d-flex">
    <ItemSelfBreadcrumb
      class="w-50"
      :username="username"
      :subs="subs"
      />
    <ItemSelfToolButtons
      class="w-50"
      :username="username"
      :pathkey="pathkey"
      :linkto="linkto"
      @startediting="startEditing"
      />
  </div>
</template>

<script>
import _ from 'lodash';
import ItemSelfBreadcrumb from '@/components/ItemSelfBreadcrumb';
import ItemSelfToolButtons from '@/components/ItemSelfToolButtons';

export default {
  name: 'ItemSelf',

  components: {
    ItemSelfBreadcrumb,
    ItemSelfToolButtons,
  },

  props: {
    username: String,
    self: Object,
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
  },

  methods: {
    startEditing() {
      this.editing = true;
    },
  },
};
</script>
