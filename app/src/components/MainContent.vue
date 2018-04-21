<template>
  <div class="p-2">
    <MainListGroup v-bind="$props"/>
  </div>
</template>

<script>
import MainListGroup from '@/components/MainListGroup';

export default {
  name: 'MainContent',

  components: {
    MainListGroup,
  },

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
};
</script>
