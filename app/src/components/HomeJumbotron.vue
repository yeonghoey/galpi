<template>
  <div>
    <b-jumbotron text-variant="light"
                 bg-variant="info">
      <template slot="header">
        Galpi
      </template>
      <template slot="lead">
        Recall links with ease.
      </template>
      <AppAuth/>
    </b-jumbotron>
  </div>
</template>

<script>
import AppAuth from '@/components/AppAuth';

export default {
  name: 'HomeJumbotron',

  components: {
    AppAuth,
  },
};
</script>
