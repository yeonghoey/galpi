<template>
  <aside
    class="d-flex flex-column p-2 bg-light">
    <div class="flex-shrink-0 mb-2 p-2">
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
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
        <b-list-group-item>Test</b-list-group-item>
      </b-list-group>
    </div>
  </aside>
</template>

<script>
export default {
  name: 'MainSidebar',
  props: {
    username: String,
  },
};
</script>
