<template>
  <b-list-group>
    <MainListGroupItem v-for="(body, name) in subs"
                       :key="name"
                       :name="name"
                       :body="body"/>
  </b-list-group>
</template>

<script>
import { mapGetters } from 'vuex';
import MainListGroupItem from '@/components/MainListGroupItem';

export default {
  name: 'MainListGroup',

  components: {
    MainListGroupItem,
  },

  computed: {
    ...mapGetters('main', [
      'subs',
    ]),
  },
};
</script>
