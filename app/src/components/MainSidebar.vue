<template>
  <aside
    class="d-flex flex-column p-2 bg-light">
    <div class="flex-shrink-0 mb-2 p-2">
      <b-img
        class="mx-auto w-75 h-auto"
        rounded
        thumbnail
        block
        :alt="myUsername"
        :src="myAvatarURL"
        />
      <h2 class="text-center">
        <b-link
          class="text-secondary"
          :to="`/${username}`"
          >
          {{ username }}
        </b-link>
      </h2>
      <hr>
      <b-button
        class="mx-auto w-75"
        size="sm"
        variant="primary"
        block
        >
        New
      </b-button>
    </div>

    <div class="px-2 overflow-y-auto">
      <b-list-group>
        <b-list-group-item>aws</b-list-group-item>
        <b-list-group-item>google</b-list-group-item>
        <b-list-group-item>terraform</b-list-group-item>
      </b-list-group>
    </div>
  </aside>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'MainSidebar',
  props: {
    username: String,
  },

  computed: {
    ...mapState('auth', [
      'myUsername',
      'myAvatarURL',
    ]),
  },
};
</script>
