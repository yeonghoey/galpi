<template>
  <div>
    <div v-if="renderUI"
         class="h-100 d-flex flex-column">
      <MainNavbar     class="flex-shrink-0"/>
      <MainBreadcrumb class="flex-shrink-0"/>
      <MainContent    class="flex-fill"/>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex';
import MainNavbar from '@/components/MainNavbar';
import MainBreadcrumb from '@/components/MainBreadcrumb';
import MainContent from '@/components/MainContent';

export default {
  name: 'MainView',

  components: {
    MainNavbar,
    MainBreadcrumb,
    MainContent,
  },

  props: {
    user: {
      type: String,
      required: true,
    },
    path: {
      type: String,
      default: '',
    },
  },

  data() {
    return {
      renderUI: false,
    };
  },

  computed: {
    ...mapState('auth', [
      'me',
    ]),
    ...mapState('main', [
      'item',
    ]),
    owner() {
      return this.me === this.user;
    },
  },

  methods: {
    ...mapMutations('main', [
      'setOwner',
    ]),
    ...mapActions('main', [
      'getItem',
    ]),
  },

  created() {
    const path = `/${this.user}/${this.path}`;
    this.getItem(path);
  },

  watch: {
    item(newItem) {
      const link = newItem.link;
      if (link) {
        window.location.href = link;
      } else {
        this.renderUI = true;
      }
    },
    me: {
      immediate: true,
      handler(user) {
        this.setOwner(user === this.user);
      },
    },
  },
};
</script>
