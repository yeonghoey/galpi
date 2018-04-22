<template>
  <div>
    <div v-if="renderUI"
         class="h-100 d-flex flex-column">
      <AppNavbar      class="flex-shrink-0"/>
      <MainBreadcrumb class="flex-shrink-0"/>
      <MainContent    class="flex-fill"/>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex';
import AppNavbar from '@/components/AppNavbar';
import MainBreadcrumb from '@/components/MainBreadcrumb';
import MainContent from '@/components/MainContent';

export default {
  name: 'MainView',

  components: {
    AppNavbar,
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
      'owner',
      'item',
    ]),
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
    this.setOwner(this.me === this.user);
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
  },
};
</script>
